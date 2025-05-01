// anything after two slashes like this is just a comment, not code

// identify which pins we connect to
#define buttonA  4 // this is the number of the pin we connect the button A to
#define led     13 // this is the number of the pin for the light on the board

// bool just means that something can be 'true' or 'false' (HIGH or LOW)
bool buttonStatusA; // this is where we will keep track of if button A is pushed

// these two lines of code just makes the rest of the code easier to understand
#define NOTPUSHED HIGH
#define PUSHED    LOW


// the "setup" code runs one time when you first run the program
void setup() {

  // the led is an output
  pinMode(led, OUTPUT);

  // the button is an INPUT
  // PULLUP allows the Arduino to detect when the button *isn't* pushed
  pinMode(buttonA, INPUT_PULLUP);
}


// the "loop" code runs over and over again
void loop() {

  buttonStatusA = digitalRead(buttonA); // read the status of button A

  // if the button is not pushed, turn on the led
  if (buttonStatusA == NOTPUSHED) {
    digitalWrite(led, HIGH); // turn the LED on
  } else {
    digitalWrite(led, LOW);  // turn the LED off
  }
}
