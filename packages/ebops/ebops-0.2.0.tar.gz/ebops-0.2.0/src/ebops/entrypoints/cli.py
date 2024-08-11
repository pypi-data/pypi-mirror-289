"""Define the command line interface."""

import logging
import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional

import typer

from .. import services
from . import utils

log = logging.getLogger(__name__)
cli = typer.Typer()


@cli.callback()
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(  # noqa: W0613, M511, B008
        None, "--version", callback=utils.version_callback, is_eager=True
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Manage e-book and org files to make analytical reading easy."""
    ctx.ensure_object(dict)
    utils.load_logger(verbose)


@cli.command()
def load(
    epub_path: Path,
    mount_point: Path = Path("/tmp/ebook"),
    books_orgmode_path: Optional[Path] = None,
) -> None:
    """Load an EPUB document, mount an e-reader, and update an Org-mode file.

    Args:
        epub_path (Path): The path to the EPUB document to load.
        mount_point (Path, optional): The directory where the e-reader should
            be mounted. Defaults to /mnt.
        books_orgmode_path (Path, optional): The path to the Org-mode file to update.
            If not provided, uses the environment variable BOOKS_ORGMODE_PATH.
    """
    # Handle optional environment variable for books_orgmode_path
    books_orgmode_path = books_orgmode_path or Path(
        os.getenv("BOOKS_ORGMODE_PATH", "books.org")
    )

    services.mount_ereader(mount_point)
    services.copy_epub_to_mount(epub_path, mount_point)

    # Convert TOC to Org-mode formatted string
    book = services.extract_epub_data(epub_path)
    toc_org = services.convert_toc_to_org(book)

    services.update_orgmode_file(books_orgmode_path, toc_org)


@cli.command()
def export_highlights(
    title_regexp: str,
    mount_point: Path = Path("/tmp/ebook"),
    learn_orgmode_path: Optional[Path] = None,
) -> None:
    """Export highlights from an EPUB to an Org-mode file.

    Args:
        mount_point (Path): The mount point where the e-reader is connected.
        title_regexp (str): The regular expression to find a title in the available
            ebooks.
        learn_orgmode_path (Optional[Path]): The path to the Org-mode file to save
            highlights. Defaults to the LEARN_ORGMODE_PATH environment variable if
            not provided.
    """
    if learn_orgmode_path is None:
        learn_orgmode_path = Path(
            os.getenv("LEARN_ORGMODE_PATH", "/path/to/default/orgmode")
        )

    services.mount_ereader(mount_point)

    epub_path = services.find_epub_path(title_regexp, mount_point)
    log.info(f"Found EPUB: {epub_path}")

    log.info("Finding KoboReader.sqlite...")
    sqlite_path = services.find_kobo_sqlite(mount_point)
    if sqlite_path is None:
        log.error("KoboReader.sqlite not found.")
        raise FileNotFoundError("KoboReader.sqlite not found.")

    # Create a temporary directory for the SQLite copy as the original is readonly
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_sqlite_path = Path(temp_dir) / "KoboReader.sqlite"

        # Copy the SQLite file to the temporary directory
        shutil.copy2(sqlite_path, temp_sqlite_path)
        log.info("Extracting EPUB data...")
        book = services.extract_epub_data(epub_path)

        log.info("Extract highlights from the SQLite database ...")
        highlights = services.extract_highlights(str(temp_sqlite_path), book.title)

        log.info("Match the highlights to sections in the book ...")
        book = services.match_highlights_to_sections(book, highlights)

        log.info("Converting highlights to Org-mode format...")
        highlights_org = services.convert_highlights_to_org(book)

        log.info(f"Saving highlights to {learn_orgmode_path}...")
        services.update_orgmode_file(learn_orgmode_path, highlights_org)

        log.info("Export complete.")


if __name__ == "__main__":
    cli()
