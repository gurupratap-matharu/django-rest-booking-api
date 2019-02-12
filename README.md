# A RestAPI implemented in Django-rest-framework for a booking App!

## Requirements

Python (3.4, 3.5, 3.6, 3.7)
Django (1.11, 2.0, 2.1)

## Django Booking App Features

* Manage data about sporting events to allow users to place bets.
* Provide API to receive data from external providers and update our system with the latest data about events in real time.
* Provide access to support team to allow the to see the most recent data for each event and to query data.

## Implementation Details:

* Data:
    - Markets are unique per Sport
    - Selections are unique per Market

* Receiving data:
    - For our purposes we can assume this API will be used by a single provider, so no need to keep track of which provider is sending the
    message.

## API Features:

* Listing all the match stored in the system
* Filtering of listed items based on query parameters like `name`, `sport`, `ordering`
* Detailed view of a particular match using its `id`
* Uses nested serializers for detailed view for full details
* Retrieve match by id. Ex http://127.0.0.1:8000/api/match/994839351740
* Retrieve football matches ordered by start_time Ex: http://127.0.0.1:8000/api/match/?sport=football&ordering=startTime
* Retrieve matches filtered by name Ex: http://127.0.0.1:8000/api/match/?name=Real%20Madrid%20vs%20Barcelona

## Specification for sports data sent by external providers

The external providers will send the data in a specific format:

## Message Types

* NewEvent:
A complete new sporting event is being created. Once the event is created successfully
the only field that will updated is the selection odds.

* UpdateOdds:
There is an update for the odds field (all the other fields remain unchanged)

## Installation

Install using pip...

pip install -r requirements.txt

That's it, we're done!

## How to run?

If running on local machine do
```python
python manage.py runserver
./manage.py runserver
```

You can now open the API in your browser at http://127.0.0.1:8000/api/, and view your new 'match' API.
For this exercise we are not using authentication. So all users have full CRUD access.

If you don't use the database provided on your local machine you need to do the
migrations and create a super user.

python manage.py createsuperuser

Access admin panel at http://127.0.0.1:8000/admin/
From the admin panel you can do more operations like add, create and delete models,
users, do grouping, etc.

You can also interact with the API using command line tools such as curl. For example, to list the match endpoint:


Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API.


Startup up a new project like so...
```python
pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
```
Now edit the `example/urls.py` module in your project:
```python
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime')
```

```python


# ViewSets define the view behavior.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
```

```python

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'match', MatchViewSet)

```
```python
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

```
We'd also like to configure a couple of settings for our API.

Add the following to your settings.py module:
```python
INSTALLED_APPS = (
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```
Documentation & Support

Full documentation for the project is available at https://www.django-rest-framework.org/.
