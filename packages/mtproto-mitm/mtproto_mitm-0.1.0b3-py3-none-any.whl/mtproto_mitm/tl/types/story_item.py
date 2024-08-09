from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0xaf6365a1, name="types.StoryItem")
class StoryItem(TLObject):
    flags: Int = TLField(is_flags=True)
    pinned: bool = TLField(flag=1 << 5)
    public: bool = TLField(flag=1 << 7)
    close_friends: bool = TLField(flag=1 << 8)
    min: bool = TLField(flag=1 << 9)
    noforwards: bool = TLField(flag=1 << 10)
    edited: bool = TLField(flag=1 << 11)
    contacts: bool = TLField(flag=1 << 12)
    selected_contacts: bool = TLField(flag=1 << 13)
    out: bool = TLField(flag=1 << 16)
    id: Int = TLField()
    date: Int = TLField()
    fwd_from: Optional[TLObject] = TLField(flag=1 << 17)
    expire_date: Int = TLField()
    caption: Optional[str] = TLField(flag=1 << 0)
    entities: Optional[list[TLObject]] = TLField(flag=1 << 1)
    media: TLObject = TLField()
    media_areas: Optional[list[TLObject]] = TLField(flag=1 << 14)
    privacy: Optional[list[TLObject]] = TLField(flag=1 << 2)
    views: Optional[TLObject] = TLField(flag=1 << 3)
    sent_reaction: Optional[TLObject] = TLField(flag=1 << 15)
