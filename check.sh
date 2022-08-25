#! /bin/bash

# Check the files

# mypy --follow-imports=silent --ignore-missing-imports --show-column-numbers --no-pretty --strict ./src
# pylint ./src
# pydocstyle ./src
# flake8 ./src
# black --check ./src

## Did we found IP address? Use exit status of the grep command ##
if [ $? -eq 0 ]; then
    echo "All checks passed"
    #exit 0
else
    echo "Checks failed" >&2
    exit 1
fi

# Do tests
pytest ./tests

if [ $? -eq 0 ]; then
    echo "All tests passed"
    #exit 0
else
    echo "Testing failed" >&2
    exit 1
fi

# Check coverage
coverage run --data-file=coverage/.coverage --source=src -m pytest ./tests

# Generate .lcov
coverage lcov --data-file=coverage/.coverage -o coverage/lcov.info

# Generate the report
coverage report --data-file=coverage/.coverage

# COV_SCORE=$($(coverage report --data-file=coverage/.coverage | awk '$1 == "TOTAL" {print $NF+0}') + 0)

# echo $COV_SCORE

# if [[ $COV_SCORE -ge 70 ]]; then
#     echo "Coverage passed"
#     #exit 0
# else
#     echo "Coverage failed" >&2
#     exit 1
# fi
