from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Dr. Kim! My EC2 instance is working properly with AWS.")
