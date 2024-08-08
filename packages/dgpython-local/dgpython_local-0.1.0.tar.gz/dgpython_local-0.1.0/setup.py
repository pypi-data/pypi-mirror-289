import sys

from setuptools import setup, Extension
from setuptools_scm import get_version
import os
import os.path
import re
import shutil
import subprocess
import glob
from setuptools.command.install import install
try:
    from setuptools.command.build import build
    pass
except ModuleNotFoundError:
    from distutils.command.build import build
    pass

# Be sure to set local_identifier
# to something that clearly identifies your organization
# or laboratory. It may contain ASCII characters a-z and
# A-Z and digits 0-9 and periods.

local_identifier=None
#local_identifier="thermal.cnde.iastate.edu"



ext_modules = []
package_data = {
    "dgpython_local": ["*.dpi"]
}

#To add scripts, make dgpython_local/bin its own package (with
#a __init__.py) and put scripts in this directory giving each
#a "main" function. Then put the names of the scripts in the
#console_scripts list here. Don't forget to also list them in
#[project.scripts] in pyproject.toml
console_scripts=[]

console_scripts_entrypoints = [ "%s = dgpython_local.bin.%s:main" % (script,script.replace("-",'_')) for script in console_scripts ]


def local_version_scheme(version): #version is a setuptools_scm.ScmVersion object.
    #print("Local_Version_Scheme")
    time_format="%Y%m%d"
    if version.exact or version.node is None:
        return version.format_choice(
            "", "+d{time:{time_format}}", time_format=time_format
        )
    else:
        if local_identifier is not None:
            return version.format_choice(
                "+{local_identifier:s}.{node}", "+{local_identifier:s}.{node}.d{time:{time_format}}", time_format=time_format, local_identifier=local_identifier
            )
        else:
            return version.format_choice(
                "+{node}", "+{node}.d{time:{time_format}}", time_format=time_format
            )
        pass
    pass

if __name__ == "__main__":
    
        
    setup(name="dgpython_local",
          description="local module definitions for dataguzzler python",
          author="Stephen D. Holland",
          #version=version,
          url="http://thermal.cnde.iastate.edu",
          ext_modules=[],
          zip_safe=False,
          cmdclass={
        
          },
          packages=[
              "dgpython_local",
              #    "dgpython_local.bin",
          ],
          package_data=package_data,
          entry_points={"console_scripts": console_scripts_entrypoints },
          # NOTE: We are using get_version() here because with current
          # setuptools_scm (8.0.4) we don't consistently get our local
          # version scheme with the local_identifier to be used.
          # The following must all work:
          #     python -m setuptools_scm
          #     python -m build .   # (perhaps with --no-isolation)
          #     python -m pip install .  # (perhaps with --no-build-isolation) 
          version=get_version(local_scheme=local_version_scheme),
          use_scm_version={"local_scheme": local_version_scheme }
          )
    pass 
