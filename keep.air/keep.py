# -*- encoding=utf8 -*-
__author__ = "luo"

from airtest.core.api import *

auto_setup(__file__, ['Android://127.0.0.1:5037/192.168.100.229:5555'], True)

wake()
stop_app('com.iplay.potatoclash.taptap')