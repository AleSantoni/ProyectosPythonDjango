from django.urls import path
from .views import ProfilesListView,ProfileDetailView


profiles_patterns =( [
    path('',ProfilesListView.as_view(),name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
    
    
],"profiles")
