#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2


DEFAULT_CONTENT = '1D6+2 sample test'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class RollDice(webapp2.RequestHandler):
    def get(self):
        message_content = self.request.get('content', DEFAULT_CONTENT)
        self.response.write('<html><body>')
        self.response.write(message_content)
        self.response.write('</body></html>')
        self.response.content = message_content + ", this works!"


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/dice',RollDice),
], debug=True)
