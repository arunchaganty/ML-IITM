from django.db import models

from taggit.managers import TaggableManager

# Create your models here.

class Item( models.Model ):
    """Data about some Item
    @name: Name of person
    @link: Link to homepage
    @content: Short bio
    @tags: Associated tags
    """
    name = models.CharField( max_length = 200 )
    link = models.URLField( max_length = 150, blank=True )
    content = models.TextField( )
    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class NewsItem( Item ):
    """News item for the home page
    @name: Title of news item
    @link: Associated link
    @content: Content of news article
    @tags: Associated tags
    @internal: Link to an internal page
    @timestamp: Timestamp
    """

    internal = models.BooleanField()
    timestamp = models.DateTimeField( auto_now = True )

class Person( Item ):
    """Data about a person
    @name: Name of person
    @link: Link to homepage
    @content: Short bio
    @tags: Associated tags
    """
    POSITIONS = (
            (u'Faculty', u'Faculty'), 
            (u'Student', u'Student'), 
            (u'Alumni', u'Alumni'), 
        )
            
    position = models.CharField( max_length = 30, choices = POSITIONS )

class Publication( Item ):
    """Data about a person
    @name: Name of publication
    @link: Link to publication
    @content: Abstract
    @tags: Associated tags
    @authors: Link to Authors
    """
    authors = models.ManyToManyField( Person )

class Project( Item ):
    """Data about a person
    @name: Name of publication
    @link = Project homepage
    @content: Abstract
    @tags: Associated tags
    @authors: Link to Authors
    """
    authors = models.ManyToManyField( Person )

class Event( Item ):
    """Data about a person
    @name: Name of publication
    @link = Event homepage?
    @content: Details
    @tags: Associated tags
    """

    pass

