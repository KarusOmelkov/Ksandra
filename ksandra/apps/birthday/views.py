from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Prize
from django.urls import reverse
import datetime
from django.utils import timezone

def code(request):
    prize_last = Prize.objects.order_by('-time_activate')[:1]
    for p in prize_last:
        prize = p

    time = prize.time_activate >= (timezone.now() - datetime.timedelta(days=1))
    next_time = prize.time_activate + datetime.timedelta(days=1, hours=5)

    return render(request, 'birthday/code.html', {'time': time, 'next_time': next_time})

def activated(request):
    activated_list = Prize.objects.order_by('-time_activate')
    return render(request, 'birthday/list.html', {'activated_list': activated_list})

def instruction(request):
    return render(request, 'birthday/instruction.html')

def prize(request):
    try:
        prize = Prize.objects.get(code=request.GET['code'])
        if not prize.activated:
            prize.activated = True
            prize.time_activate = timezone.now()
            prize.save()
    except:
        raise Http404("Код не найден!")

    return HttpResponseRedirect(reverse('birthday:prize_code', args=(prize.code,)))

def prize_code(request, code):
    prize = Prize.objects.get(code=code)
    style = prize.code == 'EYEHNV' or prize.code == 'LNYLSJ' or prize.code == 'MFBCWK'
    url = None
    if prize.poem_choose == '1':
        url = prize.image.url
    elif prize.poem_choose == '2':
        url = prize.image_add_one.url
    elif prize.poem_choose == '3':
        url = prize.image_add_two.url
    elif prize.poem_choose == '4':
        url = prize.image_add_three.url
    return render(request, 'birthday/prize.html', {'prize': prize, 'style': style, 'url': url})

def prize_poem(request):
    prize = Prize.objects.get(code='ORUHXM')
    prize.poem_choose = request.POST['choose']
    prize.save()
    return HttpResponseRedirect(reverse('birthday:prize_code', args=('ORUHXM',)))

def prize_poem_two(request):
    prize = Prize.objects.get(code='ORUHXM')
    prize.poem = request.POST['text']
    prize.save()
    return HttpResponseRedirect(reverse('birthday:prize_code', args=('ORUHXM',)))