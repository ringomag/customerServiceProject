# customerServiceProject
customer service 

In this project I used classBased views and function based views. As it was requierd, i had to set the page for admin,
so admin can do the administration things.
Because of that, i used Authentication Authorization, and created SignUp and Login page. 
Although, I used decorators in views for some classes and functions, so superuser can land on specific pages.

So, after installing requirements, use command in terminal: "./manage.py createsuperuser" and folllow the steps for creation of superuser.
Later on, you can use superuser credentials (username and password) to Login and land on admin_page and more..

I used little of materializecss framework so everithing looks nice and clean and it's responsive.

At the end, I created the API (model Customer), and for that I created a diferent app. The logic is little diferent for API and 'service' app. 
If the logic is the same for API and 'service' app, it should be stored on (third) place as a class, so you can avoid Redundant code on later usage.
I created two tests - one for testing if the object is created (Customer), and second for testing post request for customer/suport.
You can run tests by typing in terminal ("./manage.py test").
