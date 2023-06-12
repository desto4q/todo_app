from rest_framework.response import Response;
from rest_framework.decorators import api_view
from .serializer import itemSerializer
from django.shortcuts import render
from django.http import HttpResponse
from base.models import item

@api_view(["get"])
def task(request):
    taskList = item.objects.all()
    serializer = itemSerializer(taskList, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addItem(request):
    serial = itemSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)
    return Response(serial.errors)

@api_view(["GET"])
def taskDetail(request, pk):
    try:
        task = item.objects.get(id=pk)
        serializer = itemSerializer(task,many= False)
        return Response(serializer.data)
    except:
        return HttpResponse("does not exist")        


@api_view(["POST"])
def Update(request, pk):
    try:
        task = item.objects.get(id = pk)    
        serializer = itemSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:  
        return Response(serializer.errors)
    
@api_view(["GET"])
def deletetask(request, pk):
    try:
        task = item.objects.get(id=pk)
        task.delete()
        return HttpResponse("deleted")
    except:
        return HttpResponse("does not exist")




@api_view(["GET"])
def deleteitems(request):
    item.objects.all().delete()
    serial = itemSerializer(data=request.data)    
    text = "all items are deleted"
    if serial.is_valid():
        return Response(serial.data)
    else:
        return HttpResponse(text)
    
    
                
                
        
        