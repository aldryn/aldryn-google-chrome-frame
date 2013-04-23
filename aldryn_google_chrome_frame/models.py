# -*- coding: utf-8 -*-
from cmscloud.template_api import registry

META_TAG = '<meta http-equiv="X-UA-Compatible" content="chrome=1">'

registry.add_to_head(META_TAG)
