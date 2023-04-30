# `conda-forge`

Some of our packages are available on conda-forge:

- [ploomber](https://github.com/conda-forge/ploomber-feedstock)
- [ploomber-engine](https://github.com/conda-forge/ploomber-engine-feedstock)
- [ploomber-core](https://github.com/conda-forge/ploomber-core-feedstock)
- [jupysql](https://github.com/conda-forge/jupysql-feedstock)

To upload a new package, follow the instructions [(longer version here)](https://conda-forge.org/docs/maintainer/adding_pkgs.html#generating-the-recipe):

- Fork the [staged-recipes](https://github.com/conda-forge/staged-recipes) repository.
- Clone your fork

```sh
# clone the fork
git clone https://github.com/{your-user}/staged-recipes
git checkout -b {package-name}
cd staged-recipes/recipes

# generate conda-forge recipe
conda create --name grayskull
conda activate grayskull
conda install -c conda-forge grayskull
grayskull pypi --strict-conda-forge {package-name}
```

- Edit the `meta.yaml`, ensure you're listed as maintainer
- Note: there is no need to add the `LICENSE` file at `staged-recipes/recipes/LICENSE` (as their docs suggest) if the LICENSE is already in the `.tar.gz` file.


## Adding version updates

By default, PRs opeened by the bot won't detect version updates. To enable them, add this to the `conda-forge.yml`

```yaml
bot:
  inspection: update-grayskull
```