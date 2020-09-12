# You can place the script of your game in this file.
label main_menu:
    $ _game_menu_screen = None
    $ _game_quit_screen = None
# Declare images below this line, using the image statement.
image eileen happy = "m0.png"
image eileen shy = "m2.png"
image eileen vhappy = "m2.png"
image eileen concerned = "m1.png"



# Declare characters used by this game.
define e = Character('Aileen', color="#c8ffc8")

init:
    $ import AIMLBot
    image bg grey = "#aaaaaa"
    $user_input=[]

# The game starts here.
label start:
    show text "hello world" with fade
    pause 3.0
    scene bg grey with fade

    window show

    scene bg grey

    show eileen happy at center
    with pixellate

    $ response = AIMLBot.AimlBot().run('Hi')

    $renpy.say(nvl,"[response]", interact = False)

    while True:

        if user_input == "bye":
            pause 1.0
            jump end
        if user_input == "BYE":
            pause 1.0
            jump end

        nvl clear

        $user_input = renpy.input(prompt = "", allow="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ /.,'?!")

        $ response = AIMLBot.AimlBot().run(user_input)

        $renpy.say(nvl,"[response]", interact = False)





label end:

    nvl clear
    show eileen concerned at center
    with move
    "eh..."
    show eileen happy at center
    "You'll visit me again, will you?"
    show eileen vhappy at center
    "do you?"
    window hide
    pause 1.0
    hide eileen concerned at center
    with pixellate
    scene black
    with dissolve
    show text "You'll visit me again, will you?"
    with dissolve
    pause 3.0
    $ renpy.quit()


    return
