from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



def main_page (request): 
    template =loader.get_template('bookmarks/main_page.html')
    return HttpResponse(template.render({}, request))

