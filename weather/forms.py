from django.forms import CharField, Form


class WeatherForm(Form):
    city_name = CharField(max_length=100)
    country = CharField(max_length=100, required=False)
