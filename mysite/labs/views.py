from django.shortcuts import render

# Create your views here.
def labs_list(request):
    context = {}
    if request.method == 'GET': 
        
        
        return render(request, 'labs/labs_list.html', context)
    