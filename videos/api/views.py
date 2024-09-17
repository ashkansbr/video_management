from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .selectors import get_categories
from .serializers import CategorySerializer
from .services import create_category

class CategoryView(APIView):
    def get(self, request):
        categories = get_categories()
        if not categories:
            return Response(f'category not found',status=status.HTTP_404_NOT_FOUND)
        return Response(categories, status=status.HTTP_200_OK)
    @extend_schema(responses= CategorySerializer, request=CategorySerializer)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_category(name=serializer.validated_data.get('name'))

        except Exception as e:
            return Response(f"database error{e}", status=status.HTTP_400_BAD_REQUEST)


        return Response(CategorySerializer(query).data, status=status.HTTP_201_CREATED)
