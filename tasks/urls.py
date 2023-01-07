from django.urls import path
from tasks.views import *

urlpatterns = [
    path("", list_tasks),
    path("create/", create_tasks, name="create_tasks"),
    path("delete/<int:id>", delete_tasks, name="delete_tasks"),
    path("update/<int:id>", update_tasks, name="update_tasks"),
    path("update_task/<int:id>", back_update_tasks, name="back_update_tasks")
]