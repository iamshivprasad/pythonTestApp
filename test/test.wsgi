#!/usr/bin/python3

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/test")

from testapp import app as application
application.secret_key='secret_key'
