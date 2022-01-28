Simple Web API by Python/Flask
==============================

A simple rest web API for setting/getting JSON file.

========
Install
========

if you use vertualenv,

.. sourcecode:: sh

   $ virtualenv -p python3.9 --no-site-packages --clear --distribute venv
   $ source venv/bin/activate; pip install -r requirements.txt

========
Usage
========

Run Server
-------------

.. sourcecode:: sh

   $ python api.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Use Curl
----------

.. sourcecode:: sh
    
   ## Add address
   curl -X "POST" "http://localhost:5000/dsfdsfdsfdsffff123" \
     -H 'Authorization: 123' \
     -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' \
     --data-urlencode "name=Alex 2"

   ## Get addresses
   curl "http://localhost:5000/" \
     -H 'Authorization: 123' \
     -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8'


========
Test
========

.. sourcecode:: sh
    
   $ py.test test_api.py -v -s
