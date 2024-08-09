from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0x1923fa8c, name="functions.stories.Report")
class Report(TLObject):
    peer: TLObject = TLField()
    id: list[Int] = TLField()
    reason: TLObject = TLField()
    message: str = TLField()
