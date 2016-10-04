#!/bin/sh
make html
cd output
git add .
git commit -m "Update the contents"
git push origin master
cd ..
git add output
git commit -m "Update output version"
git push origin master
