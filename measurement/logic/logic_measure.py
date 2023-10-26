from ..models import Measurement

def get_measurements():
    return Measurement.objects.all()

#def create_measurement():
