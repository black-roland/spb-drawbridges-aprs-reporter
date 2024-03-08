# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from aprslib.packets import PositionReport
from aprslib.util import latitude_to_ddm, longitude_to_ddm


class ObjectReport(PositionReport):
    object_name = 'Bridge'

    def _serialize_body(self):
        object_name = self.object_name[:9].rjust(9)
        timestamp = '111111z'  # http://wa8lmf.net/bruninga/aprs/object-perm.txt

        body = [
            ';',  # packet type
            object_name,
            timestamp,
            latitude_to_ddm(self.latitude),
            self.symbol_table,
            longitude_to_ddm(self.longitude),
            self.symbol,
            self.comment,
        ]

        return "".join(body)
