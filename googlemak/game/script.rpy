## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

# CHARACTERS
define magi = Character("Магдалена")
define deni = Character("Дени")
define vilma = Character("Вилма")
define ivan = Character("Иван")
define aristotel = Character("Аристотел")

# BACKGROUNDS
image magi_room = "backgrounds/magi_room.png"
image dark_blue = "backgrounds/question_dark.jpg"

# MAGI - IMAGES
image magi_default = "characters/magi/magidefault.png"
image magi_shock2 = "characters/magi/magishock2.png"

# VILMA - IMAGES
image vilma_smile = "characters/vilma/vilmasmile.png"
image vilma_smile_small = im.Scale("characters/vilma/vilmasmile.png",300,900)
image vilma_smile_big = im.FactorScale("characters/vilma/vilmasmile6.png", 1.03)

# DENI - IMAGES
image deni_serious = "characters/deni/deniserious.png"
image deni_happy = "characters/deni/denihappy.png"
image deni_happy_big = im.FactorScale("characters/deni/denihappy.png", 1.3)
image deni_happy_small = im.Scale("characters/deni/denihappy.png",300,700)
image deni_blush = "characters/deni/deniblush.png"
image deni_blush_big = im.FactorScale("characters/deni/deniblush.png", 1.3)

label start:

    scene magi_room
    with fade
    show magi_default at Position(xpos=0.5, xanchor=1.1, ypos=1.3, yanchor=0.53)

    magi"Јас сум Магдалена. Во моментот се наоѓам пред голема одлука."
    magi"Студирам 2 година на Факултетот за Информатика во Штип. Размислувам да ја продолжам мојата иднина надвор од Македонија.... размислувам за Америка"


    show deni_happy_small at Position(xpos=0.59, xanchor=0.0, ypos=1.3, yanchor=1.2) with dissolve
    show vilma_smile_small at Position(xpos=0.8, xanchor=0.0, ypos=1.3, yanchor=0.85) with dissolve
    magi"За среќа ги имам моите другари Дени и Вилма, кои решија дека ќе ме поддржат , без разлика на одлуката која ќе ја донесам."

    jump deni_vilma

label deni_vilma:

    scene magi_room
    with fade
    show deni_blush_big at Position(ypos=1.8)
    deni"Ова е навистина голема одлука. Знаеш Маги... зборував и со Вилма .."
    show deni_happy_big at Position(ypos=1.8)
    deni"..доколку појдеш во Америка, ние би сакале да појдеме со тебе."

    show vilma_smile:
        xalign 1.3
        linear 1.0 xalign 1.0
    vilma "Ивини Маги , не сакав да го упропастам изненадувањето. Во 8-мо ти ветив дека еден ден заедно ќе ја посетиме Америка."
    deni "Што и да одлучиш , ние сме со тебе !"

    jump magi_question

label magi_question:

    scene dark_blue
    with fade
    show magi_shock2 at Position(ypos=2.4)
    "Навистина долго време размислувам за ова. Од една страна сите мои пријатели се овде... и факултетот ...ќе го оставам"
    "Од друга страна, конечно ќе го остварам својот сон... можеби ќе ми се насмевне среќата и конечно ќе добијам работа од соништата..."
    menu:
        "Време е да им ја соопштам својата одлука на пријателите.."
        "... одам за Америка.":

            jump next_day

        "... останувам во Македонија.":

            jump macedonia
