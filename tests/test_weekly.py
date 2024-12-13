from importlib import util
from pathlib import Path

import pytest

script_path = Path("./scripts")


def get_python_files(directory):
    # Use Path.glob to find all .py files in the directory
    python_files = [str(file.absolute().stem) for file in Path(directory).glob("*.py")]
    return python_files


def load_file_as_module(name, location):
    spec = util.spec_from_file_location(name, location)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# def run_script_code(script_name):
#     with open(script_name) as file:
#         script_content = file.read()
#     exec(script_content)


class TestExamples:
    @pytest.mark.parametrize(
        ("publication_scripts"),
        (
            pytest.param(
                get_python_files(directory=script_path),
            ),
        ),
    )
    def test_run_scripts(self, publication_scripts):

        for script in publication_scripts:
            load_file_as_module(
                name=script, location=script_path.joinpath(f"{script}.py")
            )
