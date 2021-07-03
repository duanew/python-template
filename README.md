Intro
=====================
This repository contains python scripts to ????.

Development Pre-Requisities
=====================
* Python 3.7.x+ installed, and ideally on your command line path.

Setting up your local development environment
=====================
It would be best to use a virual environment setup. virtualenv allows your install multiple
python packages separate to your base python installation.

* On command line, navigate to where you have checkout out the code
* Linux
  * virtualenv env
  * . env/bin/activate
  * export PYTHONPATH=/apps/servicenow-python
  * python -m pip install --upgrade pip
  * pip install -r requirements.txt
* Windows
  * C:\python37\python -m venv env
  * env\Scripts\activate
  * set PYTHONPATH=C:\Dev\servicenow-python
  * python -m pip install --upgrade pip
  * pip install -r requirements.txt


NOTE: requirements.txt has all the python dependencies (for your scripts) listed in it. pip install requirements.txt
installs all these dependencies for you

Adding/Editing dependencies
=====================
Make sure you add any python dependency you install to requirements.txt! Otherwise
it will be hard to keep track of all the packages installed.

If you run the following command in your virtualenv, you should be able to see
all the modules/versions you have installed.

* pip freeze

Standards
=====================
The following documentation gives a brief overview on what development practices should be followed
especially the directory structure and naming convention.

Directory Structure
-------------------
* All reusable/scheduled scripts should be placed under the corresponding application
in src/. For example, a script changing configuration within Firescope should be placed
under in src/firescope/
* All single-use/utility scripts should be placed in the src/scratch folder.

Naming Standards
-------------------
* The PEP style guide is to be followed for all naming standards (https://www.python.org/dev/peps/pep-0008/):
    * Modules should have short, all-lowercase names. Underscores can be used
     in the module name if it improves readability. Python packages should also have short,
     all-lowercase names, although the use of underscores is discouraged.
    * Class names should normally use the CapWords convention.
    * Function names should be lowercase, with words separated by underscores as necessary to improve readability.
    * Variable names follow the same convention as function names.
    * mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

Testing
===============
* All reusable scripts and client classes **MUST** have corresponding unit tests. All Pull Requests without
Unit testing should be **DECLINED**.
* Modules in the scratch folder *do not require* unit testing but if they reference new
functions within the application folder, those functions in the application folder will require
unit testing.
