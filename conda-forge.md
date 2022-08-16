# Conda-forge

Some of our packages are available on conda-forge. To upload a new package, follow the instructions [(longer version here)](https://conda-forge.org/docs/maintainer/adding_pkgs.html#generating-the-recipe):

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
- Add the `LICENSE` file at `staged-recipes/recipes/LICENSE`
