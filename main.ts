OLED.init(128, 64)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("Deco_1DF0", "")
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    OLED.writeStringNewLine("Temperatura este " + Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C))
    OLED.writeStringNewLine("Umiditatea este " + Environment.octopus_BME280(Environment.BME280_state.BME280_humidity))
    OLED.writeStringNewLine("Presiunea este " + Environment.octopus_BME280(Environment.BME280_state.BME280_pressure))
    OLED.writeStringNewLine("Altitudinea este " + Environment.octopus_BME280(Environment.BME280_state.BME280_altitude))
    basic.pause(2000)
})
basic.forever(function () {
    ESP8266_IoT.connectThingSpeak()
    ESP8266_IoT.setData(
    "X0JNYHX7PWF3UFCP",
    Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C),
    Environment.octopus_BME280(Environment.BME280_state.BME280_humidity),
    Environment.octopus_BME280(Environment.BME280_state.BME280_pressure),
    Environment.octopus_BME280(Environment.BME280_state.BME280_altitude)
    )
    ESP8266_IoT.uploadData()
    basic.pause(2000)
})
