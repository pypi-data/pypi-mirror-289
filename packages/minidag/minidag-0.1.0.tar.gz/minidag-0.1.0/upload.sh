#!/bin/bash
python -m build
rye run twine upload --repository pypi dist/*