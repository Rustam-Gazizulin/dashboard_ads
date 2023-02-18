from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def main(request):
    return JsonResponse({"status": "ok"}, status=200)
