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
from .protocols import (
    ResolvedBuildReq,
    SourcePackageQuery,
)


class RepoDiff:
    def __init__(self, src_pq: SourcePackageQuery, tgt_pq: SourcePackageQuery):
        self._src_pq = src_pq
        self._tgt_pq = tgt_pq

    def get_mapped_build_reqs(
        self,
        pkg_name: str,
    ) -> Collection[ResolvedBuildReq]:
        """
        Given a source package name, return its build requirements
        mapped between source repo and binary repo
        """
        resolved_build_reqs = self._src_pq.get_resolved_build_reqs(pkg_name)
        res = []
        for r in resolved_build_reqs:
            # TODO: this needs to support remapping e.g. python-* -> python3.12-*
            dest_pkg_name = r.orig_pkg_name
            res.append(
                ResolvedBuildReq(
                    req=r.req,
                    orig_pkg_name=r.orig_pkg_name,
                    orig_pkg_version=r.orig_pkg_version,
                    orig_pkg_release=r.orig_pkg_release,
                    dest_pkg_name=dest_pkg_name,
                    build_req_found=self._tgt_pq.is_req_available(r.req),
                )
            )
        return res
