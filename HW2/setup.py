from setuptools import setup, find_packages

setup(
    name="DSSS - Homework 2",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Maps "math_quiz" command to the main function
        ],
    },
    author="Rohit Potdukhe",
    author_email="rohit.potdukhe@fau.de",
    license="Apache License 2.0",
    url="https://github.com/rohitpotdukhe01/dsss_homework_2",
)
