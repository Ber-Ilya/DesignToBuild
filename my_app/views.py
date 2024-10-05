from .models import *
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .utils import paginate_objects, search_results



# Общие страницы
def home_redirect(request):
    return redirect('main/about.html')

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return render(request, 'main/about.html')


def about(request):

    query = request.GET.get('q')
    if query:
        results = search_results(query)
    else:
        results = None

    # Пагинация для изображений
    images = Example.objects.all()
    images_page_obj = paginate_objects(request, images, 5, 'image_page')

    # Пагинация для SRO
    sro = SRO.objects.all()
    sro_page_obj = paginate_objects(request, sro, 3, 'sro_page')

    # Передаем данные в шаблон
    return render(request, 'main/about.html', {
        'images_page_obj': images_page_obj,
        'sro_page_obj': sro_page_obj,
        'results': results,
    })

def proektirovanie(request):
    return render(request, 'main/stroitelstvo.html')


def stroitelstvo(request):
    return render(request, 'main/stroitelstvo.html')


def tekhnicheskijZakazchik(request):
    return render(request, 'main/proetirovanie/tekhnicheskij-zakazchik.html')




# Проектирование
def proektirovanieInzhenernyhSistem(request):
    return render(request, 'main/proetirovanie/proektirovanie-inzhenernyh-sistem.html')

def proektirovanieOtopleniya(request):
    return render(request, 'main/proetirovanie/proektirovanie-otopleniya.html')

def proektirovanieVodosnabzheniyaIKanalizacii(request):
    return render(request, 'main/proetirovanie/proektirovanie-vodosnabzheniya-i-kanalizacii.html')

def proektPereplanirovki(request):
    return render(request, 'main/proetirovanie/proekt-pereplanirovki.html')


def proektirovanieMetallokonstrukcij(request):
    # Получаем все записи для примеров
    examples = Example.objects.all()[4:]

    # Пагинация для примеров
    examples_page_obj = paginate_objects(request, examples, 10, 'examples_page')

    # Передаем данные в шаблон
    return render(request, 'main/proektirovanie/proektirovanie-metallokonstrukcij.html', {
        'examples_page_obj': examples_page_obj,
    })

# Технический заказчик
def soglasovanieArhitekturnoGradostroitelnogoOblikaObekta(request):
    return render(request, 'main/tekhnicheskijZakazchik/soglasovanie-arhitekturno-gradostroitelnogo-oblika-obekta.html')


def izmenenieVriZemelnogoUchastkaSelskohozyajstvennogoNaznacheniya(request):
    return render(request, 'main/tekhnicheskijZakazchik/izmenenie-vri-zemelnogo-uchastka-selskohozyajstvennogo-naznacheniya.html')


def poluchenieRazresheniyaNaStroitelstvo(request):
    return render(request, 'main/tekhnicheskijZakazchik/poluchenie-razresheniya-na-stroitelstvo.html')


def soglasovanieRekonstrukci(request):
    return render(request, 'main/tekhnicheskijZakazchik/soglasovanie-rekonstrukci.html')


def poluchenieGpzu(request):
    return render(request, 'main/tekhnicheskijZakazchik/poluchenie-gpzu.html')


def vVodVEhkspluataciyu(request):
    return render(request, 'main/tekhnicheskijZakazchik/vvod-v-ehkspluataciyu.html')


def organizaciyaProvedeniyaInzhenernyhIzyskanij(request):
    return render(request, 'main/tekhnicheskijZakazchik/organizaciya-provedeniya-inzhenernyh-izyskanij.html')


def legalizaciyaSamostroya(request):
    return render(request, 'main/tekhnicheskijZakazchik/legalizaciya-samostroya.html')


def izmeneniyaVPzz(request):
    return render(request, 'main/tekhnicheskijZakazchik/izmeneniya-v-pzz.html')



# Строительство
def stroitelstvoSklada(request):
    return render(request, 'main/stroitelstvo/stroitelstvo-sklada.html')

def stroitelstvoAngara(request):
    return render(request, 'main/stroitelstvo/stroitelstvo-angara.html')

def stroitelstvoMagazina(request):
    return render(request, 'main/stroitelstvo/stroitelstvo-magazina.html')


# Согласование перепланирвки
def proekt_pereplanirovki_kvartiry(request):
    return render(request, 'main/pereplanirovka/proekt-pereplanirovki-kvartiry.html')

def soglasovanie_pereplanirovki(request):
    return render(request, 'main/pereplanirovka/soglasovanie-pereplanirovki.html')

def soglasovanie_pereplanirovki_kvartiry(request):
    return render(request, 'main/pereplanirovka/soglasovanie-pereplanirovki-kvartiry.html')

def soglasovanie_pereplanirovki_nezhilogo_pomesheniya(request):
    return render(request, 'main/pereplanirovka/soglasovanie-pereplanirovki-nezhilogo-pomesheniya.html')

def uzakonit_pereplanirovku(request):
    return render(request, 'main/pereplanirovka/uzakonit-pereplanirovku.html')

def proekt_pereplanirovki_nezhilogo_zdaniya(request):
    return render(request, 'main/pereplanirovka/proekt-pereplanirovki-nezhilogo-zdaniya.html')

