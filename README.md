# Django-Api
 Generate a django project and expose a sample api which can accept get and post request and send some sample data in response.
 
To generate a Django project, you can use the following command in your terminal:
First of I installed a virtual environment in order to install django, the below is the command I input in the terminal 

“Python -m venv my_app”

Again input 

“my_app\Scripts\activate “

Install pip by inputing
“
Pip install django
“””


django-admin startproject project sample_api


To expose a sample API, you can create a new app within your project using the following command:


python manage.py startapp sample_api


Within my sample_api app, I create d the a new view in views.py that accepts GET and POST requests and returns some sample data. Here's an example:

python
from django.http import JsonResponse

def sample_api(request):
    if request.method == 'GET':
        data = {'message': 'This is a GET request.'}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = {'message': 'This is a POST request.'}
        return JsonResponse(data)


Don't forget to add the URL pattern for this view in your app's urls.py file:

python
from django.urls import path
from . import views

urlpatterns = [
    path('sample-api/', views.sample_api, name='sample-api'),
]


Finally, run the development server using the following command:


python manage.py runserver


You can now send GET and POST requests to your sample API at http://localhost:8000/sample-api/.
