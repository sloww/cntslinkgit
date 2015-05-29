from django.shortcuts import render
from app_label.models import Label, Material
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
def index(request, setUrl):
    try:
        if setUrl == 'all':
            labels = Label.objects.all()
        else:
            filter_material = Material.objects.get(setUrl=setUrl)
            if filter_material:
                labels = Label.objects.filter(material=filter_material)
        if labels:
            labels = labels.order_by('material', 'width', 'height')
            return render(request, 'label/stock.html', locals())
        else:
            raise Http404('页面不存在')
    except ObjectDoesNotExist:
        raise Http404('对象不存在')
    #except :
    #    raise Http404('此页面正在建设中，请稍后访问-2')

def detail(request, setUrl):
    try:
        if setUrl:
            label = Label.objects.get(setUrl=setUrl)
        if label:
            return render(request, 'label/detail.html', locals())
        else:
            raise Http404('页面不存在')
    except:
        raise Http404('此页面正在建设中，请稍后访问-2')

