from invoke import task


@task
def build(c):
    c.run("jupyter-book build .")
