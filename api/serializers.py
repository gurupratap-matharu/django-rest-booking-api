from api.models import Match, Sport, Market, Selection
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')

class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds')

class MarketSerializer(serializers.ModelSerializer):
    selections = SelectionSerializer(many=True)
    class Meta:
        model = Market
        fields = ('id', 'name','selections')

class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime')



class MatchDetailSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    market = MarketSerializer()
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime', 'sport', 'market')

    # def create(self, validated_data):
    #     message = validated_data.pop('message_type')
    #     print("Veer the message is = ", message)
    #     if message == "NewEvent":
    #         match = validated_data.pop('event')
    #         sport = match.pop('sport')
    #         markets = match.pop('markets')
    #         markets = markets[0]
    #         selections = markets.pop('selections')
    #         selections = selections[0]
    #         s = Sport.objects.create(**sport)
    #         market = Market.objects.create(**markets, sport=s)
    #         for selection in selections:
    #             market.selections.create(**selection)
    #         mat = Match.objects.create(**match, sport=s, market=market)
    #         return mat



