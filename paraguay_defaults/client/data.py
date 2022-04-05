# Copyright (c) 2022, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import requests

ENDPOINT = "https://bo.tzcode.tech/api/method/validate_token"

def validate_access(scope):
    token = get_encryption_key()
    params = {
        "token": token, 
        "scope": scope,
    }

    request = requests.get(ENDPOINT, params=params)
    
    response = request.json()

    message = response.get("message", None)

    if message is not None:
        if message:
            return True

    return False


def get_encryption_key():
    conf = frappe.get_conf()

    encryption_key = conf.get("encryption_key")

    if not encryption_key:
        frappe.throw("Encrytpion Key not generated yet.")

    return encryption_key
