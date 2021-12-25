from django.shortcuts import render
from django.views import generic

# Index Class
class IndexView(generic.ListView):
    """
    Index View - Populates the index.html on the base URL
    """

    def get(self, request, **kwargs):
        return render(request, 'index.html')