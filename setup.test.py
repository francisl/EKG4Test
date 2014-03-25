### SETUP FOR TESTS, TEST DON'T REQUIRE PYOBJC - SHOULD BE TESTABLE ON OTHER OS THAN OSX
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setup import setup_var

setup_var["install_requires"] = []

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