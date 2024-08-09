from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0x74bbb43d, name="functions.phone.ToggleGroupCallSettings")
class ToggleGroupCallSettings(TLObject):
    flags: Int = TLField(is_flags=True)
    reset_invite_hash: bool = TLField(flag=1 << 1)
    call: TLObject = TLField()
    join_muted: bool = TLField(flag=1 << 0, flag_serializable=True)
