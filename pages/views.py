from django.views.generic import TemplateView, ListView
from django.views import View
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product

class homePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {
            "title": "Products - Online Store",
            "subtitle": "List of products",
            "products": Product.objects.all()
        }
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)

        viewData = {
            "title": f"{product.name} - Online Store",
            "subtitle": f"{product.name} - Product information",
            "product": product
        }
        return render(request, self.template_name, viewData)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price'] 

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {"title": "Create product", "form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Asegúrate de que 'index' es correcto
        return render(request, self.template_name, {"title": "Create product", "form": form})

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products - Online Store'
        context['subtitle'] = 'List of products'
        return context  
