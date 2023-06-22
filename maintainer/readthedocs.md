# Readthedocs

This is the default configuration we use:

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "mambaforge-4.10"

  jobs:
    # delete pre_build if using conf.py, keep it if using _config.yml
    pre_build:
      - "jupyter-book config sphinx doc/"

    # this will print all dependencies and versions, useful for debugging
    post_create_environment:
      - "conda env export"

conda:
  environment: doc/environment.yml

sphinx:
  builder: html
  fail_on_warning: true

```

More details below.

## `fail_on_warning`

At this time of writing, Jupyter Book (`0.13.1`) only emits warnings (not errors) when
a notebook fails. Hence, the only way to make the readthedocs build fail is by setting
`fail_on_warning`.


```yaml
sphinx:
  builder: html
  fail_on_warning: true
```

However, this setting makes the doc building process too strict.

## Build docs on PRs

[See here.](https://github.com/readthedocs/actions/tree/main/preview)

## Debugging failed notebooks

Readthedocs includes ANSI color codes in the notebook's traceback, which are unreadable in the readthedocs build. Example:

```
Cell [0;32mIn[4], line 3[0m
[1;32m      1[0m [38;5;28;01mfrom[39;00m [38;5;21;01msklearn_evaluation[39;00m [38;5;28;01mimport[39;00m plot
[0;32m----> 3[0m cm [38;5;241m=[39m [43mplot[49m[38;5;241;43m.[39;49m[43mInteractiveConfusionMatrix[49m[38;5;241;43m.[39;49m[43mfrom_raw_data[49m[43m([49m
[1;32m      4[0m [43m    [49m[43my_test[49m[38;5;241;43m.[39;49m[43mtolist[49m[43m([49m[43m)[49m[43m,[49m
[1;32m      5[0m [43m
```


To fix it, use the following script, which will print the logs in your terminal (which can render ANSI color codes):

```python
pip install pyppeteer

# get the script
curl -O https://raw.githubusercontent.com/ploomber/contributing/main/scripts/rtdlogs.py

# run it
python rtdlogs.py https://readthedocs.org/projects/PROJECT/builds/BUILD
```


More info: https://github.com/ploomber/contributing/issues/77
