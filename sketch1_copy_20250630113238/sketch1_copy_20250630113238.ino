const int LED = 13; //This is creating a constant called LED that is of type integer corresponding to the pin
// The LED is connected to

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT); //defines as an output pin

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED, HIGH); //Turning on the LED
  delay(1000); //wait 1 sec
  digitalWrite(LED, LOW);
  delay(1000);

}
