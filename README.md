# Robot Toy Challenge

## Testing
Pytest was used to write tests for this program. To turn the tests: 

``python -m pytest -s tests``

To get a coverage report, please run:

1. ``coverage run --source=toy_robot -m pytest -v tests``

2. ``coverage report``

3. ``coverage report --show-missing`` (to get the lines that are missing)