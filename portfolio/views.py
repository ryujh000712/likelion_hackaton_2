
# Create your views here.
from django.shortcuts import render
from .models import Portfolio


# Create your views here.



def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios':portfolios})