#define ledDer 7
#define ledIzq 8
#define ledLucesPWM 6
#define ledStop 12
#define ledDoor 10

const int sensorPin = A1;
int coma1,n,led;
String datos, numero, indice;
float volt, signalLuces, signal1, valueAdc, volts, celsius, valorLuces;
unsigned long tiempo1, tiempo2;
unsigned long t1 = 0, t2 = 200;
volatile int contador = 0;

float a = 0;
float b = 0;
float c = 0;
float d = 0;

void setup() {
  
  Serial.begin(9600);
  pinMode(ledIzq, INPUT);
  pinMode(ledDer, INPUT);
  pinMode(ledStop, INPUT);
  pinMode(ledLucesPWM, OUTPUT);
  pinMode(ledDoor, INPUT);
  //attachInterrupt(0,interrupcion0,RISING);
  
  
}

void loop() {
  
  tiempo1 = millis();
  tiempo2 = millis();

  //Sensor de puertas / digital
  int valueDoor = digitalRead(ledDoor);
  Serial.print(valueDoor);

  //Luces direccionales / digital (actuador)
  int valueIzq = digitalRead(ledIzq);
  Serial.print(valueIzq);
 
  int valueDer = digitalRead(ledDer);
  Serial.print(valueDer);
  
  int valueStop = digitalRead(ledStop);
  Serial.print(valueStop);
  Serial.print("     ");

  //Luces medias y altas / analógico
  signalLuces = analogRead(A2);
  valorLuces = (((signalLuces/1023)*5.5));
  
  //Sensor de rpm / analógico
  signal1 = analogRead(A0);
  contador = (((signal1/1023)*5.5)*100);
  
  //Sensor de temperatura / analógico
  valueAdc = analogRead(sensorPin);
  volts = (valueAdc * 5) / 1023.0;
  celsius = volts * 100.00; 
  
  if (tiempo1-t1>=200){
    t1 = tiempo1;
    delay(999); // retardo de casi 1 segundo
    Serial.print(valorLuces);
    Serial.print("     ");
    Serial.print(contador*60);
    Serial.print("     ");
    Serial.print (((contador*60)*6.28/60)/11); 
    Serial.print ("     ");
    a=(((contador*60)*6.28/60)*0.2159);
    c=a+b;
    b=c;
    Serial.print(d); 
    Serial.print("     ");
    if (c>1000){
      d=d+1;
      Serial.print(d);
      c=0;
      a=0;
      b=0;
    }
    contador = 0;
    Serial.println(celsius);
    
  }
  
/*
 //Luces medias y altas (led y slider)
 if (tiempo2-t2>=200){
  t2 = tiempo2;
  if (Serial.available()>0){
    
    datos = Serial.readString();
    coma1 = datos.indexOf(',');
    indice = datos.substring(0, coma1);
    numero = datos.substring(coma1+1);

    led = numero.toInt();
    n = indice.toInt();
    
    if(n == 1){
      analogWrite(ledLucesPWM, led);
     }    
  }
}
*/
}

//void interrupcion0(){
//  contador++;
//}
