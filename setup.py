#!/usr/bin/env python
######################################################################
# \file
# \author David J. Kessler <david.j.kessler@jpl.nasa.gov>
# \brief
#
# \copyright
# Copyright 2009-2016, by the California Institute of Technology.
# ALL RIGHTS RESERVED.  United States Government Sponsorship
# acknowledged. Any commercial use must be negotiated with the Office
# of Technology Transfer at the California Institute of Technology.
# \copyright
# This software may be subject to U.S. export control laws and
# regulations.  By accepting this document, the user agrees to comply
# with all U.S. export laws and regulations.  User has the
# responsibility to obtain export licenses, or other export authority
# as may be required before exporting such information to foreign
# countries or providing access to foreign persons.
######################################################################

from setuptools import setup, find_packages

setup(
    name="password-gen",
    description='Random Password Generator',
    author='David J Kessler',
    author_email='djkessler@me.com',
    install_requires=[
        'cracklib',
        ],
    packages=find_packages(),
    scripts=[
        'pwdgen']
)
