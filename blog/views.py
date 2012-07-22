from blog.models import BlogPost, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def blog_list(request):
    latest_blog_post = BlogPost.objects.all().order_by('-created')[:10]
    return render_to_response('blog_list.html',{
        'latest_blog_post' : latest_blog_post,
        'blogClass' : 'active',
        })

def blog(request, blog_id):
    p = get_object_or_404(BlogPost, pk=blog_id) 
    name = request.POST.get('name', None)
    comment = request.POST.get('comment', None)
    if (name == None or comment == None) :
        return render_to_response('blog_post.html', {
            'blog':p,
            'error_message': "You didn't enter any comment.",
            'blogClass' : 'active',
            }, context_instance = RequestContext(request))
    else :
        c = Comment(
            author = name, 
            body = comment, 
            post = BlogPost.objects.get(id=blog_id))
        c.save()
        return HttpResponseRedirect(reverse('blog.views.blog', args= (p.id,)))
        
def index(request):
    return render_to_response('index.html')

def project(request):
    return render_to_response('project.html')
