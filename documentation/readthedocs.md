At this time of writing, Jupyter Book (`0.13.1`) only emits warnings (not errors) when
a notebook fails. Hence, the only way to make the readthedocs build fail is by setting
`fail_on_warning`.


```yaml
sphinx:
  builder: html
  fail_on_warning: true
```

However, this setting makes the doc building process too strict.