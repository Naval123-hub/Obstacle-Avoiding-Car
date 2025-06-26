#include <Servo.h>

#define trigPin 9
#define echoPin 10
#define motor1A 2
#define motor1B 3
#define motor2A 4
#define motor2B 5

Servo myServo;

long readDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void moveForward() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
}

void moveBackward() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
}

void turnLeft() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
}

void turnRight() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
}

void stopMotors() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, LOW);
}

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motor1A, OUTPUT);
  pinMode(motor1B, OUTPUT);
  pinMode(motor2A, OUTPUT);
  pinMode(motor2B, OUTPUT);

  Serial.begin(9600);
  myServo.attach(6);
  myServo.write(90);  // Center
}

void loop() {
  myServo.write(90);
  delay(300);
  long front = readDistance();
  Serial.print("Front: "); Serial.println(front);

  if (front < 20) {
    stopMotors();
    delay(200);

    myServo.write(150);
    delay(500);
    long left = readDistance();
    Serial.print("Left: "); Serial.println(left);

    myServo.write(30);
    delay(500);
    long right = readDistance();
    Serial.print("Right: "); Serial.println(right);

    myServo.write(90);
    delay(300);

    if (left > 20) {
      turnLeft();
      delay(700);
    } else if (right > 20) {
      turnRight();
      delay(700);
    } else {
      moveBackward();
      delay(700);
    }
  } else {
    moveForward();
  }

  delay(100);
}
