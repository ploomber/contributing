# Notes on jupyter-book

We use jupyter-book for our documentation (except for the `ploomber` package), here are a few things to  be aware of.

## `_config.yaml`

Default values we use:

```yaml
sphinx:
  config:
    # print traceback, otherwise it'll store
    # it in a file and it won't be visible from
    # readthedocs console
    execution_show_tb: True
```

### Notebook caching

[Caching notebooks](https://jupyterbook.org/en/stable/content/execute.html#trigger-notebook-execution) is convenient for rapid local builds but it's buggy (it relies on the jupyter-cache pacakge). We encountered a problem where one notebook would always crash with a cryptic error, changing to `execute_notebook: auto` fixed it, but this implies losing the caching feature.

```yaml
execute:
    execute_notebook: cache
```

## Binder

We enable binder so user can run our examples.