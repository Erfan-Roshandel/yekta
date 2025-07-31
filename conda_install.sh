#!/bin/bash
# conda_install.sh

# Create environment
conda env create -f environment.yml

# Activate
conda activate email-classifier

# Initialize NLTK
python -c "import nltk; nltk.download('punkt')"

# Verify
python -c "import sklearn; print(f'scikit-learn {sklearn.__version__} installed')"
