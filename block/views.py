from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from crawler.fetcher import Fetcher
from .models import Block

# Create your views here.

#get the block number from user input
b_num = 16051539


#get block data by crawler
blockFetcher = Fetcher(block_num=b_num)

Block.objects.create(difficulty=0,
                    extraData = '0x6275696c64657230783639',
                    hash = '0x4338d33acdf1035b71b7e81d4b041524062afb2c40476a1f3220aa2692391fec',
                    )

#
@require_http_methods(["GET"])
def index(request):
    pass