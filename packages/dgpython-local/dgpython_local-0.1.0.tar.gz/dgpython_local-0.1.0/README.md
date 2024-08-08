dgpython-local
==============

dgpython-local is a placeholder package that is intended so you
can make your own private branches with dataguzzler-python
configuration local to your organization, laboratory, or system.

In most cases you don't want to install the published version,
except possibly as a placeholder until you have your own
customizations in place. Instead, make your customizations
to dgpython_local/local.dpi that define equipment installed
locally, and then install your customized version.

Be sure to set local_identifier in setup.py to
something that clearly identifies your organization or laboratory.
It may contain ASCII characters a-z and A-Z and digits 0-9 and
periods.

The example dgpython_local/local.dpi illustrates how you can
provide local functionality. Since it is all Python code,
you can perform operations such as checking the hostname
to select appropriate equipment, or you can just keep
different customized versions for different computers.

Basic requirements are Python v3.8 or above with the following
packages: numpy, setuptools, wheel, build, setuptools_scm, pip

Basic installation is (possibly as root or Administrator):
    pip install --no-deps --no-build-isolation .


