[![Falkonry Logo](https://app.falkonry.ai/img/logo.png)](http://falkonry.com/)

[![Build status](https://img.shields.io/travis/Falkonry/falkonry-python-client.svg?style=flat-square)](https://travis-ci.org/Falkonry/falkonry-python-client)

Falkonry Python Client to access [Falkonry Condition Prediction](falkonry.com) APIs

[Releases](https://github.com/Falkonry/falkonry-python-client/releases)



## Installation

```bash
$ pip install falkonryclient
```

## Features

    * Create Datastream for narrow/historian style data from a single entity
    * Create Datastream for narrow/historian style data from a multiple entities
    * Create Datastream for wide style data from a single entity
    * Create Datastream for wide style data from a multiple entities
    * Create Datastream with microseconds precision
    * Create Datastream for batch identifier
    * Retrieve Datastreams
    * Retrieve Datastream by Id
    * Delete Datastream
    * Add EntityMeta to a Datastream
    * Get EntityMeta of a Datastream
    * Add historical narrow input data (json format) to multi entity Datastream (Used for model revision)
    * Add historical narrow input data (csv format) single entity to Datastream (Used for model revision)
    * Add historical wide input data (json format) to single entity Datastream (Used for model revision)
    * Add historical wide input data (csv format) to multi entity Datastream (Used for model revision)
    * Add live input data (json format) to Datastream (Used for live monitoring) 
    * Add live input data (csv format) to Datastream (Used for live monitoring) 
    * Add live input data (json format) from a stream to Datastream (Used for live monitoring) 
    * Add live input data (csv format) from a stream to Datastream (Used for live monitoring)
    * Add narrow input data (csv format) with batch identifier to multi entity Datastream
    * Add narrow input data (json format) with batch identifier to single entity Datastream
    * Add wide input data (csv format) with batch identifier to multi entity Datastream
    * Add wide input data (json format) with batch identifier to single entity Datastream
    * Create Assessment
    * Retrieve Assessments
    * Retrieve Assessment by Id
    * Delete Assessment
    * Get Condition List Of Assessment
    * Add facts data (json format) to Assessment of single entity datastream
    * Add facts data (json format) with addition tag to Assessment of multi entity datastream
    * Add facts data (csv format) to Assessment of single entity datastream
    * Add facts data (csv format) with tags Assessment of single entity datastream
    * Add facts data (json format) from a stream to Assessment of multi entity datastream
    * Add facts data (csv format) from a stream to  Assessment of multi entity datastream
    * Get Historian Output from Assessment
    * Get Streaming Output
    * Get Facts Data
    * Get Input Data of Datastream
    * Datastream On (Start live monitoring of datastream)
    * Datastream Off (Stop live monitoring of datastream)

## Quick Start
```
    * Get auth token from Falkonry Service UI
    * Read the examples provided for integration with various data formats
```

## Examples 

#### Create Datastream for narrow/historian style data from a single entity
    
Data :

```
    {"time" :"2016-03-01T01:01:01Z", "tag" : "signal1", "value" : 3.4}
    {"time" :"2016-03-01T01:01:02Z", "tag" : "signal2", "value" : 9.3}

    or

    time, tag, value
    2016-03-01T01:01:01Z, signal1, 3.4
    2016-03-01T01:01:02Z, signal2, 9.3
```

Usage :
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream
time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("iso_8601")                                 # set time format of the datastream
field.set_time(time)            
signal.set_valueIdentifier("value")                         # set value identifier
signal.set_signalIdentifier("signal")                       # set signal identifier
field.set_signal(signal)                                    # set signal in field
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
        
#create Datastream
createdDatastream = fclient.create_datastream(datastream)
```

#### Create Datastream for narrow/historian style data from multiple entities
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "signal" : "signal1", "entity" : "entity1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:02", "signal" : "signal2", "entity" : "entity2", "value" : 1.4}
    {"time" :"2016-03-01 01:01:03", "signal" : "signal3", "entity" : "entity3", "value" : 9.3}
    {"time" :"2016-03-01 01:01:04", "signal" : "signal2", "entity" : "entity2", "value" : 4.3}

    or

    time,signal,entity,value
    2016-03-01 01:01:01,signal1,entity1,3.4
    2016-03-01 01:01:01,signal2,entity2,1.4
    2016-03-01 01:01:01,signal3,entity3,9.3
    2016-03-01 01:01:01,signal4,entity4,4.3
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream
time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("YYYY-MM-DD HH:mm:ss")                      # set time format of the datastream
field.set_time(time)
signal.set_valueIdentifier("value")                         # set value identifier
field.set_signal(signal)                                    # set signal in field
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
        
#create Datastream
createdDatastream = fclient.create_datastream(datastream)
```

#### Create Datastream for wide style data from a single entity
   
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
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()
input1 = Schemas.Input()
input2 = Schemas.Input()
input3 = Schemas.Input()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream

input1.set_name("Signal1")                                  # set name of input signal
input1.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input1.set_event_type("Samples")                            # set event type of input signal
input2.set_name("Signal2")                                  # set name of input signal
input2.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input2.set_event_type("Samples")                            # set event type of input signal
input3.set_name("Signal3")                                  # set name of input signal
input3.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input3.set_event_type("Samples")                            # set event type of input signal
inputs = []
inputs.append(input1)
inputs.append(input2)
inputs.append(input3)

time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("millis")                                   # set time format of the datastream
field.set_time(time)            
field.set_signal(signal)                                    # set signal in field
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
datastream.set_inputs(inputs)
        
#create Datastream
createdDatastream = falkonry.create_datastream(datastream)
```

#### Create Datastream for wide style data from multiple entities

Data :

```python
    {"time":1467729675422, "entity": "entity1", "signal1":41.11, "signal2":82.34, "signal3":74.63, "signal4":4.8}
    {"time":1467729668919, "entity": "entity2", "signal1":78.11, "signal2":2.33, "signal3":4.6, "signal4":9.8}

    or

    time, entity, signal1, signal2, signal3, signal4
    1467729675422, entity1, 41.11, 62.34, 77.63, 4.8
    1467729675445, entity1, 43.91, 82.64, 73.63, 3.8
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()
input1 = Schemas.Input()
input2 = Schemas.Input()
input3 = Schemas.Input()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream

input1.set_name("Signal1")                                  # set name of input signal
input1.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input1.set_event_type("Samples")                            # set event type of input signal
input2.set_name("Signal2")                                  # set name of input signal
input2.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input2.set_event_type("Samples")                            # set event type of input signal
input3.set_name("Signal3")                                  # set name of input signal
input3.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input3.set_event_type("Samples")                            # set event type of input signal
inputs = []
inputs.append(input1)
inputs.append(input2)
inputs.append(input3)

time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("millis")                                   # set time format of the datastream
field.set_time(time)            
field.set_signal(signal)                                    # set signal in field
field.set_entityIdentifier("entity")                         # set entity identifier as "entity"
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
datastream.set_inputs(inputs)
        
#create Datastream
createdDatastream = falkonry.create_datastream(datastream)
```

#### Create Datastream with microseconds precision

Data :

```
    {"time" :"2016-03-01 01:01:01", "signal" : "signal1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:02", "signal" : "signal2", "value" : 9.3}

    or

    time,signal,value
    2016-03-01 01:01:01,signal1,3.4
    2016-03-01 01:01:02,signal2,9.3
```

Usage :
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream
datastream.set_time_precision("micro")                      # this is use to store your data in different date time format. If input data precision is in micorseconds then set "micro" else "millis". If not sent then it will be "millis"
time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("YYYY-MM-DD HH:mm:ss")                      # set time format of the datastream
field.set_time(time)            
signal.set_valueIdentifier("value")                         # set value identifier
signal.set_signalIdentifier("signal")                       # set signal identifier
field.set_signal(signal)                                    # set signal in field
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
        
#create Datastream
createdDatastream = fclient.create_datastream(datastream)
```

#### Create Datastream for batch identifier

Data :

```
    {"time" :"2016-03-01 01:01:01", "signal1" : 3.4, "signal2" : 5.1, "signal3": 7.4, "batch": "batch_1"}
    {"time" :"2016-03-01 01:01:02", "signal1" : 13.4, "signal2" : 15.1, "signal3": 17.4, "batch": "batch_1"}

    or

    time, signal1, signal2, signal3, batch
    2016-03-01 01:01:01, 3.4, 5.1, 7.4, batch_1
    2016-03-01 01:01:02, 13.4, 15.1, 17.4, batch_1
```

Usage :
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
datastream = Schemas.Datastream()
datasource = Schemas.Datasource()
field = Schemas.Field()
time = Schemas.Time()
signal = Schemas.Signal()
input1 = Schemas.Input()
input2 = Schemas.Input()
input3 = Schemas.Input()

datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream

input1.set_name("Signal1")                                  # set name of input signal
input1.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input1.set_event_type("Samples")                            # set event type of input signal
input2.set_name("Signal2")                                  # set name of input signal
input2.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input2.set_event_type("Samples")                            # set event type of input signal
input3.set_name("Signal3")                                  # set name of input signal
input3.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
input3.set_event_type("Samples")                            # set event type of input signal
inputs = []
inputs.append(input1)
inputs.append(input2)
inputs.append(input3)

time.set_zone("GMT")                                        # set timezone of the datastream
time.set_identifier("time")                                 # set time identifier of the datastream
time.set_format("iso_8601")                                 # set time format of the datastream
field.set_time(time)
field.set_signal(signal)                                    # set signal in field
field.set_batchIdentifier("batch")                          # set batchIdentifier in field
datasource.set_type("STANDALONE")                           # set datastource type in datastream
datastream.set_datasource(datasource)
datastream.set_field(field)
datastream.set_inputs(inputs)
        
#create Datastream
createdDatastream = fclient.create_datastream(datastream)
```

#### Retrieve Datastreams
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')
        
#return list of Datastreams
datastreams = falkonry.get_datastreams()
```

#### Retrieve Datastream by id
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'
        
#return sigle datastream
datastreams = falkonry.get_datastream(datastreamId)
```

#### Delete Datastream by id
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'
        
falkonry.delete_datastream(datastreamId)
```

#### Add EntityMeta to a Datastream

Data :

```python
     [{"sourceId": "testId","label": "testName","path": "root/path"}]
```

Usage :
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry = Falkonry('http://localhost:8080', 'auth-token')
data = [{"sourceId": "testId","label": "testName","path": "root/path"}]
datastreamId = 'id of the datastream'

entityMetaResponse = fclient.add_entity_meta(datastreamId, {}, data)
```

#### Get EntityMeta of a Datastream

Data :

```python
     [{"sourceId": "testId","label": "testName","path": "root/path"}]
```

Usage :
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry = Falkonry('http://localhost:8080', 'auth-token')
datastreamId = 'id of the datastream'

entityMetaResponse = fclient.get_entity_meta(datastreamId)
```

#### Add historical narrow input data (json format) to multi entity Datastream (Used for model revision)
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "signal" : "current", "value" : 12.4, "car" : "car1"}
    {"time" :"2016-03-01 01:01:01", "signal" : "vibration", "value" : 3.4, "car" : "car1"}
    {"time" :"2016-03-01 01:01:01", "signal" : "state", "value" : on, "car" : "car1"}
    {"time" :"2016-03-01 01:01:01", "signal" : "current", "value" : 31.4, "car" : "car2"}
    {"time" :"2016-03-01 01:01:01", "signal" : "vibration", "value" : 2.4, "car" : "car2"}
    {"time" :"2016-03-01 01:01:01", "signal" : "state", "value" : off, "car" : "car2"}
```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"current\", \"value\" : 12.4, \"car\" : \"car1\"} + "\n"
        + "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"vibration\", \"value\" : 2.4, \"car\" : \"car1\"} + "\n"
        + "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"state\", \"value\" : on, \"car\" : \"car1\"} + "\n"
        + "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"current\", \"value\" : 22.4, \"car\" : \"car2\"} + "\n"
        + "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"vibration\", \"value\" : 3.4, \"car\" : \"car2\"} + "\n"
        + "{\"time\" :\"2016-03-01 01:01:01\", \"signal\" : \"state\", \"value\" : off, \"car\" : \"car2\"}";

        
# set hasMoreData to True if data is sent in batches. When the last batch is getting sent then set  'hasMoreData' to False. For single batch upload it shpuld always be set to False
options = {'streaming': False,
           'hasMoreData': False,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time",
           'signalIdentifier': 'signal',
           'valueIdentifier': 'value',
           'entityIdentifier': 'car'}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, data)
```

#### Add historical narrow input data (csv format) single entity to Datastream (Used for model revision)
    
Data :

```
    time, signal, value
    2016-03-01 01:01:01, current, 3.4
    2016-03-01 01:01:01, vibration, 1.4

```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = "time,signal,value " + "\n"
        + "2016-03-01 01:01:01,current,3.4" + "\n"
        + "2016-03-01 01:01:01,vibration,1.4";
        
# set hasMoreData to True if data is sent in batches. When the last batch is getting sent then set  'hasMoreData' to False. For single batch upload it shpuld always be set to False
options = {'streaming': False,
           'hasMoreData': False,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time"}
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, data)
```

#### Add historical wide input data (json format) to single entity Datastream (Used for model revision)
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}
    {"time" :"2016-03-01 01:01:02", "current" : 11.3, "vibration" : 2.2, "state" : "On"}
    {"time" :"2016-03-01 01:01:03", "current" : 10.5, "vibration" : 3.8, "state" : "On"}
    {"time" :"2016-03-01 01:02:03", "current" : 19.2, "vibration" : 3.8, "state" : "On"}
    {"time" :"2016-03-01 01:02:03", "current" : 1.2, "vibration" : 0.8, "state" : "Off"}
    {"time" :"2016-03-01 01:02:05", "current" : 0.2, "vibration" : 0.3, "state" : "Off"}
```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
stream   = io.open('./data.json')
        
# set hasMoreData to True if data is sent in batches. When the last batch is getting sent then set  'hasMoreData' to False. For single batch upload it shpuld always be set to False

options = {'streaming': False,
           'hasMoreData': False,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time"}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, stream)
```

#### Add historical wide input data (csv format) to multi entity Datastream (used for model revision)

Data :

```
    time,signal,value,car
    2016-03-01 01:01:01,current,3.4,car1
    2016-03-01 01:01:02,current,2.2,car1
    2016-03-01 01:01:03,vibration,3.8,car1
    2016-03-01 01:02:03,vibration,3.8,car1
    2016-03-01 01:02:03,state,on,car2
    2016-03-01 01:02:05,state,off,car2
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
stream   = io.open('./dataMultientity.csv')

# set hasMoreData to True if data is sent in batches. When the last batch is getting sent then set  'hasMoreData' to False. For single batch upload it shpuld always be set to False

options = {'streaming': False,
           'hasMoreData': False,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time"}
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, stream)
```

#### Add live input data (json format) to a Datastream (Used for live monitoring) 
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "signal" : "signal1", "entity" : "entity1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:02", "signal" : "signal2", "entity" : "entity2", "value" : 1.4}
    {"time" :"2016-03-01 01:01:03", "signal" : "signal3", "entity" : "entity3", "value" : 9.3}
    {"time" :"2016-03-01 01:01:04", "signal" : "signal2", "entity" : "entity2", "value" : 4.3}
```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = "{\"time\" : \"2016-03-01 01:01:01\", \"signal\" : \"signal1\", \"entity\" : \"entity1\", \"value\" : 3.4}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:01\", \"signal\" : \"signal2\", \"entity\" : \"entity2\", \"value\" : 1.4}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:02\", \"signal\" : \"signal3\", \"entity\" : \"entity3\", \"value\" : 9.3}" + "\n"
        + "{\"time\" : \"2016-03-01 01:01:02\", \"signal\" : \"signal4\", \"entity\" : \"entity4\", \"value\" : 4.3}";
        
options = {'streaming': True,
           'hasMoreData': True,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time",
           'signalIdentifier': 'signal',
           'entityIdentifier': 'entity',
           'valueIdentifier': 'value'}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, data)
```

####  Add live data (csv format) to a Datastream (Used for live monitoring) 
    
Data :

```
    time,signal,entity,value
    2016-03-01 01:01:01,signal1,entity1,3.4
    2016-03-01 01:01:01,signal2,entity2,1.4
    2016-03-01 01:01:01,signal3,entity3,9.3
    2016-03-01 01:01:01,signal4,entity4,4.3

```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = "time,signal,entity,value" + "\n"
        + "2016-03-01 01:01:01,signal1,entity1,3.4" + "\n"
        + "2016-03-01 01:01:01,signal2,entity1,1.4";
        
options = {'streaming': True,
           'hasMoreData': False}
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, data)
```

#### Add live data (json format) from a stream to a Datastream (Used for live monitoring)
    
Data :

```
    {"time" :"2016-03-01 01:01:01", "signal" : "signal1", "entity" : "entity1", "value" : 3.4}
    {"time" :"2016-03-01 01:01:02", "signal" : "signal2", "entity" : "entity2", "value" : 1.4}
    {"time" :"2016-03-01 01:01:03", "signal" : "signal3", "entity" : "entity3", "value" : 9.3}
    {"time" :"2016-03-01 01:01:04", "signal" : "signal2", "entity" : "entity2", "value" : 4.3}
```

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
stream   = io.open('./data.json')
        
options = {'streaming': True,
           'hasMoreData': False,
           'timeFormat': "YYYY-MM-DD HH:mm:ss",
           'timeZone': "GMT",
           'timeIdentifier': "time",
           'signalIdentifier': 'signal',
           'entityIdentifier': 'entity',
           'valueIdentifier': 'value'}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, stream)
```

#### Add live data (csv format) from a stream to a Datastream (Used for live monitoring)
    
Data :

```
    time,signal,entity,value
    2016-03-01 01:01:01,signal1,entity1,3.4
    2016-03-01 01:01:01,signal2,entity2,1.4
    2016-03-01 01:01:01,signal3,entity3,9.3
    2016-03-01 01:01:01,signal4,entity4,4.3
```

Usage :  

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
stream   = io.open('./data.csv')
        
options = {'streaming': True}   
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, stream)
```

#### Add narrow input data (csv format) with batch identifier to multi entity Datastream

Data :

```
    time,batchId,unit,signal,value
    1467729675010,batch_1,unit1,signal1,9.95
    1467729675020,batch_1,unit1,signal1,4.45
    1467729675030,batch_2,unit1,signal1,1.45
    1467729675040,batch_2,unit1,signal1,8.45
    1467729675050,batch_2,unit1,signal1,2.45
    1467729675010,batch_1,unit1,signal2,19.95
    1467729675020,batch_1,unit1,signal2,14.45
    1467729675030,batch_2,unit1,signal2,10.45
    1467729675040,batch_2,unit1,signal2,18.45
    1467729675050,batch_2,unit1,signal2,12.45
    1467729675010,batch_1,unit1,signal3,39.95
    1467729675020,batch_1,unit1,signal3,34.45
    1467729675030,batch_2,unit1,signal3,30.45
    1467729675040,batch_2,unit1,signal3,38.45
    1467729675050,batch_2,unit1,signal3,32.45
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = 'time,batchId,unit,signal,value\n'
    +'1467729675010,batch_1,unit1,signal1,9.95\n'
    +'1467729675020,batch_1,unit1,signal1,4.45\n'
    +'1467729675030,batch_2,unit1,signal1,1.45\n'
    +'1467729675040,batch_2,unit1,signal1,8.45\n'
    +'1467729675050,batch_2,unit1,signal1,2.45\n'
    +'1467729675010,batch_1,unit1,signal2,19.95\n'
    +'1467729675020,batch_1,unit1,signal2,14.45\n'
    +'1467729675030,batch_2,unit1,signal2,10.45\n'
    +'1467729675040,batch_2,unit1,signal2,18.45\n'
    +'1467729675050,batch_2,unit1,signal2,12.45\n'
    +'1467729675010,batch_1,unit1,signal3,39.95\n'
    +'1467729675020,batch_1,unit1,signal3,34.45\n'
    +'1467729675030,batch_2,unit1,signal3,30.45\n'
    +'1467729675040,batch_2,unit1,signal3,38.45\n'
    +'1467729675050,batch_2,unit1,signal3,32.45\n'
        
options = {
    'streaming': False,
    'hasMoreData': False
}
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, data)
```

#### Add narrow input data (json format) with batch identifier to single entity Datastream

Data :

```
    {"time": 1467729675010,"batchId": "batch_1","signal": "signal1","value": 9.95}
    {"time": 1467729675020,"batchId": "batch_1","signal": "signal1","value": 4.45}
    {"time": 1467729675030,"batchId": "batch_2","signal": "signal1","value": 1.45}
    {"time": 1467729675040,"batchId": "batch_2","signal": "signal1","value": 8.45}
    {"time": 1467729675050,"batchId": "batch_2","signal": "signal1","value": 2.45}
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = '{"time": 1467729675010,"batchId": "batch_1","signal": "signal1","value": 9.95}\n'
    +'{"time": 1467729675020,"batchId": "batch_1","signal": "signal1","value": 4.45}\n'
    +'{"time": 1467729675030,"batchId": "batch_2","signal": "signal1","value": 1.45}\n'
    +'{"time": 1467729675040,"batchId": "batch_2","signal": "signal1","value": 8.45}\n'
    +'{"time": 1467729675050,"batchId": "batch_2","signal": "signal1","value": 2.45}'
        
options = {
    'streaming': False,
    'hasMoreData': False,
    'timeFormat': time.get_format(),
    'timeZone': time.get_zone(),
    'timeIdentifier': time.get_identifier(),
    'signalIdentifier': 'signal',
    'valueIdentifier': 'value',
    'batchIdentifier': 'batchId'
}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, data)
```

#### Add wide input data (csv format) with batch identifier to multi entity Datastream

Data :

```
    time,batchId,unit,signal1,signal2,signal3
    1467729675010,batch_1,unit1,9.95,19.95,39.95
    1467729675020,batch_1,unit1,4.45,14.45,34.45
    1467729675030,batch_2,unit1,1.45,10.45,30.45
    1467729675040,batch_2,unit1,8.45,18.45,38.45
    1467729675050,batch_2,unit1,2.45,12.45,32.45
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = 'time,batchId,unit,signal1,signal2,signal3\n'+
    '1467729675010,batch_1,unit1,9.95,19.95,39.95\n'+
    '1467729675020,batch_1,unit1,4.45,14.45,34.45\n'+
    '1467729675030,batch_2,unit1,1.45,10.45,30.45\n'+
    '1467729675040,batch_2,unit1,8.45,18.45,38.45\n'+
    '1467729675050,batch_2,unit1,2.45,12.45,32.45'
        
options = {
    'streaming': False,
    'hasMoreData': False
}
inputResponse = falkonry.add_input_data(datastreamId, 'csv', options, data)
```

#### Add wide input data (json format) with batch identifier to single entity Datastream

Data :

```
    {"time": 1467729675010,"batchId": "batch_1","signal1": 9.95,"signal2": 19.95,"signal3": 39.95}
    {"time": 1467729675020,"batchId": "batch_1","signal1": 4.45,"signal2": 14.45,"signal3": 34.45}
    {"time": 1467729675030,"batchId": "batch_2","signal1": 1.45,"signal2": 10.45,"signal3": 30.45}
    {"time": 1467729675040,"batchId": "batch_2","signal1": 8.45,"signal2": 18.45,"signal3": 38.45}
    {"time": 1467729675050,"batchId": "batch_2","signal1": 2.45,"signal2": 12.45,"signal3": 32.45}
```

Usage :

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

#add data to Datastream
String data = '{"time": 1467729675010,"batchId": "batch_1","signal1": 9.95,"signal2": 19.95,"signal3": 39.95}\n'
    +'{"time": 1467729675020,"batchId": "batch_1","signal1": 4.45,"signal2": 14.45,"signal3": 34.45}\n'
    +'{"time": 1467729675030,"batchId": "batch_2","signal1": 1.45,"signal2": 10.45,"signal3": 30.45}\n'
    +'{"time": 1467729675040,"batchId": "batch_2","signal1": 8.45,"signal2": 18.45,"signal3": 38.45}\n'
    +'{"time": 1467729675050,"batchId": "batch_2","signal1": 2.45,"signal2": 12.45,"signal3": 32.45}'
        
options = {
    'streaming': False,
    'hasMoreData': False,
    'timeFormat': time.get_format(),
    'timeZone': time.get_zone(),
    'timeIdentifier': time.get_identifier(),
    'batchIdentifier': 'batchId'
}
inputResponse = falkonry.add_input_data(datastreamId, 'json', options, data)
```

#### Create Assessment

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

datastreamId = 'id of the datastream'

asmtRequest = Schemas.AssessmentRequest()
asmtRequest.set_name('Assessment Name'))         # Set new assessment name
asmtRequest.set_datastream(response.get_id())    # Set datatsream id
asmtRequest.set_rate('PT0S')                     # Set assessment rate

# create new assessment
assessmentResponse = fclient.create_assessment(asmtRequest)
```

#### Retrieve Assessments

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

assessmentResponse = fclient.get_assessments()
```

#### Retrieve Assessment by Id

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

assessmentId = 'id of the assessment'
assessmentResponse = fclient.get_assessment(assessmentId)
```

#### Delete Assessment

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

assessmentId = 'id of the assessment'
assessmentResponse = fclient.delete_assessment(assessmentId)
```

#### Get Condition List Of Assessment

Usage :    

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry   = Falkonry('http://localhost:8080', 'auth-token')

assessmentId = 'id of the assessment'
assessmentResponse = fclient.get_assessment(assessmentId)

// aprioriConditionList 
conditionList = assessment.get_aprioriConditionList()

```

#### Add facts data (json format) to Assessment of a multi entity datastream
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('http://localhost:8080', 'auth-token')

assessmentId = 'id of the assessment'
data          = '{"time" : "2011-03-26T12:00:00.000Z", "car" : "HI3821", "end" : "2012-06-01T00:00:00.000Z", "Health" : "Normal"}'

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'entityIdentifier': "car",
        'valueIdentifier': "Health"
    }
inputResponse = falkonry.add_facts(assessmentId, 'json', options, data)
```

#### Add facts data (json format) to Assessment of a single entity datastream

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
data          = '{"time" : "2011-03-26T12:00:00.000Z", "end" : "2012-06-01T00:00:00.000Z", "Health" : "Normal"}'

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'valueIdentifier': "Health"
    }
inputResponse = falkonry.add_facts(assessmentId, 'json', options, data)

```


#### Add facts data (json format) with addition tag to Assessment of multi entity datastrea
    
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
data          = '{"time" : "2011-03-26T12:00:00.000Z", "car" : "HI3821", "end" : "2012-06-01T00:00:00.000Z", "Health" : "Normal"}'

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'entityIdentifier': "car",
        'valueIdentifier': "Health",
        'additionalTag': "testTag"
    }
inputResponse = falkonry.add_facts(assessmentId, 'json', options, data)
```

#### Add facts data (csv format) to Assessment of single entity datastream

```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
data          = 'time,end,Health' + "\n"
                 + '2011-03-26T12:00:00.000Z,2012-06-01T00:00:00.000Z,Normal' + "\n"
                 + '2014-02-10T23:00:00.000Z,2014-03-20T12:00:00.000Z,Spalling';

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'valueIdentifier': "Health"
    }

inputResponse = falkonry.add_facts(assessmentId, 'csv', options, data)
```

#### Add facts data (csv format) with tags Assessment of multi entity datastream
```python
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

#instantiate Falkonry
falkonry      = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
data          = 'time,car,end,Health,Tag' + "\n"
                 + '2011-03-26T12:00:00.000Z,HI3821,2012-06-01T00:00:00.000Z,Normal,testTag1' + "\n"
                 + '2014-02-10T23:00:00.000Z,HI3821,2014-03-20T12:00:00.000Z,Spalling,testTag2';

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'entityIdentifier': "car",
        'valueIdentifier': "Health",
        'tagIdentifier': 'Tag'
    }

inputResponse = falkonry.add_facts(assessmentId, 'csv', options, data)
```

#### Add facts data (json format) from a stream to Assessment of a multi entity datastream

Sample file:
```
    {"time" : "2011-03-26T12:00:00.000Z", "car" : "HI3821", "end" : "2012-06-01T00:00:00.000Z", "Health" : "Normal"}
    {"time" : "2014-02-10T23:00:00.000Z", "car" : "HI3821", "end" : "2014-03-20T12:00:00.000Z", "Health" : "Spalling"}
```

```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
stream   = io.open('./factsData.json')

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'entityIdentifier': "car",
        'valueIdentifier': "Health"
    }

response = falkonry.add_facts_stream(assessmentId, 'json', options, stream)

```

#### Add facts data (csv format) from a stream to Assessment of a multi entity datastream

Sample File
```
    time,car,end,Health
    2011-03-26T12:00:00.000Z,HI3821,2012-06-01T00:00:00.000Z,Normal
    2014-02-10T23:00:00.000Z,HI3821,2014-03-20T12:00:00.000Z,Spalling
```

```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas
from falkonryclient import schemas as Schemas

falkonry = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
stream   = io.open('./factsData.csv')

options = {
        'startTimeIdentifier': "time",
        'endTimeIdentifier': "end",
        'timeFormat': "iso_8601",
        'timeZone': time.get_zone(),
        'entityIdentifier': "car",
        'valueIdentifier': "Health"
    }

response = falkonry.add_facts_stream(assessmentId, 'csv', options, stream)

```


#### Get Historian Output from Assessment (Generate output for given time range)
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'

options = {'startTime':'2011-01-01T01:00:00.000Z','endTime':'2011-06-01T01:00:00.000Z','format':'application/json'}

response = fclient.get_historical_output(assessment, options)

'''If data is not readily available then, a tracker id will be sent with 202 status code. While falkonry will generate output data
 Client should do timely pooling on the using same method, sending tracker id (__id) in the query params
 Once data is available server will response with 200 status code and data in json/csv format.'''

if response.status_code is 202:
    trackerResponse = Schemas.Tracker(tracker=response._content)
    #get id from the tracker
    trackerId = trackerResponse.get_id()
    #use this tracker for checking the status of the process.
    options = {"tarckerId": trackerId, "format":"application/json"}
    newResponse = fclient.get_historical_output(assessment, options)
    '''if status is 202 call the same request again
    if status is 200, output data will be present in httpResponse.response field'''
```


#### Get Streaming output of Assessment
    
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
options = {"format":"text/csv"}
stream    = falkonry.get_output(assessmentId, options)
for event in stream.events():
    print(json.dumps(json.loads(event.data)))
```


#### Get Facts Data
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
assessmentId = 'id of the assessment'
options = {'startTime':'2011-01-01T01:00:00.000Z','endTime':'2011-06-01T01:00:00.000Z','format':'application/json',}
response = falkonry.get_facts(assessmentId, options)
print(response.text)
```

#### Get Input Data of Datastream
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
datastreamId = 'id of the datastream'
options = {'format':"application/json"}
response = fclient.get_datastream_data(datastream, options)
pprint(response.text)
```
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
datastreamId = 'id of the datastream'
options = {'format':"text/csv"}
response = fclient.get_datastream_data(datastream, options)
pprint(response.text)
```



#### Datastream On (Start live monitoring of datastream)
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
datastreamId = 'id of the datastream'

# Starts live monitoring of datastream. For live monitoring, datastream must have at least one assessment with an active model. 
response = falkonry.on_datastream(datastreamId)
```

#### Datastream Off (Stop live monitoring of datastream)
```python
import os, sys
from falkonryclient import client as Falkonry
from falkonryclient import schemas as Schemas

falkonry  = Falkonry('http://localhost:8080', 'auth-token')
datastreamId = 'id of the datastream'

# Stops live monitoring of datastream.
response = falkonry.off_datastream(datastreamId)
```

## Docs

   [Falkonry APIs](http://localhost:8080/api)
     
## Tests

  To run the test suite, first install the dependencies, then run `Test.sh`:
  
```bash
$ pip install -r requirements.txt
$ python test/*.py
```

##Run test cases from test directory

## License

  Available under [MIT License](LICENSE)
