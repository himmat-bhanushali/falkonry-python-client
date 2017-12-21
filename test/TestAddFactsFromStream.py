import os
import io
import unittest
import random
import time as timepkg

host  = os.environ['FALKONRY_HOST_URL']  # host url
token = os.environ['FALKONRY_TOKEN']     # auth token


def check_data_ingestion(self, tracker):
    tracker_obj = None
    for i in range(0, 12):
        tracker_obj = self.fclient.get_status(tracker['__$id'])
        if tracker_obj['status'] == 'FAILED' or tracker_obj['status'] == 'ERROR':
            self.assertEqual(0, 1, 'Cannot add input data to datastream')
        if tracker_obj['status'] == 'COMPLETED' or tracker_obj['status'] == 'SUCCESS':
            break
        timepkg.sleep(5)

    if tracker_obj['status'] == 'FAILED' or tracker_obj['status'] == 'PENDING':
        self.assertEqual(0, 1, 'Cannot add input data to datastream')


# Add facts for single entity datastream
class TestAddFacts(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        self.created_datastreams = []
        pass

    # Add facts data (json format) from a stream to Assessment
    def test_add_json_facts(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())

            # creating assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = self.fclient.create_assessment(asmtRequest)

                # adding fact to the assessment
                data = io.open('./resources/factsData.json')
                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'valueIdentifier': "Health"
                }
                response = self.fclient.add_facts_stream(resp_assessment.get_id(), 'json', options, data)

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, "Cannot create datastream")

    # Add facts data (csv format) from a stream to  Assessment
    def test_add_csv_facts(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())

            # creating assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = self.fclient.create_assessment(asmtRequest)

                # adding fact to the assessment
                data = io.open('./resources/factsData.csv')

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'valueIdentifier': "Health"
                }
                response = self.fclient.add_facts_stream(resp_assessment.get_id(), 'csv', options, data)

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, "Cannot create datastream")

    # Add facts data (csv format) with tags from a stream to  Assessment
    def test_add_csv_facts_with_tags(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())

            # creating assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = self.fclient.create_assessment(asmtRequest)

                # adding fact to the assessment
                data = io.open('./resources/factsDataWithTags.csv')

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'valueIdentifier': "Health",
                    'tagIdentifier': "Tags"
                }
                response = self.fclient.add_facts_stream(resp_assessment.get_id(), 'csv', options, data)

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, "Cannot create datastream")

    # Add facts data (csv format) with additional Tag from a stream to  Assessment
    def test_add_csv_facts_with_additional_tags(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())

            # creating assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = self.fclient.create_assessment(asmtRequest)

                # adding fact to the assessment
                data = io.open('./resources/factsData.csv')

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'valueIdentifier': "Health",
                    'additionalTag': "testTag"
                }

                response = self.fclient.add_facts_stream(resp_assessment.get_id(), 'csv', options, data)

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, "Cannot create datastream")

    def tearDown(self):  # teardown
        for ds in self.created_datastreams:
            try:
                self.fclient.delete_datastream(ds)
            except Exception as e:
                print(e.message)
    pass


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
