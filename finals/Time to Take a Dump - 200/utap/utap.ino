int portsActive = 4;
int portNow[4] = {0, 0, 0, 0};
int portThreshold[4] = {300, 300, 300, 300};
boolean dn[4] = {false, false, false, false};
boolean dl[4] = {false, false, false, false};
int portCount[4] = {0, 0, 0, 0};

void setup() {
  Serial.begin(9600);
  Serial.println("0123: p27 p30 p44 p52");
}

void loop() {
  for(int i = 0; i < portsActive; i++){
    portNow[i] = analogRead(i);
    
    /*
    Serial.print(i);
    Serial.print(" : ");
    Serial.println(portNow[i]);//*/
    
    if(portNow[i] > portThreshold[i] && dl[i] == false){
      /*
      portCount[i]++;
      Serial.print(i);
      Serial.print(": ");
      Serial.println(portCount[i]);//*/
      
      Serial.print(i);
      dn[i] = true;
    }else if (dl[i] == true && portNow[i] < portThreshold[i]){
      dn[i] = false;
    }
    dl[i] = dn[i];
  }
}
