from django.urls import path
from .views import PublicationListCreateView, PublicationDetailView

urlpatterns = [
    path('publications/', PublicationListCreateView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]
