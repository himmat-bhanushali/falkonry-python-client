import os
import unittest
import xmlrunner
from pprint import pprint

host        = os.environ['FALKONRY_HOST_URL']               # host url
token       = os.environ['FALKONRY_TOKEN']                  # auth token
assessment  = os.environ['FALKONRY_ASSESSMENT_SLIDING_ID']  # host url
assessmentB = os.environ['FALKONRY_ASSESSMENT_BATCH_ID']    # auth token

class TestAssessmentGetFacts(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        pass

    def test_get_assessment_facts(self):

        try:
            response = self.fclient.get_facts(assessment, {})
            pprint(response.content)
            self.assertEqual(len(response.content) == 0, False, 'Invalid facts response')
        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, "Cannot get facts from the assessment")

    def test_get_assessment_facts_with_model(self):

        try:
            options = {'startTime': '2011-01-02T00:00:00.000Z', 'endTime': '2014-01-01T00:00:00.000Z', 'model': '1'}
            response = self.fclient.get_facts(assessment, options)
            pprint(response.content)
            self.assertEqual(len(response.content) == 0, False, 'Invalid facts response')
        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, "Cannot get facts from the assessment for a specific model")

    def test_get_assessment_facts_with_batch(self):

        try:
            response = self.fclient.get_facts(assessmentB, {})
            pprint(response.content)
            self.assertEqual('batch' in str(response.content), True, 'Invalid facts with batch response')
            self.assertEqual(len(response.content)==0,False, 'Invalid facts with batch response')
        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, "Cannot get facts from the assessment for batch case")


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
        from falkonryclient.helper.utils import exception_handler

    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
        from ..falkonryclient.helper.utils import exception_handler

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='out'),
        failfast=False, buffer=False, catchbreak=False)
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
    from falkonryclient.helper.utils import exception_handler
