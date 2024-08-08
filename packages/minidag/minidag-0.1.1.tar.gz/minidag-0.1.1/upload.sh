#!/bin/bash
rm -rf dist
python -m build
rye run twine upload --repository pypi dist/*