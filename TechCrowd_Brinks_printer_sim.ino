#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
  while (!Serial); // Wait for the serial port to be ready
}

void loop() {
  // Create a JSON object
  StaticJsonDocument<200> jsonDoc; // Adjust the size based on your data size
  jsonDoc["name"] = "Bukaj Dzi";
  jsonDoc["age"] = 274;
  jsonDoc["city"] = "Bukajovice";

  // Serialize the JSON object into a buffer
  char buffer[200]; // Adjust the size based on your data size
  serializeJson(jsonDoc, buffer);

  // Send the JSON data via serial communication
  Serial.println(buffer);

  // Wait for a few seconds before sending the next JSON data
  delay(5000);
}
