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

from collections.abc import (
    Collection,
    Mapping,
)
from typing import Protocol

from fedrq.backends.base import PackageCompat, RepoqueryBase
from fedrq.config import RQConfig, get_config

from .protocols import (
    BinaryPackageQuery,
    Package,
    ResolvedBuildReq,
    SourcePackageQuery,
)


class DnfQuery(SourcePackageQuery, BinaryPackageQuery):
    def __init__(self, release: str):
        self._release = release
        config: RQConfig = get_config(backend="libdnf5")
        self._rq: RepoqueryBase = config.get_rq(release)

    def get_build_reqs(self, pkg_name: str) -> Collection[str]:
        pkg = self.get_src_pkg(pkg_name)
        return [str(req) for req in pkg.requires]

    def get_resolved_build_reqs(self, pkg_name: str) -> Collection[ResolvedBuildReq]:
        dnf_build_reqs = self.get_build_reqs(pkg_name)
        return [
            ResolvedBuildReq(
                req=req,
                orig_pkg_name=p.source_name,
                orig_pkg_version=p.version,
                orig_pkg_release=p.release,
                dest_pkg_name=None,
                build_req_found=None,
            )
            for req in dnf_build_reqs
            for p in self._rq.resolve_pkg_specs(specs=[req], resolve=True)
        ]

    def get_install_reqs(self, pkg_name: str) -> Collection[str]:
        pkgs = self.get_pkg_names([pkg_name])
        return [str(req) for pkg in pkgs for req in pkg.requires]

    def get_pkg_names(self, source_pkg_names: Collection[str]) -> Collection[Package]:
        srpms = self._rq.resolve_pkg_specs(source_pkg_names)
        srpms.filterm(arch="src")
        query = self._rq.get_subpackages(
            srpms,
        )
        return sorted(pkg for pkg in query)

    def get_src_pkg(self, pkg_name: str) -> Package:
        srpms = self._rq.query(name=pkg_name, arch="src")
        pkgs = [p for p in srpms]
        if len(pkgs) != 1:
            raise LookupError(f"Error: expected unique result, found {pkgs}")
        return pkgs[0]

    def is_pkg_available(self, pkg_name: str, arch: str = "src") -> bool:
        res = self._rq.query(name=pkg_name, arch=arch)
        return len(res) >= 1

    def is_req_available(self, req: str) -> bool:
        return len(self._rq.resolve_pkg_specs(specs=[req], resolve=True)) >= 1
