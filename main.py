def on_button_pressed_a():
    basic.show_number(randint(1, 100))
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
