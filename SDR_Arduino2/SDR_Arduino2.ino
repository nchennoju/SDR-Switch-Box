#define SERIAL_PORT_SPEED 115200

const int relayPins[] = {10, 11, 12, 13};
int in;
int state = 0;


void setup() {
  Serial.begin(SERIAL_PORT_SPEED);
  for (int i = 0; i < sizeof(relayPins); i++) {
    pinMode(relayPins[i], OUTPUT);
  }
}

void loop() {

  if (Serial.available() > 0) {
      in = Serial.parseInt(); //2 digit number, 1st digit relay, 2nd digit state

      state = in%10;
      in /= 10;

      if(in >= 1 && in <= 4){
        if(state == 1){
          digitalWrite(relayPins[in - 1], HIGH);
          Serial.println(String(in) + "\tHIGH");
        }else if(state == 0){
          digitalWrite(relayPins[in - 1], LOW);
          Serial.println(String(in) + "\tLOW");
        }
      }
  }
  
}
