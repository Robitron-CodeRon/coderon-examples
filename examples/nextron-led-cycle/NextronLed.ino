// NEXTRON kartının kendi ışığını sırayla kırmızı, yeşil, mavi yakıp kapatır.
// CodeRon kart profili: NEXTRON OTA / Serbest kod.
// CodeRonBoard.h dosyasını CodeRon derleyicisi sağlar.
#include <Arduino.h>  // Zamanı okumak için kullandığımız millis() gibi temel Arduino araçlarını ekler.
#include "CodeRonBoard.h"  // nextronLed() ve nextronStop() gibi NEXTRON komutlarını kullanmamızı sağlar.

constexpr uint32_t COLOR_INTERVAL_MS = 750;  // Her rengin 750 milisaniye, yani 0,75 saniye kalmasını belirler. 1500 yazarsan renkler daha yavaş değişir.
constexpr uint8_t LED_LEVEL = 32;  // Işığın parlaklığını 32 yapar. 0 kapalı, 255 en parlaktır; burada düşük parlaklık kullanılır.
uint32_t lastLedChange = 0;  // Rengin en son değiştiği zamanı tutacak kutuyu oluşturur; başlangıç değeri 0'dır.
uint8_t ledPhase = 3;  // Hangi rengin sırada olduğunu tutar. 3 kapalı aşamadır; sonraki adım 0, yani kırmızı olur.

void robotSetup() {  // Proje başlarken bir kez yapılacak hazırlıkların başladığı yerdir. Süslü parantez bu bölümü açar.
  nextronStop();  // Başlangıçta motorların durmasını ister; bu örnek robotu hareket ettirmez.
  nextronLed(0, 0, 0);  // Kırmızı, yeşil ve maviyi 0 yaparak ışığı başlangıçta kapatır.
  ledPhase = 3;  // Renk sayacını kapalı aşamaya getirir; ilk değişimde kırmızı seçilecektir.
  lastLedChange = millis();  // Kartın açılışından beri geçen milisaniyeyi kaydeder. İlk renk değişimi bu andan 750 ms sonra olur.
}  // Başlangıç hazırlıkları burada biter.

bool robotCanRun() {  // Servisin, bu örneğin çalışmasına izin verilip verilmediğini sorduğu bölümü açar.
  // LED örneğinin çalışmasına izin verir; motor hareketini başlatmaz.
  return true;  // Evet anlamındaki true değerini döndürerek örneğin çalışmasına izin verir.
}  // Çalışma izni bölümü burada biter.

bool robotSafety() {  // Servisin proje güvenlik durumunu sorduğu bölümü açar.
  return true;  // Bu LED örneğinin ek bir durdurma koşulu olmadığını bildirir. Bu satır fiziksel bir güvenlik sensörü ölçmez.
}  // Bu kontrol bölümü burada biter.

void robotLoop() {  // Proje çalışırken tekrar tekrar çağrılan ana bölümü açar.
  // Bu örnek yalnız ışığı kontrol eder; motorları hareket ettirmez.
  nextronStop();  // Her turda motorların durmasını ister.
  const uint32_t now = millis();  // Şu anki zamanı now adlı kutuya koyar. Süreyi bu değerle karşılaştıracağız.
  if (uint32_t(now - lastLedChange) < COLOR_INTERVAL_MS) {  // Son renk değişiminden beri 750 ms geçip geçmediğine bakar. Geçmediyse aşağıdaki kısa çıkışı çalıştırır.
    return;  // Bu turu hemen bitirir. Kartı bekletmez; servis diğer işlerini sürdürebilir ve sonraki turda süre yeniden kontrol edilir.
  }  // Süre kontrolünün içindeki bölüm burada biter.
  lastLedChange = now;  // 750 ms geçtiyse son değişim zamanını şimdi olarak günceller.
  ledPhase = (ledPhase + 1) % 4;  // Renk sayacını bir artırır. % 4 sayesinde sıra 0, 1, 2, 3 olur, sonra tekrar 0'a döner.

  switch (ledPhase) {  // Renk sayacına bakıp aşağıdaki dört seçenekten birini çalıştırır.
    case 0:  // Sayaç 0 ise kırmızı seçeneği buradan başlar.
      nextronLed(LED_LEVEL, 0, 0);  // Üç sayı sırasıyla kırmızı, yeşil ve mavidir. Yalnız kırmızıyı LED_LEVEL parlaklığında yakar.
      break;  // Kırmızı seçeneğini bitirir; diğer renklerin komutlarına devam etmez.
    case 1:  // Sayaç 1 ise yeşil seçeneği buradan başlar.
      nextronLed(0, LED_LEVEL, 0);  // Yalnız yeşili LED_LEVEL parlaklığında yakar; kırmızı ve mavi kapalıdır.
      break;  // Yeşil seçeneğini bitirir.
    case 2:  // Sayaç 2 ise mavi seçeneği buradan başlar.
      nextronLed(0, 0, LED_LEVEL);  // Yalnız maviyi LED_LEVEL parlaklığında yakar; kırmızı ve yeşil kapalıdır.
      break;  // Mavi seçeneğini bitirir.
    default:  // Diğer durumda, burada sayaç 3 olduğunda, kapalı seçeneğini kullanır.
      nextronLed(0, 0, 0);  // Üç rengin parlaklığını da 0 yaparak ışığı kapatır. 750 ms sonra döngü yeniden kırmızıya geçer.
      break;  // Kapalı seçeneğini bitirir.
  }  // Renk seçme bölümü burada biter.
}  // Tekrarlanan ana bölüm burada biter; servis uygun olduğunda tekrar çağırır.
