# online_courses


## install dependancy 
create python vertualenv
>>$ python -m venv [venv]
>>$ source [venv]/bin/activate
>>$ pip install -r requirment.txt

>>$ python manage.py tailwind install


## run app
in this app we configer tailwind css [tailwindcss](https://django-tailwind.readthedocs.io/en/latest/usage.html)
be sure you have node version 14 or higer

### make migrations
>>$ python manage.py migrate

### create super user 
>>$ python manage.py createsuperuser

### start tailwind server
>>$ python manage.py tailwind start

### start django server
>>$ python manage.py runserver


## setup environment variable

we use django configuration to set env var in our app [ Django Configurations](https://django-configurations.readthedocs.io/en/stable/)

We set DJANGO_CONFIGURATION for development mode by defult in manage.py 
if error during run development server check 
>>$ echo $DJANGO_CONFIGURATION
out put >> Dev  
