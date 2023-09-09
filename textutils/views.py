# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercaps = request.POST.get('lowercaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')

    # To Store all performed functions in a list
    purpose =[]
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        purpose.append("Removed Punctuations")
        params = { 'purpose':purpose, 'sub_purpose':'Removed Punctuations',  'analyzed_text': analyzed }
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()


        purpose.append("Changed to Uppercase")
        params = {'purpose':purpose, 'sub_purpose': ' And Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(lowercaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        purpose.append("And Changed to LowerCase")
        params = {'purpose':purpose, 'sub_purpose': 'Changed to LowerCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        purpose.append("And Removed ExtraSpaces")
        params = {'purpose':purpose, 'sub_purpose': 'Removed ExtraSpaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        purpose.append("And Removed NewLines")
        params = {'purpose':purpose, 'sub_purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        purpose.append("And Removed Numbers")
        params = {'purpose':purpose, 'sub_purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed

    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on"  and numberremover != "on" and  fullcaps != "on" and lowercaps !="on"):
        return HttpResponse("please select any operation and try again")

    if fullcaps == "on" and lowercaps =="on":
        return HttpResponse("Fullcaps And Full lowercaps : Only One can run a time!")

    return render(request, 'analyze.html', params)



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')