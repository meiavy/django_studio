from django.shortcuts import render_to_response
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_mail(
            #    cd['subject'],
            #    cd['message'],
            #    cd.get('email', 'noreply@example.com'),
            #    ['siteowner@example.com'],
                #)
            #return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
           )
    return render_to_response('contact_form.html',{'form': form},context_instance=RequestContext(request))