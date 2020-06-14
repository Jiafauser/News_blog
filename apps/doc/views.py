from django.shortcuts import render


# Create your views here.
def doc_list(request):
    return render(request, 'doc/docDownload.html')
