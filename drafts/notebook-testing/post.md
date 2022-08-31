---
title: Testing Jupyter Notebooks
---


## Introduction

If you’re in the data space, you’ll likely use Jupyter notebooks the most from your developer toolbox. However, notebooks do have a reputation of not being "production-friendly". So how do you go from development-friendly to production-friendly notebooks?

As a developer, testing your code—from modular units like classes and functions to larger scripts and notebooks—is important. Writing robust test suites for your notebooks can take them a step closer to production. 

In this guide, we’ll go over four approaches for testing Jupyter notebooks. We’ll enumerate the advantages and limitations of each approach, along with the open-source tool recommendations to implement each of the approaches.

By the end of this tutorial, you'll have learned enough to start testing your Jupyter notebooks. Let's dive in!

## Smoke Testing

* simplest way of testing notebooks, we are just checking if they run
* pretty trivial to implement but it's not robust since we're not testing the code
* good for: checking that all dependencies are documented. code at least executes successfully

example code:

```python
from pathlib import Path
from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File

dag = DAG()
first = NotebookRunner(Path('first.ipynb'), File('out/first.ipynb'), dag=dag)
second = NotebookRunner(Path('second.ipynb'), File('out/second.ipynb'), dag=dag)
first >> second

dag.build() 
```

And a YAML API:

```yaml
tasks:
  - source: first.ipynb
    product: out/first.ipynb

  - source: second.ipynb
    product: out/second.ipynb
```

That you can execute from the CLI:

```
ploomber build
```

you can also use papermill or nbclient, but they're more limited in features

## Snapshot Testing

TODO: summarize from the other blog post and link to it
https://ploomber.io/blog/snapshot-testing/

## Unit Testing

In most cases, notebooks contain function and class definitions that help modularize the code. Testing those functions and classes is a good practice to ensure they are funcioning correctly. Testing an isolated part in our codebase is called a unit test; since we are only testing a part in our code.

If we were working with a regular `.py` file, we could define a function like this:

```python
# my_module.py

def my_function(x, y):
    return x + y
```

And then importing in some other file (say `test_my_module.py`) for testing it:

```python
# test_my_module.py
from my_module import my_function

def test_my_function():
    assert my_function(1, 1) == 2
```

Unfortunately, this isn't straightforward with notebooks (`.ipynb` extension). This is where [testbook](https://github.com/nteract/testbook) comes in: it allows us to extract definitions from notebooks for testing:

```python
# test_my_module.py
from testbook import testbook


@testbook('/path/to/notebook.ipynb', execute=True)
def test_func(tb):
   func = tb.get("my_function")
   assert func(1, 1) == 2
```

Testbook advocates for an interesting approach: to produce self-contained notebooks that contain function, and class definitions. 

Alternatively, we could use [nbdev](https://github.com/fastai/nbdev); which takes the inverse approach that testbook does. In testbook we define a function in a notebook and then we extract that definition and test it in a different file. In contrast, in nbdev we define the functions *and the tests* in the notebook file.

Based on my experience, testbook is better suited when your notebooks are parts of a pipeline; for example, if you're using [ploomber](https://github.com/ploomber/ploomber) and you want to test functions defined in your notebooks; while nbdev is better suited when you're writing Python libraries and you want to use Jupyter as your development environment: nbdev allows you to keep the source code, documentation, examples, and tests in the same file.


## Integration Testing

Developing all your code in a single notebook is an anti-pattern: it makes your codebase hard to test and debug. Furthermore, it complicates collaboration when all the project is contained in a single file.

A better approach is to break our logic into multiple steps, where the output of the first step becomes the input of the second one so on and so forth.

This modularization gives us the opportunity to test the integration of each part (hence, the name). In Data Science, we can use this approach to measure the data quality of each step (that's why these tests are also called data quality tests).

TODO: diagram

For example, you may create a notebook that loads data from the warehouse but before proceeding with further processing, you may want to run a few tests on the data. This practice is extremely useful to stop execution to prevent wrong data form entering our pipeline. For example, you may write a test like this:

```python
# integration_tests.py
import pandas as pd

def test_data_quality(product):
    df = pd.read_csv(product['data'])
    # check 'column' does not have NAs
    assert not df.column.isna().sum()
    # check 'another' has less than 5% NAs
    assert df.another.isna().mean() < 0.05
```

And add it to your pipeline:

```yaml
tasks:
  - source: first.ipynb
    product:
        nb: out/first.ipynb
        data: out/data.csv
    # run function to test data quality once first.ipynb is executed
    on_finish: integration_tests.test_data_quality

  - source: second.ipynb
    product: out/second.ipynb
```

Then, you can execute from the CLI:

```
ploomber build
```

To learn more, check out [the documentation.](https://docs.ploomber.io/en/latest/cookbook/hooks.html)
