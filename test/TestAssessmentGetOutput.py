import unittest
import json

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                        # auth token
assessment = 'jrvk3e8mnc0nyc'                     # assessment id


class TestAssessmentGetOutput(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skip("streaming can only be done once ")
    def test_get_assessment_output(self):
        fclient = FClient(host=host, token=token)

        try:
            stream = fclient.get_output(assessment)
            for event in stream.events():
                print(json.dumps(json.loads(event.data)))

        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Error getting output of a Assessment')

    @unittest.skip("streaming can only be done once ")
    def test_get_assessment_historical_output(self):
        fclient = FClient(host=host, token=token)
        try:
            options = {'startTime':'2011-01-01T01:00:00.000Z','endTime':'2013-06-13T01:00:00.000Z','responseFormat':'application/json'}
            response = fclient.get_historical_output(assessment, options)
            '''If data is not readily available then, a tracker id will be sent with 202 status code. While falkonry will genrate ouptut data
             Client should do timely pooling on the using same method, sending tracker id (__id) in the query params
             Once data is available server will response with 200 status code and data in json/csv format.'''

            if response.status_code is 202:
                trackerResponse = Schemas.Tracker(tracker=json.loads(response.text))
                #get id from the tracker
                trackerId = trackerResponse.get_id()

                #use this tracker for checking the status of the process.
                options = {"trackerId": trackerId, "responseFormat":"application/json"}
                newResponse = fclient.get_historical_output(assessment, options)

                #if status is 202 call the same request again

            if response.status_code is 200:
                #if status is 200, output data will be present in httpResponse.response field'''
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Error getting output of a Assessment')

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
