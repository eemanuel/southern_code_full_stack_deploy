from django.shortcuts import render
from django.views import View

from weather.forms import WeatherForm
from weather.services import WeatherService


class WeatherView(View):
    form_class = WeatherForm
    template_name = "search.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["city_name"]
            country = form.cleaned_data["country"]
            data = WeatherService().get_data(city_name, country)
            if data.get("error"):
                return render(request, "error.html", data)
            return render(request, "table.html", data)
        return render(request, "error.html")
