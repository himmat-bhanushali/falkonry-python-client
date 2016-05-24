[![Falkonry Logo](http://static1.squarespace.com/static/55a7df64e4b09f03368a7a78/t/569c6441ab281050fe32c18a/1453089858079/15-logo-transparent-h.png?format=500w)](http://falkonry.com/)

[![Build status](https://img.shields.io/travis/Falkonry/falkonry-python-client.svg?style=flat-square)](https://travis-ci.org/Falkonry/falkonry-python-client)

Falkonry Python Client to access [Falkonry Condition Prediction](falkonry.com) APIs

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

    * To create Pipeline
    
```python
from falkonryclient import Falkonry
from falkonryclient import Schemas

falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')

assessment = Schemas.Assessment();
                .set_name('Health')
                .set_input_signals(['current', 'vibration'])
                        
pipeline   = Schemas.Pipeline()
                .set_name('Motor Health')
                .set_thing_name('Motor')
                .set_time_identifier('time')
                .set_time_format('YYYY-MM-DD HH:MM:SS')
                .set_input_signals({'current' : 'Numeric', 'vibration' : 'Numeric'})
                .set_assessment(assessment)
        
createdPipeline = falkonry.createPipeline(pipeline)
```

    * To get all Pipelines
    
```python
from falkonryclient import Falkonry
from falkonryclient import Schemas

falkonry   = Falkonry('https://service.falkonry.io', 'auth-token')
pipelines  = falkonry.getPipelines()
```

    * To add data
    
```python
from falkonryclient import Falkonry
from falkonryclient import Schemas

var data = [
    {
        'time'      : 1456528122024,
        'current'   : 3.86,
        'vibration' : 4.2
    },
    {
        'time'      : 1456528132024,
        'current'   : 4.456,
        'vibration' : 6.8
    },
    {
        'time'      : 1456528142024,
        'current'   : 2.4690,
        'vibration' : 9.3
    }
]

falkonry      = Falkonry('https://service.falkonry.io', 'auth-token')

inputResponse = falkonry.addInput('pipeline_id', data)
```

    * To add data from a stream
    
```python
import os, sys
from falkonryclient import Falkonry
from falkonryclient import Schemas

falkonry = Falkonry('https://service.falkonry.io', 'auth-token')
stream   = open('/tmp/sample.json', 'r')

response = falkonry.addInputFromStream('pipeline_id', stream)
```

    * To get output of a Pipeline
    
```python
import os, sys
from falkonryclient import Falkonry
from falkonryclient import Schemas

falkonry     = Falkonry('https://service.falkonry.io', 'auth-token')
stream       = open('/tmp/sample.json', 'r');
startTime    = '1457018017'; //seconds since unix epoch 
endTime      = '1457028017'; //seconds since unix epoch
outputStream = falkonry.getOutput('pipeline_id', startTime, endTime);
with open("/tmp/pipelineOutput.json", 'w') as outputFile:
    for line in outputStream:
        outputFile.write(line + '\n')
```

## Docs

    * [Falkonry APIs](https://service.falkonry.io/api)
     
## Tests

  To run the test suite, first install the dependencies, then run `Test.sh`:
  
```bash
$ pip install -r requirements.txt
$ python test/*.py
```

## License

  Available under [MIT License](LICENSE)
