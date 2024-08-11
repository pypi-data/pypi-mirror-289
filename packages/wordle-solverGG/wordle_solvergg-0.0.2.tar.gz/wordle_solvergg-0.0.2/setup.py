from setuptools import setup, find_packages

setup(
    name="wordle_solverGG",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pyautogui',
    ],
    author="Your Name",
    author_email="firi8228@gmail.com",
    description="A package to automatically solve Wordle puzzles",
    long_description="This package provides functionality to automatically solve Wordle puzzles using Selenium and PyAutoGUI.",
    url="http://example.com/wordle_solver",
)