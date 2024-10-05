from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = "main"

urlpatterns = [

    # Фильтры и поиск


    # Согласование перепланировки
    path('proekt-pereplanirovki-kvartiry/', proekt_pereplanirovki_kvartiry, name='proekt-pereplanirovki-kvartiry'),
    path('soglasovanie-pereplanirovki/', soglasovanie_pereplanirovki, name='soglasovanie-pereplanirovki'),
    path('soglasovanie-pereplanirovki-kvartiry/', soglasovanie_pereplanirovki_kvartiry, name='soglasovanie-pereplanirovki-kvartiry'),
    path('soglasovanie-pereplanirovki-nezhilogo-pomesheniya/', soglasovanie_pereplanirovki_nezhilogo_pomesheniya, name='soglasovanie-pereplanirovki-nezhilogo-pomesheniya'),
    path('uzakonit-pereplanirovku/', uzakonit_pereplanirovku, name='uzakonit-pereplanirovku'),
    path('proekt-pereplanirovki-nezhilogo-zdaniya/', proekt_pereplanirovki_nezhilogo_zdaniya, name='proekt-pereplanirovki-nezhilogo-zdaniya'),



    # Строительство

    path('stroitelstvo-angara', stroitelstvoSklada, name='stroitelstvo-angara'),
    path('stroitelstvo-magazina', stroitelstvoSklada, name='stroitelstvo-magazina'),
    path('stroitelstvo-sklada', stroitelstvoSklada, name='stroitelstvo-sklada'),



    # Технический заказчик
    path('tekhnicheskij-zakazchik/', soglasovanieArhitekturnoGradostroitelnogoOblikaObekta,
         name='tekhnicheskij-zakazchik'),
    path('soglasovanie-arhitekturno-gradostroitelnogo-oblika-obekta/',
         soglasovanieArhitekturnoGradostroitelnogoOblikaObekta,
         name='soglasovanie-arhitekturno-gradostroitelnogo-oblika-obekta'),
    path('izmenenie-vri-zemelnogo-uchastka-selskohozyajstvennogo-naznacheniya/',
         izmenenieVriZemelnogoUchastkaSelskohozyajstvennogoNaznacheniya,
         name='izmenenie-vri-zemelnogo-uchastka-selskohozyajstvennogo-naznacheniya'),
    path('poluchenie-razresheniya-na-stroitelstvo/', poluchenieRazresheniyaNaStroitelstvo,
         name='poluchenie-razresheniya-na-stroitelstvo'),
    path('soglasovanie-rekonstrukci/', soglasovanieRekonstrukci, name='soglasovanie-rekonstrukci'),
    path('poluchenie-gpzu/', poluchenieGpzu, name='poluchenie-gpzu'),
    path('vvod-v-ehkspluataciyu/', vVodVEhkspluataciyu, name='vvod-v-ehkspluataciyu'),
    path('organizaciya-provedeniya-inzhenernyh-izyskanij/', organizaciyaProvedeniyaInzhenernyhIzyskanij,
         name='organizaciya-provedeniya-inzhenernyh-izyskanij'),
    path('legalizaciya-samostroya/', legalizaciyaSamostroya, name='legalizaciya-samostroya'),
    path('izmeneniya-v-pzz/', izmeneniyaVPzz, name='izmeneniya-v-pzz'),

    # Проектирование
    # Добавить razrabotka-agr, proekt-rekonstrukcii,inzhenerno-geologicheskie-izyskaniya, proekt-zdaniya-dlya-razresheniya-na-stroitelstvo, proekt-dlya-razresheniya-na-stroitelstvo, situacionnyj-plan
    path('proektirovanie-metallokonstrukcij/', proektirovanieMetallokonstrukcij, name='proektirovanie-metallokonstrukcij'),  # Страница с примерами и пагинацией
    path('inzhenerno-geologicheskie-izyskaniya/', proektirovanieMetallokonstrukcij, name='inzhenerno-geologicheskie-izyskaniya'),  # Страница с примерами и пагинацией
    path('proektirovanie-inzhenernyh-sistem/', stroitelstvo, name='proektirovanie-inzhenernyh-sistem'),  # Страница с примерами и пагинацией
    path('proektirovanie-vodosnabzheniya-i-kanalizacii/', stroitelstvo, name='proektirovanie-vodosnabzheniya-i-kanalizacii'),  # Страница с примерами и пагинацией
    path('proekt-ehlektros-nabzheniya/', stroitelstvo, name='proekt-ehlektros-nabzheniya'),  # Страница с примерами и пагинацией
    path('proektirovanie-otopleniya/', stroitelstvo, name='proektirovanie-otopleniya'),  # Страница с примерами и пагинацией
    path('proekt-ventilyacii/', stroitelstvo, name='proekt-ventilyacii'),  # Страница с примерами и пагинацией
    path('proekt-pereplanirovki/', stroitelstvo, name='proekt-pereplanirovki'),  # Страница с примерами и пагинацией
    path('stroitelstvo/', stroitelstvo, name='stroitelstvo'),  # Страница с примерами и пагинацией
    path('proektirovanie/', proektirovanie, name='proektirovanie'),  # Страница с примерами и пагинацией
    path('', about, name='about'),  # Страница с примерами и пагинацией
    # path('<str:page>/', other_page, name='other_page'),  # Другие страницы
    path('redirect/', home_redirect, name='home_redirect'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

