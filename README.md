## Sprite2 Client

Example client demonstrates how to use sprite2


### Install

First, you will need to install the requirments:

	pip install -r requirements.txt

### AWS

This example executes your functions on aws lambda.  This requires you to setup and configure your aws account.

Once you have your aws account, please make sure your aws environment is configured.  See the aws cli instructions here: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html:

	aws configure

Finally, you will need to run the sprite2 utilities that manage your executer deployment:

	AWS_PROFILE=[my profile] sprite2 aws-create


### Run

To run, simply execute the python example script:

	AWS_PROFILE=[my profile] python primes.py
