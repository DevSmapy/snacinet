from django.shortcuts import render
from .utils import query_data


def search_view(request):
    column_name = request.GET.get("column", "")
    value = request.GET.get("value", "")
    if column_name and value:
        try:
            results = query_data(column_name, value)
            return render(request, "search_results.html", {"results": results})
        except ValueError as e:
            return render(request, "search_results.html", {"error": e})
    return render(
        request,
        "search_results.html",
        {"error": "Please provide a column name and value."},
    )
