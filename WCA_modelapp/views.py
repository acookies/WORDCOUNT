from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def about(request):
    return render(request, 'about.html')

def wordcount(request):
    full_text = request.GET['fulltext']
    en = '?!.,@#$%^&*()<>;:~`'
    for i in en:
        full_text = full_text.translate({ord(i): ' '})

    word_list = full_text.split()
    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'wordcount.html', {'fulltext' : full_text, 'total' : len(word_list), 'dictionary' : word_dictionary.items()})