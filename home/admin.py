from django.contrib import admin

from home.models import NewsItem, Person, Publication, Project, Event

admin.site.register(NewsItem)
admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(Event)

