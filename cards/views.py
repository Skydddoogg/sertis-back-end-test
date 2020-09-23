from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CardList(APIView):
    def get(self, request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CardDetail(APIView):
    def get_object(self, pk):
        try:
            card = Card.objects.get(pk=pk)
            return card
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)