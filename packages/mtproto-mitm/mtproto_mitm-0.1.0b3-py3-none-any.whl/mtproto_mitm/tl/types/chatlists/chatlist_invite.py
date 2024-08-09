from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0x1dcd839d, name="types.chatlists.ChatlistInvite")
class ChatlistInvite(TLObject):
    flags: Int = TLField(is_flags=True)
    title: str = TLField()
    emoticon: Optional[str] = TLField(flag=1 << 0)
    peers: list[TLObject] = TLField()
    chats: list[TLObject] = TLField()
    users: list[TLObject] = TLField()
