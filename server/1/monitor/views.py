from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from monitor.models import Message
from honey.settings import IS_SEA_ENV, UPLOAD_PATH, BASE_DIR
import json, os, uuid, time


def index(request):
    latest_message_list = Message.objects.order_by('-log_time')[:5]
    for item in latest_message_list:
        item.time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(item.log_time))

    min_id = 0
    if latest_message_list:
        min_id = min(latest_message_list, key=lambda a: a.id).id
    context = {'latest_message_list': latest_message_list, 'min_id': min_id}
    return render(request, 'monitor/index.html', context)


def prev(request, id):
    latest_message_list = Message.objects.filter(id__lt=id).order_by('-log_time')[:5]
    for item in latest_message_list:
        item.time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(item.log_time))
    min_id = 0
    if latest_message_list:
        min_id = min(latest_message_list, key=lambda a: a.id).id
    context = {'latest_message_list': latest_message_list, 'min_id':min_id }
    return render(request, 'monitor/prev.html', context)


def recive_gps(request):

    json = request.POST['data']
    data = json.loads(json);

    for item in data:
        msg = Message(type=4,
                  log_time=item['log_time'],
                  latitude=item['latitude'],
                  longitude=item['longitude'],
                  altitude=item['altitude'],
                  address=item['address'],
                  name=item['name']),

        msg.save()

    return HttpResponse("Hello, world. You're at the monitor recive_gps.")


def recive_file(request):

    type = request.POST['type']
    log_time = request.POST['log_time']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    altitude = request.POST['altitude']
    address = request.POST['address']
    name = request.POST['name']
    file_url = ''
    if not request.FILES:
        type = 4
    else:
        file_obj = request.FILES['file']
        filename = str(uuid.uuid1()) + file_obj.name
        if IS_SEA_ENV:
            from sae.storage import Bucket
            bucket = Bucket('res')
            bucket.put_object(filename, file_obj.read())
            file_url = bucket.generate_url(filename)
        else:
            file_path = os.path.join(BASE_DIR, UPLOAD_PATH)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_path = os.path.join(file_path,filename)
            dest = open(file_path,'wb+')
            dest.write(file_obj.read())
            dest.close()
            file_url = os.path.join("/", UPLOAD_PATH.replace("\\", "/"), filename)

    msg = Message(type=type,
                  file_path=file_url,
                  log_time=log_time,
                  latitude=latitude,
                  longitude=longitude,
                  altitude=altitude,
                  address=address,
                  name=name)
    msg.save()

    return HttpResponse("Hello, world. You're at the monitor recive_file.")


def demo(request):
    return render(request, 'monitor/demo.html')