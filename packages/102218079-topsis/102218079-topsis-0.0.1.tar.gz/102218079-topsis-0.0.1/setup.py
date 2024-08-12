from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.0.1'
DESCRIPTION = 'topsis program'
LONG_DESCRIPTION = 'TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a decision-making method that helps identify the most suitable alternative by evaluating how close each option is to the ideal solution and how far it is from the worst-case scenario. The process involves normalizing the decision matrix to standardize performance measures, applying weights to reflect the importance of different criteria, and calculating distances from the ideal and negative-ideal solutions. By determining the relative closeness of each alternative to the ideal solution, TOPSIS provides a straightforward way to rank options and make informed decisions based on multiple criteria.'

# Setting up
setup(
    name="102218079-topsis",
    version=VERSION,
    author="aabha manroa",
    author_email="aabhamanroa@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)