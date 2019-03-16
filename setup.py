from setuptools import setup

setup(
    name="horimote",
    version="0.4.1",
    author="Ben Lebherz & Auke Willem Oosterhoff",
    author_email="git@benleb.de",
    description="Async API wrapper for Samsumgs set-top boxes SMT-G7400 and SMT-G7401.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/benleb/horimote",
    packages=["horimote"],
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia",
    ],
)
