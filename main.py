n2 = 0
n1 = 0

def on_received_number(receivedNumber):
    for index in range(2):
        basic.show_number(receivedNumber)
        if receivedNumber == n2:
            basic.show_icon(IconNames.ASLEEP)
        elif receivedNumber < n2:
            basic.show_icon(IconNames.HAPPY)
        else:
            basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("hola")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global n1, n2
    n1 = randint(0, 6)
    radio.send_number(n1)
    n2 = randint(0, 6)
    basic.show_number(n2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
