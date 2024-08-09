# This file is part of Citrand.
# Copyright (C) 2024 Taylor Rodríguez.
#
# Citrand is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Citrand is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Citrand. If not, see <https://www.gnu.org/licenses/>.

"""PRNG manipulation aide for emulated Pokémon 3DS titles."""

__all__ = ["__author__", "__license__", "__summary__", "__version__"]

from importlib import metadata

_metadata = metadata.metadata(__package__)

# Retrieve package metadata to be used throughout the program.
__author__ = _metadata["Author"]
__license__ = _metadata["License"]
__summary__ = _metadata["Summary"]
__version__ = _metadata["Version"]

del _metadata
