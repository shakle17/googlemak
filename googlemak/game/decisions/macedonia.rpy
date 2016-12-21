#BACKGROUNDS
image classroomday = "backgrounds/classroomday.png"
image town = "backgrounds/town.png"

#DENI - IMAGES
image deni_surprised = im.Scale("characters/deni/denisurprised.png", 350, 650)

#MAGI - IMAGES
image magi_smile4 = im.Scale("characters/magi/smile4.png", 350, 1100)
image magi_smile2 = im.Scale("characters/magi/magismile1.png", 350, 1100)
image magi_shock2_small = im.Scale("characters/magi/magishock2.png", 350, 1100)

#VILMA - IMAGES
image vilma_shock3 = im.Scale("characters/vilma/vilmashock3.png", 350, 740)
image vilma_smile6 = im.Scale("characters/vilma/vilmasmile6.png", 350, 900)


label macedonia:

    scene magi_room
    with fade
    show magi_smile2 at Position(xpos=0.5, xanchor=1.1, ypos=1.0, yanchor=0.53)
    show deni_surprised at Position(xpos=0.5, xanchor=0.0, ypos=1.3, yanchor=1.2)
    show vilma_shock3 at Position(xpos=0.77, xanchor=0.0, ypos=1.5, yanchor=1.2)
    magi "После долго размислување, решив да ја градам својата иднина во Македонија."
    magi "Ќе се фокусирам на учење и усовршување на моите програмрски вештини."
    hide vilma_shock3 
    show vilma_smile_small at Position(xpos=0.77, xanchor=0.0, ypos=1.7, yanchor=1.2)
    vilma "Како што кажа Дени претходно, ние те поддржуваме во секоја твоја одлука."
    magi "Ви балгодарам и на двајцата за поддршката."
    hide deni_surprised
    show deni_happy_small at Position(xpos=0.5, xanchor=0.0, ypos=1.3, yanchor=1.2)
    deni "Станува доцна, време е да си одиме Вилма. Утре имаме предавање на факултет."
    hide vilma_smile_small
    show vilma_shock3 at Position(xpos=0.77, xanchor=0.0, ypos=1.4, yanchor=1.1)
    vilma "Имаш право."
    deni "Чао Меги, се гледаме утре."
    magi "Се гледаме утре."

    jump classroom


label classroom:
    
    scene classroomday
    with fade
    show magi_smile2 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    show vilma_smile_small at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.59)
    magi "Здраво Вилма, Дени не е со тебе?"
    vilma "Го чекав заедно да одиме на факултет, но тој не се појави."
    hide vilma_smile_small
    show vilma_smile6 at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.56)
    vilma "Најверојатно повторно не го слушнал алармот"

    show deni_happy_small:
        xalign 1.3
        yalign 1.9
        linear 1.0 xalign 0.9

    deni "Едвај успеав да стигнам навреме."
    deni "Заборавив да го наместам алармот"
    vilma "Како и обично..."
    magi "хаха"
    deni "Дали сакате кога ќе завршат предавањата да излеземе во градот?"

    menu:
        "Да":
            jump magi_town
        "Не":
            jump magi_home
    

label magi_town:
    
    magi "Тоа е одлична идеја. Не сме излегле сите заедно долго време"
    scene town
    with fade

    show magi_smile2 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    show vilma_smile_small at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.59)
    show deni_happy_small at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)

    vilma "Времето е прекрасно, мило ми е што излеговме"
    magi "Да да"
    deni "Имате ли некои планови за вечерва?"
    magi "Јас вечерва ќе работам на новиот софтвер што го развивам."
    vilma "Јас имам фамилијарна вечера"
    hide deni_happy_small
    show deni_blush at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)
    deni "Баш сте здодевни"
    vilma "Станува доцна, јас си одам. Се гледам утре"
    magi "Исто и јас. Се гледаме"
    deni "Поздрав"

    jump magi_mail


label magi_home:
    magi "За жал нема да можам бидејќи после предавањата ќе одам дома и ќе работам на новиот софтвер кој го развивам."
    deni "Во ред."

    jump magi_mail


label magi_mail:

    scene magi_room
    with fade

    show magi_smile4 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    "После многу работа конечно успеав да го завршам софтверот што го развивав последните 4 месеци"
    hide magi_smile4
    show magi_shock2_small at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    "Само што добив мејл од Google. Се прашувам за што ли станува збор"
    hide magi_shock2_small
    show magi_smile4 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    "Ова е одлична вест. Google дознале за мојот софтвер и сакаат да ме вработат да развивам алгоритми за нив."
    "Ќе морам да им ја соопштам оваа вест на Вилма и Дени."

    jump magi_news


label magi_news:    
    
    scene town
    with fade

    show magi_smile2 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    show vilma_smile_small at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.59)
    show deni_happy_small at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)

    magi "Имам одлична вест. Сепак одиме во Америка"
    hide vilma_smile_small
    hide deni_happy_small
    show vilma_shock3 at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.59)
    show deni_surprised at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)

    vilma "Што? Навистина?"
    magi "Вчера добил известување од Google. Сакаат да работам кај нив во Америка и да развивам алгоритми."
    hide deni_surprised
    show deni_happy_small at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)
    deni "Тоа е одлична вест, ни го разубави денот на сите."

    scene black_screen
    "... во Америка"

    jump america


label america:
    

    scene america1
    with fade   

    show magi_smile2 at Position(xpos=0.1, xanchor=0.1, ypos=1.0, yanchor=0.53)
    show vilma_smile_small at Position(xpos=0.7, xanchor=1.1, ypos=1.0, yanchor=0.59)
    show deni_happy_small at Position(xpos=1.0, xanchor=1.1, ypos=0.8, yanchor=0.59)

    deni "Погледнете ги сите овие големи згради"
    vilma "Да, прекрасни се"
    magi "Ќе се упатам кон канцелатијата на Google. Се гледаме подоцна."
    deni "Со среќа"
    vilma "Со среќа"
    magi "Ви благодарам и на двајцата"

    jump intro_google