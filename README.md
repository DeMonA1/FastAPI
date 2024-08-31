# FastAPI
##Start
Start: > py main.py
       > curl -method [POST, GET, PUT, DELETE] -uri <http://127.0.0.1:8080/>
              -headers @{"accept"="application/json"; "Content-Type"="applcation/json"      ; "Authorization"="Bearer >access-token<"}
                                                                     "x-www-form-urlencoded"
              -body '{"xx":"xx",.....}'
Tests
Library: pytest.
Commands: > pytest #all tests
          > pytest ***.py
          > coverage run -m pytest
          > coverage  report
          > coverage html
          
## 🌟 Highlights

- Some functionality made easy!
- This problem handled
- etc.


## ℹ️ Overview

This is simple FastAPI app which emplement without rendering of templates.

Tests can be implement on Windows and Linux with curl.

## 🚀 Usage

```bash
pytest        #all tests

pytest ***.py

coverage run -m pytest

coverage  report

coverage html
```


```py
>>> import mypackage
>>> mypackage.do_stuff()
'Oh yeah!'
```


## ⬇️ Installation

Simple, understandable installation instruction.

```bash
pip install -r requirements.txt
```

And be sure to specify any other minimum requirements like Python versions or operating systems.

*You may be inclined to add development instructions here, don't.*


## 💭 Feedback and Contributing

Add a link to the Discussions tab in your repo and invite users to open issues for bugs/feature requests.

This is also a great place to invite others to contribute in any ways that make sense for your project. Point people to your DEVELOPMENT and/or CONTRIBUTING guides if you have them.
