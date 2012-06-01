from django.db import models

class BlogPost(models.Model):
    # how do we want to define a blog post?
    title = models.CharField (max_length = 256)
    author = models.CharField (max_length = 256)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def next_post(self):
        nextEntries = BlogPost.objects.filter(id__gt=self.id)
        if (len(nextEntries)>0):
            return nextEntries[0].id
        else:
            return None
    
    def previous_post(self):
        previousEntries = BlogPost.objects.filter(id__lt=self.id).order_by('-id')
        if (len(previousEntries)>0):
            return previousEntries[0].id
        else:
            return None
    
    def bodySample (self):
        return self.body[:100]
        
    def __unicode__(self):
        #Returned a 'label' for the class, BlogPost, that
        #is easily understandable for humans to read.
        return self.title
        
class Comment (models.Model):
    
    crated = models.DateTimeField(auto_now_add=True)
    author = models.CharField ('Name',max_length = 256)
    body = models.TextField('Comment')
    post = models.ForeignKey(BlogPost)
    
    def __unicode__(self):
        #Returned a 'label' for the class, Comment, that
        #is easily understandable for humans to read.
        return unicode("%s: %s" % (self.post, self.body[:60]))        

