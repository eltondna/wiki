from django.shortcuts import render 
from . import util
from django.http import HttpResponseNotFound, HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from random import randint


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



#Create New Page 

def newpage(request):
    if request.method == "POST":
        topic = request.POST.get("new_topic")
        content = request.POST.get("new_content")
    # Check whether thios topic exists already
        if util.get_entry(topic) !=None:
            error = "This topic already exists"
            return render(request,"encyclopedia/newpage.html",{
                "error": error,
            })
        else:
            util.save_entry(topic,content)
    # Redirect user back to the Home Page
            return HttpResponseRedirect(reverse('index'))
    return render(request,"encyclopedia/newpage.html")



# Random Page set up 
def random(request):
    entry_ls = util.list_entries()
    length = len(entry_ls)

    number = randint(0,length-1)
    random_entry = entry_ls[number]
    return HttpResponseRedirect(random_entry)


def edit(request):
    if request.method=="GET":
        topic = request.GET.get("topic")
        content = util.get_entry(topic)

        return render(request,"encyclopedia/edit.html",{
            "topic": topic,
            "content": content,
        })

    else:
        topic = request.POST.get("topic")
        edited_content = request.POST.get("edited_content")
        util.save_entry(topic, edited_content)
        return HttpResponseRedirect(topic)
        
        
    












