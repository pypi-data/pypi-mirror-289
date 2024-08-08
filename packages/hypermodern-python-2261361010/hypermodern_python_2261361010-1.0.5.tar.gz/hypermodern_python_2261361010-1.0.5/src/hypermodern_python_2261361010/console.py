# src/hypermodern_python/console.py
"""Command-line interface."""

import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    r"""\b Fetches a random Wikipedia article and prints it to the console.

    This paragraph is formatted normally and Click does
    not preserve new lines.

    \b
    This paragraph is formatted as it
    appears in the source:
    item 1
    item 2

    This paragraph is formatted normally and Click does
    not preserve new lines.

    Args:
        language (str): Language edition of Wikipedia.

    Returns:
        None
    """
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))


# @click.command()
# @click.version_option(version=__version__)
# def main():
#     """
#     \b
#     The hypermodern Python project.
#     Fetches a random Wikipedia article and prints it to the console.

#     This paragraph is formatted normally and Click does
#     not preserve new lines.

#     \b
#     This paragraph is formatted as it
#     appears in the source:
#     item 1
#     item 2

#     This paragraph is formatted normally and Click does
#     not preserve new lines.

#     """
#     data = wikipedia.random_page()

#     title = data["title"]
#     extract = data["extract"]

#     click.secho(title, fg="green")
#     click.echo(textwrap.fill(extract))
