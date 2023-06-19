Summary of changes from all Ploomber products. Used internally to create social media content. The entries are usually a subset of what we publish in each `CHANGELOG.md`.


## JupySQL - 0.7.9 (2023-06-19)

* [Feature] Modified `histogram` command to support data with NULL values ([#176](https://github.com/ploomber/jupysql/issues/176))
* [Feature] Automated dependency inference when creating CTEs. `--with` is now deprecated and will display a warning. ([#166](https://github.com/ploomber/jupysql/issues/166))
* [Feature] Close all connections when Python shuts down ([#563](https://github.com/ploomber/jupysql/issues/563))
* [Fix] Fixed `ResultSet` class to display result table with proper style and added relevant example ([#54](https://github.com/ploomber/jupysql/issues/54))
* [Fix] Fixed `Set` method in `Connection` class to recognize same descriptor with different aliases  ([#532](https://github.com/ploomber/jupysql/issues/532))
* [Fix] Added bottom-padding to the buttons in table explorer. Now they are not hidden by the scrollbar ([#540](https://github.com/ploomber/jupysql/issues/540))
* [Fix] `psutil` is no longer a dependency for JupySQL ([#541](https://github.com/ploomber/jupysql/issues/541))
* [Fix] Validating arguments passed to `%%sql` ([#561](https://github.com/ploomber/jupysql/issues/561))
* [Doc] Added bar and pie examples in the plotting section ([#564](https://github.com/ploomber/jupysql/issues/564))
* [Doc] Added more details to the SQL parametrization user guide. ([#288](https://github.com/ploomber/jupysql/issues/288))
* [Doc] Snowflake integration guide ([#384](https://github.com/ploomber/jupysql/issues/384))
* [Doc] User guide on using JupySQL in `.py` scripts ([#449](https://github.com/ploomber/jupysql/issues/449))


## Ploomber - 0.22.4 (2023-06-01)

* [Feature] Add `executor` option to NotebookRunner to choose ploomber-engine or papermill. ploomber-engine provides enhanced capabilities for debugging, testing and monitoring notebook execution ([Documentation](https://docs.ploomber.io/en/latest/cookbook/nb_executors.html))
* [Fix] Fix error in `ScriptRunner` that didn't allow to import modules in script's directory ([#1072](https://github.com/ploomber/ploomber/issues/1072)) 

## JupySQL - 0.7.8 (2023-06-01)

* [Feature] Add `%sqlplot bar` and `%sqlplot pie` (#508) ([Example](https://jupysql.ploomber.io/en/latest/api/magic-plot.html#sqlplot-bar))

## JupySQL - 0.7.7 (2023-05-31)

* [Feature] `%sql --connections` now displays an HTML table in Jupyter and a text-based table in the terminal ([Example](https://jupysql.ploomber.io/en/latest/api/magic-sql.html#list-connections))
* [Doc] Hiding connection string when passing `--alias` when opening a connection ([#432](https://github.com/ploomber/jupysql/issues/432)) ([Example](https://jupysql.ploomber.io/en/latest/howto.html#hide-connection-string))
* [Doc] Added Howto documentation for enabling JupyterLab cell runtime display ([#448](https://github.com/ploomber/jupysql/issues/448)) ([Example](https://jupysql.ploomber.io/en/latest/howto/benchmarking-time.html))

