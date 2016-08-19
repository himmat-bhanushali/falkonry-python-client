[![Falkonry Logo](http://static1.squarespace.com/static/55a7df64e4b09f03368a7a78/t/569c6441ab281050fe32c18a/1453089858079/15-logo-transparent-h.png?format=500w)](http://falkonry.com/)

[![Build status](https://img.shields.io/travis/Falkonry/falkonry-python-client.svg?style=flat-square)](https://travis-ci.org/Falkonry/falkonry-python-client)

Falkonry Python Client to access [Falkonry Condition Prediction](falkonry.com) APIs

[Releases](https://github.com/Falkonry/falkonry-python-client/releases)

## Installation

```bash
$ pip install falkonryclient
```

## Features

    * Create Eventbuffer
    * Retrieve Eventbuffers
    * Create Pipeline
    * Retrieve Pipelines
    * Add data to Eventbuffer (csv/json, stream)
    * Retrieve output of Pipeline
    * Create subscription for Eventbuffer
    * Create publication for Pipeline
    
## Quick Start
```
    * Get auth token from Falkonry Service UI
    * Read the examples provided for integratioin with various data formats
```

## Examples 

#### Setup Eventbuffer for narrow/historian style data from a single thing
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "tag" : "signal1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:02", "tag" : "signal2", "value" : 9.3}

    or

    time, tag, value
    2016-03-01 01:01:01, signal1, 3.4
    2016-03-01 01:01:02, signal2, 9.3

```

Usage :
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

eventbuffer = Schemas.Eventbuffer()
eventbuffer.set_name('Motor Health' + str(random.random())) #set name of the Eventbuffer    
eventbuffer.set_time_identifier('time')                     #set property to identify time in the data
eventbuffer.set_time_format('iso_8601')                     #set format of the time in the data
eventbuffer.set_signals_tag_field('tag')                    #property that identifies signal tag in the data
eventbuffer.set_value_column('value')                       #property that identifies value of the signal in the data
        
#create Eventbuffer
createdEventbuffer = falkonry.create_eventbuffer(eventbuffer)

#add data to Eventbuffer
String data = "{\"time\" : \"2016-03-01 01:01:01\", \"tag\" : \"signal1\", \"value\" : 3.4}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:02\", \"tag\" : \"signal2\", \"value\" : 9.3}";
inputResponse = falkonry.add_input_data('eventbuffer_id', 'json', {}, data)
```

#### Setup Eventbuffer for narrow/historian style data from multiple things
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "tag" : "signal1_thing1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:01", "tag" : "signal2_thing1", "value" : 1.4}
    {"time" :"2016-03-01 01:01:02", "tag" : "signal1_thing2", "value" : 9.3}
    {"time" :"2016-03-01 01:01:02", "tag" : "signal2_thing2", "value" : 4.3}

    or

    time, tag, value
    2016-03-01 01:01:01, signal1_thing1, 3.4
    2016-03-01 01:01:01, signal2_thing1, 1.4
    2016-03-01 01:01:02, signal1_thing2, 9.3
    2016-03-01 01:01:02, signal2_thing2, 4.3
```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as 

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

eventbuffer = Schemas.Eventbuffer()
eventbuffer.set_name('Motor Health')                    #set name of the Eventbuffer
eventbuffer.set_time_identifier('time')                 #set property to identify time in the data
eventbuffer.set_time_format('iso_8601')                 #set format of the time in the data
eventbuffer.set_thing_identifier('motor')               #set property to identify things in the data
eventbuffer.set_signals_tag_field("tag")                #property that identifies signal tag in the data
eventbuffer.set_signals_delimiter('_')                  #delimiter used to concat thing id and signal name to create signal tag
eventbuffer.set_signals_location('prefix')              #part of the tag that identifies the signal name
eventbuffer.set_value_column("value")                   #property that identifies value of the signal in the data
       
#create Eventbuffer
createdEventbuffer = falkonry.create_eventbuffer(eventbuffer)

#add data to Eventbuffer
String data = "{\"time\" : \"2016-03-01 01:01:01\", \"tag\" : \"signal1_thing1\", \"value\" : 3.4}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:01\", \"tag\" : \"signal2_thing1\", \"value\" : 1.4}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:02\", \"tag\" : \"signal1_thing1\", \"value\" : 9.3}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:02\", \"tag\" : \"signal2_thing2\", \"value\" : 4.3}";

inputResponse = falkonry.add_input_data('eventbuffer_id', 'json', {}, data)
```

#### Setup Eventbuffer for wide style data from a single thing
   
Data :

```python
    {"time":1467729675422, "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
    {"time":1467729668919, "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

    or

    time, signal1, signal2, signal3, signal4
    1467729675422, 41.11, 62.34, 77.63, 4.8
    1467729675445, 43.91, 82.64, 73.63, 3.8
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

eventbuffer = Schemas.Eventbuffer()
eventbuffer.set_name('Motor Health')                    #set name of the Eventbuffer
eventbuffer.set_time_identifier('time')                 #set property to identify time in the data
eventbuffer.set_time_format('iso_8601')                 #set format of the time in the data
       
#create Eventbuffer
createdEventbuffer = falkonry.create_eventbuffer(eventbuffer)

#add data to Eventbuffer
String data = "{\"time\":1467729675422,\"signal1\":41.11,\"signal2\":82.34,\"signal3\":74.63,\"signal4\":4.8}" + "\n"
        + "{\"time\":1467729668919,\"signal1\":78.11,\"signal2\":2.33,\"signal3\":4.6,\"signal4\":9.8}";
inputResponse = falkonry.add_input_data('eventbuffer_id', 'json', {}, data)
```

#### Setup Eventbuffer for wide style data from multiple things

Data :

```python
    {"time":1467729675422, "thing": "Thing1", "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
    {"time":1467729668919, "thing": "Thing2", "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

    or

    time, thing, signal1, signal2, signal3, signal4
    1467729675422, thing1, 41.11, 62.34, 77.63, 4.8
    1467729675445, thing1, 43.91, 82.64, 73.63, 3.8
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

eventbuffer = Schemas.Eventbuffer()
eventbuffer.set_name('Motor Health')                    #set name of the Eventbuffer
eventbuffer.set_time_identifier('time')                 #set property to identify time in the data
eventbuffer.set_time_format('iso_8601')                 #set format of the time in the data
eventbuffer.set_thing_identifier('thing1')               #set property to identify things in the data
       
#create Eventbuffer
createdEventbuffer = falkonry.create_eventbuffer(eventbuffer)

#add data to Eventbuffer
String data = "time, thing, signal1, signal2, signal3, signal4" + "\n"
        + "1467729675422, thing1, 41.11, 62.34, 77.63, 4.8" + "\n"
        + "1467729675445, thing1, 43.91, 82.64, 73.63, 3.8";
inputResponse = falkonry.add_input_data('eventbuffer_id', 'json', {}, data)
```

#### Get an Eventbuffer
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')
        
#return list of Eventbuffers
eventbuffers = falkonry.get_eventbuffers()
```

#### Add json data from a stream to an Eventbuffer
    
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry = Falkonry('https://service.falkonry.io', 'auth-token')

stream   = io.open('./data.json')                    

response = falkonry.add_input_stream('eventbuffer_id', 'json', {}, stream)
```

#### Add csv data from a stream to an Eventbuffer

```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry = Falkonry('https://service.falkonry.io', 'auth-token')

stream   = io.open('./data.csv')                    

response = falkonry.add_input_stream('eventbuffer_id', 'csv', {}, stream)
```

#### Setup Pipeline from Eventbuffer
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

eventbuffer.set_name('Motor Health')
eventbuffer.set_time_identifier('time')
eventbuffer.set_time_format('iso_8601')
        
createdEventbuffer = falkonry.create_eventbuffer(eventbuffer)

assessment = Schemas.Assessment()
                .set_name('Health')                                                     #set name for the Assessment
                .set_input_signals(['current', 'vibration'])                            #add signal data
                        
pipeline   = Schemas.Pipeline()
                .set_name('Motor Health')                                               #set name for the Pipeline
                .set_eventbuffer(createdEventbuffer.get_id())                           #set Eventbuffer for the Pipeline
                .set_input_signals({'current' : 'Numeric', 'vibration' : 'Numeric'})    #signals present in the Eventbuffer
                .set_assessment(assessment)                                             #add an Assessment to the Pipeline
        
#create Pipeline
createdPipeline = falkonry.createPipeline(pipeline)
```

#### To get all Pipelines
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

#return list of Pipelines
pipelines  = falkonry.getPipelines()
```

#### Add verification data (json format) to a Pipeline
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('https://service.falkonry.io', 'auth-token')

data          = '{"time" : "2011-03-26T12:00:00Z", "car" : "HI3821", "end" : "2012-06-01T00:00:00Z", "Health" : "Normal"}'
inputResponse = falkonry.add_verification('pipeline_id', 'json', {}, data)
```

#### To add verification data (csv format) to a Pipeline
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('https://service.falkonry.io', 'auth-token')

data          = 'time,car,end,Health' + "\n"
                 + '2011-03-26T12:00:00Z,HI3821,2012-06-01T00:00:00Z,Normal' + "\n"
                 + '2014-02-10T23:00:00Z,HI3821,2014-03-20T12:00:00Z,Spalling';

inputResponse = falkonry.add_verification('pipeline_id', 'json', {}, data)
```
    
#### Add verification data (json format) from a stream to a Pipeline
    
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry = Falkonry('https://service.falkonry.io', 'auth-token')
stream   = io.open('./data.json')

response = falkonry.add_verification_stream('pipeline_id', 'json', {}, stream)

```

#### Add verification data (csv format) from a stream to a Pipeline
    
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry = Falkonry('https://service.falkonry.io', 'auth-token')
stream   = io.open('./data.csv')

response = falkonry.add_verification_stream('pipeline_id', 'json', {}, stream)

```

#### Get output of a Pipeline
    
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry     = Falkonry('https://service.falkonry.io', 'auth-token')
stream       = open('/tmp/sample.json', 'r')
startTime    = '1457018017'                     #seconds since unix epoch 
endTime      = '1457028017'                     #seconds since unix epoch
outputStream = falkonry.getOutput('pipeline_id', startTime, endTime)
with open('/tmp/pipelineOutput.json', 'w') as outputFile:
    for line in outputStream:
        outputFile.write(line + '\n')
```

#### To create and delete a subscription for an Eventbuffer
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('https://service.falkonry.io', 'auth-token')

subscription  = Schemas.Subscription()
subscription.set_type('MQTT') \                         #set Subscription type
            .set_path('mqtt://test.mosquito.com') \     #set Mosquitto broker host url
            .set_topic('falkonry-eb-1-test') \          #set topic for the Subscription
            .set_username('test-user') \                #optional parameter
            .set_password('test') \                     #optional parameter
            
#create Subscription
subscription  = falkonry.create_subscription('eventbuffer_id', subscription)

#delete Subscription
falkonry.delete_subscription('eventbuffer_id', subscription)
```

#### To create and delete a publication for a Pipeline
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('https://service.falkonry.io', 'auth-token')

publication   = Schemas.Publication() \                 
                .set_type('WEBHOOK') \                  #set Publication type
                .set_path('https://test.example.com/getFalkonryData') \
                .set_headers({                          #set headers to send 
                    'Authorization': 'Token 1234567890'
                })

#create Publication
publication   = falkonry.create_publication('pipeline_id', publication)

#delete Publication
falkonry.delete_publication('pipeline_id', publication)
```

## Docs

   [Falkonry APIs](https://service.falkonry.io/api)
     
## Tests

  To run the test suite, first install the dependencies, then run `Test.sh`:
  
```bash
$ pip install -r requirements.txt
$ python test/*.py
```

## License

  Available under [MIT License](LICENSE)
