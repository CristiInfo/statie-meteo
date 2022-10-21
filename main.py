OLED.init(128, 64)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("Deco_1DF0", "")
basic.show_icon(IconNames.YES)

def on_forever():
    OLED.write_string_new_line("Temperatura este " + str(Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C)))
    OLED.write_string_new_line("Umiditatea este " + str(Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY)))
    OLED.write_string_new_line("Presiunea este " + str(Environment.octopus_BME280(Environment.BME280_state.BME280_PRESSURE)))
    OLED.write_string_new_line("Altitudinea este " + str(Environment.octopus_BME280(Environment.BME280_state.BME280_ALTITUDE)))
    basic.pause(2000)
basic.forever(on_forever)

def on_forever2():
    ESP8266_IoT.connect_thing_speak()
    ESP8266_IoT.set_data("X0JNYHX7PWF3UFCP",
        Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C),
        Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY),
        Environment.octopus_BME280(Environment.BME280_state.BME280_PRESSURE),
        Environment.octopus_BME280(Environment.BME280_state.BME280_ALTITUDE))
    ESP8266_IoT.upload_data()
    basic.pause(2000)
basic.forever(on_forever2)
