## How do?

1. Install `virtualenv`.

       pip2 install virtualenv

2. Create a virtualenv and activate it.

       virtualenv -p `which python2` .venv
       source .venv/bin/activate

3. Activate the virtualenv.

       pip install -r requirements.txt

4. Hackity hack.

5. Create the deployment package.

       ./bundle.sh

6. Push it. Replace `hackweek` with whatever you've called your `awscli` profile.

       aws --profile hackweek lambda update-function-code --function askSweden222 --zip-file fileb://ask-sweden.zip
