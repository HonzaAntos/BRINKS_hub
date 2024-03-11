#include <ArduinoJson.h> // Install this library via Arduino Library Manager if not already installed

void setup() {
  Serial.begin(9600); // Set the baud rate to match the one used in your serial monitor
}

void loop() {
  // JSON data as a string
  const char* jsonData = R"(
    {
      "printerName": "OfficePrinter1",
      "printerStatus": "Online",
      "paperTray": {
        "capacity": 250,
        "remainingSheets": 150
      },
      "inkCartridges": [
        {
          "color": "Black",
          "level": 80
        },
        {
          "color": "Cyan",
          "level": 60
        },
        {
          "color": "Magenta",
          "level": 70
        },
        {
          "color": "Yellow",
          "level": 75
        }
      ],
      "isDuplexSupported": true,
      "isColorPrintingSupported": true,
      "supportedPaperSizes": ["A4", "Letter", "Legal", "A3"],
      "maintenanceSchedule": {
        "lastMaintenanceDate": "2023-07-15",
        "nextMaintenanceDate": "2023-09-30",
        "maintenanceHistory": [
          {
            "date": "2023-04-01",
            "type": "Cleaning"
          },
          {
            "date": "2023-06-15",
            "type": "Ink Replacement"
          }
        ]
      },
      "networkStatus": {
        "isConnected": true,
        "ipAddress": "192.168.1.100",
        "subnetMask": "255.255.255.0",
        "gateway": "192.168.1.1",
        "dnsServers": ["8.8.8.8", "8.8.4.4"]
      }
    }
  )";

  // Send the JSON data via serial communication
  Serial.println(jsonData);

  // Wait for a short period before sending again (adjust as needed)
  delay(10000);
}
