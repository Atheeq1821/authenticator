# verification/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,Http404,HttpResponse
from .models import SerialKey
import io
import csv

def check_and_update_serial_key(serial_key):
    key_object = get_object_or_404(SerialKey, key=serial_key, used_time__lt=2)

    # Increment used_time
    key_object.used_time += 1

    # If used_time is 2 or more, delete the key
    if key_object.used_time >= 2:
        key_object.delete()
    else:
        key_object.save()

    return key_object.used_time

def openAddKeys(request):
    return render(request, 'verification/addKeys.html',{"message":""})

def appendKeys(request):
    if request.method=="POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        data = csv.reader(io.StringIO(csv_file.read().decode("utf-8")))
        for row in data:
            k = row[0]
            SerialKey.objects.get_or_create(key=k)
        return render(request, 'verification/addKeys.html',{"message":"Successfully Added keys from the file"})
    return render(request, 'verification/addKeys.html',{"message":""})

def replaceKeys(request):
    if request.method=="POST" and request.Files.get("csv_file"):
        SerialKey.objects.all().delete()
        csv_file = request.FILES["csv_file"]
        data = csv.reader(io.StringIO(csv_file.read().decode("utf-8")))
        i=0
        for row in data:
            if i!=0:
                k = row[0]
                SerialKey.objects.get_or_create(key=k)
            i+=1
        return render(request, 'verification/addKeys.html',{"message":"Succesfully replaced the keys from the file"})
    return render(request, 'verification/addKeys.html',{"message":""})

def check_serial_key_in_database(serial_key):
    try:
        key_object = SerialKey.objects.get(key=serial_key)
       # key_object.delete()
        return True
    except SerialKey.DoesNotExist:
        return False

def verify_authenticity(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        serial_key = request.POST.get('serial_key', '')

        is_authentic = check_serial_key_in_database(serial_key)

        if is_authentic:
            used_time = check_and_update_serial_key(serial_key)
            response_data = {'result': 'authentic'}
        else:
            response_data = {'result': 'not_authentic'}

        return JsonResponse(response_data)

    return render(request, 'verification/verification_page.html')
def homepage(request):
    return render(request, 'verification/homepage.html')
def dianabol(request):
    return render(request,'verification/dianabol.html')
def anavar(request):
    return render(request,'verification/anavar.html')
def clen(request):
    return render(request,'verification/clen.html')
def winr(request):
    return render(request,'verification/winr.html')
def anadrol(request):
    return render(request,'verification/anadrol.html')


def loadProduct(request):
    product_name = request.GET.get('product', '')

    if product_name:
        template_name = f"verification/{product_name}.html"
        try:
            return render(request, template_name)
        except Exception:

            raise Http404("Page not found")
    else:
        return HttpResponse("Invalid request")
