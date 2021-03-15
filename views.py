# I have created file-Prince

# To get the responce from the server
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index2.html")

def analyze(request):
    # get the text
    # we have two type of request, 1: is GET and 2: is POST. Here we are using POST request for
    # protecting our data
    djtext = request.POST.get("text", "default")
    # check checkbox value
    removepunc = request.POST.get("removepunc", "off")
    changecaps = request.POST.get("changecaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    spaceremover = request.POST.get("spaceremover", "off")
    charcount = request.POST.get("charcount", "off")

    # check which checkbox is on
    if removepunc == "on":
        punctuations = """!()-[]{};:'"\|,<>./?@#$%^&*_~"""
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
        djtext = analyzed
    if changecaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {"purpose": "change in uppercase", "analyzed_text": analyzed}
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
                params = {"purpose": "Removed Newlines", "analyzed_text": analyzed}
        djtext = analyzed
    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Removed Spaces", "analyzed_text": analyzed}
        djtext = analyzed
    if charcount == "on":
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
                params = {
                    "purpose": "Total characters in this text is:",
                    "analyzed_text": count,
                }
        djtext = count
    if (
        removepunc != "on"
        and changecaps != "on"
        and newlineremover != "on"
        and spaceremover != "on"
        and charcount != "on"
    ):
        return HttpResponse("<h1>Please select any one of the checkbox</h1>")
    return render(request, "analyze.html", params)