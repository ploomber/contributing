`.github/workflows/scheduled.yml`

```yaml
name: check-for-broken-links

on:
  schedule:
    - cron: '0 8 * * *'

jobs:
  broken-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pkgmt
      - name: Check for broken links
        run: |
          pkgmt check-links
```


`.github/workflows/ci.yml`


```yaml

name: CI

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install 'pkgmt>=0.1.1'
      - name: Check project
        run: |
          pkgmt check
```