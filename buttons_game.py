
import machine
from machine import Timer
from machine import I2C
from i2c_lcd import Display

from Button import Button
from time import sleep

i2c = machine.I2C(sda=machine.Pin(12), scl=machine.Pin(11))
display = Display(i2c, lcd_addr=0x3e)

reset_timer = Timer(-1)

game_state = 0
player_one_score = 0
player_two_score = 0
winning_player = 0
max_score = 20

def render_players_score():
    global winning_player
    display.move(0, 1)
    score_a = "{:>2}".format(player_one_score)
    score_b = "{:>2}".format(player_two_score)
    display.write(f'{score_a}    A--B    {score_b}')

    if player_two_score >= max_score:
        winning_player = 2
        change_state(3)
        return

    if player_one_score >= max_score:
        winning_player = 1
        change_state(3)
        return

def change_state(new_state):
    global game_state, player_one_score, player_two_score, winning_player

    print(f"changing state to {new_state}")
    sleep(1)

    if new_state == 0:
        player_one_score = 0
        player_two_score = 0
        winning_player = 0

        display.clear()
        display.write("  play with me")
        display.move(0, 1)
        display.write("  press button")

    if new_state == 1:
        display.clear()
        display.write("    2 players")
        display.move(0, 1)
        display.write("   fastest wins")

    if new_state == 2:
        display.clear()
        display.write("game ongoing")
        display.move(0, 1)
        display.write("2 players")

    if new_state == 3:
        display.clear()
        display.write("  the winner is")
        display.move(0, 1)
        display.write(f"player {winning_player}")
        reset_timer.init(period=3000, mode=Timer.ONE_SHOT, callback=reset_game)

    game_state = new_state

def player_one_score_increase():
    global player_one_score
    player_one_score = player_one_score + 1
    render_players_score()

def player_two_score_increase():
    global player_two_score
    player_two_score = player_two_score + 1
    render_players_score()

def button_one_action(little_pin, massive_event):
    global player_one_score
    print(f'button on pin {little_pin} registered {massive_event}')
    if massive_event == Button.RELEASED:
        player_one_score_increase()

def button_two_action(little_pin, massive_event):
    global player_two_score
    print(f'button on pin {little_pin} registered {massive_event}')
    if massive_event == Button.RELEASED:
        player_two_score_increase()

def button_three_action(little_pin, massive_event):
    global game_state
    print(f'button on pin {little_pin} registered {massive_event}')
    if game_state == 0 and massive_event == Button.RELEASED:
        change_state(1)
        return

    if game_state == 1 and massive_event == Button.RELEASED:
        change_state(2)
        return

buttonA = Button(5, rest_state=True, callback=button_one_action)
buttonB = Button(6, rest_state=True, callback=button_two_action)
buttonC = Button(7, rest_state=False, callback=button_three_action)

change_state(0)

def reset_game(timer_object):
    change_state(0)

while True:
    if game_state == 0:
        buttonC.update()

    if game_state == 1:
        buttonC.update()

    if game_state == 2:
        buttonA.update()
        buttonB.update()

    if game_state == 3:
        pass

    if game_state == 4:
        pass
