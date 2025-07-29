from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements():
    requirements = []
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Tanishk",
    author_email="tanishkkumarshrivastava@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)