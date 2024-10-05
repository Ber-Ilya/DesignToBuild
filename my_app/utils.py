# utils.py
from django.core.paginator import Paginator
from .models import Stati
def paginate_objects(request, object_list, items_per_page, page_param):
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get(page_param)
    page_obj = paginator.get_page(page_number)
    return page_obj


def search_results(request):
    query = request.get.Get('q')
    if query:
        results = Stati.objects.filters(
            Q(title__icontains = query) |
            Q(description__icontains = query) |
            Q(content_icontents = query)
        )
    else:
        results = Stati.objects.none()

    return results
