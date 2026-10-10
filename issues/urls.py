from django.urls import path
from .views import IssueView, ReporterView

urlpatterns = [
    #path("get-all-tasks", __get_all_tasks),
    path("issues/", IssueView.as_view()),
    #path("issues/<int:id>/", IssueView.as_view()),#because we are asked to pass it as query parameter and not as path parameter
    path("reporters/", ReporterView.as_view())
]