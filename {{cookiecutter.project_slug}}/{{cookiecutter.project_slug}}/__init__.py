# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
import os.path
version_filename = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_filename) as version_file:
    __version__ = version_file.read().strip()
