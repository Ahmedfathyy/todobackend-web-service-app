from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import TodoItem

# create your tests here.
def createItem(client):
    url = reverse('todoitem-list')
    data = {'title' :'walk the log'}
    return client.post(url, data, format='json')

class TestCreateTodoItem(APITestCase):
    """
    Ensure we can create a new todo item
    """
