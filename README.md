# jnote
jupyter notebook/python toy project

# Setting up development environment

* Install [anaconda](https://www.anaconda.com/distribution/) for your system.

* Checkout the code and create a python environment.

```bash
git clone https://github.com/tulay/jnote.git
cd jnote
conda env create -f environment.yml
conda activate jnote

#Once done
conda deactive
```

* Then import project in IntelliJ and add a Python SDK using Conda Environment setup before.
* If you need to re-create environment, you need to remove it first.

```bash
# To remove the env to start from scratch
conda env remove -n jnote
```

* For minor update, you can also simply update it
```bash
conda activate jnote
conda env update --file environment.yml
```
# Jupyter Notebook
Refer to documentation about [Notebook](https://jupyter.readthedocs.io/en/latest/running.html)
```bash
jupyter notebook jnote.ipynb
```
