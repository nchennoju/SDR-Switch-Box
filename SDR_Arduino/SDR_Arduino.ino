#define SERIAL_PORT_SPEED 115200

const int relayPins[] = {10, 11, 12, 13};
int relayState[] = {0, 0, 0, 0};
int in;


void setup() {
  Serial.begin(SERIAL_PORT_SPEED);
  for (int i = 0; i < sizeof(relayPins); i++) {
    pinMode(relayPins[i], OUTPUT);
  }
}

void loop() {

  if (Serial.available() > 0) {
      in = Serial.parseInt();
     
      if(in == -1){
        Serial.println("ALL OFF");
      }else if(in >= 1 && in <= 4){
        if(relayState[in-1] == 0){
          relayState[in-1] = 1;
          digitalWrite(relayPins[in-1], HIGH);
        }else if(relayState[in-1] == 1){
          relayState[in-1] = 0;
          digitalWrite(relayPins[in-1], LOW);
        }
      }
  }
  
}

void off() {
  for(int i = 0; i < sizeof(relayPins); i++){
    digitalWrite(relayPins[i], LOW);
  }
}
