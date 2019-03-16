from setuptools import setup

setup(
    name="horimote",
    version="0.4.1",
    author="Ben Lebherz & Auke Willem Oosterhoff",
    author_email="b@benleb.de",
    description="Async API wrapper for Samsumgs set-top boxes SMT-G7400 and SMT-G7401.",  # NOQA
    url="https://github.com/benleb/horimote",
    packages=["horimote"],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia",
    ],
)
