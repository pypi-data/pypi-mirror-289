# -*- coding: utf-8 -*-

# (c) Meta Platforms, Inc. and affiliates.
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

from collections.abc import Collection
from typing import (
    NamedTuple,
    Optional,
    Protocol,
)


class ResolvedBuildReq(NamedTuple):
    req: str
    orig_pkg_name: str
    orig_pkg_version: str
    orig_pkg_release: Optional[str]
    dest_pkg_name: Optional[str]
    build_req_found: Optional[bool]


class Package(Protocol):
    """
    compatible subset of fedrq.backends.base.PackageCompat
    """

    @property
    def name(self) -> str: ...

    @property
    def requires(self) -> Collection: ...

    @property
    def version(self) -> str: ...


class SourcePackageQuery(Protocol):
    def get_build_reqs(self, pkg: str) -> Collection[str]: ...

    def get_resolved_build_reqs(
        self, pkg_name: str
    ) -> Collection[ResolvedBuildReq]: ...

    def is_pkg_available(self, pkg: str) -> bool: ...

    def is_req_available(self, req: str) -> bool: ...


class BinaryPackageQuery(Protocol):
    def get_pkg_names(
        self, source_pkg_names: Collection[str]
    ) -> Collection[Package]: ...

    def get_install_reqs(self, pkg: str) -> Collection[str]: ...
