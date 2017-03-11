# Install virtualenv.
pip2 install virtualenv

# Create a virtualenv.
virtualenv -p `which python2` .venv

# Activate the virtualenv.
source .venv/bin/activate

# Install the dependencies.
pip install -r requirements.txt
