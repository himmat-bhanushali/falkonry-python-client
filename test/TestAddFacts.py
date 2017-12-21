import unittest
import random
import json



host  = 'https://localhost:8080'            # host url
token = '6lt48c29d62nb4hmm2nhjwrcjwjcy76h'  # auth token


# Add facts for single entity datastream
class TestAddFacts(unittest.TestCase):

    def setUp(self):
        pass

    # Add facts data (json format) to Assessment
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
            options = {'streaming': False,
                       'hasMoreData': False}
            response = fclient.add_input_data(datastreamResponse.get_id(), 'json', {}, data)

            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(datastreamResponse.get_id())
            asmtRequest.set_rate('PT0S')

            try:
                resp_assessment = fclient.create_assessment(asmtRequest)
                data = '{"time" : "2011-03-26T12:00:00.000Z", "car" : "HI3821", "end" : "2012-06-01T00:00:00.000Z", "Health" : "Normal"}'

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'entityIdentifier': "car",
                    'valueIdentifier': "Health"
                }

                response = fclient.add_facts(resp_assessment.get_id(), 'json', options, data)
                # tear down
                try:
                    fclient.delete_assessment(resp_assessment.get_id())
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    print(e.message)
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

    # Add facts data (csv format) to Assessment
    def test_add_csv_facts(self):
        pass
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
                data = "time,end,car,Health\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,IL9753,Normal\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,HI3821,Normal"

                options = {
                    'startTimeIdentifier': "time",
                    'endTimeIdentifier': "end",
                    'timeFormat': "iso_8601",
                    'timeZone': time.get_zone(),
                    'valueIdentifier': "Health"
                }

                response = fclient.add_facts(resp_assessment.get_id(), 'csv', options, data)
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

    # Add facts data (csv format) with tags to Assessment
    def test_add_csv_facts_with_tags(self):
            pass
            fclient = FClient(host=host, token=token, options=None)
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
                    data = "time,end,car,Health,Tags\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,IL9753,Normal,testTag1\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,HI3821,Normal,testTag2"

                    options = {
                        'startTimeIdentifier': "time",
                        'endTimeIdentifier': "end",
                        'timeFormat': "iso_8601",
                        'timeZone': time.get_zone(),
                        'valueIdentifier': "Health",
                        'tagIdentifier': 'Tags'
                    }

                    response = fclient.add_facts(resp_assessment.get_id(), 'csv', options, data)
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
                self.assertEqual(0, 1, "Cannot add data")

    # Add facts data (csv format) with additional Tag to Assessment
    def test_add_csv_facts_with_tags(self):
            pass
            fclient = FClient(host=host, token=token, options=None)
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
                    data = "time,end,car,Health\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,IL9753,Normal\n2011-03-31T00:00:00.000Z,2011-04-01T00:00:00.000Z,HI3821,Normal"

                    options = {
                        'startTimeIdentifier': "time",
                        'endTimeIdentifier': "end",
                        'timeFormat': "iso_8601",
                        'timeZone': time.get_zone(),
                        'valueIdentifier': "Health",
                        'additionalTag': 'testTag'
                    }

                    response = fclient.add_facts(resp_assessment.get_id(), 'csv', options, data)
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
                self.assertEqual(0, 1, "Cannot add data")

    # Add facts data (csv format) with batch identifier to Assessment
    def test_add_csv_fact_with_batch(self):
        fclient = FClient(host=host, token=token, options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()
        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("millis")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        field.set_batchIdentifier('batches')
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = '{"time": 1,"batchId": "batch_1","signal1": 9.95,"signal2": 19.95,"signal3": 39.95}\n{"time": 2,"batchId": "batch_1","signal1": 4.45,"signal2": 14.45,"signal3": 34.45}\n{"time": 3,"batchId": "batch_2","signal1": 1.45,"signal2": 10.45,"signal3": 30.45}\n{"time": 4,"batchId": "batch_2","signal1": 8.45,"signal2": 18.45,"signal3": 38.45}\n{"time": 5,"batchId": "batch_2","signal1": 2.45,"signal2": 12.45,"signal3": 32.45}'
                options = {
                    'streaming': False,
                    'hasMoreData': False,
                    'timeFormat': time.get_format(),
                    'timeZone': time.get_zone(),
                    'timeIdentifier': time.get_identifier(),
                    'batchIdentifier': 'batchId'
                }
                response = fclient.add_input_data(datastreamResponse.get_id(), 'json', options, data)
                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                asmtRequest = Schemas.AssessmentRequest()
                asmtRequest.set_name('Assessment Name ' + str(random.random()))
                asmtRequest.set_datastream(datastreamResponse.get_id())
                asmtRequest.set_rate('PT0S')

                try:
                    resp_assessment = fclient.create_assessment(asmtRequest)
                    data = "batchId,value\nbatch_1,normal\nbatch_2,abnormal"

                    options = {
                        'valueIdentifier': "value",
                        'batchIdentifier': 'batchId'
                    }

                    response = fclient.add_facts(resp_assessment.get_id(), 'csv', options, data)
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

                # tear down
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

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
