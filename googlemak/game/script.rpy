## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

image magi_tears = "characters/magi/magi_default_562x1696.png"
image deni_blush = "characters/deni/denihappy_281x619.png"
image vilma_angry = "characters/vilma/vilma_smile3_253x842.png"

image magi_room = "backgrounds/magi_room.png"


define magi = Character("Магдалена")


label start:

    scene magi_room
    with fade
    show magi_tears at Position(xpos=0.5, xanchor=1.1, ypos=1.3, yanchor=0.53)

    magi"Јас сум Магдалена. Во моментот се наоѓам пред голема одлука."
    magi"Да почнеме од почеток..."


    show deni_blush at Position(xpos=0.59, xanchor=0.0, ypos=1.3, yanchor=1.2) with dissolve
    show vilma_angry at Position(xpos=0.8, xanchor=0.0, ypos=1.3, yanchor=0.85) with dissolve
    magi"d"
   
    return
