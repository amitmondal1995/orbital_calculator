# Orbital Mechanics Assignment

This is the assignment of Orbital Mechanics.

## Run

- The server can directly be run using prebuilt docker image

```shell
docker run --rm -it -p 8000:8000 ghcr.io/ayush1325/orbital_calculator:main
```

## Development

### Virtualenv

1. Create virtualenv:
```shell
python -m venv .venv
```
2. Install dependencies
```shell
pip install -r requirements.txt
```
3. Run Server
```shell
python manage.py runserver
```
4. Goto `http://localhost:8000/`

### Docker

1. Build Image
```shell
docker build . -t orbital_calculator_dev
```
2. Run Image
```shell
docker run --rm -it -p 8000:8000 orbital_calculator_dev
```
3. Goto `http://localhost:8000/`

- Note: This is only tested on Linux.

## How to Contribute

Here is a video showing the PR process for anyone unfamiliar

[![PR Process](https://img.youtube.com/vi/8lGpZkjnkt4/maxresdefault.jpg)](https://youtu.be/8lGpZkjnkt4)

- Add your task/formula in a file under `calculator_gui/tasks/somthing.py`. Remember to add your name and admission number as commments.
- Create a function that takes any inputs the formula needs as inputs.
- Add any extra dependencies you use in the `requirements.txt`.
- Add some Django tests. At least add 1 test to ensure that the function does not crash. I do not care if the output is correct but the function should not crash.
- Use [Python type hints](https://docs.python.org/3/library/typing.html) in argumentes and for return type of the function that backend is supposed to use. This is to ensure that I can make appropriate conversions before calling the function.
- Format code properly

## Things to Remember

- If you are not using python, add a python wrapper around your code so that it can be used from python. I will not accept it otherwise.
- Do not use Exceptions. Instead return None or something else.

## Helpful Links

- [Testing in Django](https://docs.djangoproject.com/en/5.0/topics/testing/)
