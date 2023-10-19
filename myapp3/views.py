from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

def hello(request):
    return HttpResponse("Hello world from function")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello world from class!")


def year_post(request, year):
    text = ""
    return HttpResponse(f"posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создает списки в питон list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                   " какой способ создания списков быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "Igor"}
    return render(request, "myapp3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет мир"
        context['number'] = 5
        return context