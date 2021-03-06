#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-twilio-encrypted',
    version='0.5.0',
    description="A django-otp plugin that delivers tokens via Twilio's SMS service.",
    long_description=open('README.rst').read(),
    author='Peter Sagerson',
    author_email='psagersDjwublJf@ignorare.net',
    packages=find_packages(),
    include_package_data=True,
    url='git+https://github.com/prototypsthlm/otp_twilio_encrypted',
    license='BSD',
    install_requires=[
        'django-otp >= 0.5.0',
        'requests',
        'django-extensions'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)
