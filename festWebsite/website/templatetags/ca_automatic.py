import pandas as pa
from website.models import Campus_Ambassdors
from django.conf import settings

def ca():
    a = list(Campus_Ambassdors.objects.all().values_list())
    print(a)

ca()