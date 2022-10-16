from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from rest_framwork import status
from rest_framwork import viewsets
from rest_framwork.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

#create your views here.
class TodoItemViewSet(viewsets.modelViewSet) :
    queryset = TodoItem.objects.all()
    serializers_class = TodoItemSerializer


    def perform_create(self, serializers):
        # save instanse to get primary key and then update URL
        instance = serializers.save()
        instance.url =reverse('todoitem-detail', args=(instance.pk), request=self.request)
        instance.save()

        # deletes all todo items
    def delete(self,request):
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

