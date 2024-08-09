# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause
"""Helper functions for the vetox unit test suite."""

from __future__ import annotations

import contextlib
import pathlib
import tempfile
import typing

from vetox import __main__ as vmain


if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Final


TOX_OLD_LOW: Final = (4, 1)
"""The lower bound on the "old Tox version" if specified."""

TOX_OLD_HIGH: Final = (4, 2)
"""The upper bound on the "old Tox version" if specified."""


def get_old_tox_req() -> str:
    """Build the requirements string if an old Tox version should be used."""

    def join_ints(bound: tuple[int, ...]) -> str:
        """Use a dot to join a tuple of integers into a string."""
        return ".".join(str(word) for word in bound)

    return f">= {join_ints(TOX_OLD_LOW)}, < {join_ints(TOX_OLD_HIGH)}"


@contextlib.contextmanager
def tempd_and_config(
    *,
    use_old_tox: bool,
    use_tox_uv: bool,
    use_uv: bool,
) -> Iterator[tuple[pathlib.Path, vmain.Config]]:
    """Create a temporary directory tree, initialize a `Config` object."""
    with tempfile.TemporaryDirectory() as tempd_obj:
        tempd: Final = pathlib.Path(tempd_obj)

        package_dir: Final = tempd / "package"
        package_dir.mkdir(mode=0o755)

        cfg_tempd: Final = tempd / "tmp"
        cfg_tempd.mkdir(mode=0o755)

        cfg: Final = vmain.Config(
            conf=package_dir / "tox.ini",
            env=vmain.clean_env(),
            log=vmain.build_logger(),
            tempd=cfg_tempd,
            tox_req=get_old_tox_req() if use_old_tox else None,
            tox_uv=use_tox_uv,
            uv=use_uv,
        )
        yield (tempd, cfg)
