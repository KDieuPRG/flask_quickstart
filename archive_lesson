#! /bin/bash

lesson_num=$1

mkdir "./lesson_archive/lesson_$lesson_num"
mv app.py "./lesson_archive/lesson_$lesson_num"
mv templates "./lesson_archive/lesson_$lesson_num"

touch app.py
chmod +x app.py
echo "from flask imort Flask" > app.py

mkdir templates
touch ./templates/index.html
touch ./templates/base.html
