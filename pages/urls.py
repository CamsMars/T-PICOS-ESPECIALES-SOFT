from django.urls import path
from .views import homePageView,AboutPageView,ProductIndexView,ProductShowView,ProductCreateView,CartView,CartRemoveAllView,ImageViewFactory,ImageViewNoDI,CustomLoginView, CustomLogoutView
from .utils import ImageLocalStorage


urlpatterns = [
    path("", homePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<int:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='create'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'), 
    path('image-not-di/', ImageViewNoDI.as_view(), name='imagenotdi_index'),
    path('image-not-di/save/', ImageViewNoDI.as_view(), name='imagenotdi_save'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]