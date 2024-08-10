# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Parse an expression using the `pyparsing` library."""

from __future__ import annotations

import dataclasses
import typing

import pyparsing as pyp

from . import expr


if typing.TYPE_CHECKING:
    from typing import Any


@dataclasses.dataclass
class Error(Exception):
    """A base class for parse-related errors."""


@dataclasses.dataclass
class ParseResultError(Error):
    """The pyparsing module returned an unexpected series of tokens."""

    tokens: pyp.ParseResults
    """The unexpected sequence of tokens."""

    def __str__(self) -> str:
        """Provide a human-readable representation of the error."""
        return f"Unexpected sequence of parse tokens: {self.tokens!r}"


@dataclasses.dataclass
class ParseError(Error):
    """Our pyparsing handlers returned an unexpected object."""

    res: Any
    """The unexpected object returned."""

    def __str__(self) -> str:
        """Provide a human-readable representation of the error."""
        return f"Unexpected parsed object: {self.res!r}"


EMPTY_SET_SPECS = ["", "0", "none"]
"""The list of exact strings that `parse_stage_ids()` will return an empty list for."""


_p_or_expr = pyp.Forward()

_p_ws = pyp.White()[...]

_p_tag = pyp.Char("@").suppress() + pyp.Word(pyp.alphanums + "_-")

_p_keyword = pyp.Word(pyp.alphanums + "_-")

_p_bracketed = (
    pyp.Char("(").suppress()
    + _p_ws.suppress()
    + _p_or_expr
    + _p_ws.suppress()
    + pyp.Char(")").suppress()
)

_p_atom = _p_tag | _p_keyword | _p_bracketed

_p_not_atom = pyp.Literal("not").suppress() + _p_ws.suppress() + _p_atom

_p_and_expr = (_p_not_atom | _p_atom) + (
    _p_ws.suppress() + pyp.Literal("and").suppress() + _p_ws.suppress() + (_p_not_atom | _p_atom)
)[...]

_p_or_expr <<= (
    _p_and_expr
    + (_p_ws.suppress() + pyp.Literal("or").suppress() + _p_ws.suppress() + _p_and_expr)[...]
)

_p_spec = _p_ws.suppress() + _p_or_expr + _p_ws.suppress()


@_p_tag.set_parse_action
def _parse_tag(tokens: pyp.ParseResults) -> expr.TagExpr:
    """Parse a tag name."""
    match tokens:
        case [str(tag)]:
            return expr.TagExpr(tag=tag)

        case _:
            raise ParseResultError(tokens)


@_p_keyword.set_parse_action
def _parse_keyword(tokens: pyp.ParseResults) -> expr.KeywordExpr:
    """Parse a keyword."""
    match tokens:
        case [str(keyword)]:
            return expr.KeywordExpr(keyword=keyword)

        case _:
            raise ParseResultError(tokens)


@_p_atom.set_parse_action  # type: ignore[misc]
def _parse_atom(tokens: pyp.ParseResults) -> expr.BoolExpr:
    """Parse an atom (a tag or a keyword)."""
    match tokens:
        case [expr.TagExpr() | expr.KeywordExpr() | expr.OrExpr() as atom]:
            return atom

        case _:
            raise ParseResultError(tokens)


@_p_not_atom.set_parse_action  # type: ignore[misc]
def _parse_not_atom(tokens: pyp.ParseResults) -> expr.NotExpr:
    """Parse a "not @tag" or "not keyword" element."""
    match tokens:
        case [expr.BoolExpr() as child]:
            return expr.NotExpr(child=child)

        case _:
            raise ParseResultError(tokens)


@_p_and_expr.set_parse_action  # type: ignore[misc]
def _parse_and_expr(tokens: pyp.ParseResults) -> expr.BoolExpr:
    """Parse a "atom [and atom...]" subexpression."""
    children: list[expr.BoolExpr] = tokens.as_list()
    match children:
        case [expr.BoolExpr() as child]:
            return child

        case children if children and all(isinstance(item, expr.BoolExpr) for item in children):
            return expr.AndExpr(children=children)

        case _:
            raise ParseResultError(tokens)


@_p_or_expr.set_parse_action
def _parse_or_expr(tokens: pyp.ParseResults) -> expr.BoolExpr:
    """Parse a "subexpr [or subexpr...]" subexpression."""
    children: list[expr.BoolExpr] = tokens.as_list()
    match children:
        case [expr.BoolExpr() as child]:
            return child

        case children if children and all(isinstance(item, expr.BoolExpr) for item in children):
            return expr.OrExpr(children=children)

        case _:
            raise ParseResultError(tokens)


_p_complete = _p_spec.leave_whitespace()


def parse_spec(spec: str) -> expr.BoolExpr:
    """Parse an expression using the `pyparsing` library."""
    res = _p_complete.parse_string(spec, parse_all=True).as_list()
    match res:
        case [expr.BoolExpr() as spec]:
            return spec

        case _:
            raise ParseError(res)


_p_stage_id = pyp.Word(pyp.srange("[1-9]"), pyp.srange("[0-9]"))

_p_stage_range = _p_stage_id + pyp.Opt(pyp.Literal("-").suppress() + _p_stage_id)

_p_stage_ids = _p_stage_range + (pyp.Literal(",").suppress() + _p_stage_range)[...]


@_p_stage_id.set_parse_action
def _parse_stage_id(tokens: pyp.ParseResults) -> int:
    """Parse a single stage ID, return it as a zero-based index."""
    match tokens:
        case [str(stage_id)]:
            res = int(stage_id) - 1
            if res < 0:
                raise ParseResultError(tokens)
            return res

        case _:
            raise ParseResultError(tokens)


@_p_stage_range.set_parse_action
def _parse_stage_range(tokens: pyp.ParseResults) -> list[int]:
    """Parse a range of stage IDs (possibly only containing a single one)."""
    match tokens:
        case [int(stage_id)]:
            return stage_id

        case [int(start), int(end)]:
            return list(range(start, end + 1))

        case _:
            raise ParseResultError(tokens)


_p_stage_ids_complete = _p_stage_ids.leave_whitespace()


def parse_stage_ids(spec: str, *, empty_set_specs: list[str] | None = None) -> list[int]:
    """Parse a list of stage ranges, return them as zero-based indices.

    As a special case, the exact strings "" (an empty string), "0", and "none" will
    produce an empty list. Note that none of these strings are considered valid
    stage ranges, so they cannot be combined with any others (e.g. "0,3" is invalid).

    The default list of strings that signify an empty set ("", "0", "none") may be
    overridden by the `empty_set_specs` parameter.
    """
    if empty_set_specs is None:
        empty_set_specs = EMPTY_SET_SPECS
    if spec in empty_set_specs:
        return []

    res: list[int] = _p_stage_ids_complete.parse_string(spec, parse_all=True).as_list()
    if any(not isinstance(item, int) or item < 0 for item in res):
        raise ParseError(res)
    return res
