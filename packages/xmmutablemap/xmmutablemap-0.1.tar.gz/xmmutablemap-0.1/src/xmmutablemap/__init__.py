"""
Copyright (c) 2024 Galactic Dynamics Maintainers. All rights reserved.

xmmutablemap: Immutable Map, compatible with JAX & Equinox
"""

__all__ = ["__version__", "ImmutableMap"]

from ._core import ImmutableMap
from ._version import version as __version__
