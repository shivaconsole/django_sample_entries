from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.EnquiryListView.as_view()), name='enquiry'),
    path('create/', login_required(views.EnquiryCreateView.as_view()), name='enquiry_create'),
    path('<int:pk>/change', login_required(views.EnquiryCreateView.as_view()), name='enquiry_create'),

    path('enqyiry_type/', login_required(views.EnquiryTypeListView.as_view()), name='enquiry_type'),
    path('enqyiry_type/create/', login_required(views.EnquiryTypeCreateView.as_view()), name='enquiry_type_create'),
    path('enqyiry_type/<int:pk>/change', login_required(views.EnquiryTypeCreateView.as_view()), name='enquiry_type_change'),

    # path('add-class-teacher', login_required(views.ClassTeacherCreateView.as_view()), name='add-class-teacher'),
    # path('edit-class-teacher/<int:pk>', login_required(views.ClassTeacherEditView.as_view()), name='edit-class-teacher'),
    # path('class-teachers', login_required(views.ClassTeacherListView.as_view()), name='class-teachers'),
]