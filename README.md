# customerServiceProject
customer service 

In this project I used classBased views and function based views. As it was requierd, I had to set the page for admin,
so that admin could do the administration.
Because of that, I used Authentication Authorization, and created SignUp and Login page. 
Also, I used decorators in views for some classes and functions, so ONLY superuser can land on specific pages.

So, after installing requirements, use command in terminal: "./manage.py createsuperuser" and folllow the steps for creation of superuser.
Later on, you can use superuser credentials (username and password) to Login and land on admin_page and more..

I used Materializecss framework so that everything would look organized and "clean" and be responsive.
Database is this project is sqlite3, so before you run the server ("./manage.py runserver"), make migrations and migrate ("./manage.py makemigrations" , "manage.py migrate")

At the end, I created the API (model Customer), and for that I created a diferent app. The logic is a little diferent for API and 'service' app because I wanted to have PUT method in API call(which was not in the requirements). 
If the logic is the same for API and 'service' app, it should be stored on (third) place as a class, so you can avoid Redundant code on later usage.
I created two tests - one for testing if the object is created (Customer), and the second for testing post request for customer/suport.
You can run tests by typing in terminal ("./manage.py test").


