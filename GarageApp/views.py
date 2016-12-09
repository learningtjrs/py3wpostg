#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render

from GarageApp.models import Contact


def index(request):
    return HttpResponse("is it here")


def detail(request, contact_id):
    return HttpResponse("you are looking at the contact %s" % contact_id)


def results(request, contact_id):
    response = "do you know %s."
    return HttpResponse(response % contact_id)


def vote(request, contact_id):
    return HttpResponse("you are voting for %s." % contact_id)


# def index(request):
#     latest_contact_list = Contact.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.contact_first_name for p in latest_contact_list])
#     return HttpResponse(output)


# def index(request):
#     latest_contact_list = Contact.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('garageapp/index.html')
#     context = RequestContext(request, {
#         'latest_contact_list': latest_contact_list,
#     })
#     return HttpResponse(template.render(context))


def index(request):
    latest_contact_list = Contact.objects.order_by('-pub_date')[:5]
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'garageapp/index.html', context)


####### sample #######
# def addUserAccount(request):
#     if request.method == 'POST':
#         form = User_AccountForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/sla/all')
#     form = CircuitForm()
#     return render_to_response('sla/add.html', {'form': form})