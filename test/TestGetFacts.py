import unittest
from pprint import pprint

host  = 'https://localhost:8080'  # host url
token = 'lmm3orvm1yaa4j1y5b78i8f870fhon6z'                        # auth token
assessment = '743cveg32hkwl2'                     # assessment id


class TestAssessmentGetFacts(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_assessment_facts(self):
        fclient = FClient(host=host, token=token, options=None)
        try:
            response = fclient.get_facts(assessment, {})
            pprint(response.text)
            self.assertEqual(len(response.text)==0,True, 'Invalid facts response')
        except Exception as e:
            print(e.message)

    def test_get_assessment_facts_with_model(self):
        fclient = FClient(host=host, token=token, options=None)
        try:

            options = {'startTime':'2007-01-01T01:00:00.000Z','endTime':'2017-06-13T01:00:00.000Z','model':'3'}
            response = fclient.get_facts(assessment, options)
            pprint(response.text)
            self.assertEqual(len(response.text)==0,True, 'Invalid facts response')
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
    unittest.main()
