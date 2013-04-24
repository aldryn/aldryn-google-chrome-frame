# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):

    installation_prompt = forms.CheckboxField('Display Google Chrome Frame installation prompt')

    def to_settings(self, data, settings):
        settings['GOOGLE_CHROME_FRAME_PROMPT'] = data['installation_prompt']
        return settings
