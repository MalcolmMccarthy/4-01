# created by malcolm
# for ics3u
# in november 2017
# calculates degrees in farenheit

import ui

def calculation(temperature_in_degrees_celcius):
    temperature_in_degrees_farenheit = temperature_in_degrees_celcius * 1.8 + 32
    view['answer_label'].text =str(temperature_in_degrees_farenheit)

def calculate_button(sender):
    temperature_in_degrees_celcius = int(view['temperature_textfield'].text)
    calculation(temperature_in_degrees_celcius)


view = ui.load_view()
view.present('sheet')
