# Table-Builder App

## About Project
Simple app for generating dynamic Table.

### App contains:
* Core app
* tables app


## Tech Stack
* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* Docker-compose


### AWS
* 

### Linux 

First you need to clone`git clone git@gitlab.com:zero-deposit/....git`

Follow the instructions below:

1. include provided by author variables into `.example.env`
2. run `make first_setup`
3. each subsequent run `make setup`

A specific Super User is created during the setup, with the following credentials provided in the `.env` file:

File `Makefile` contains all the commands needed to run the project.

### Documentation
* Available on `/api/swagger/` path.

### Authentication
* Available paths:  `/api/token/`, `/api/token/refresh/` and `/api/token/verify/`

### Troubleshooting
* Make sure all dependencies are properly installed.
* Docker and Postgres are the proper version installed.
* In case of any problems with the installation, please report to the author of the project.

### TODO..
App needs to be extended by:
* Implement custom UserManager
* Pre-commit with linter/formater
* App needs more tests coverage
* Swagger needs to be adjusted