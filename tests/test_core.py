"""Tests for `python_boilerplate` package."""

from pathlib import Path

from python_boilerplate import core


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    print(core.__file__ + "foo")
    file = Path(__file__).parent / "foobar.txt"
    assert not file.exists()
    file.write_text("foobar")
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
