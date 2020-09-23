from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CardList(APIView):
    def get(self, request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
