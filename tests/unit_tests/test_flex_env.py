import pytest


def test_show_catalogs(flex_env):
    df = flex_env.show_catalogs()
    assert df.count() != 0