[![PyPI version](https://badge.fury.io/py/pydykit.svg)][url_pypi_this_package]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- [![arXiv](https://img.shields.io/badge/arXiv-1234.56789-b31b1b.svg)](https://arxiv.org/abs/1234.56789) -->
<!-- [![DOI](https://zenodo.org/badge/440932364.svg)][url_latest_doi] -->

# `PHDAEDiscreteGradients`

This repository contains the source code, which contains selected contributions of the paper
_Kinon, P. L., Morandin, R. & Schulze, P. (2025): Discrete-gradient methods for port-Hamiltonian descriptor systems_.
<!-- [Kinon, P. L., Morandin, R. & Schulze, P. (2025): Discrete-gradient methods for port-Hamiltonian descriptor systems][url_article]. -->
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#citation">Citation</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>

## Citation

If you found our project helpful or you have used it in your academic work, please consider citing it:

```bibtex
@article{kinon_morandin_schulze_2025,
  title   = {Discrete gradient methods for port-Hamiltonian descriptor systems},
  author  = {Kinon, Philipp L. and Morandin, Riccardo and Schulze, Philipp},
  year    = {2025}
}
```
  <!-- ,
  journal = {ArXiv e-print XY},
  doi     = {DOI} -->
<!-- } -->

<!-- and the latest [Zenodo-DOI][url_latest_doi]. -->
Please see [license][url_license].
<!-- and [acknowledgements](#acknowledgements). -->


## Installation

The implementation of time integrators and example systems has been done in the package [`pydykit`][pydykit_repo], which is used here.

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
pip install pydykit==0.0.6
```


## Usage

This repo can be used in two ways:

1. For validation:

   Extract your desired result data as `.csv`-file data from the [results folder](results).

2. For verification:

   In the terminal, with the activated environment, run your desired script:
   ```bash
   python scripts/*.py
   ```
   This will overwrite the correspoding results file in the [results folder](results). For the error analysis choose the desired integration scheme in the respective script.

<!-- ## Acknowledgements

The research documented in this repository has been funded by the
[German Research Foundation (DFG, Deutsche Forschungsgemeinschaft)][dfg_website] - project number -->
<!-- [255730231][dfg_project]. -->

[dfg_website]: https://www.dfg.de/
<!-- [dfg_project]: https://gepris.dfg.de/gepris/projekt/255730231 -->

[url_license]: LICENSE
<!-- [url_latest_doi]: https://zenodo.org/badge/latestdoi/440932364 -->
<!-- [url_article]: https://doi.org/10.1016/j.mechmat.2022.104307 -->
[url_how_to_clone]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

[url_env_python]: https://docs.python.org/3/tutorial/venv.html

[url_pypi_this_package]: https://pypi.org/project/pydykit/0.0.6/?cacheSeconds=0

[pydykit_repo]: https://github.com/pydykit/pydykit/
