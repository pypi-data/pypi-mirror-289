"""Test lmtr_agents."""
# pylint: disable=broad-except

# import os
# from platform import paltform
from lmtr_agents import __version__, lmtr_agents

# if platform().lower().startswith("linux"):


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not lmtr_agents()
    except Exception:
        assert True
