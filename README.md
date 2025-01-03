[![PyPI version](https://badge.fury.io/py/pydykit.svg)][url_pypi_this_package]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<!-- [![DOI](https://zenodo.org/badge/440932364.svg)][url_latest_doi] -->
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# `PHDAEDiscreteGradients`

This repository contains the source code, which contains selected contributions of the paper

```bibtex
@article{KinonMorandinSchulze2025,
    author = {Philipp L. Kinon, Riccardo Morandin and Philipp Schulze},
    title = {Discrete-gradient methods of port-Hamiltonian descriptor systems},
    journal = {arXiv},
    ...
    doi = {...},
    url = {...}
}
```

and largely depends on the [`pydykit` package][pydykit_repo].

Please see [license][url_license],
[acknowledgment](#acknowledgment)
and cite the [paper given above][url_article] and the latest [Zenodo-DOI][url_latest_doi].

## Installation

1. [Clone][url_how_to_clone] this repository to your machine.
2. Open a terminal and navigate to your local clone.
3. Create a new [virtual environment][url_env_python] and activate it. We recommend using `venv`:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

4. Install pydykit from
[![PyPI](https://badge.fury.io/py/pydykit.svg)][url_pypi_this_package]
```bash
pip install pydykit
```


## Run scripts
In the terminal, with the activated environment, run your desired script:
   ```bash
   python scripts/*.py
   ```

## Acknowledgements

The research documented in this repository has been funded by the
[German Research Foundation (DFG, Deutsche Forschungsgemeinschaft)][dfg_website] - project number
<!-- [255730231][dfg_project]. -->

[dfg_website]: https://www.dfg.de/
<!-- [dfg_project]: https://gepris.dfg.de/gepris/projekt/255730231 -->

[url_license]: LICENSE
<!-- [url_latest_doi]: https://zenodo.org/badge/latestdoi/440932364 -->
<!-- [url_article]: https://doi.org/10.1016/j.mechmat.2022.104307 -->
[url_how_to_clone]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

[url_env_python]: https://docs.python.org/3/tutorial/venv.html

[url_pypi_this_package]: https://pypi.org/project/pydykit/

[pydykit_repo]: https://github.com/pydykit/pydykit/
