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
        activated_list = Prize.objects.filter(activated=True)
        if not prize.activated:
            if len(activated_list) < 8 and (prize.code == 'DMQSGA' or prize.code == 'LNYLSJ'):
                pass
            else:
                prize.activated = True
                prize.time_activate = timezone.now()
                prize.save()
    except:
        return render(request, 'birthday/NotFound.html')

    return HttpResponseRedirect(reverse('birthday:prize_code', args=(prize.code,)))


def prize_code(request, code):
    global check
    prize = Prize.objects.get(code=code)
    activated_list = Prize.objects.filter(activated=True)
    if len(activated_list) < 1 and (prize.code == 'DMQSGA' or prize.code == 'LNYLSJ'):
        check = True
    else:
        check = False

    mini_ksandra = prize.code == 'QGDIRM'
    style = prize.code == 'EYEHNV' or prize.code == 'LNYLSJ' or prize.code == 'MFBCWK'
    url = None
    if prize.poem_choose == '1':
        url = prize.image
    elif prize.poem_choose == '2':
        url = prize.image_add_one
    elif prize.poem_choose == '3':
        url = prize.image_add_two

    return render(request, 'birthday/prize.html', {'prize': prize, 'mini_ksandra': mini_ksandra, 'style': style, 'url': url, 'check': check, 'count': 7 - len(activated_list)})


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