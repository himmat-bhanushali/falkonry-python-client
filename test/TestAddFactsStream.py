import io
import unittest
import random

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                       # auth token


class TestAddFacts(unittest.TestCase):

    def setUp(self):
        pass

    # Add facts data (json format) from a stream to Assessment
    def test_add_json_facts(self):
        fclient = FClient(host=host, token=token,options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
            response = fclient.add_input_data(datastreamResponse.get_id(), 'json', {}, data)

            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = fclient.create_assessment(asmtRequest)
                data = io.open('./test/factsData.json')

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    # 'entityIdentifier': "car",
                    'valueIdentifier': "Health"
                }
                response = fclient.add_facts_stream(resp_assessment.get_id(), 'json', options, data)
                # tear down
                try:
                    fclient.delete_assessment(resp_assessment.get_id())
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0,1,"Cannot add data")

    # Add facts data (csv format) from a stream to  Assessment
    def test_add_csv_facts(self):
        fclient = FClient(host=host, token=token,options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
            response = fclient.add_input_data(datastreamResponse.get_id(), 'json', {}, data)

            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = fclient.create_assessment(asmtRequest)
                data = io.open('./test/factsData.csv')

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    # 'entityIdentifier': "car",
                    'valueIdentifier': "Health"
                }


                response = fclient.add_facts_stream(resp_assessment.get_id(), 'csv', options, data)
                # tear down
                try:
                    fclient.delete_assessment(resp_assessment.get_id())
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
                self.assertEqual(0, 1, 'Cannot create assessment')
        except Exception as e:
            print(e.message)
            self.assertEqual(0,1,"Cannot add data")

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
