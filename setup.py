try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup_var = {
    "name": "EKG4Test",
    "author": "Francis Lavoie",
    "author_email": "lav.francis@gmail.com",
    "url": "https://github.com/francisl/EKG4Test",
    "version": "0.5.1",
    "packages": ["EKG4Test"],
    "tests_require": ["nose", "mock"],
    "install_requires": [],
    "test_suite": 'EKG4Test.tests',
    "license": "MIT License",
    "description": "Display live status of all your test running in the background",
    "long_description": open("README.md").read()
}

setup(
    name=setup_var["name"],
    author=setup_var["author"],
    author_email=setup_var["author_email"],
    url=setup_var["url"],
    version=setup_var["version"],
    packages=setup_var["packages"],
    install_requires=setup_var["install_requires"],
    tests_require=setup_var["tests_require"],
    test_suite=setup_var["test_suite"],
    license=setup_var["license"],
    description=setup_var["description"],
    long_description=setup_var["long_description"]
)

