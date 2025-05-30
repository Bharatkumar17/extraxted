#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7246658062:AAFihBmIU_oShvmhz1f-r8Rxu4dCt4Y950A")
    API_ID = int(os.environ.get("API_ID", "26729193"))
    API_HASH = os.environ.get("API_HASH", "a94598ef642481e35466292df95f251e")
    AUTH_USERS = "1012164907"

