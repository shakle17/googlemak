# BACKGROUNDS
image black_screen = "backgrounds/black_screen.png"
image library = "backgrounds/library.png"
image color_back = "backgrounds/colours1.jpg"
image america1 = "backgrounds/america_la.png"
image hostel = "backgrounds/hostel.png"
image magi_hostel_room = "backgrounds/magi_hostel_room.png"
image google_invite = "backgrounds/google.jpg"
image balcony = "backgrounds/balcony.png"
image starbucks = "backgrounds/starbucks.jpg"

# MAGI - IMAGES
image magi_default = "characters/magi/magidefault.png"
image magi_crazy = "characters/magi/magicrazy1.png"
image magi_crazy2_small = im.Scale("characters/magi/magicrazy2.png",100,400)
image magi_smile_talking:
    "characters/magi/smile3.png"
    pause 0.5
    "characters/magi/smile4.png"
    pause 0.5
    repeat
image magi_smile_talking_flip:
    im.Flip("characters/magi/smile3.png",horizontal=True)
    pause 0.5
    im.Flip("characters/magi/smile4.png",horizontal=True)
    pause 0.5
    repeat
image magi_confused = "characters/magi/pout3.png"
image magi_smile1 = im.Flip("characters/magi/smile1.png",horizontal=True)

# DENI - IMAGES
image deni_surprised = "characters/deni/denisurprised.png"
image deni_talking:
    "characters/deni/denisurprised.png"
    pause 0.4
    "characters/deni/deniserious.png"
    pause 0.4
    "characters/deni/denisad.png"
    pause 0.4
    "characters/deni/deniserious.png"
    repeat

# VILMA IMAGES
image vilma_winking:
    "characters/vilma/vilmawink.png"
    pause 0.5
    "characters/vilma/vilmawink2.png"
    pause 0.5
    repeat
image vilma_talk_small = im.Scale("characters/vilma/vilmatalk.png",100,400)

label next_day:
    scene black_screen
    with fade
    "...следниот ден...."
    jump school_before_america

# IVAN IMAGES
image ivan_talking:
    im.FactorScale("characters/ivan/MS4-alarmed1.png",1.5)
    pause 0.4
    im.FactorScale("characters/ivan/MS4-alarmed2.png",1.5)
    pause 0.4
    im.FactorScale("characters/ivan/MS4-angry1.png",1.5)
    pause 0.4
    im.FactorScale("characters/ivan/MS4-angry2.png",1.5)
    pause 0.4
    im.FactorScale("characters/ivan/MS4-argue.png",1.5)
    repeat
image ivan_smile = im.FactorScale("characters/ivan/MS4-default.png",1.5)

label school_before_america:
    with fade
    scene library
    with dissolve
    show magi_crazy at Position(ypos=2.5)
    magi "Пријатели , јас решив, ОДИМЕ ЗА АМЕРИКА !!!"
    jump deni_surprised

label deni_surprised:
    scene color_back
    with dissolve
    show deni_surprised:
        pos (400.0, 0.0)
        linear 30.0 zoom 3.0 pos (500, 0.0)
    deni "Навистина? Чекај,чекај .. дали сериозно одиме за Америка ???"
    jump friends_happy

transform lock:
    rotate 0
    linear 0.0 rotate 0
    block:
        linear 0.75 rotate -15
        linear 0.75 rotate 15
        repeat

label friends_happy:
    scene color_back
    with dissolve
    show deni_happy_big at lock:
        pos (-200,0)
    show vilma_winking at Position(xpos=0.8,ypos=2.5)
    vilma "ЈЕССССССССССС !!!  ВРЕМЕ Е ЗА ЕДНА ГОЛЕМА АВАНТУРА !!!"
    jump next_america

label next_america:
    scene black_screen
    with fade
    "... во Америка ...."
    jump america_intro

label america_intro:
    scene america1
    with fade
    show magi_crazy2_small at Position(xpos=0.6)
    show vilma_talk_small at Position(xpos=0.7)
    show deni_talking at Position(xpos=0.3,ypos=1.5)
    deni "УАУ ! Ова навистина изгледа преголемо. Досега немам видено ваков начин на живот.."
    deni "Сите се зафатени,брзаат некаде... сигурно луѓето овде го планираат целиот свој ден"
    menu:
        deni "Маги,Вилма дали би сакале да се сместиме за почеток во некој хостел?"

        "... во ред, тогаш да побараме некој хостел.":

            jump intro_hostel

        "... побарајте вие, јас ќе отидам до Старбакс.":

            jump intro_starbucks

transform rotate_40:
    pos(400,0)
    rotate -20

label intro_hostel:
    scene hostel
    with fade
    "ОВА Е 2-от спрат, вашиот апартман е право , па веднаш десно."
    "Ве замолуваме да го почитувате куќниот ред, во хостелот. Правилата можете да ги видите долу,на рецепција"
    with dissolve
    show magi_smile_talking at rotate_40
    magi "Јас би сакала да ја имам најизолираната соба."
    magi "Ми треба за да се концентрирам на програмирањето."
    magi "Ветувам дека ќе наскоро ќе заработам за подобро сместување."
    jump magi_hostel_room

label magi_hostel_room:
    scene black_screen
    with fade
    "... во собата ...."
    jump magi_in_room


label magi_in_room:
    scene magi_hostel_room
    with fade
    show magi_crazy2_small
    magi "Ми се допаѓа собата, средено е и ги имате сите работи кои ми се потребни."
    magi "Сега ќе имам време да ги завршам сите проекти кои ги имам започнато, а ќе аплицирам и за работа во некој стартап или некоја компанија."
    magi "Се надевам дека и добро ќе се согласувам со моите колеги."
    magi "А сега малку да ја расчистам мојата соба...."
    hide magi_crazy2_small
    with dissolve
    show magi_confused at Position(xpos=0.3,ypos=2.5)
    magi "...(хммм).... што е ова ливче до компјутерот ?"
    menu:
        " отвори го.":
            jump google_intro
    jump magi_in_room

label google_intro:
    scene google_invite
    with fade
    scene color_back
    show magi_smile_talking at Position(xpos=0.4,ypos=2.5)
    magi "Иван Трајков , тим-лидер во оделот за Вештачка Интелегенција во Google Inc."
    magi "\"За секој љубител на технологијата , слобдно може да ме пронајде во Starbucks 5ч поручек, одма до главниот парк.\""
    magi ".... не можам да верувам, имам читано многу за Иван - тој е еден од најуспешните луѓе на Балканот во полето на технологијата ... "
    hide magi_smile_talking
    with fade
    show magi_shock2:
        pos (300.0, 0.0)
        linear 30.0 zoom 3.0 pos (500, 0.0)
    magi "Наредниот вторник ќе отидам во Starbucks и се надевам дека ќе ми даде шанса да се докажам во една од најголемите компании во светот."

label tell_friends_about_ivan:
    scene balcony
    with fade
    show deni_happy_small(xpos=0.8)
    show magi_smile_talking at Position(xpos=0.2,ypos=2.5)
    magi "Дени , извести ја и Вилма, случајно пронајдов контакт од Иван Трајков - го знаете, првиот македонец вработен во Google."
    magi "Ќе отидам во Starbucks да го запознаам.... се надевам дека ќе ми даде шанса ..."
    hide vilma_smile_small
    hide deni_happy_small
    hide magi_smile_talking
    with fade
    show magi_crazy at Position(xpos=0.5,ypos=2.5)
    magi "... Мислам дека ќе го имресионирам со моето познавање на невронските мрежи, се надевам дека на крајот на денот ќе бидиме колеги."
    jump intro_starbucks

label intro_starbucks:
    scene black_screen
    with fade
    "... во Starbucks..."
    jump at_starbucks

label at_starbucks:
    scene starbucks
    with fade
    show ivan_talking at Position(xpos=0.2,ypos=2.5)
    show magi_smile1 at Position(xpos=0.6,ypos=2.5)
    ivan "Здраво Магдалена, многу сум среќен што некој од нашите простори (особено девојка-програмер , што ретко се наоѓа кај нас) , дошла олку далеку и решила да ја проба својата среќа овде. "
    ivan "Како што знаеш , јас работам во оделот за Вештачка Интелегенција и доколку те интересира таа област и имаш познавања од истата можеби ќе можеш да ни помогнеш."
    hide ivan_talking
    hide magi_smile1
    show ivan_smile at Position(xpos=0.2,ypos=2.5)
    show magi_smile_talking_flip at Position (xpos=0.6,ypos=2.5)
    magi "Здраво Иван. Многу сум среќна , што начекав ваква прилика... ова не можев ни да го сонувам пред да тргнам за Америка."
    magi "..Инаку и моја желба е да работав во делот на Вештачката интелегенција (невронските мрежи). Имам некои проекти, кои ќе ти ги доставам."
    magi "Се надевам дека ќе ми дадеш шанса, а несомнено, ваква прилика се добива еднаш во живот"
    hide ivan_smile
    hide magi_smile_talking_flip
    with fade
    show ivan_talking at Position(xpos=0.2,ypos=2.5)
    show magi_smile1 at Position(xpos=0.6,ypos=2.5)
    ivan "Во ред тогаш се гледаме на интервју, во кампусот во Google. Утре 08.00, ќе ја побараш канцеларијата на Трајков, обезбедувањето ќе те упати. Имај убаво ден. "

    jump intro_google
