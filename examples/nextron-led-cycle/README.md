# NEXTRON — Dahili RGB LED renk döngüsü

Bu gerçek kaynak kodu, CodeRon'un mevcut `nextronLed(r, g, b)` servis API'si için hazırlanmıştır. Kullanıcı derlemenin başarılı olduğunu ve NEXTRON kartında kırmızı, yeşil, mavi renklerin sırayla yandığını bildirdi. Kullanılan PC/Android platformu belirtilmedi; ayrıntılar `verification.md` içindedir.

## Amaç

NEXTRON'un dahili RGB LED'ini sırayla kırmızı, yeşil, mavi ve kapalı durumuna geçirmek. Her durum 750 ms sürer. `delay()` yerine `millis()` kullanılır; döngü bekleyerek durdurulmaz. Parlaklık örnekte 32/255'tir.

Kod motor hareket komutu vermez; `nextronStop()` çağırır. `robotCanRun()` LED mantığının çalışmasına izin verir, kendi başına hareket başlatmaz.

## Malzemeler ve bağlantılar

- 1 adet NEXTRON kartı ve kartın standart kullanımına uygun beslemesi.
- İlk servis kurulumu/USB yükleme için uygun veri kablosu; mevcut servisle kablosuz yükleme kullanılıyorsa CodeRon'un normal bağlantı akışı.
- Harici LED, direnç veya ek pin bağlantısı gerekmez. Doğrudan GPIO numarası atanmaz.

## CodeRon'da açma

1. `NextronLed.ron` dosyasını PC veya Android CodeRon'da `.ron aç` ile açın.
2. Kartı **NEXTRON**, profili **NEXTRON OTA / Serbest kod** olarak kontrol edin. Genel/servissiz Arduino profili bu örneğin API'sini sağlamaz.
3. Kaynağı inceleyin, ardından normal CodeRon derleme/yükleme düğmelerini kullanın. Dosyayı açmak kendiliğinden derleme veya yükleme başlatmaz.
4. Dört anahtarın tamamı ON iken servis modu seçilir; bu modun LED göstergeleri örneğin renk döngüsünden ayrıdır. Örneği normal proje modunda başlatın. Mevcut servis başlangıç penceresi yaklaşık 3,5 saniyedir.

`CodeRonBoard.h` ve servis kaynakları CodeRon tarafından derleme sırasında sağlanır. Bunları elle proje dosyalarına kopyalamayın. API'nin kullandığı Adafruit NeoPixel bağımlılığı CodeRon'un mevcut servis araç zincirinden gelir; bu örnek ek kütüphane kurdurmaz.

## Beklenen sonuç ve değiştirme

Kodun beklenen döngüsü, normal proje modunda yaklaşık 750 ms aralıklarla kırmızı → yeşil → mavi → kapalı şeklindedir. Kullanıcı kartta kırmızı/yeşil/mavi sırasını doğruladı; kapalı aşaması ve süre ölçümü ayrıca bildirilmedi.

- Hız: `COLOR_INTERVAL_MS` değerini değiştirin.
- Parlaklık: `LED_LEVEL` için 0–255 arasında değer kullanın.
- Renk: `nextronLed(kırmızı, yeşil, mavi)` parametrelerini değiştirin.

## Doğrulama

Kaynak API karşılaştırması, gerçek PC/Android proje hazırlama/içe aktarma kontrolleri ve kullanıcının başarılı derleme/kart çalışması bildirimi `verification.md` içinde raporlanır. Kullanılan platform ve yükleme yöntemi belirtilmediğinden PC ve Android derleme/yükleme durumları ayrı ayrı doğrulanmış sayılmaz. SPEEDRON uyumluluğu bu örnekle ilan edilmez.

## Yayın ve lisans

Kullanıcı bu örnek için **MIT** lisansını seçti. Metin bu klasördeki `LICENSE` dosyasındadır; telif sahibi **Robitron Robot Teknolojileri**, yıl **2026**. Aynı bildirim `.ron` paketinin `files` listesinde `LICENSE.txt` olarak da bulunur; uygulamaya kopyalanan projede korunur. Bu seçim bu örneğin kaynak kodu ve beraberindeki açıklamaları kapsar; CodeRon uygulama kaynaklarına, kart firmware'ine veya üçüncü taraf kütüphanelere lisans atamaz.

MIT bilgisi ve gerçek paket özeti `catalog-entry.pending.json` içindedir. Canlı `catalog.json` henüz değiştirilmedi. Web Codex örnek dosyalarını depoya ekleyip bu kaydı mevcut katalogla birleştirerek yayımlayabilir. Yayımlanmadan önce yerel `.ron` dosyasıyla çalışılabilir.
