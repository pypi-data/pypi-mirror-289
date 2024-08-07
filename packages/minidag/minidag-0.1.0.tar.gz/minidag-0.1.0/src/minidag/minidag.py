import logging
from functools import wraps
from collections import OrderedDict
import inspect
from graphlib import TopologicalSorter

__all__ = ["MiniDAG"]


class MiniDAG:
    """
    Bare minimum DAG implementation for in-process sorting of jobs with
    dependency injection. Runs jobs in topological order.

    Usage:
    ```python
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
    """

    def __init__(self):
        self.graph = OrderedDict()
        self.context = {}
        self.jobs = {}

    def job(self):
        def decorator(f):
            name = f.__name__
            spec = inspect.getfullargspec(f)
            arg_names = spec[0]

            for arg in arg_names:
                if arg not in self.graph:
                    self.graph[arg] = []
                self.graph[arg].append(name)
            self.graph[name] = []
            self.jobs[name] = f

            @wraps(f)
            def wrapper(*args, **kwargs):
                self.jobs[f.__name__] = f
                return f(*args, **kwargs)

            return wrapper

        return decorator

    def run(self, **kwargs):
        for k, v in kwargs.items():
            self.context[k] = v

        ts = TopologicalSorter(self.graph)
        jobs_in_order = reversed(tuple(ts.static_order()))

        for job in jobs_in_order:
            if job in self.context:
                # input values added via kwargs to run
                continue

            if job not in self.jobs:
                raise ValueError(f"Job {job} not found in jobs")

            logging.info(f"Running job {job}")
            func = self.jobs[job]
            spec = inspect.getfullargspec(func)
            arg_names = spec[0]
            kwargs = {arg: self.context[arg] for arg in arg_names}
            result = func(**kwargs)
            self.context[job] = result

        return self.context
