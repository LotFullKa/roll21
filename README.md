# roll21
[![codecov](https://codecov.io/gh/ProKam/roll21/branch/develop/graph/badge.svg?token=EBKPNYKPN1)](https://codecov.io/gh/ProKam/roll21)
![Django Test](https://github.com/ProKam/roll21/workflows/Django%20Test/badge.svg)

* look coverage report on [codecov.io](https://codecov.io/gh/ProKam/roll21)

## Local setup

### Run project on docker
- You can use it if us have docker and docker compose installed on your workstation
- Just run `docker-compose up -d` and navigate to [localhost:8080](http://localhost:8080)

### Python
- Setup python >= 3.7
- run `pip install pipenv`
- navigate to project dir
- run pipenv `install`
- If u need to activate your environment in shell run `pipenv shell`

### Run local django server
- python manage.py migrate
- run `python manage.py runserver`

### Vuejs
- navigate to `frontend` dir
- run `npm install`

### Serve frontend
- run `npm run serve` in `frontend` dir
