from webapp2 import RequestHandler, uri_for

import jinja2
import models
import os
import logging
import json

J_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


def render_to_string(filename, context):
    template = J_ENV.get_template('templates/' + filename)
    return template.render(context)


def render_with_context(self, filename, context):
    from google.appengine.api import users

    template = J_ENV.get_template('templates/' + filename)
    self.response.out.write(template.render(context))


def json_response(self, context):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(context))


class Home(RequestHandler):
    def get(self):
        context = {

        }

        render_with_context(self, 'coming_soon.html', context)