from django.shortcuts import render
from bot.test import main
from bot.search import searchbot
from bot.bot import test
from bot.tocsv import text2csva, text2csvb, text2csvc, text2csvd
# from fakenewsFE.google_searcher import start_predict
# from fakenewsFE.check_site import checker
import random as rand
# from .models import Article, Output
# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def bota(request):
    if 'corpusa' in request.POST:
        screenname = request.POST.get("KeyWordA", None)

        print(screenname)
        text2csva(screenname)
        return render(request, 'bota.html')
    if 'corpusb' in request.POST:
        screenname = request.POST.get("KeyWordB", None)

        print(screenname)
        text2csvb(screenname)
        return render(request, 'bota.html')
    if 'corpusc' in request.POST:
        screenname = request.POST.get("KeyWordC", None)

        print(screenname)
        text2csvc(screenname)
        return render(request, 'bota.html')
    if 'generate' in request.POST:

        run = main()

    if 'stop' in request.POST:
        run = ""

        return render(request, 'bota.html')
    return render(request, 'bota.html')


def botb(request):

    # run = test()

    if 'stop' in request.POST:
        run = ""

        return render(request, 'botb.html')
    return render(request, 'botb.html')


def botc(request):
    if 'generate' in request.POST:
        screenname = request.POST.get("Number", None)
        hashtag = request.POST.get("hashtag", None)
        reply = request.POST.get("reply", None)
        print(hashtag)

        print(screenname)
        # text2csvd(screenname)
        screenname = int(screenname)
        run = searchbot(screenname, hashtag, reply)

        return render(request, 'botc.html')

    if 'stop' in request.POST:
        run = ""

        return render(request, 'botc.html')
    return render(request, 'botc.html')
