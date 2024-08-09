from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0xaadfc8f, name="types.Channel")
class Channel(TLObject):
    flags: Int = TLField(is_flags=True)
    creator: bool = TLField(flag=1 << 0)
    left: bool = TLField(flag=1 << 2)
    broadcast: bool = TLField(flag=1 << 5)
    verified: bool = TLField(flag=1 << 7)
    megagroup: bool = TLField(flag=1 << 8)
    restricted: bool = TLField(flag=1 << 9)
    signatures: bool = TLField(flag=1 << 11)
    min: bool = TLField(flag=1 << 12)
    scam: bool = TLField(flag=1 << 19)
    has_link: bool = TLField(flag=1 << 20)
    has_geo: bool = TLField(flag=1 << 21)
    slowmode_enabled: bool = TLField(flag=1 << 22)
    call_active: bool = TLField(flag=1 << 23)
    call_not_empty: bool = TLField(flag=1 << 24)
    fake: bool = TLField(flag=1 << 25)
    gigagroup: bool = TLField(flag=1 << 26)
    noforwards: bool = TLField(flag=1 << 27)
    join_to_send: bool = TLField(flag=1 << 28)
    join_request: bool = TLField(flag=1 << 29)
    forum: bool = TLField(flag=1 << 30)
    flags2: Int = TLField(is_flags=True, flagnum=2)
    stories_hidden: bool = TLField(flag=1 << 1, flagnum=2)
    stories_hidden_min: bool = TLField(flag=1 << 2, flagnum=2)
    stories_unavailable: bool = TLField(flag=1 << 3, flagnum=2)
    id: Long = TLField()
    access_hash: Optional[Long] = TLField(flag=1 << 13)
    title: str = TLField()
    username: Optional[str] = TLField(flag=1 << 6)
    photo: TLObject = TLField()
    date: Int = TLField()
    restriction_reason: Optional[list[TLObject]] = TLField(flag=1 << 9)
    admin_rights: Optional[TLObject] = TLField(flag=1 << 14)
    banned_rights: Optional[TLObject] = TLField(flag=1 << 15)
    default_banned_rights: Optional[TLObject] = TLField(flag=1 << 18)
    participants_count: Optional[Int] = TLField(flag=1 << 17)
    usernames: Optional[list[TLObject]] = TLField(flag=1 << 0, flagnum=2)
    stories_max_id: Optional[Int] = TLField(flag=1 << 4, flagnum=2)
    color: Optional[TLObject] = TLField(flag=1 << 7, flagnum=2)
    profile_color: Optional[TLObject] = TLField(flag=1 << 8, flagnum=2)
    emoji_status: Optional[TLObject] = TLField(flag=1 << 9, flagnum=2)
    level: Optional[Int] = TLField(flag=1 << 10, flagnum=2)
