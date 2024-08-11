# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Load the Tox configuration, look for our tags thing."""

from __future__ import annotations

import contextlib
import pathlib
import sys
import tempfile
from typing import TYPE_CHECKING

import pytest
import utf8_locale

import tox_trivtags.parse as ttt_parse


if sys.version_info >= (3, 11):
    import contextlib as contextlib_chdir
else:
    import contextlib_chdir

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from contextlib import AbstractContextManager
    from typing import Final


_EXPECTED: Final[dict[str, list[str]]] = {
    "format": ["check", "quick"],
    "reformat": ["format", "manual"],
    "unit-tests-no-tox": ["tests"],
    "unit-tests-tox-4": ["tests"],
    ".pkg": [],
    "t-single": ["something"],
    "t-several": ["all", "the", "things"],
    "t-special": ["So,", "how many", "$tags", 'is "too many",', "'eh\"?"],
}


@contextlib.contextmanager
def _cfg_filename_cwd() -> Iterator[pathlib.Path]:
    """No arguments, parse the tox.ini file in the current directory."""
    yield pathlib.Path("tox.ini")


@contextlib.contextmanager
def _cfg_filename_tempdir() -> Iterator[pathlib.Path]:
    """Create a temporary directory, enter it, pass `-c` with the original cwd."""
    cwd: Final = pathlib.Path().absolute()
    with tempfile.TemporaryDirectory() as tempd:
        print(f"Temporary directory: {tempd}; current directory: {cwd}")
        with contextlib_chdir.chdir(tempd):
            yield cwd / "tox.ini"


def _do_test_run_showconfig(filename: pathlib.Path) -> None:
    """Parse the `tox --showconfig` output."""
    u8env: Final = utf8_locale.UTF8Detect().detect().env
    print(f"Using {u8env['LC_ALL']} as a UTF-8-capable locale")

    envs: Final = ttt_parse.parse_showconfig(filename, env=u8env)
    print(f"Got some Tox config sections: {' '.join(sorted(envs))}")
    for envname, expected in _EXPECTED.items():
        print(f"- envname {envname!r} expected {expected!r}")
        assert envs[envname].tags == expected


@pytest.mark.parametrize("cfg_filename", [_cfg_filename_cwd, _cfg_filename_tempdir])
def test_run_showconfig(cfg_filename: Callable[[], AbstractContextManager[pathlib.Path]]) -> None:
    """Run `tox --showconfig` expecting tox.ini to be in the specified directory."""
    print()
    with cfg_filename() as filename:
        _do_test_run_showconfig(filename)
