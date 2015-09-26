from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from publisher.models import Publisher,Book

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'

class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the publisher
        context['book_list'] = Book.objects.all()
        return context

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

class AcmeBookList(ListView):

    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='Acme Publishing')
    template_name = 'publisher/acme_list.html'

class PublisherBookList(ListView):

    template_name = 'publisher/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)