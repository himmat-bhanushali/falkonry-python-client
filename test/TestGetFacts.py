import os
import unittest
import xmlrunner
from pprint import pprint

host       = os.environ['FALKONRY_HOST_URL']  # host url
token      = os.environ['FALKONRY_TOKEN']     # auth token
assessment = 'y7dcwmp72v68tr'            # assessment id


class TestAssessmentGetFacts(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        pass

    def test_get_assessment_facts(self):

        try:
            response = self.fclient.get_facts(assessment, {})
            pprint(response.text)
            self.assertEqual(len(response.text) == 0, False, 'Invalid facts response')
        except Exception as e:
            print(e.message)

    def test_get_assessment_facts_with_model(self):

        try:

            options = {'startTime': '2011-01-01T00:00:00.000Z', 'endTime': '2014-12-31T00:00:00.000Z', 'model': '2'}
            response = self.fclient.get_facts(assessment, options)
            pprint(response.text)
            self.assertEqual(len(response.text) == 0, False, 'Invalid facts response')
        except Exception as e:
            print(e.message)

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(
            path.dirname(
                path.dirname(
                    path.abspath(__file__)
                )
            )
        )
        from falkonryclient import schemas as Schemas
        from falkonryclient import client as FClient
    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='out'),
        failfast=False, buffer=False, catchbreak=False)
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
