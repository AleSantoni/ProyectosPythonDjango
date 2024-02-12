from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView

from registration.models import Profile

# Create your views here.


# listView para mostrar una lista de usuarios 

class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 6
 

# Detail profiles views

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    