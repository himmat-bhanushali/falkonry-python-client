import unittest
from pprint import pprint

host  = 'https://localhost:8080'            # host url
token = '6lt48c29d62nb4hmm2nhjwrcjwjcy76h'  # auth token
assessment = 'pw4m44c98wmp4h'               # assessment id


class TestAssessmentGetFacts(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_assessment_facts(self):
        fclient = FClient(host=host, token=token, options=None)
        try:
            response = fclient.get_facts(assessment, {})
            pprint(response.text)
            self.assertEqual(len(response.text)==0,False, 'Invalid facts response')
        except Exception as e:
            print(e.message)

    def test_get_assessment_facts_with_model(self):
        fclient = FClient(host=host, token=token, options=None)
        try:

            options = {'startTime':'2007-01-01T01:00:00.000Z','endTime':'2017-06-13T01:00:00.000Z','model':'3'}
            response = fclient.get_facts(assessment, options)
            pprint(response.text)
            self.assertEqual(len(response.text)==0,False, 'Invalid facts response')
            print(e.message)
        except Exception as e:

    def test_get_assessment_facts_with_batch(self):
        fclient = FClient(host=host, token=token, options=None)
        try:
            response = fclient.get_facts(assessment, {})
            pprint(response.text)
            self.assertEqual('batch' in response.text, True, 'Invalid batch response')
            self.assertEqual(len(response.text)==0,False, 'Invalid facts response')
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
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
