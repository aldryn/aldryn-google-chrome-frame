# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):

    CHOICES = [(x, 'IE%d' % (x,)) for x in range(9, 5, -1)]

    max_version = forms.SelectField(u'Max IE version for Chrome rendering', choices=CHOICES)
    installation_prompt = forms.CheckboxField(u'Display installation prompt', required=False)

    def to_settings(self, data, settings):
        settings['GOOGLE_CHROME_FRAME_PROMPT'] = data['max_version']
        settings['GOOGLE_CHROME_FRAME_MAX_VERSION'] = data['installation_prompt']
        return settings
