# `phdae_discrete_gradients`

## How to start

1. Starting on a new machine, create a new virtual environment and activate it. We recommend using `venv`:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

2. Install and use pre-commit

   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. Following [this discussion](https://stackoverflow.com/questions/4830856/is-it-possible-to-use-pip-to-install-a-package-from-a-private-github-repository) we install the pydykit from private repo (currently with specific branch):

   ```bash
   pip install git+ssh://git@github.com/pydykit/pydykit.git
   ```

4. Run your script:
   ```bash
   python scripts/*.py
   ```
