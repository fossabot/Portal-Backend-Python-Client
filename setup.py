from setuptools import setup

setup(
    name="portal_client",
    version="0.1",
    description="Client to interact with Portal's API for application management",
    url="https://github.com/Innoactive/Portal-Backend-Python-Client",
    author="Benedikt Reiser",
    author_email="benedikt.reiser@innoactive.de",
    license="Apache2",
    packages=["portal_client"],
    scripts=["bin/innoactive-portal"],
    zip_safe=False,
)
