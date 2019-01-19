from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def alpstrip(word):
    res = ''
    for i in word:
        if i.isalpha() == True:
            res += i
    return res

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    wordDict = {}
    for word in words:
        word = alpstrip(word)
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    #단어 빈도수 많은 순으로 정렬
    wordDict = sorted(wordDict.items(), key=lambda t : t[1], reverse=True)
    return render(request, 'wordcount/result.html', {'full':text, 'total':len(words), 'wordDict':wordDict})