from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Topsis program'
LONG_DESCRIPTION = 'TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a Python package designed to facilitate multi-criteria decision-making by evaluating and ranking alternatives based on various criteria. It supports data normalization, weight assignment, and computes the Euclidean distances to both ideal and negative-ideal solutions. This method is useful for scenarios like supplier selection, project prioritization, and risk assessment, where multiple factors need to be considered to make an informed decision. The package is easy to integrate into larger systems or use as a standalone tool..'

# Setting up
setup(
    name="102218077_topsis",
    version=VERSION,
    author="Shruti",
    author_email="<ishrutisahota@gmail.com>",
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