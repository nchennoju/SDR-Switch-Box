// Read Pot Adjustable Analog Voltage
// Use External voltage source
// Wire Potentiomenter to potPin

const int potPin = A0;

void setup() {

  // Initiate serial Communications
  Serial.begin(9600);

}

// Code Start
void loop() {

  // Read Pot Value and Display as Voltage in serial monitor
  Serial.println(map(analogRead(potPin),0,1023,0,5));

  // Delay for stability
  delay(1);

}
