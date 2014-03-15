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
    tests_require=["mock>1.0.0"],
    install_requires = [
        "nose>1.3",
        "setuptools>2.2",
        "objc>=2.5.1"

    ],
    test_suite='tests',
    license="MIT License",
    description="Display live status of all your test running in the background",
    long_description=open("README.md").read(),
    entry_points = {
        'nose.plugins.0.10': [
            'nosepride = nosepride:Nosepride'
        ]
    }
)