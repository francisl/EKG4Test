### SETUP FOR TESTS, TEST DON'T REQUIRE PYOBJC - SHOULD BE TESTABLE ON OTHER OS THAN OSX
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
    name="EKG4Test",
    author="Francis Lavoie",
    author_email="lav.francis@gmail.com",
    url="https://github.com/francisl/EKG4Test",
    version="0.5.0",
    packages=[
        "EKG4Test"
    ],
    tests_require=["nose", "mock"],
    install_requires=[],
    test_suite='EKG4Test.tests',
    license="MIT License",
    description="Display live status of all your test running in the background",
    long_description=open("README.md").read()
)

