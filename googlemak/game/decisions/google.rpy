# BACKGROUNDS
image google_hall = "backgrounds/hallwayday_done.png"
image aristotel_offices = "backgrounds/aristotel_office.png"
image google_fountain = "backgrounds/google_fountain.png"
image google_gate = "backgrounds/google_gate.png"
image google_lib = "backgrounds/google_lib.png"
image google_outside = "backgrounds/google_outside.png"
image google_stairs = "backgrounds/google_stairs.png"
image roof_top = "backgrounds/roof_top.png"

# MAGI
image magi_default_med = im.Scale("characters/magi/magidefault.png",300,800)
image magi_default_fliped = im.Flip("characters/magi/magidefault.png",horizontal=True)
image magi_winking:
    "characters/magi/wink1.png"
    pause 0.5
    "characters/magi/wink2.png"
    pause 0.5
    "characters/magi/wink3.png"
    pause 0.5
    "characters/magi/wink4.png"
    pause 0.5

# IVAN
image ivan_smile2_small = im.Flip(im.Scale("characters/ivan/MS4-sadsmile1.png",100,400),horizontal=True)
image ivan_smile2_med = im.Flip(im.Scale("characters/ivan/MS4-sadsmile1.png",300,800),horizontal=True)


# DENI
image deni_happy_anim:
    "characters/deni/denihappy.png"
    pause 0.5
    "characters/deni/deniblush.png"
    pause 0.5
    repeat

# ARISTOTEL
image aristotel1 = "characters/aristotel/aristotel1.png"
image aristotel2 = "characters/aristotel/aristotel2.png"
image aristotel3 = "characters/aristotel/aristotel3.png"
image aristotel4 = "characters/aristotel/aristotel4.png"
image aristotel5 = "characters/aristotel/aristotel5.png"
image aristotel6 = "characters/aristotel/aristotel6.png"
image aristotel7 = "characters/aristotel/aristotel7.png"


label intro_google:
    scene black_screen
    with fade
    " .. во Google Inc."
    jump at_google

label at_google:
    scene google_hall
    with fade
    show magi_crazy2_small at Position(xpos=0.4,ypos=0.8)
    show ivan_smile2_small at Position(xpos=0.55,ypos=0.8)
    magi "Неверојатно! Ова е толку огромно место, не ни можев да замислам."
    ivan "Да. И можеш да замислиш, овој кампус е посветен само за Вештачка Интелегенција и Алгоритми за компресија на слики."
    ivan "Имаш среќа да работиш во една од најинтересните околини, и да бидеш опкружена со интелегентни луѓе од различни области."
    ivan "А сега, ќе те запознаам и со главниот експерт, кој е на кормилото на делот - Вештачка Интелегенција"
    magi "Навистина? Многу сум среќна и не можам да дочекам да работам во ова прекрасно место."
    jump aristotel_office

label aristotel_office:
    scene aristotel_office
    with fade
    show aristotel1 at Position(xpos=0.2,ypos=1.2)
    show magi_default_med at Position(xpos=0.6,ypos=1.5)
    show ivan_smile2_med at Position(xpos=0.85,ypos=1.5)
    aristotel "Здраво Магдалена, јас сум г-н Аристотел, главен во оделот за Вештачка Интелегенција во Google Inc."
    aristotel "Бидејќи доаѓате од иста земја со Иван , мислам дека добро би било за почеток да бидеш во тимот на Иван."
    hide ivan_smile2_med
    hide magi_default_med
    with fade
    show magi_default_fliped at Position(xpos=0.6,ypos=2.5)
    aristotel "Сепак на тебе ќе ти оставам да одлучиш дали би се приклучила во тимот на Иван или пак ќе ми се приклучиш мене на еден интересен проект поврзан со компресија на слики"
    menu:
        magi "време е да одлучам во која насока ќе продолжам"

        "... ќе продолжам со Иван.":

            jump join_ivan

        "... ќе продолжам со Аристотел.":

            jump aristotel_office

label join_ivan:
    scene google_stairs
    with fade
    show ivan_smile2_med at Position(xpos=0.8,ypos=1.3)
    show magi_default_med at Position(xpos=0.55,ypos=1.3)
    ivan "Сега ќе те прошетам низ кампусот, сакам да се навикнеш на ова место што побргу - да го осеќаш како свој дом."
    ivan "Сигурно за неколку години ќе се сеќаваш на овие први моменти во компанијата , затоа уживај максимално (хаха)"
    jump google_fountain

label google_fountain:
    scene google_fountain
    with fade
    show ivan_smile2_med at Position(xpos=0.6,ypos=1.3)
    show magi_default_med at Position(xpos=0.35,ypos=1.3)
    ivan "Моментално работам на еден интересен алгоритам, кој ќе го искористиме во најновиот гаџет на Google Inc."
    ivan "Не смеам многу да откривам детали, но ветувам дека откако ќе се вклучив во проектот , ќе ти биде многу возбудливо."
    jump google_lib

label google_lib:
    scene google_lib
    with fade
    show ivan_smile2_med at Position(xpos=0.6,ypos=1.3)
    show magi_default_med at Position(xpos=0.35,ypos=1.3)
    ivan "Ова е една од главните библиотеки во овој кампус."
    ivan "Овде можеш да пронајдеш книги, кои ги нема достапни на Интернет ( па дури и пиратирани , хаха)"
    ivan "Денес е ден за едукација, така што денес нема да имаш практична работа - туку ќе истражуваш нови теми..."
    ivan "А сега можеш да почнеш да читаш материјали за quasi-Newton (Backpropagation алгоритми) и на крајот на недела сакам да ги чујам твоите импресии на оваа тема."
    jump google_lib

label google_lib:
    scene black_screen
    with fade
    " .. истата вечер.."
    jump first_end

label first_end:
    scene roof_top
    with fade
    show magi_winking at Position(ypos=2.5)
    magi ".... 8 години посветив на програмирањето и технологијата..."
    magi "...вакви прилики се случуваат еднаш во животот... морам да се посветам потполно на мојата работа.."
    with dissolve
    show vilma_winking at Position(xpos=0.2,ypos=2.5)
    show deni_happy_anim at Position(xpos=0.8,ypos=1.5)
    show magi_winking with dissolve:
            pos (655,2.5)
            linear 30.0 zoom 3.0 pos (1000, 5.5)
    magi "... ова е новo поглавје во мојот живот , моите родители ќе бидат многу среќни кога ќе им ја соопштам оваа вест !!!"
    return 
