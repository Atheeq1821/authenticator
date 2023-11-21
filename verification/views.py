# verification/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import SerialKey

def check_serial_key_in_database(serial_key):
    try:
        key_object = SerialKey.objects.get(key=serial_key)
        key_object.delete()
        return True
    except SerialKey.DoesNotExist:
        return False

def verify_authenticity(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        serial_key = request.POST.get('serial_key', '')

        is_authentic = check_serial_key_in_database(serial_key)

        if is_authentic:
            response_data = {'result': 'authentic'}
        else:
            response_data = {'result': 'not_authentic'}
        
        return JsonResponse(response_data)

    return render(request, 'verification/verification_page.html')
def homepage(request):
    return render(request, 'verification/home.html')