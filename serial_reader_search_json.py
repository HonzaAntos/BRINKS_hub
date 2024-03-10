import serial
import multiprocessing
import json

def read_from_printer(serial_port, baud_rate=9600, timeout=1):
    try:
        ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=timeout)
        if ser.is_open:
            print(f"Connected to {serial_port} at {baud_rate} bps")

            while True:
                data = ser.readline().decode().strip()
                if data:
                    print(f"Printer {serial_port}: {data}")

                    try:
                        # Parse the received data as JSON
                        json_data = json.loads(data)

                        # Search for data in the JSON data
                        search_criteria = "name"
                        if search_criteria in json_data:
                            found_value = json_data[search_criteria]
                            print(f"Found '{search_criteria}' in printer {serial_port} JSON data.")
                            print(f"Value: {found_value}")

                    except json.JSONDecodeError:
                        print("Received data is not a valid JSON format.")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # List of serial ports for your printers connected to the USB hub
    serial_ports = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2"]

    # Create a process for each printer
    processes = []
    for port in serial_ports:
        process = multiprocessing.Process(target=read_from_printer, args=(port,))
        processes.append(process)
        process.start()

    try:
        # Wait for all processes to finish (this will never happen because the read loops are infinite)
        for process in processes:
            process.join()

    except KeyboardInterrupt:
        # If you want to stop reading, press Ctrl+C to interrupt the program
        print("\nStopping the printer reading processes.")
        for process in processes:
            process.terminate()
