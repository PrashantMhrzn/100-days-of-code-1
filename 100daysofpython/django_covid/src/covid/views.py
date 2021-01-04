from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
import requests


def get_covid_data(country=None):
    if country is None:
        url = 'https://disease.sh/v3/covid-19/all'
    else:
        url = 'https://disease.sh/v3/covid-19/countries/'+country
    res = requests.get(url).json()
    return res


def home(request):
    result = get_covid_data()
    context = {
        'cases': result['cases'],
        'today_cases': result['todayCases'],
        'deaths': result['deaths'],
        'recovered': result['recovered'],
        'active': result['active'],
        'tests': result['tests']
    }
    return render(request, 'home.html', context)


def country_data(request):
    context = {}
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        result = get_covid_data(country=country_name)
        try:
            context = {
                'country': result['country'],
                'flag': result['countryInfo']['flag'],
                'cases': result['cases'],
                'today_cases': result['todayCases'],
                'deaths': result['deaths'],
                'recovered': result['recovered'],
                'active': result['active'],
                'tests': result['tests']
            }
        except KeyError:
            context['message'] = result['message']
        return render(request, 'country_data.html', context)

    return render(request, 'country_data.html')
