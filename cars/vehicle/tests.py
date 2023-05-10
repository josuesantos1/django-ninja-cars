from django.test import TestCase

from .models import Vehicle

class VehicleTest(TestCase):
    

    def test_create_vehicle():
        Vehicle.objects.create(
            title       = 'novo civic',
            brand       = 'honda',
            model       = 'civic',
            description = 'novo civic 2023, maximo conforto'
        )
    
    def test_get_vehicle(self):
        vehicle = Vehicle.objects.get(title = 'novo civic')
        self.assertEquals(vehicle.brand, 'honda')
    
    def test_list_vehicle():
        pass
    
    def test_update_vehicle():
        pass
    
    def test_delete_vehicle():
        pass
    