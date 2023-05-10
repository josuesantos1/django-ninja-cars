from django.contrib import admin
from django.urls import path


from ninja import NinjaAPI

from vehicle.views import VehicleView

api = NinjaAPI()

api.add_router('/vehicles/', VehicleView.router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
