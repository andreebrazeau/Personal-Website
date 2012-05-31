from blog.models import BlogPost, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from reportlab.pdfgen import canvas

def index(request):
    latest_blog_post = BlogPost.objects.all().order_by('-created')[:10]
    return render_to_response('index.html',{
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
        
def home(request):
    return render_to_response('aboutMe.html',{ 'aboutMeClass' : 'active' })

def contact(request):
    return render_to_response('contact.html', { 'contactClass' : 'active' })

def resume(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
