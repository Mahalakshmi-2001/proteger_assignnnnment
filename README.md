# proteger_assignnnnment

Steps to run a file
Step 1 - create a virtual environment using command (python -m venv env)
Step 2 - activate environment (.\env\Scripts\Activate)
Step 3 - install requirements (pip install -r requirements.txt)
Step 4 - Start xampp mysql and apache
Step 5 - Make migrations (python manage.py makemigrations)
Step 6 - Make migrate (python manage.py migrate)
Step 7 - Run the python file (python manage.py runserver)

API

1.Create asset

curl --location 'http://127.0.0.1:8000/proteger_assignment/assets/' \
--header 'Content-Type: application/json' \
--data '{
    "name":"maya",
    "category":"test",
    "purchase_date":"2025-10-11"
}'


2.Get all assets

curl --location 'http://127.0.0.1:8000/proteger_assignment/assets/' \
--data ''

3.Get assests by id

curl --location 'http://127.0.0.1:8000/proteger_assignment/assets/2' \
--data ''


4.Update assets
curl --location --request PUT 'http://127.0.0.1:8000/proteger_assignment/assets/2/' \
--header 'Content-Type: application/json' \
--data '{
    "name":"mayaa"
   
}'

5.Delete assets
curl --location --request DELETE 'http://127.0.0.1:8000/proteger_assignment/assets/1/' \
--data ''

6.Generate pdf by id
curl --location --request DELETE 'http://127.0.0.1:8000/proteger_assignment/assets/1/' \
--data ''