# minidag

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/minidag)

Bare minimum DAG implementation for in-process sorting of jobs with
dependency injection. Runs jobs in topological order.

Install:
`pip install minidag`

Usage:
```python
from minidag import MiniDAG

dag = MiniDAG()

@dag.job()
def job1():
    return 1

@dag.job()
def job2(job1):
    return job1 + 1

@dag.job()
def job3(job1, job2):
    return job1 + job2

@dag.job()
def job4(some_external_value, job3)
    return some_external_value + job3

dag.run(some_external_value=10)
# > {'job1': 1, 'job2': 2, 'job3': 3, 'job4': 13, 'some_external_value': 10}
```