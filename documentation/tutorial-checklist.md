---
jupytext:
  notebook_metadata_filter: myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"user_expressions": []}

# Tutorial checklist

```{note}
This guidelines also apply to [blog posts](https://ploomber.io/blog/)
```

## Sample data must be publicly available

Datasets must be available publicly so we can download them inline. In other words, you should be able to get a URL that when opened should take you to the raw data ([example](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv)). Furthermore, the data should be available in a third-party site and not uploaded to any of our repositories.

This will allow us to use is like this:

```{code-cell} ipython3
from urllib.request import urlretrieve
import pandas as pd

urlretrieve("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv", "penguins.csv")
pd.read_csv("penguins.csv").head()
```
