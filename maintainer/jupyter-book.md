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

## Notebook caching

[Caching notebooks](https://jupyterbook.org/en/stable/content/execute.html#trigger-notebook-execution) is convenient for rapid local builds but it's buggy (it relies on the jupyter-cache pacakge). We encountered a problem where one notebook would always crash with a cryptic error, changing to `execute_notebook: auto` fixed it, but this implies losing the caching feature.

```yaml
execute:
    execute_notebook: cache
```

## Dynamic Binder links

We build our documentation on each PR. To build dynamic Binder links that allow us to quickly test the code in the PR, we need to make a few changes to the default jupyter-book configuraton:

1. Generate `config.py` from `_config.yml` with `jupyter-book config sphinx path/to/doc`
2. Change `.readthedocs.yml`: we no longer need the `jupyter-book config sphinx` in the pre-build step
3. Update the docs environment (usually `doc/environment.yml`, but check `.readthedocs.yml`): add `pkgmt>=0.1.7` under the `pip` section
4. Modify `conf.py` you can use [sklearn-evaluation's as reference.](https://github.com/ploomber/sklearn-evaluation/blob/master/docs/conf.py)

