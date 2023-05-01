from django.shortcuts import render
from .models import Architect,PortfolioItem,Project,Design,Payment
def login(request):
    return render(request, 'login.html')


def base(request):
    architect = Architect.objects.all()
    return render(request, 'base.html',{'architect': architect})

def portfolio(request, architect_id):
    architect = Architect.objects.get(pk=architect_id)
    portfolio_items = PortfolioItem.objects.filter(architect=architect)
    return render(request, 'portfolio.html', {'architect': architect, 'portfolio_items': portfolio_items})


def projects(request, project_id):
    architect = Architect.objects.get(pk=project_id)
    Projectss = Project.objects.filter(architect=architect)
    return render(request, 'projects.html', {'architect': architect, 'projectss': Projectss})


def designpage(request, design_id):
    designss = Design.objects.filter(pk=design_id)
    return render(request, 'designpage.html', {'designss': designss})

def payment_detail(request):
    paymentss = Payment.objects.all()
    return render(request, 'payment_detail.html', {'paymentss': paymentss})

#def sample(request):
 #   return render(request, 'sample.html')

