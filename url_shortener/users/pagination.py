from rest_framework import pagination


class CustomPagination(pagination.CursorPagination):
    ordering = ['-id']
    page_size = 2
