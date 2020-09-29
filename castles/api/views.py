from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from castles.main.models import Castle
from .serializers import CastleSerializer


@api_view(['GET', 'POST'])
def castle_list(request, format=None):
    """
    List all castles
    """
    if request.method == 'GET':
        castles = Castle.objects.all()
        serializer = CastleSerializer(castles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CastleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def castle_detail(request, pk, format=None):
    """
    Retrieve, update or delete a castle.
    """
    try:
        castle = Castle.objects.get(pk=pk)
    except Castle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CastleSerializer(castle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CastleSerializer(castle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     castle.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)
