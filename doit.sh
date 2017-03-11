#!/bin/sh
ZIP_FILE=$(pwd)/ask-sweden.zip
cd ask_sweden || exit
zip -r "$ZIP_FILE" ./*
cd "$VIRTUAL_ENV/lib/python2.7/site-packages" || exit
zip -r "$ZIP_FILE" ./*
