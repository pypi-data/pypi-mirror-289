# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Query Tox for the tags defined in the specified file."""

from __future__ import annotations

import ast
import configparser
import dataclasses
import itertools
import pathlib
import subprocess  # noqa: S404
import sys
import typing


if typing.TYPE_CHECKING:
    from typing import Final, TypeVar

    _T = TypeVar("_T")


DEFAULT_FILENAME = pathlib.Path("tox.ini")


@dataclasses.dataclass(frozen=True)
class TestenvTags:
    """A Tox environment along with its tags."""

    cfg_name: str
    name: str
    tags: list[str]


def _validate_constant(value: ast.expr, expected: _T) -> _T:
    """Match an AST constant of the specified type."""
    match value:
        case ast.Constant as c_value:
            match c_value.value:
                case expected() as inner:
                    return inner

                case _:
                    raise ValueError(value)

        case _:
            raise ValueError(value)


def _validate_parsed_bool(value: ast.expr) -> bool:
    """Make sure a boolean value is indeed a boolean value."""
    return _validate_constant(value, bool)


def _validate_parsed_str(value: ast.expr) -> str:
    """Make sure a string is indeed a string."""
    return _validate_constant(value, str)


def _validate_parsed_strlist(value: ast.expr) -> list[str]:
    """Make sure a list of strings is indeed a list of strings."""
    return [_validate_parsed_str(item) for item in _validate_constant(value, ast.List).elts]


def _parse_bool(value: str) -> bool:
    """Parse a Python-esque representation of a boolean value without eval()."""
    return _validate_parsed_bool(_validate_constant(value, ast.Expr).value)


def _parse_strlist(value: str) -> list[str]:
    """Parse a Python-esque representation of a list of strings without eval()."""
    return _validate_parsed_strlist(_validate_constant(value, ast.Expr).value)


def _parse_lines(value: str) -> list[str]:
    """Parse a list of text lines as Tox 4 wants to output the tags."""
    return [line for line in value.splitlines() if line]


def _parse_tags(value: str) -> list[str]:
    """Invoke `_parse_lines()` or `_parse_strlist()` as appropriate."""
    return _parse_strlist(value) if value.lstrip().startswith("[") else _parse_lines(value)


def remove_prefix(value: str, prefix: str) -> str:
    """Remove a string's prefix if it is there.

    Will be replaced with str.removeprefix() once we can depend on Python 3.9+.
    """
    parts: Final = value.partition(prefix)
    return parts[2] if parts[1] and not parts[0] else value


def parse_showconfig(
    filename: pathlib.Path = DEFAULT_FILENAME,
    *,
    env: dict[str, str] | None = None,
    tox_invoke: list[str | pathlib.Path] | None = None,
) -> dict[str, TestenvTags]:
    """Run `tox --showconfig` and look for tags in its output."""
    if tox_invoke is None:
        tox_invoke = [sys.executable, "-u", "-m", "tox"]
    tox_cmd: Final = [
        *tox_invoke,
        "-q",
        "config",
        "-c",
        filename,
        "-e",
        "ALL",
    ]

    def parse_output() -> configparser.ConfigParser:
        """Run Tox, parse its output as an INI-style file."""
        lines: Final = subprocess.run(  # noqa: S603
            tox_cmd,
            check=True,
            encoding="UTF-8",
            env=env,
            shell=False,
            stdout=subprocess.PIPE,
        ).stdout.splitlines()
        # Drop the lines that Tox outputs at the start if it needs to bootstrap
        # a more recent version due to a `tox.minversion` specification.
        lines_real: Final = itertools.dropwhile(lambda line: not line.startswith("["), lines)

        cfgp: Final = configparser.ConfigParser(interpolation=None)
        cfgp.read_string("\n".join(lines_real) + "\n")
        return cfgp

    def process_config(cfgp: configparser.ConfigParser) -> dict[str, TestenvTags]:
        """Build the result dictionary."""
        return {
            name: TestenvTags(
                cfg_name=cfg_name,
                name=name,
                tags=_parse_tags(tags),
            )
            for cfg_name, name, tags in (
                (cfg_name, name, env["tags"])
                for cfg_name, name, env in (
                    (cfg_name, remove_prefix(cfg_name, "testenv:"), env)
                    for cfg_name, env in cfgp.items()
                )
                if cfg_name != name
            )
        }

    cfgp_no_req: Final = parse_output()
    if any("tags" in env for env in cfgp_no_req.values()):
        return process_config(cfgp_no_req)

    tox_cmd.extend(["-x", "tox.requires=test-stages >= 0.1.3"])
    return process_config(parse_output())
