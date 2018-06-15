from rest_framework import serializers
from .models import Stock

#This converts data to JSON
class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('ticker', 'volume')
        #send all data (not adviseable)
        #fields = '__all__'