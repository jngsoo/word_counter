from django.shortcuts import render
from konlpy.tag import Okt
import re
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, plot

okt = Okt()

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def cleanText(rawText):
    toBeTerminated = '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]'
    strippedText = re.sub(toBeTerminated,'',rawText)
    return strippedText

def krword_tokenize(sent):
    result = []
    sample = okt.pos(sent, norm=True, stem=True)
    for hts in sample:
        if 'Noun' in hts or 'alpha' in hts:
            result.append(hts)
    return result

def alpstrip(word):
    res = ''
    for i in word:
        if i.isalpha() == True:
            res += i
    return res

def result(request):
    text = request.GET['fulltext']
    text = cleanText(text)
    words = krword_tokenize(text)
    wordDict = {}
    for word in words:
        print(word)
        word = alpstrip(word[0])
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    #단어 빈도수 많은 순으로 정렬
    wordDict = sorted(wordDict.items(), key=lambda t : t[1], reverse=True)
    return render(request, 'wordcount/result.html', {'full':text, 'total':len(words), 'wordDict':wordDict})
