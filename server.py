# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request, jsonify

import flask_restful as restful

import os
import time
import json
from datetime import datetime


app = Flask(__name__)
api = restful.Api(app)


polltext = ["defult_string"]

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
    return r

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postdata', methods=['POST'])
def postdata():
    print(request.data)
    # import ipdb; ipdb.set_trace()
    # requested_data = request.get_json()
    # data = ""
    pairs = map(lambda i:"-".join(i), request.form.items())
    data = " ".join(pairs)
    print(request.form)
    resp = jsonify({"data": data, "success": True})
    return resp


class DataUpdate(restful.Resource):

    def _is_updated(self, request_time):
        """
        Returns if resource is updated or it's the first
        time it has been requested.
        args:
            request_time: last request timestamp
        """
        return False

    def get(self):
        """
        Returns 'data.txt' content when the resource has
        changed after the request time
        """
        request_time = time.time()
        while not self._is_updated(request_time):
            time.sleep(0.5)
        content = ''

        return {'content': content,
                'date': datetime.now().strftime('%Y/%m/%d %H:%M:%S')}


class Data(restful.Resource):

    def get(self):
        """
        Returns the current data content
        """
        content = ''
        return {'content': content}


api.add_resource(DataUpdate, '/data-update')
api.add_resource(Data, '/data')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
