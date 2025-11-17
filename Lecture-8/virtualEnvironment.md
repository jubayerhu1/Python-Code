# Virtul Environment 


### Pip list 
It will all list | PIP is the package installer for Python and serves as the primary tool for installing and managing external Python libraries and packages
 
conda env list | It will show list of environment

### Create :
conda crate -n env_name python=3.9 -y
conda create --name env_name python=3.9 -y

conda env list

### Acivate environment:
conda activate env_name

### Deacivate environment:
conda deactivate env_name

### Remove envronment :
conda remove -n env_name --all
conda remove --name env_name --all

----------
### Inside folder to crate environment :
conda crate --prfix .\env_name python=3.9 -y

conda activate env_name

### Inside folder to romove environment :
conda remove -p .\v-env2 --all

pip list 