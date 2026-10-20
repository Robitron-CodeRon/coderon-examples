// CodeRon - NEXTRON: dahili RGB LED renk dongusu.
// NEXTRON OTA / Serbest kod profiliyle derleyin.
// CodeRonBoard.h, CodeRon servis derleyicisi tarafindan saglanir.
#include <Arduino.h>
#include "CodeRonBoard.h"

constexpr uint32_t COLOR_INTERVAL_MS = 750;
constexpr uint8_t LED_LEVEL = 32;
uint32_t lastLedChange = 0;
uint8_t ledPhase = 3;

void robotSetup() {
  nextronStop();
  nextronLed(0, 0, 0);
  ledPhase = 3;
  lastLedChange = millis();
}

bool robotCanRun() {
  // LED orneginin calismasina izin verir; motor hareketi baslatmaz.
  return true;
}

bool robotSafety() {
  return true;
}

void robotLoop() {
  // Bu ornek motor hareket komutu vermez.
  nextronStop();
  const uint32_t now = millis();
  if (uint32_t(now - lastLedChange) < COLOR_INTERVAL_MS) {
    return;
  }
  lastLedChange = now;
  ledPhase = (ledPhase + 1) % 4;

  switch (ledPhase) {
    case 0:
      nextronLed(LED_LEVEL, 0, 0);  // Kirmizi
      break;
    case 1:
      nextronLed(0, LED_LEVEL, 0);  // Yesil
      break;
    case 2:
      nextronLed(0, 0, LED_LEVEL);  // Mavi
      break;
    default:
      nextronLed(0, 0, 0);          // Kapali
      break;
  }
}
