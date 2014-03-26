try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="EKGnose",
    author="Francis Lavoie",
    author_email="lav.francis@gmail.com",
    url="https://github.com/francisl/EKGnose",
    version="0.1.0",
    packages=[
        "EKGnose"
    ],
    tests_require=["mock>1.0.0"],
    install_requires = [
        "nose",
        "setuptools"
    ],
    test_suite='tests',
    license="MIT License",
    description="Display live status of all your test running in the background",
    long_description=open("README.md").read(),
    entry_points = {
        'nose.plugins.0.10': [
            'ekgnose = EKGnose.plugin:EKGnose'
        ]
    }
)