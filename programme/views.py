from django.http import JsonResponse
from django.shortcuts import render

from test import ingest


def ingest_data(request):
    response = ingest()
    return JsonResponse({'status': 'ok', 'data': response})