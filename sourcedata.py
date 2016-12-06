# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

def get_file_data(location):
    with open(location) as sfile:
        body = json.load(sfile)
        return body

if __name__ == "__main__":
	get_file_data()
