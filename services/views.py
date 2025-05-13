from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'services/home.html')

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/track_requests.html', {'requests': requests})
