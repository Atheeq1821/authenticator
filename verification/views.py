# verification/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import SerialKey,UserKeyUsage


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


def check_serial_key_in_database(serial_key):
    try:
        key_object = SerialKey.objects.get(key=serial_key)
       # key_object.delete()
        return True
    except SerialKey.DoesNotExist:
        return False




def verify_authenticity(request):
    if request.method == 'POST':
        phone = request.POST.get('Phone_Number', '')
        serial_key = request.POST.get('serial_key', '')

        is_authentic = check_serial_key_in_database(serial_key)

        if is_authentic:
            used_time = check_and_update_serial_key(serial_key)
            response_data = {'result': 'authentic'}
            user_key_usage = UserKeyUsage(key=serial_key, phone_number=phone)
            user_key_usage.save()
            
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