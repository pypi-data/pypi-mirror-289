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

"""Manages the TUI (terminal user interface) application."""

__all__ = ["main"]

import citrand


def main() -> None:
    """Initialise the TUI application."""
    # Display version information.
    version = f"{__package__} v{citrand.__version__} by {citrand.__author__}"
    print(version)
