#
# The Qubes OS Project, https://www.qubes-os.org/
#
# Copyright (C) 2017  Wojtek Porczyk <woju@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

'''Qrexec call: u2f.Register'''

import asyncio
import sys

from .. import const
from .. import proto
from .. import tools

def main():
    '''Main routine of ``u2f.Register`` qrexec call'''

    tools.setup_logging()
    loop = asyncio.get_event_loop()

    with proto.apdu_error_responder():
        apdu = proto.CommandAPDURegister.from_stream(sys.stdin.buffer)

    rapdu = loop.run_until_complete(tools.mux(apdu))

    if rapdu.sw == const.U2F_SW.NO_ERROR:
        loop.run_until_complete(tools.qrexec_register_argument(
            'u2f.Authenticate', rapdu.qrexec_arg))

if __name__ == '__main__':
    sys.exit(main())
