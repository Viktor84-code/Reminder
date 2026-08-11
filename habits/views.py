from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination

from .models import Habit
from .serializers import HabitSerializer


class HabitPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Пользователь видит только свои привычки"""
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """При создании автоматически подставляется пользователь"""
        serializer.save(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """Список публичных привычек (только чтение)"""

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)
