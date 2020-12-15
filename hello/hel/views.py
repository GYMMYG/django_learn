from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader,RequestContext
import json
# def my_render(request,template_path,context_dict = {}):
#     # use template
#     # 1.load template file
#     temp = loader.get_template(template_path)
#     # 2.define the template data  #dont need reponsse,need a dict
#     context = context_dict
#     # 3.generate the standard html
#     res_html = temp.render(context)
#     # 4.return
#     return HttpResponse(res_html)

# Create your views here.
#1.define view
#2.match url and view
def index(request):
    #return HttpResponse('yue')
    #return my_render(request,'hel/index.html')
    return render(request, 'hel/index.html',{'content':'yue','list':list(range(0,9))})
    # data = {
    # 'pet_id': '1',
    # 'GPS': '1,1',
    # 'temperature': '36',
    # 'heart_rate': '50',
    # }
    # return  JsonResponse(data)
    # #return HttpResponse(json.dumps(data), content_type="application/json")