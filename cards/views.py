from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from bson.objectid import ObjectId

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

        # Provide error message code with request header
        request.META['error_message'] = 'BAD_REQUEST'

class CardDetail(APIView):
    def get_object(self, pk):
        try:
            card = Card.objects.get(_id=ObjectId(pk))
            return card
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        card = self.get_object(pk)
        current_card_author = card.author.lower()
        data = request.data
        serializer = CardSerializer(card, data=data)

        if serializer.is_valid():

            # Check author field in request data and see whether it is provided or not.
            if 'author' in data:
                incoming_card_author = data['author'].lower()

                # Check card's author whether it is correct or not.
                if incoming_card_author == current_card_author:
                    serializer.save()
                    return Response(serializer.data)
                else:
                    request.META['error_message'] = 'FORBIDDEN'
                    return
        request.META['error_message'] = 'BAD_REQUEST'

    def delete(self, request, pk, format=None):
        card = self.get_object(pk)
        current_card_author = card.author.lower()
        data = request.data

        if 'author' in data:
            incoming_card_author = data['author'].lower()
            if incoming_card_author == current_card_author:
                card.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                request.META['error_message'] = 'FORBIDDEN'
                return
        request.META['error_message'] = 'BAD_REQUEST'