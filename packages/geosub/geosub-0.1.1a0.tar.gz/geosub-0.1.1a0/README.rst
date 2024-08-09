.. image:: https://github.com/dmayo3/geosub/actions/workflows/ci.yaml/badge.svg
    :target: https://github.com/dmayo3/geosub/actions/workflows/ci.yaml?query=branch%3Amain
    :alt: Github Actions Status
.. image:: https://codecov.io/github/dmayo3/geosub/graph/badge.svg?token=A0WO17S0KD
 :target: https://codecov.io/github/dmayo3/geosub
.. image:: https://readthedocs.org/projects/geosub/badge/?version=latest
    :target: https://geosub.readthedocs.io/en/stable/?badge=latest
    :alt: Documentation Status
.. image:: https://badge.fury.io/py/geosub.svg
    :target: https://badge.fury.io/py/geosub
    :alt: PyPI Package
.. image:: https://img.shields.io/pypi/pyversions/geosub.svg
    :target: https://pypi.org/project/geosub
    :alt: Supported versions
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code style: black
.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: Type checked by mypy
.. image:: https://img.shields.io/badge/License-CC%20BY%204.0%20%2B%20MIT-yellow
   :target: https://github.com/dmayo3/geosub/blob/main/LICENSE
   :alt: License


geosub v0.1.1a0
---------------

Docs: https://geosub.readthedocs.io/

Lookup ISO 3166-2 geographic subdivisions from postal and country codes, using GeoNames and pycountry.

Adapted from a very similar library for looking up timezones: https://github.com/dmayo3/geotz

Motivation
----------

1. Easy to use. No API key or external API service required.

2. Fast offline lookup.

3. No downloads required; the necessary data comes bundled with the package.

4. No network requests.

5. I tried to keep the extra dependencies to a minimum. Only pycountry is required.

6. Data is loaded from disk on demand, so as to not use unnecessary memory.

Development
-----------

To run the build, there's the GitHub actions workflows as well as the option to run locally.

For running the build locally, use `pip install tox` and the run `tox` in the repository base
directory (or `tox -p` to run the build in parallel).

1. Ensure you have `tox` installed e.g. by running `pip install tox`

2. Extract data `tox -e extract_data`

3. Run the build: `tox`
