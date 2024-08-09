from __future__ import annotations

from mtproto_mitm.tl.core_types import *
from mtproto_mitm.tl.tl_object import TLObject, tl_object, TLField
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


@tl_object(id=0x1a46500a, name="functions.messages.RequestSimpleWebView")
class RequestSimpleWebView(TLObject):
    flags: Int = TLField(is_flags=True)
    from_switch_webview: bool = TLField(flag=1 << 1)
    from_side_menu: bool = TLField(flag=1 << 2)
    bot: TLObject = TLField()
    url: Optional[str] = TLField(flag=1 << 3)
    start_param: Optional[str] = TLField(flag=1 << 4)
    theme_params: Optional[TLObject] = TLField(flag=1 << 0)
    platform: str = TLField()
