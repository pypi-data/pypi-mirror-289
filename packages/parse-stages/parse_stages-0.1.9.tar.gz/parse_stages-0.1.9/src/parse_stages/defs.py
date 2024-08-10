# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Common definitions for the parse-stages library."""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class TaggedFrozen:
    """A base class for representing a constant object that has some tags."""

    name: str
    """The name of the object, e.g. the name of the Tox test environment."""

    tags: list[str]
    """The tags specified for this object."""

    def get_keyword_haystacks(self) -> list[str]:
        """Get the strings to look for keywords in.

        Default: the object's `name` attribute.
        """
        return [self.name]


@dataclasses.dataclass
class Tagged:
    """A base class for representing an object that has some tags."""

    name: str
    """The name of the object, e.g. the name of the Tox test environment."""

    tags: list[str]
    """The tags specified for this object."""

    def get_keyword_haystacks(self) -> list[str]:
        """Get the strings to look for keywords in.

        Default: the object's `name` attribute.
        """
        return [self.name]


VERSION = "0.1.9"
