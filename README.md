# FastAPI

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
