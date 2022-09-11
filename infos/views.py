from django.shortcuts import render
# Create your views here.



def main_page(request):
    return render(
        request=request,
        template_name="main.html",
    )

def about_me_page(request):
    return render(
        request=request,
        template_name="about_me.html",
    )

def contact_page(request):
    return render(
        request=request,
        template_name="contact.html",
    )