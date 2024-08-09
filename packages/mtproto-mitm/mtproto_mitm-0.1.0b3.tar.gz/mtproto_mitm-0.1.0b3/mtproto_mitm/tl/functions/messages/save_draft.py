from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0x7ff3b806, name="functions.messages.SaveDraft")
class SaveDraft(TLObject):
    flags: Int = TLField(is_flags=True)
    no_webpage: bool = TLField(flag=1 << 1)
    invert_media: bool = TLField(flag=1 << 6)
    reply_to: Optional[TLObject] = TLField(flag=1 << 4)
    peer: TLObject = TLField()
    message: str = TLField()
    entities: Optional[list[TLObject]] = TLField(flag=1 << 3)
    media: Optional[TLObject] = TLField(flag=1 << 5)
