from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from myblog import views
from myprojects import settings

urlpatterns = [
    path('',views.showindex),
    path('signup/',views.showsignup.as_view()),
    path('welcome-back-user/',views.showlogin,name='user-login'),
    path('userpanel/',views.showuserpanel),
    path('newblog/',views.BlogCreate),
    path('show-blog-posts/',views.BlogList, name='bloglist'),
    path('blog-details/<int:id>',views.BlogDetails,name='detailspage'),
    path('blog-update-list/',views.BlogUpdateDelete),
    path('blog-update/<int:id>',views.BlogUpdate.as_view(),name='updatepage'),
    path('blog-delete/<int:id>',views.deleteblog,name='deletepage'),
    path('logout/',views.mylogout,name='logging-out'),
    path('change-password/',views.changepass,name='changepassword'),
    path('reach-out/',views.showcontactus,name='contactus'),
    path('talk-to-us/',views.showfeedback.as_view(),name='feedback'),
    ]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)