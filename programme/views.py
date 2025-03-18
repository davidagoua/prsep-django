from django.http import JsonResponse
from django.shortcuts import render

from test import ingest


def ingest_data(request, sheet_name):
    response = ingest(sheet_name)
    return JsonResponse({'status': 'ok', 'data': response})