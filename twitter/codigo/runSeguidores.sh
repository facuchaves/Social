#/bin/sh

git pull

source ../bin/activate

python mainSeguidores.py

git add .

git commit -m "Automatic Commit."

git push
