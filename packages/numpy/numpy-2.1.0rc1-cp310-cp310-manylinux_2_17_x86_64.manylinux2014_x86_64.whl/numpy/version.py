
"""
Module to expose more detailed version info for the installed `numpy`
"""
version = "2.1.0rc1"
__version__ = version
full_version = version

git_revision = "6592a643be720354c9b8ef0d6d3f97ed0710d0e4"
release = 'dev' not in version and '+' not in version
short_version = version.split("+")[0]
