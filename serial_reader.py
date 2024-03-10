# BRINKS - HUB READER
# Code for reading data from printers via serial comm
import serial
import multiprocessing

# Function to read data from individual printer
def read_from_printer(serial_port, baud_rate=9600, timeout=1):
    try:
        ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=timeout)
        if ser.is_open:
            print(f"Connected to {serial_port} at {baud_rate} bps")

            while True:
                data = ser.readline().decode().strip()
                if data:
                    print(f"Printer {serial_port}: {data}")

    except serial.SerialException as e:
        print(f"Error: {e}")

# Infinite loop of program
if __name__ == "__main__":
    # List of serial ports for your printers connected to the USB hub
    # Here add more ports
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

