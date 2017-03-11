#!/bin/sh
aws --profile "$AWS_PROFILE" \
  lambda update-function-code \
  --function askSweden222 \
  --zip-file fileb://ask-sweden.zip
