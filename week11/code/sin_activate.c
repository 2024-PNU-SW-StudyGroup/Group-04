#include <SPI.h>

// 핀 설정
const int LE = 10;   // Latch Enable 핀 (Arduino 핀 10)
const int CE = 9;    // Chip Enable 핀
const int MUX = 8;   // MUX 핀 (선택 사항)

// 레지스터 값 (1.4GHz 생성용)
uint32_t regValues[] = {
  0x00580005, // R0 - 주파수 설정 (Frac-N 모드)
  0x80008011, // R1 - PLL 프리셋
  0x0000004B, // R2 - 충돌 방지
  0x000004B3, // R3 - Charge Pump 및 기타 설정
  0x00C80004, // R4 - Band Select 및 필터 설정
  0x00580005  // R5 - Lock Detect 및 기타 제어
};

void setup() {
  // 핀 모드 설정
  pinMode(LE, OUTPUT);
  pinMode(CE, OUTPUT);
  pinMode(MUX, OUTPUT);

  // 기본 상태 초기화
  digitalWrite(LE, HIGH);
  digitalWrite(CE, LOW);
  digitalWrite(MUX, LOW);

  // SPI 설정
  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));

  // ADF4350 초기화
  digitalWrite(CE, HIGH); // ADF4350 활성화
  delay(10);              // 안정화 대기

  // 레지스터 전송
  for (int i = 5; i >= 0; i--) { // R5 -> R0 순서로 전송
    sendRegister(regValues[i]);
  }
}

void loop() {
  // 1.4GHz 신호가 생성됩니다.
}

// ADF4350 레지스터 전송 함수
void sendRegister(uint32_t value) {
  digitalWrite(LE, LOW); // Latch 비활성화
  SPI.transfer((value >> 24) & 0xFF); // 상위 8비트 전송
  SPI.transfer((value >> 16) & 0xFF);
  SPI.transfer((value >> 8) & 0xFF);
  SPI.transfer(value & 0xFF);         // 하위 8비트 전송
  digitalWrite(LE, HIGH); // Latch 활성화
}