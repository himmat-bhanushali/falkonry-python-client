import unittest
import random

host  = 'https://localhost:8080'  # host url
token = 'npp766l2hghmhrc7ygrbldjnkb9rn7mg'                       # auth token


class TestCreateAssessment(unittest.TestCase):

    def setUp(self):
        pass

    # Create Assessment
    def test_create_assessment(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')


            # Create assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(response.get_id())
            asmtRequest.set_rate('PT0S')

            assessmentResponse = fclient.create_assessment(asmtRequest)
            self.assertEqual(isinstance(assessmentResponse, Schemas.Assessment), True, 'Invalid Assessment object after creation')
            self.assertEqual(isinstance(assessmentResponse.get_id(), unicode), True, 'Invalid id of Assessment after creation')
            self.assertEqual(assessmentResponse.get_name(), asmtRequest.get_name(), 'Invalid name of Assessment after creation')
            self.assertEqual(assessmentResponse.get_datastream(), asmtRequest.get_datastream(), 'Invalid datastream in assessment after creation')
            self.assertEqual(assessmentResponse.get_rate(), asmtRequest.get_rate(), 'Invalid rate of Assessment after creation')
            self.assertEqual(assessmentResponse.get_live(), 'OFF', 'Invalid rate of Assessment after creation')
            # tear down
            try:
                fclient.delete_assessment(assessmentResponse.get_id())
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Retrieve Assessments
    def test_get_assessments(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')


            # Create assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(response.get_id())
            asmtRequest.set_rate('PT0S')

            assessmentResponse = fclient.create_assessment(asmtRequest)
            self.assertEqual(isinstance(assessmentResponse, Schemas.Assessment), True, 'Invalid Assessment object after creation')
            self.assertEqual(isinstance(assessmentResponse.get_id(), unicode), True, 'Invalid id of Assessment after creation')
            self.assertEqual(assessmentResponse.get_name(), asmtRequest.get_name(), 'Invalid name of Assessment after creation')
            self.assertEqual(assessmentResponse.get_datastream(), asmtRequest.get_datastream(), 'Invalid datastream in assessment after creation')
            self.assertEqual(assessmentResponse.get_rate(), asmtRequest.get_rate(), 'Invalid rate of Assessment after creation')
            self.assertEqual(assessmentResponse.get_live(), 'OFF', 'Invalid rate of Assessment after creation')
           

            # get assessments
            assessmentListResponse = fclient.get_assessments()
            self.assertEqual(isinstance(assessmentListResponse, list), True, 'Invalid Assessment object after creation')
            self.assertEqual(len(assessmentListResponse)>0,True,'Invalid length of assessment')


            # tear down
            try:
                fclient.delete_assessment(assessmentResponse.get_id())
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Retrieve Assessment by Id
    def test_get_assessment_by_id(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')


            # Create assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(response.get_id())
            asmtRequest.set_rate('PT0S')

            assessmentResponse = fclient.create_assessment(asmtRequest)
            self.assertEqual(isinstance(assessmentResponse, Schemas.Assessment), True, 'Invalid Assessment object after creation')
            self.assertEqual(isinstance(assessmentResponse.get_id(), unicode), True, 'Invalid id of Assessment after creation')
            self.assertEqual(assessmentResponse.get_name(), asmtRequest.get_name(), 'Invalid name of Assessment after creation')
            self.assertEqual(assessmentResponse.get_datastream(), asmtRequest.get_datastream(), 'Invalid datastream in assessment after creation')
            self.assertEqual(assessmentResponse.get_rate(), asmtRequest.get_rate(), 'Invalid rate of Assessment after creation')
            self.assertEqual(assessmentResponse.get_live(), 'OFF', 'Invalid rate of Assessment after creation')

            # get assessments
            assessmentGetResp = fclient.get_assessment(assessmentResponse.get_id())
            self.assertEqual(isinstance(assessmentGetResp, Schemas.Assessment), True, 'Invalid Assessment object after creation')
            self.assertEqual(assessmentGetResp.get_id(), assessmentResponse.get_id(), 'Invalid assessment fetched')
            self.assertEqual(isinstance(assessmentGetResp.get_aprioriConditionList(), list), True, 'Invalid aprioriConditionList object after creation')
            self.assertEqual(len(assessmentGetResp.get_aprioriConditionList()) == 0,True,'Invalid length of aprioriConditionList')

            # tear down
            try:
                fclient.delete_assessment(assessmentResponse.get_id())
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Delete Assessment
    def test_delete_assessment(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')


            # Create assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(response.get_id())
            asmtRequest.set_rate('PT0S')

            assessmentResponse = fclient.create_assessment(asmtRequest)
            self.assertEqual(isinstance(assessmentResponse, Schemas.Assessment), True, 'Invalid Assessment object after creation')
            self.assertEqual(isinstance(assessmentResponse.get_id(), unicode), True, 'Invalid id of Assessment after creation')
            self.assertEqual(assessmentResponse.get_name(), asmtRequest.get_name(), 'Invalid name of Assessment after creation')
            self.assertEqual(assessmentResponse.get_datastream(), asmtRequest.get_datastream(), 'Invalid datastream in assessment after creation')
            self.assertEqual(assessmentResponse.get_rate(), asmtRequest.get_rate(), 'Invalid rate of Assessment after creation')
            self.assertEqual(assessmentResponse.get_live(), 'OFF', 'Invalid rate of Assessment after creation')

            # delete assessment
            try:
                fclient.delete_assessment(assessmentResponse.get_id())
            except Exception as e:
                print(e.message)
                pass

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
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
