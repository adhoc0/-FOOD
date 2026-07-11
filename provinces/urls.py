from django.http import HttpResponse
from django.urls import path


def province_placeholder(request, slug):
    return HttpResponse(f"Province: {slug}")


app_name = "provinces"

urlpatterns = [
    path("<slug:slug>/",province_placeholder,name="province_detail",),
]