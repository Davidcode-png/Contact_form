from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Profile
from django.http import HttpResponseRedirect, HttpResponseServerError


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')

        profile = Profile.objects.create(name=name, email=email, title=title, message=message)

        profile.save()
        instance = profile.save()
        print("The user id is", profile.id)

        context = {
            "name": name,
            "email": email,
            "title": title,
            "message": message,
        }

        return render(request, 'resume.html', context=context)

    return render(request, 'index.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    # template = loader.get_template("resume.html")
    # html = template.render({'user_profile':user_profile})
    # option = {
    #     'page-size':'Letter',
    #     'encoding':'UTF-8'
    # }
    # pdf = pdfkit.from_string(html,False,option)
    # response = HttpResponse(pdf,content_type='application/resume_app')
    # response['Content-Disposition'] = 'attachment'

    return render(request, "resume.html", {'user_profile': user_profile})
