import serial
import matplotlib.pyplot as plt
import time
import re
import sys

# ========= USER CONFIGURATION =========
SERIAL_PORT = 'COM3'  # Change this to match your system
BAUD_RATE = 9600
MAX_POINTS = 50
# ======================================

def connect_serial(port, baud):
    try:
        ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)  # Allow Arduino to reset
        print(f"✅ Connected to {port}")
        return ser
    except serial.SerialException:
        print(f"❌ Error: Could not open serial port {port}")
        sys.exit(1)

def parse_line(line):
    """
    Parses a line like 'Front: 25' and returns ('Front', 25)
    """
    match = re.match(r"(Front|Left|Right):\s*(\d+)", line)
    if match:
        label = match.group(1)
        value = int(match.group(2))
        return label, value
    return None, None

def plot_front_distance(front_data):
    plt.cla()
    plt.plot(front_data, label="Front Distance (cm)", color='blue')
    plt.ylim(0, 100)
    plt.xlabel("Time (frames)")
    plt.ylabel("Distance (cm)")
    plt.title("Live Front Distance from Ultrasonic Sensor")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.pause(0.01)

def main():
    ser = connect_serial(SERIAL_PORT, BAUD_RATE)

    front_data = []
    left_data = []
    right_data = []

    plt.ion()
    fig = plt.figure()

    try:
        while True:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    print(f"📟 {line}")
                    label, value = parse_line(line)

                    if label == "Front":
                        front_data.append(value)
                        if len(front_data) > MAX_POINTS:
                            front_data.pop(0)
                        plot_front_distance(front_data)

                    # Optionally collect left/right data
                    elif label == "Left":
                        left_data.append(value)
                    elif label == "Right":
                        right_data.append(value)

    except KeyboardInterrupt:
        print("\n👋 Exiting gracefully...")
        ser.close()
        plt.ioff()
        plt.close()
        sys.exit(0)

if __name__ == "__main__":
    main()
