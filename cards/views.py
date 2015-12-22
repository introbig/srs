from django.shortcuts import render

def hello_world(request):
    return render(request, "cards/hello_world.html")

def card_view(request, id):
    id = 2
    return render(request, "cards/card_template.html", {"id":id})

