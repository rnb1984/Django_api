from django import forms

class UploadImageForm(forms.Form):
    file  = forms.FileField()

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError

# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file

@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Only POST here')

    form = UploadImageForm(request.POST, request.FILES)
    if not form.is_valid():
        return HttpResponseServerError("Invalid call")

    handle_uploaded_file(request.FILES['file'])
    return HttpResponse('OK')