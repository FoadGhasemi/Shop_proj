from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from .forms import ProductComment
from .models import Product


def product_details(request, slug):
    p = Product.objects.get(slug=slug)
    return render(request, 'product/product_details.html', {'product': p})


def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        print(f"Search query: {query}")
        print(f"Matched posts: {products}")
    else:
        products = Product.objects.none()
        print("No query found.")

    return render(request, 'product/search.html', {'product': products, 'q': query})


@login_required
def product_comment(request, pk):
    p = Product.objects.get(id = pk)
    form = ProductComment(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.parent_product = p
        comment.save()
        return redirect('home:home')
    else:
        form = ProductComment()

    return render(request, 'product/product_comment.html', {'form': form, 'product': p})
