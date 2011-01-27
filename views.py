import datetime
from django.http import HttpResponse, Http404
from django.core import serializers
from kral.models import *

def top_weblinks(query,format):
    query = query.lower()
    
    # qs = [something to create a valid queryset of all weblinks related to query]

    results = serializers.serialize(format, qs.all()[:15])
    return HttpResponse(results)
