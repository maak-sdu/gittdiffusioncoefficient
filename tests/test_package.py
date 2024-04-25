from __future__ import annotations

import importlib.metadata

import gittdiffusioncoefficient as m


def test_version():
    assert importlib.metadata.version("gittdiffusioncoefficient") == m.__version__
