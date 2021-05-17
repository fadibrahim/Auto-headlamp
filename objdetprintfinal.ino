
  250 200   
  VFR
  32e#include <Servo.h>
int servoPin1 = 6;
int servoPin2 = 11;
Servo servo1;
Servo servo2;
int x_line;
int center = 340;
int sudut = 90;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);
  servo1.write(sudut);
  servo2.write(sudut);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    x_line = Serial.parseInt();
  }
  sudut = map(x_line, 0, 640, 0, 180);
  servo1.write(sudut);
  servo2.write(sudut);
  Serial.println(sudut);
//  for (x_line; x_line > center; sudut++)
//  {
//    Servo1.write(servoPin, sudut);
//  }
//  for (x_line; x_line < center; sudut--)
//  {
//    Servo1.write(servoPin, sudut);
//  }
  delay(100);
}
