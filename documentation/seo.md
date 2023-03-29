# SEO

## HTML metadata

### `.md` files

Add the following `myst` section:

```yaml
---
jupytext:
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
