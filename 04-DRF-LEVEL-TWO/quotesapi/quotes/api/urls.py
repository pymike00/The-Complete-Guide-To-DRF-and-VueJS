from django.urls import path
from quotes.api.views import QuoteDetailAPIview, QuoteListCreateAPIView

urlpatterns = [
    path("quotes/", QuoteListCreateAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", QuoteDetailAPIview.as_view(), name="quote-detail")
]