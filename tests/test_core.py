#!/usr/bin/env python

"""Tests for `python_boilerplate` package."""

import pytest

from python_boilerplate import core


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/arup-group/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    print(core.__file__)
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

    #!/usr/bin/env python
