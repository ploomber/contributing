Summary of changes from all Ploomber products. Used internally to create social media content. The entries are usually a subset of what we publish in each `CHANGELOG.md`.

## JupySQL 0.9.0 (2023-08-01)

*Full [changelog here.](https://github.com/ploomber/jupysql/blob/master/CHANGELOG.md#090-2023-08-01)*

* [Feature] Allow loading configuration value from a `pyproject.toml` file upon magic initialization ([#689](https://github.com/ploomber/jupysql/issues/689)) ([Docs](https://jupysql.ploomber.io/en/latest/api/configuration.html#loading-configuration-from-a-pyproject-toml-file))
* [Feature] allows parametrizing queries with `:variable` with `%config SqlMagic.named_parameters = True` ([Docs](https://jupysql.ploomber.io/en/latest/user-guide/template.html#id1))
* [Feature] Using native methods to convert to data frames from DuckDB when using native connections and SQLAlchemy to maximize performance ([Docs](https://jupysql.ploomber.io/en/latest/integrations/duckdb.html))
* [Fix] Fixed a bug when computng histogram bins ([#751](https://github.com/ploomber/jupysql/issues/751)) ([Docs](https://jupysql.ploomber.io/en/latest/user-guide/ggplot.html))

## JupySQL 0.8.0 (2023-07-18)

* [Feature] Better performance when using DuckDB native connection and converting to `pandas.DataFrame` or `polars.DataFrame` (when using a native DuckDB connection, JupySQL now uses DuckDB's [native methods](https://duckdb.org/docs/api/python/overview.html#result-conversion) for converting to `pandas` and `polars`, this allows for maximum performance)
* [Fix] Lazy loading results ([#470](https://github.com/ploomber/jupysql/issues/470)) (when you run a query, only a few rows are fetched from the database to show a data preview. It's only when you request all results that JupySQL will fetch them from the database)


## JupySQL - 0.7.9 (2023-06-19)

* [Feature] Modified `histogram` command to support data with NULL values ([#176](https://github.com/ploomber/jupysql/issues/176)) ([Documentation](https://jupysql.ploomber.io/en/latest/plot.html#histogram))
* [Feature] Automated dependency inference when creating CTEs. `--with` is now deprecated and will display a warning. ([#166](https://github.com/ploomber/jupysql/issues/166)) ([Documentation](https://jupysql.ploomber.io/en/latest/compose.html))
* [Fix] Fixed `ResultSet` class to display result table with proper style and added relevant example ([#54](https://github.com/ploomber/jupysql/issues/54))
* [Doc] Snowflake integration guide ([#384](https://github.com/ploomber/jupysql/issues/384)) ([Documentation](https://jupysql.ploomber.io/en/latest/integrations/snowflake.html))
* [Doc] User guide on using JupySQL in `.py` scripts ([#449](https://github.com/ploomber/jupysql/issues/449)) ([Documentation](https://jupysql.ploomber.io/en/latest/user-guide/py-scripts.html))


## Ploomber - 0.22.4 (2023-06-01)

* [Feature] Add `executor` option to NotebookRunner to choose ploomber-engine or papermill. ploomber-engine provides enhanced capabilities for debugging, testing and monitoring notebook execution ([Documentation](https://docs.ploomber.io/en/latest/cookbook/nb_executors.html))
* [Fix] Fix error in `ScriptRunner` that didn't allow to import modules in script's directory ([#1072](https://github.com/ploomber/ploomber/issues/1072)) 

## JupySQL - 0.7.8 (2023-06-01)

* [Feature] Add `%sqlplot bar` and `%sqlplot pie` (#508) ([Example](https://jupysql.ploomber.io/en/latest/api/magic-plot.html#sqlplot-bar))

## JupySQL - 0.7.7 (2023-05-31)

* [Feature] `%sql --connections` now displays an HTML table in Jupyter and a text-based table in the terminal ([Example](https://jupysql.ploomber.io/en/latest/api/magic-sql.html#list-connections))
* [Doc] Hiding connection string when passing `--alias` when opening a connection ([#432](https://github.com/ploomber/jupysql/issues/432)) ([Example](https://jupysql.ploomber.io/en/latest/howto.html#hide-connection-string))
* [Doc] Added Howto documentation for enabling JupyterLab cell runtime display ([#448](https://github.com/ploomber/jupysql/issues/448)) ([Example](https://jupysql.ploomber.io/en/latest/howto/benchmarking-time.html))

