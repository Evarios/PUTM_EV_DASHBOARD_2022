int engmode = 1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int speed = 10;
  int lv = 10;
  
  float lv_voltage = 0.25;
  float lv_temp = 0.2;
  //speed test
  for(int i = 0; i < 20; i++){
    Serial.println("speed:"+String(speed*i));
    delay(250);
  }
  //lv test
  for(int i = 0; i < 10; i++){
    Serial.println("lv_charge_percent:"+String(lv*i));
    delay(500);
  }
  for(int i = 0; i < 10; i++){
    Serial.println("lv_voltage:"+String(20+i*lv_voltage));
    delay(500);
  }

  for(int i = 0; i < 10; i++){
    Serial.println("lv_avg_temp:"+String(20+i*lv_temp));
    delay(500);
  }
  //hv test
  for(int i = 0; i < 10; i++){
    Serial.println("hv_charge_percent:"+String(lv*i));
    delay(500);
  }
  for(int i = 0; i < 10; i++){
    Serial.println("hv_voltage:"+String(490+10*i*lv_voltage));
    delay(500);
  }

  for(int i = 0; i < 10; i++){
    Serial.println("hv_avg_temp:"+String(40+i*lv_temp));
    delay(500);
  }
  if(engmode == 1){
    Serial.println("engine_mode:1");
    engmode=2;
  } else{
    Serial.println("engine_mode:2");
    engmode=1;
  }



}
