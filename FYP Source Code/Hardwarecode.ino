#include <Wire.h>
#include <Adafruit_ADXL345_U.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SoftwareSerial.h>

// Pin Assignments
#define PULSE_SENSOR A0
#define ONE_WIRE_BUS 4

// GPS Module
SoftwareSerial gpsSerial(18, 19); // RX, TX

// DS18B20 Setup
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// ADXL345 Accelerometer
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

void setup() {
    Serial.begin(115200);   // Set baud rate for Serial Monitor
    gpsSerial.begin(115200); // Set the same baud rate for GPS

    // Initialize DS18B20
    sensors.begin();
    
    // Initialize ADXL345
    if (!accel.begin()) {
        Serial.println("No ADXL345 detected. Check wiring.");
        while (1);
    }
    accel.setRange(ADXL345_RANGE_2_G);

    Serial.println("Sensors Initialized.");
}

void loop() {
    // Read Heartbeat Pulse Sensor
    int pulseValue = analogRead(PULSE_SENSOR);
    Serial.print("Pulse: ");
    Serial.print(pulseValue);
    
    // Read Temperature from DS18B20
    sensors.requestTemperatures();
    float temperatureC = sensors.getTempCByIndex(0);
    Serial.print(" | Temperature: ");
    Serial.print(temperatureC);
    Serial.print("°C");
    
    // Read Accelerometer Data
    sensors_event_t event;
    accel.getEvent(&event);
    Serial.print(" | Accel X: ");
    Serial.print(event.acceleration.x);
    Serial.print(" Y: ");
    Serial.print(event.acceleration.y);
    Serial.print(" Z: ");
    Serial.print(event.acceleration.z);
    
    // Read GPS Data
    Serial.print(" | GPS Data: ");
    while (gpsSerial.available()) {
        char c = gpsSerial.read();
        Serial.write(c);
    }
    
    Serial.println();
    delay(1000); // 1-second delay
}
