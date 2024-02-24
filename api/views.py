from rest_framework.views import APIView
from rest_framework.response import Response
from hotels.models import Hotel
from .serializers import HotelSerializer


class HotelListView(APIView):
    def get(self, request):
        city_id = request.GET.get('city_id')
        from_id = request.GET.get('from_id')
        limit = request.GET.get('limit')

        queryset = Hotel.objects.all()

        if city_id:
            queryset = queryset.filter(city_id=city_id)
        if from_id:
            queryset = queryset.filter(id__gte=from_id)
        if limit:
            queryset = queryset[:int(limit)]

        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)
