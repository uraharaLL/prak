from solution import views

urlpatterns = [
    url(r'^index/$', views.index,
                    name = 'index'),
]
