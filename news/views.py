from django.http import HttpResponse
from news.models import News


# Create your views here.

def home(request):
    news = News.objects.all()
    text = ""
    for new in news:
        text += f"<b>{new.title}</b> <br><p>{new.description}</p>"
    return HttpResponse(f"{text}")
