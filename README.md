# 🤖 Obstacle-Avoiding Car using Arduino + Python

This project demonstrates a DIY robotic car that avoids obstacles in real-time using ultrasonic sensors and intelligent path decision-making. The system is built using an Arduino microcontroller and enhanced with Python-based real-time visualization through serial communication.

---

## 🚗 Features

- Real-time obstacle detection using ultrasonic sensors
- Directional path correction: turn left, right, or reverse when blocked
- Servo-based sensor scanning
- Serial communication between Arduino and Python
- Live data visualization in Python using `matplotlib`

---

## 🛠️ Hardware Components

| Component           | Quantity |
|---------------------|----------|
| Arduino UNO         | 1        |
| HC-SR04 Ultrasonic Sensor | 1  |
| SG90 Servo Motor    | 1        |
| L298N Motor Driver  | 1        |
| DC Motors           | 2        |
| Robot Chassis       | 1        |
| Jumper Wires, Battery, USB cable | as needed |

---

## 💻 Software Requirements

- **Arduino IDE** (for uploading code to the Arduino board)
- **Python 3.7+**
  - `pyserial`
  - `matplotlib`

Install Python libraries with:

```bash
pip install -r python/requirements.txt
