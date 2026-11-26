#!/usr/bin/env python3
"""Сборка демо «Мишины шарики» v3 (правки Александры 22.11). Запуск: python3 build.py"""
from pathlib import Path
OUT = Path(__file__).parent
A = "https://cdn.insales-shop.ru/assets/1/2761/11569865/1794991589/"
LOGO = "mishiny-shariki.svg"
WB = "https://www.wildberries.ru/brands/mishiny-shariki"
SITE = "https://mshariki.ru"
TEL, TEL_H = "+79258886000", "+7 925 888-60-00"
MAIL = "info@mshariki.ru"

MAX_CHANNEL = "https://max.ru/mishinishariki"
VK_COMMUNITY = "https://vk.com/mishinishariki"
WAREHOUSE = "РФ, Московская область, Ленинский городской округ, Каширское шоссе, 31-й километр, 235с6"
MAP = "https://yandex.ru/navi/org/mishiny_shariki/218148518369?si=qc6xx1685ekte7j0r8a49wp5cr"
MAX_CHAT = "https://max.ru/u/f9LHodD0cOLCOaXU0WAd0PNVzI9SR448RvfAEXOCIW4v3wh_Av6IUVL_Di0"

NAV = [("o-kompanii.html", "О компании"), ("optovym-klientam.html", "Оптовым клиентам"), ("kontakty.html", "Контакты")]

def head(title, cur):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Мишины шарики</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"></head><body>
<div class="demo-flag">Демо-макет редизайна для согласования · не опубликован</div>
<header class="hdr" id="hdr"><div class="wrap">
<a class="logo" href="index.html" aria-label="Мишины шарики — на главную"><img src="{LOGO}" alt="Мишины шарики"></a>
<nav>{nav}</nav>
<a class="btn btn-main hdr-cta" href="{WB}" target="_blank" rel="noopener">Купить на Wildberries</a>
<button class="burger" aria-label="Меню" onclick="document.getElementById('hdr').classList.toggle('open')">☰</button>
</div></header><main>"""

FOOT = f"""</main><footer class="ftr"><div class="wrap">
<div class="ftr-grid">
 <div><a class="logo" href="index.html"><img src="{LOGO}" alt="Мишины шарики"></a>
  <p>Товары для праздника: воздушные шары, фотозоны, декор и сервировка. Покупайте на Wildberries.</p>
  <a class="btn btn-main" href="{WB}" target="_blank" rel="noopener" style="min-height:44px;font-size:15px">Магазин на Wildberries</a></div>
 <div><h4>Компания</h4><ul><li><a href="o-kompanii.html">О компании</a></li><li><a href="optovym-klientam.html">Оптовым клиентам</a></li><li><a href="kontakty.html">Контакты</a></li><li><a href="videoinstruktsii.html">Видеоинструкции</a></li></ul></div>
 <div><h4>Покупателям</h4><ul><li><a href="{SITE}/page/oferta">Публичная оферта</a></li><li><a href="{SITE}/page/agreement">Пользовательское соглашение</a></li><li><a href="{SITE}/page/exchange">Обмен и возврат</a></li><li><a href="{SITE}/page/privacy-policy">Политика конфиденциальности</a></li></ul></div>
 <div><h4>Связаться</h4><ul><li><a class="big" href="tel:{TEL}">{TEL_H}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul>
  <div class="social"><a href="{VK_COMMUNITY}" aria-label="Мишины Шарики во ВКонтакте"><b aria-hidden="true">ВК</b></a><a href="{MAX_CHANNEL}" aria-label="Канал Мишиных Шариков в MAX"><img src="https://cdn.insales-shop.ru/files/1/5425/138122545/original/MAX-24x24.png" alt=""></a></div></div>
</div>
<div class="ftr-bottom"><span>ООО «Гармония» · ИНН 9725002724 · ОГРН 1197746107140</span><span>© Мишины шарики, 2026</span></div>
</div></footer>
<script>
(function(){{var h=document.getElementById('hdr');addEventListener('scroll',function(){{h.classList.toggle('scrolled',scrollY>10)}},{{passive:true}});
document.querySelectorAll('.slider').forEach(function(s){{var t=s.querySelector('.track'),p=s.querySelector('.prev'),n=s.querySelector('.next');if(!t||!p||!n)return;
function st(){{p.disabled=t.scrollLeft<=4;n.disabled=t.scrollLeft+t.clientWidth>=t.scrollWidth-4}}
function step(){{var c=t.querySelector('.card');return c?c.getBoundingClientRect().width+24:t.clientWidth}}
p.onclick=function(){{t.scrollBy({{left:-step()}})}};n.onclick=function(){{t.scrollBy({{left:step()}})}};t.addEventListener('scroll',st,{{passive:true}});addEventListener('resize',st);st()}});
}})();
</script></body></html>"""

# Всё, что сейчас опубликовано в её блоге, + 2 честных места под будущие инструкции
VIDEOS = [
    ("Как использовать баллоны с гелием?", f"{SITE}/blogs/videoinstruktsii/chernovik-stati-ot-21102026-1026", "https://cdn.insales-shop.ru/files/1/5937/99276593/original/block-category.jpg"),
    ("Фотозона своими руками: как собрать гирлянду из воздушных шаров", f"{SITE}/blogs/videoinstruktsii/fotozona-svoimi-rukami-kak-sobrat-girlyandu-iz-vozdushnyh-sharov", "https://cdn.insales-shop.ru/images/articles/1/4929/12997441/mceclip0-1758555579370.jpg"),
    ("Фотозона на день рождения: как собрать фотозону с фольгированными шарами", f"{SITE}/blogs/videoinstruktsii/fotozona-kak-nadut-shar-i-ispolzovat-uzlovyaz", "https://cdn.insales-shop.ru/files/1/49/100376625/original/banner_94f40b63a5e8bab4c2ad0e14fa8c6d6b.jpg"),
]
SOON = ["Место для новой инструкции", "Место для новой инструкции"]

def card(t, u, img):
    return f"""<a class="card" href="{u}" target="_blank" rel="noopener"><div class="thumb"><img src="{img}" alt="" loading="lazy"><span class="play"></span></div>
<div class="card-body"><h3>{t}</h3><span class="btn btn-main">Смотреть</span></div></a>"""

def soon(t):
    return f"""<div class="card soon"><div class="thumb"></div><div class="card-body"><h3>{t}</h3><span style="color:var(--muted);font-size:15px;margin-top:auto">появится, когда опубликуете</span></div></div>"""

def index():
    cards = "".join(card(*v) for v in VIDEOS) + "".join(soon(s) for s in SOON)
    return head("Товары для праздника", "") + f"""
<section class="hero"><div class="wrap"><div class="hero-card">
<div class="circle circle1"></div><div class="circle circle2"></div>
<div class="hero-content"><div class="hero-brand"><img src="mishiny-shariki-dark.svg" alt="Мишины Шарики" width="125" height="51"></div><h1>Бренд товаров для праздника</h1>
<p>В нашем каталоге — свежие идеи для домашнего дня рождения и большого торжества. Выберите свой стиль и соберите всё оформление в одной теме: от шаров и фотозоны до декора праздничного стола.</p>
<div class="hero-cta"><a class="btn btn-main" href="{WB}" target="_blank" rel="noopener">Выбрать на Wildberries</a></div></div>
<img class="slider-el slider-el-left" src="{A}balon-left.png" alt=""><img class="slider-el slider-el-right" src="{A}balon-right.png" alt=""><img class="slider-el slider-cake" src="{A}cake.png" alt="">
</div></div></section>
<section class="sec" id="video"><div class="wrap"><div class="vid-panel">
<div class="sec-head"><h2>Видеоинструкции</h2><p>Как красиво собрать гирлянду, оформить фотозону и другие полезные советы по сборке и креплению.</p></div>
<div class="slider"><button class="arrow prev" aria-label="Назад">←</button><div class="track">{cards}</div><button class="arrow next" aria-label="Вперёд">→</button></div>
<div class="sec-foot"><a class="btn btn-line" href="videoinstruktsii.html">Все видеоинструкции</a></div>
</div></div></section>
<section class="sec"><div class="wrap"><div class="band">
<h2>Хотите купить много?</h2><p>Получите оптовые цены. Работаем напрямую, без дистрибьютеров и посредников: лучшие цены, стабильное наличие, полный пакет документов.</p>
<a class="btn btn-main" href="optovym-klientam.html" style="margin-top:24px">Условия для партнёров</a></div></div></section>
""" + FOOT

def inner(slug, title, lead, body):
    content_class = "wrap brand-backdrop" if slug in {"o-kompanii.html", "kontakty.html"} else "wrap"
    return head(title, slug) + f"""
<div class="{content_class}"><div class="crumbs"><a href="index.html">Главная</a> / {title}</div>
<div class="page-head"><h1>{title}</h1><p class="lead">{lead}</p></div>
{body}</div>""" + FOOT

ABOUT = """<div class="prose">
<h2>Как всё начиналось</h2>
<p>В 2021 году мы начали с готовых наборов воздушных шаров. Хотели, чтобы каждый мог своими руками собрать гирлянду или оформить фотозону. Мы подбирали цвета и размеры шаров и составляли понятные инструкции. Особое внимание уделяли качеству: искали фабрики, которые могли обеспечить стабильные оттенки и качество шаров от партии к партии.</p>
<p>Первые наборы, которые мы создавали с заботой о покупателях, быстро стали популярными. В 2023 году мы решили расширить ассортимент. К воздушным шарам добавились растяжки, свечи, праздничная посуда и другой декор. Так «Мишины Шарики» стали брендом товаров для праздника.</p>
<p>Сегодня товары «Мишиных Шариков» ежегодно выбирают больше миллиона покупателей. Мы продолжаем развивать ассортимент, сохраняя то, что было важно для нас с самого начала: доступные цены, хорошее качество, актуальные идеи оформления и простоту сборки.</p>
<h2>Почему «Мишины Шарики»</h2>
<p>Когда мы придумывали название, воздушные шары напомнили нам об Олимпийском Мишке, одном из самых узнаваемых символов Олимпиады 1980 года. Так у бренда появилось имя, а его символом стал добрый медвежонок.</p>
<h2>Как мы работаем</h2>
<h3>Проверяем качество</h3>
<p>Мы лично посещаем фабрики, проверяем материалы, упаковку и готовые изделия. При разработке каждого набора смотрим, как сочетаются оттенки, удобно ли собирать композицию и всё ли необходимое есть в комплекте.</p>
<h3>Следим за мировыми трендами</h3>
<p>Мы посещаем международные выставки и привозим в Россию новые цвета, материалы и идеи оформления. На их основе создаём наборы, с которыми понравившийся декор легко повторить самостоятельно.</p>
<h3>Работаем с профессионалами</h3>
<p>Наши товары выбирают аэродизайнеры, команды по оформлению мероприятий и общественные организации. При разработке продукции мы учитываем то, что важно для больших композиций и регулярных заказов: стабильность оттенков, удобную упаковку и предсказуемый результат при сборке.</p>
<h2>Идеи для праздника в наших соцсетях</h2>
<p>В наших соцсетях мы делимся готовыми идеями оформления для разных поводов. Показываем, как собрать гирлянду, оформить фотозону и подобрать декор для праздничного стола. К каждому решению даём подробные пошаговые инструкции, чтобы вы могли повторить его своими руками.</p>
<h2>Открыты к совместным проектам</h2>
<p>Мы рады сотрудничеству с брендами, дизайнерами, специалистами по оформлению праздников и производителями. Если вы хотите создать совместную коллекцию или обсудить другую идею, <a class="about-contact" href="https://mayorov-portfolio.website.yandexcloud.net/mishiny-shariki/v3/kontakty.html">напишите нам</a>.</p>
<p>Ваш праздник начинается здесь 🎈</p>
</div>"""

OPT = """<div class="prose">
<p>Закупайте нашу продукцию оптом напрямую у бренда «Мишины Шарики». Воздушные шары, наборы для фотозон, декор и товары для сервировки отгружаем с собственного склада. Мы предлагаем оптовые цены без наценок посредников и предоставляем полный пакет необходимых документов.</p>
</div>
<section class="sec" style="padding-bottom:0"><div class="form-card" style="max-width:980px;margin:0 auto">
<h2 style="text-align:center">Обратная связь</h2><p class="sub">Доступ к оптовому каталогу предоставляется верифицированным партнёрам. Для верификации заполните, пожалуйста, форму обратной связи ниже и дождитесь звонка нашего менеджера.</p>
<form onsubmit="event.preventDefault();this.querySelector('button').textContent='В демо форма не отправляется'">
<div class="fields"><div><label for="n">Имя</label><input id="n" required></div><div><label for="c">Компания</label><input id="c"></div>
<div><label for="p">Телефон</label><input id="p" type="tel" required></div><div><label for="e">E-mail</label><input id="e" type="email"></div>
<div class="full"><label for="m">Комментарий</label><textarea id="m" placeholder="Что вас интересует: ассортимент, объёмы, регион доставки"></textarea></div></div>
<label class="agree"><input type="checkbox" required> Согласен с обработкой персональных данных и политикой конфиденциальности</label>
<div style="text-align:center"><button class="btn btn-main" type="submit">Отправить заявку</button></div></form></div></section>"""

CONT = f"""<dl class="contact-list">
<dt>Телефон</dt><dd><a href="tel:{TEL}">{TEL_H}</a></dd>
<dt>Электронная почта</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
<dt>MAX</dt><dd><a href="{MAX_CHAT}">Написать нам в MAX</a></dd>
<dt>Где купить</dt><dd><a href="{WB}">Открыть каталог на Wildberries</a></dd>
<dt>Наши вакансии</dt><dd><a href="https://hh.ru/employer/10332983?hhtmFrom=vacancy&amp;tab=DESCRIPTION">Смотреть вакансии на hh.ru</a></dd>
<dt>Оптовым клиентам</dt><dd><a href="optovym-klientam.html">Перейти на страницу оптовых закупок</a></dd>
<dt>Адрес склада</dt><dd><p>{WAREHOUSE}.</p><a href="{MAP}">Открыть в Яндекс Картах</a></dd>
<dt>Вопросы по заказам на маркетплейсах</dt><dd><p>Если вы оформили заказ на маркетплейсе, напишите в чат поддержки той площадки, где сделали заказ.</p></dd>
<dt>Официальные социальные сети бренда</dt><dd><ul class="social-links"><li><a href="{VK_COMMUNITY}">ВКонтакте</a></li><li><a href="{MAX_CHANNEL}">MAX</a></li><li><a href="https://dzen.ru/mishinishariki">Дзен</a></li><li><a href="https://www.tiktok.com/@mishinishariki">TikTok</a></li><li><a href="https://ru.pinterest.com/mishinishariki/">Pinterest</a></li></ul></dd>
<dt>Реквизиты</dt><dd><p>ООО «Гармония»<br>ИНН 9725002724 · КПП 772501001<br>ОГРН 1197746107140</p></dd>
</dl>"""

VID = '<div class="vgrid">' + "".join(card(*v) for v in VIDEOS) + "".join(soon(s) for s in SOON) + "</div>"

pages = {
    "index.html": index(),
    "o-kompanii.html": inner("o-kompanii.html", "О компании", "«Мишины Шарики» — российский бренд товаров для праздника. Мы создаём готовые наборы воздушных шаров и фотозон, подбираем декор и сервировку. С нашими товарами вы можете стильно оформить и праздник дома, и большое торжество.", ABOUT),
    "optovym-klientam.html": inner("optovym-klientam.html", "Оптовым клиентам", "Продаёте много? У вас большое мероприятие?", OPT),
    "kontakty.html": inner("kontakty.html", "Контакты", "Ответим на вопросы о продукции и сотрудничестве.", CONT),
    "videoinstruktsii.html": inner("videoinstruktsii.html", "Видеоинструкции", "Все инструкции по воздушным шарам, гирляндам и фотозонам в одном месте. Новые будут появляться здесь, как только Вы опубликуете их в блоге.", VID),
}
for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print("✓", name, len(html))
