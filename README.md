# Orbital Mechanics Assignment

This is the assignment of Orbital Mechanics.

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
