let n2 = 0
let n1 = 0
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    for (let index = 0; index < 2; index++) {
        basic.showNumber(receivedNumber)
        if (receivedNumber == n2) {
            basic.showIcon(IconNames.Asleep)
        } else if (receivedNumber < n2) {
            basic.showIcon(IconNames.Happy)
        } else {
            basic.showIcon(IconNames.Sad)
        }
        
    }
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("hola")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    n1 = randint(0, 6)
    radio.sendNumber(n1)
    n2 = randint(0, 6)
    basic.showNumber(n2)
})
basic.forever(function on_forever() {
    
})
