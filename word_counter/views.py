#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse('working')
    return render(request, 'home.html')

def count(request):

    fullText = request.GET['full-text']
    wordCount = fullText.split()
    wordDictionary = {}

    for word in wordCount:

      if word in wordDictionary:
          wordDictionary[word] += 1
      else:
          wordDictionary[word] = 1

    return render(request, 'count.html', {'fullText': fullText,
                                          'count': len(wordCount),
                                          'wordDictionary': wordDictionary.items()})
