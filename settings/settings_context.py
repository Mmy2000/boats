from .models import Settings , Images

def myfooter(request):
    myfooter = Settings.objects.last()
    images = Images.objects.filter(settings=myfooter)
    return{'myfooter':myfooter, 'images': images}