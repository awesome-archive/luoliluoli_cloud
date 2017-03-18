# -*- coding: utf-8 -*-
# file: forms.py
# author: JinTian
# time: 18/03/2017 9:31 PM
# Copyright 2017 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
from django.forms import ModelForm
from user.models import User, UserPhoto


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_gender', 'user_avatar', 'user_avatar_url', 'user_birthday',
                  'user_grade', 'user_home', 'user_location', 'user_major', 'user_phone',
                  'user_QQ', 'user_register_time', 'user_relation_status', 'user_school',
                  'user_sign', 'user_wechat']


class UserPhotoForm(ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['user', 'user_photo', 'user_photo_url']