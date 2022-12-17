from django.shortcuts import render
from . import util
from django.http import HttpResponseNotFound


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def pages(request, page):
    # chenck whether page route exist 
    page_content  = util.get_entry(page)

    # Return page content if it exists
    if ( page_content != None):
        return render(request, "encyclopedia/pages.html",{
            "page" : page.capitalize(),
            "content":page_content
        })

    #Return Error when page not exist 
    else:
        return HttpResponseNotFound(f"Cannot find the ' {page} ' page ")




        




