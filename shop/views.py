from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector

from .forms import ShopForm, SearchForm
from shop.models import Shop

# Create your views here.
def shop_upload(request):
    if request.method == 'POST':
        shop_form = ShopForm(request.POST, request.FILES)
        if shop_form.is_valid():
            shop = shop_form.save(commit=False)
            shop.user = request.user
            shop.save()

            return render(request, 'shop/image_show.html', {'shop':shop})
    else:
        shop_form = ShopForm()
    return render(request, 'shop/shop_upload.html', {'form': shop_form})

def shop_list(request):
    shop_all = Shop.objects.all()
    shop_page = Paginator(shop_all, 30)

    page = request.GET.get('page', 1)
    
    try:
        shops = shop_page.page(page)
    except PageNotAnInteger:
        shops = shop_page.page(1)
    except EmptyPage:
        shop = shop_page.page(shop_page.num_pages)

    return render(request, 'shop/shop_list.html', {'shops' : shop_all})

def shop_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            results = Shop.objects.annotate(search=SearchVector('name', 'description'),
                        ).filter(search=query)

    return render(request, 'shop/shop_search.html', {'form': form,
                                                    'query': query,
                                                    'results': results})