from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def count(request):
    mytext = request.GET['fulltext']
    wordlist = mytext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase the value count
            worddict[word] +=1
        else:
            #add the word to dictionary
            worddict[word]=1

    sortedlist= sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':mytext,'count':len(wordlist),'myworddictionary':sortedlist})
