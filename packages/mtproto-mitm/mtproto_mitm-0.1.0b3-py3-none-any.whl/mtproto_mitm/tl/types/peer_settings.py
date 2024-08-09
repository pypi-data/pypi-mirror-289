from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0xa518110d, name="types.PeerSettings")
class PeerSettings(TLObject):
    flags: Int = TLField(is_flags=True)
    report_spam: bool = TLField(flag=1 << 0)
    add_contact: bool = TLField(flag=1 << 1)
    block_contact: bool = TLField(flag=1 << 2)
    share_contact: bool = TLField(flag=1 << 3)
    need_contacts_exception: bool = TLField(flag=1 << 4)
    report_geo: bool = TLField(flag=1 << 5)
    autoarchived: bool = TLField(flag=1 << 7)
    invite_members: bool = TLField(flag=1 << 8)
    request_chat_broadcast: bool = TLField(flag=1 << 10)
    geo_distance: Optional[Int] = TLField(flag=1 << 6)
    request_chat_title: Optional[str] = TLField(flag=1 << 9)
    request_chat_date: Optional[Int] = TLField(flag=1 << 9)
