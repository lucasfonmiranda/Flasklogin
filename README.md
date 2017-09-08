    Flask-Login example
    
 - Requirements
 
 ```shell
 pip install flask
 ```
 
 - Example to create one app flask:
 
```python
import flask
from flask import Flask

app = Flask(__name__)

```

- Example to access one route:

```python
@app.route('/')
def index():
  return '<h1>Hello World</h1>
```

- Example to determine one route:

```python
if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 4000)
```