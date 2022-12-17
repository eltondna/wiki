from django.shortcuts import render 
from . import util
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse




# Main Page # 
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Content Page #
def pages(request, page):
    # chenck whether page route exist #
    page_content  = util.get_entry(page)
    # Return page content if it exists #
    if ( page_content != None):
        return render(request, "encyclopedia/pages.html",{
            "page" : page.capitalize(),
            "content":page_content
        })
    else:
        return HttpResponseNotFound(f"Page {page} Not found ")

    #Return Error when page not exist #


# Search route
def search(request):
        entry_list  = util.list_entries()
        result = request.GET.get("q")
        results = []
        # Search Result does not meet topic
        if util.get_entry(result) == None:
        # Search match topic from list_entries
            for entry in entry_list: 
                if result in entry:
                    results.append(entry)
            return render(request, "encyclopedia/search.html",{
                "results": results
            })

        # Direct to the topic page 
        else:
            return HttpResponseRedirect(result)



def newPage(request):
    pass




