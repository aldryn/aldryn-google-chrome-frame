# -*- coding: utf-8 -*-
from cmscloud.template_api import registry
from django.conf import settings

META_TAG = '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">'

registry.add_to_head(META_TAG)

PROMPT_SCRIPT = """<!--[if lte IE 9 ]>
    <script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.2/CFInstall.min.js"></script>
    <script>window.attachEvent("onload",function(){CFInstall.check({mode:"overlay"})})</script>
<![endif]-->"""

if getattr(settings, 'GOOGLE_CHROME_FRAME_PROMPT', False):
    registry.add_to_tail(PROMPT_SCRIPT)
