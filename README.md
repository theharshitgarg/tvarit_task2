# This app solves the following problem

```
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as
command line arguments and output is to be printed on screen
```


## Installation

Make sure the that the ptython version is >=3.8. 

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
$ make virtualenv

$ source env/bin/activate

```

### Intall dependencies

To install the dependencies, run the following:


```
$ pip install -r requirements.txt
```

## Run 

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

Go to the project root directory and execute the command:

```
$ make run
```
Alternatively, you can try 

```
$ docker-compose up
```

## Examples

To get the examples, you can try the following commands

```
$ make show_examples
$ make show_success_examples
$ make show_error_examples
```

Alternatively,

```
$ sh examples/test_api.sh
$ sh examples/test_api_errors.sh
```

## Testcases

The command to test it as follows:

```
$ make test

or

$ python tvarit_backend/manage.py test tvarit_backend
```

## Docker

Included is a basic `Dockerfile` for building and running the application, and can be built with the included `make` helper:

```
$ make docker
```

