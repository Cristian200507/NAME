from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginaPersonalizada(PageNumberPagination):
    page_size = 10  # valor por defecto
    page_size_query_param = "tam_pagina"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "pagina_actual": self.page.number,
            "total_paginas": self.page.paginator.num_pages,
            "total_elementos": self.page.paginator.count,
            "resultados": data
        })
