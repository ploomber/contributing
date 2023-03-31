# Writting docs


Most documentation files are written in MyST format, which is an extension of the Markdown (hence, the `.md` extension). This guide will show you the basics of writting MyST files.

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


## SEO metadata

Each documentation file must contain metadata for search engines. Here's the format depending on the extension type.

### `.md` files

Add the following `myst` section:

```yaml
---
jupytext:
  notebook_metadata_filter: myst # ADD THIS IF MISSING!

  # some existing metadata
  ...

myst:
  html_meta:
    description lang=en: "Some description"
    keywords: "Key1, Key2"
    property=og:locale: "en_US"
---
```

### `.ipynb` files

Add the following `myst` section:

```json
{
    "myst": {
        "html_meta": {
            "description lang=en": "Description",
            "keywords": "Key1, Key2",
            "property=og:locale": "en_US"
        }
    }
}
```

To open the metadata editor:

![jupyter-metadata](../assets/jupyter-metadata.png)

### `.rst` files

```rst
.. meta::
    :description lang=en:
        Some description
    :keywords: Tag1, Tag2
```


## Tutorials

By default, `.md` are static. However, in many cases, we want them to be runnable, meaning the code will be executed (and results displayed) when building the documentation.

[Here's an example](https://jupysql.ploomber.io/en/latest/integrations/duckdb.html) of runnable content. To make your `.md` file runnable, [see here.](../documentation/notebooks.md)
