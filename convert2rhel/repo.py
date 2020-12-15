# -*- coding: utf-8 -*-
#
# Copyright(C) 2016 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

from convert2rhel.systeminfo import system_info


def get_rhel_repoids():
    """Get IDs of the Red Hat CDN repositories that correspond to the current system."""
    repos_needed = system_info.default_rhsm_repoids

    loggerinst = logging.getLogger(__name__)
    loggerinst.info("RHEL repository IDs to enable: %s" % ', '.join(repos_needed))

    return repos_needed
