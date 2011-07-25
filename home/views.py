# Create your views here.

from django.shortcuts import render_to_response 
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from endless_pagination.decorators import page_template

import models

def home( request ):

    # Get all the news items
    news_items = models.NewsItem.objects.order_by( '-timestamp' )[0:10]
        
    return render_to_response("home.html", {
            'news_items' : news_items,
        },
        context_instance = RequestContext(request))

@page_template("news_page.html") # just add this decorator
def news( request, news_id = None, template="news.html", extra_context=None ):
    # Get all the news items
    if news_id == None:
        news_items = models.NewsItem.objects.order_by( '-timestamp' ).all()
        context = {
                'news_items' : news_items,
            }
        context.update( extra_context )
        return render_to_response(template, context, context_instance = RequestContext(request))
    else:
        page_template="news_page.html"
        template="news_item.html"
        news_item = models.NewsItem.objects.get( id=news_id )
        return render_to_response(template, {
                'item' : news_item,
            },
            context_instance = RequestContext(request))

