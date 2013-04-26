# -*- coding: utf-8 -*-
from cmscloud.template_api import registry
from django.conf import settings


def get_meta_version(max_version):
    assert 6 <= max_version <= 9
    if max_version == 9:
        return '1'
    else:
        return 'IE%d' % (max_version, )

META_TAG = '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=%(meta_version)s">'

registry.add_to_head(META_TAG % {'meta_version': get_meta_version(settings.GOOGLE_CHROME_FRAME_MAX_VERSION)})

PROMPT_SCRIPT = """<!--[if lte IE %(max_version)d ]>
    <script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.2/CFInstall.min.js"></script>
    <script>window.attachEvent("onload",function(){CFInstall.check({mode:"overlay"})})</script>
<![endif]-->"""

if getattr(settings, 'GOOGLE_CHROME_FRAME_PROMPT', False):
    registry.add_to_tail(PROMPT_SCRIPT % {'max_version': settings.GOOGLE_CHROME_FRAME_MAX_VERSION})
