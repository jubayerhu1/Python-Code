# virtul Environment 


Pip list -> it will all show lib | PIP is the package installer for Python and serves as the primary tool for installing and managing external Python libraries and packages
-----  
conda env list 
create :
conda crate -n env_name python=3.9 -y
conda create --name env_name python=3.9 -y

conda env list

conda activate env_name
conda deactivate env_name

remve envronment :
conda remove -n env_name --all
conda remove --name env_name --all

----------
inside folder to crate environment :
conda crate --prfix .\env_name python=3.9 -y

conda activate env_name
romove :
conda remove -p .\v-env2 --all

pip list 