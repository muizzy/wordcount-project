from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {'name': 'Muizz'})


def count(request):
    words = request.GET['words']
    wordlist_a = words.split(" ")
    wordlist = [word.lower() for word in wordlist_a]

    wordcounts = {}
    for word in wordlist:
        if word not in wordcounts.keys():
            wordcounts[word] = 1
        else:
            wordcounts[word] += 1

    max_word = max(wordcounts, key=wordcounts.get)
    sorted_words = sorted(wordcounts.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'words': words, 'count': len(wordlist), 'dict': sorted_words ,'max': {'key': max_word, 'value': wordcounts[max_word]}})

def about(request):
    return render(request, 'about.html')