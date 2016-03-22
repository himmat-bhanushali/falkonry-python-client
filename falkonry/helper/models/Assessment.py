"""
Falkonry Client

Client to access Condition Prediction APIs

:copyright: (c) 2016 by Falkonry Inc.
:license: MIT, see LICENSE for more details.

"""

import json


class Assessment:
    """Assessment schema class"""

    def __init__(self, **kwargs):
        self.raw = kwargs.get('assessment') if 'assessment' in kwargs else {}

    def get_key(self):
        return self.raw['key']

    def set_name(self, name):
        self.raw['name'] = name
        return self

    def get_name(self):
        return self.raw['name']

    def set_input_signals(self, inputs):
        self.raw['inputList'] = inputs
        return self

    def get_input_signals(self):
        return self.raw['inputList']

    def set_apriori_conditions(self, conditions):
        self.raw['aprioriConditionList'] = conditions
        return self

    def get_apriori_conditions(self):
        return self.raw['aprioriConditionList']

    def to_json(self):
        return json.dumps(self.raw)
