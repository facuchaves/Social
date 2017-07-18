#/bin/sh

git pull

source ../bin/activate

echo python mainSeguidores.py | tee seguidores.log

git add .

git commit -m "Automatic Commit."

git push
