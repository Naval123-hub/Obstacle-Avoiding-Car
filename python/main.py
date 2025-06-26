import serial
import matplotlib.pyplot as plt
import time

PORT = 'COM3'  # Change this to match your system
BAUD = 9600

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)  # Allow time for Arduino reset
except:
    print(f"Error: Could not open serial port {PORT}")
    exit()

plt.ion()
fig, ax = plt.subplots()
ydata = []

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("Front:"):
            distance = int(line.split(":")[1].strip())
            ydata.append(distance)
            if len(ydata) > 50:
                ydata.pop(0)

            ax.clear()
            ax.plot(ydata, label="Front Distance (cm)")
            ax.set_ylim(0, 100)
            ax.set_ylabel("Distance (cm)")
            ax.set_title("Real-Time Obstacle Distance")
            ax.legend()
            plt.pause(0.01)
    except KeyboardInterrupt:
        print("Stopped by user.")
        break
    except:
        continue
