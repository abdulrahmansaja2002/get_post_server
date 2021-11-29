from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def index(request):
  data = {}
  kumpulan_data = {
    "id_1" : {
      "data1" : "data1 untuk id_1",
      "data2" : "data2 untuk id_1",
      },
    "id_2" : {
      "data1" : "data1 untuk id_2",
      "data2" : "data2 untuk id_2",
      },
    "id_3" : {
      "data1" : "data1 untuk id_3",
      "data2" : "data2 untuk id_3",
      },
    "id_4" : {
      "data1" : "data1 untuk id_4",
      "data2" : "data2 untuk id_4",
      },
    "id_5" : {
      "data1" : "data1 untuk id_5",
      "data2" : "data2 untuk id_5",
      },
    "id_6" : {
      "data1" : "data1 untuk id_6",
      "data2" : "data2 untuk id_6",
      },
  }
  if request.method == 'POST':
    data1 = request.POST['data1'] # 'data1' disesuaikan dengan request yang diterima 
    data2 = request.POST['data2'] # 'data2' disesuaikan dengan request yang diterima 
    data = {
      'data1': data1,
      'data2': data2
    }
  else :
    # secara default methodnya pasti GET
    data = kumpulan_data

  return JsonResponse(data, safe=False)
