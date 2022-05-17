from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView,DetailView
from .utils import utils_of_index_page,articles_objects_view_utils
from .models import articles

#from django.views import View
#from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    title = "RED-index"
    ajker_res, ager_res =utils_of_index_page()
    
    return render(request, 'RED/index.html', {'title': title,'ajker_res':ajker_res,'ager_res':ager_res})



    # return render(request,'RED/index.html', {'title': title,'present_date':present_date, 'yesterday':yesterday, 'nasa_api':nasa_api ,
    #     'previous_nasa_api_response':previous_nasa_api_response,'nasa_api_response':jsondata})


# def index():
#     # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
#     today = date.today()
#     previous_date = today - timedelta(days=1)
#     print(today)
#     print(previous_date)

#     nasa_api_response = nasa_api.get_data(SECRET_KEY, today)

#     previous_nasa_api_response = nasa_api.get_data(SECRET_KEY, previous_date)

#     im_url = nasa_api.get_url(nasa_api_response)
#     im_url_previous = nasa_api.get_url(previous_nasa_api_response)

#     present_date = nasa_api.get_date(nasa_api_response)
#     yesterday = nasa_api.get_date(previous_nasa_api_response)

#     nasa_api.download_image(im_url, present_date)
#     nasa_api.download_image(im_url_previous, yesterday)

#     return render_template("index.html", present_date=present_date, yesterday=yesterday, nasa_api=nasa_api, previous_nasa_api_response=previous_nasa_api_response,nasa_api_response=nasa_api_response)








#@login_required
def home(request):
    title = "RED-home"
    return render(request,'RED/home.html', {'title': title})

def donate(request):
    title = "RED-donate"
    return render(request,'RED/donate.html', {'title': title})

def history(request):
    title = "RED-history"
    article = articles.objects.all()
    return render(request,'RED/history.html', {'title': title, 'article' : article})

def haddits(request):
    title = "RED-haddits"
    return render(request,'RED/haddit.html', {'title': title})

def quran(request):
    title = "RED-quran"
    return render(request,'RED/quran.html', {'title': title})

def science(request):
    title = "RED-science"
    return render(request,'RED/science.html', {'title': title})

def local(request):
    title = "Local"
    return render(request, 'RED/local.html', {'title': title})

#@login_required
def about(request):
    title = "About"
    return render(request, 'RED/about.html', {'title': title})



# class product_list_view(ListView):
#     model = auctioned_product 
#     template_name = 'OMart/home.html'
#     context_object_name = 'products'
#     ordering=['-auction_end_dateTime']
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title']='Homepage'
#         title="index"
#         context['current_time'] = timezone.now()
#         return context


# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})


