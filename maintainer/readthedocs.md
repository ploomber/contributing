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
