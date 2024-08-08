"""Client for the Wikipedia REST API, version 1.

This module provides functionality to fetch a random Wikipedia page. It defines a data
class to represent a Wikipedia page and a function to fetch a random page. It uses the
requests library to make HTTP requests and the desert and marshmallow libraries for data
validation and deserialization.
"""

from dataclasses import dataclass

import click
import desert
import marshmallow
import requests

API_URL: str = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@dataclass
class Page:
    """A data class that represents a Wikipedia page.

    Attributes:
        title (str): The title of the page.
        extract (str): A summary of the page.

    Example:
        >>> page = Page(title="Python (programming language)",
        ...             extract="Python is an interpreted, high-level, " +
        ...                     "general-purpose programming language.")
        >>> page.title
        'Python (programming language)'
        >>> page.extract
        'Python is an interpreted, high-level, general-purpose programming language.'
    """

    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_page(language: str = "en") -> Page:
    """Fetch a random Wikipedia page for a given language.

    Args:
        language (str, optional): The language of the Wikipedia to fetch the page from.
        Defaults to "en".

    Raises:
        click.ClickException: If a requests exception occurs.

    Returns:
        Page: A Page object containing the page data.

    Example:
        >>> page = random_page("en")
        >>> isinstance(page, Page)
        True
    """
    url: str = f"https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data: dict = response.json()
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message: str = str(error)
        raise click.ClickException(message)
