from django.shortcuts import render
from django import forms
from .tasks import sectionb

class SectionBForm(forms.Form):
    r0 = forms.CharField(label="R0", widget=forms.TextInput(attrs={'placeholder': '1 2 3'}))
    v0 = forms.CharField(label="V0", widget=forms.TextInput(attrs={'placeholder': '1 2 3'}))
    t = forms.IntegerField(label="t")

# Create your views here.
def home(request):
    return render(request, 'home.html')

def section_b(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SectionBForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            t = int(form.cleaned_data["t"])
            r0 = list(map(float, form.cleaned_data["r0"].split(" ")))
            v0 = list(map(float, form.cleaned_data["v0"].split(" ")))
            r, v = sectionb.main1(r0, v0, t)
            context["r_val"] = " ".join(map(str, r))
            context["v_val"] = " ".join(map(str, v))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SectionBForm()
        context["r_val"] = ""
        context["v_val"] = ""

    context["form"] = form

    return render(request, "section_b.html", context)
