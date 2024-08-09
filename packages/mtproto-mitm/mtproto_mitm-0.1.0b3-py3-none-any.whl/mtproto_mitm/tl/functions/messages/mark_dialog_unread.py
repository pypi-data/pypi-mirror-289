from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0xc286d98f, name="functions.messages.MarkDialogUnread")
class MarkDialogUnread(TLObject):
    flags: Int = TLField(is_flags=True)
    unread: bool = TLField(flag=1 << 0)
    peer: TLObject = TLField()
