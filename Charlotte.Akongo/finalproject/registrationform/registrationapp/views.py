from django.shortcuts import render
from .forms import PostForm
  
# Create your views here.
def register(request):
    context = {}
    form = PostForm(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("first_name", "last_name", "date_of_birth", "gender", "country", "state", "town")
            print(temp)
    return render(request, "products/register.html", context)   