# Formatting


Most documentation files are written in MyST format, which is an extension of the Markdown (hence, the `.md` extension). This guide will show you the basics of writting MyST files.

## Runnable content

By default, `.md` are static. However, in many cases, we want them to be runnabel, meaning the code will be executed (and results displayed) when building the documentation.

[Here's an example](https://jupysql.ploomber.io/en/latest/integrations/duckdb.html) of runnable content.

To make your `.md` file runnable, [see here.](../documentation/notebooks.md)

## Links

### Link to another page

```
[some text](../contributing/setup.md)
```

Example: [some text](../contributing/setup.md).

### Link to specific section


```
[link to section](../contributing/setup.md#pre-requisites)
```

Example: [link to section](../contributing/setup.md#pre-requisites).

```{warning}
Linking to a specific section can be tricky, as not all sections work automatically. For more information see [jupyter-book documentation](https://jupyterbook.org/en/stable/content/references.html).
```
## Admonitions

Admonitions allow you to grab reader's attention:

~~~
```{warning}
Some warning
```
~~~

Example:

```{warning}
Some warning
```

~~~
```{note}
Some note
```
~~~

Example:

```{note}
Some note
```

For more information, see [jupyter-book documentation.](https://jupyterbook.org/en/stable/reference/cheatsheet.html#admonitions)

