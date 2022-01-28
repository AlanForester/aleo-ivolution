# coding: utf-8

import requests
from unittest import TestCase

SERVER = 'http://127.0.0.1:5000'


class APITest(TestCase):

    def post_api(self, key, val):
        """POST /"""
        res = requests.post(
            '/address',
            headers=self.headers,
            data='{"%s":"%s"}' % (key, val)
        )
        return res

    def get_api(self):
        """GET /"""
        res = requests.get(
            '/'
        )
        return res