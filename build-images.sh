#!/usr/bin/env bash
if test -z "$1"
then
      echo "Usage ./build-images.bash VERSION"
      echo "No version was passed! Please pass a version to the script e.g. 0.1"
      exit 1
fi

VERSION=$1
docker build -t glucose-prediction/app:$VERSION app