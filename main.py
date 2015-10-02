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
import logging
import json
import random


DEFAULT_CONTENT = '1D6+2 sample test'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

# """
# input sample
# {
#     chooseAmong: True (not implemented yet)
#     chooseNum: 3 (not implemented yet)
#     dice_num: 4
#     dice_face:6
#     adjust_sign: +
#     adjust_value:4
#     comment: test
# }
# """
class RollDice(webapp2.RequestHandler):
    def get(self):
        dice_num = self.request.get('dice_num', 2)
        dice_face = self.request.get('dice_face', 6)
        adjust_sign = self.request.get('adjust_sign', "+")
        adjust_value = self.request.get('adjust_value', 0)
        comment = self.request.get('comment', '')
        dice_result = []
        final_calculation = eval(adjust_sign+`str(adjust_value)`)
        for i in range(int(dice_num)):
            roll = int(random.randint(1, int(dice_face)))
            dice_result.append(roll)
            final_calculation = roll + int(final_calculation)

        result = {
                'content': final_calculation,
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result))


app = webapp2.WSGIApplication([
    ('/', MainHandler), 
    ('/dice', RollDice),
], debug=True)
