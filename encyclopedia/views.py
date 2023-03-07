from django.shortcuts import render
from markdown2 import Markdown
from . import util

markdowner = Markdown()
markdowner.convert("*CSS!*")
def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    coffee = util.get_entry("coffee")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 'csspage':css_file
    })


def csst(request):
    css_file = util.get_entry("CSS")
    return render(request,'encyclopedia/css.html')