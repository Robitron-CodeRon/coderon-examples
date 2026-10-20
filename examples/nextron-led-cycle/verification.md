# Doğrulama kaydı — NEXTRON LED örneği

Tarih: 20 Ekim 2026. Yerel CodeRon PC 1.33.0 / Android 1.23 kaynaklarıyla kontrol edildi.

## Geçen kontroller

- `.ron` içindeki `source` ve ana dosya, gerçek `NextronLed.ino` ile birebir aynı.
- Aday katalog girdisi uygulamanın gerçek katalog doğrulayıcısından geçti; boyut ve SHA-256 gerçek dosyadan hesaplandı.
- PC ve Android ortak örnek proje ayrıştırıcısı dosyaları, NEXTRON modelini, OTA profilini ve `free` çalışma türünü kabul etti.
- Android'in mevcut `mobile.js:validateRon` işlevi gerçek paketle çalıştırıldı ve dosya/ayarlar korundu.
- Gerçek PC `prepareService` işlevi NEXTRON servis korumasını ve LED API'sini ekledi; kaynak dosya değiştirilmedi, `NX_TACTICS 0` üretildi.
- Gerçek Android `ProjectSource`, `SketchSource`, `OfflineCompiler`, `Esp32Image` Java kaynakları JVM'de derlendi. `ProjectSource.prepare` gerçek örnekle çalıştırıldı; API, robot hook'ları, `NX_TACTICS 0` ve özgün kaynağın korunması kontrol edildi.
- Kaynakta motor hareketi/doğrudan pin yazımı veya `delay()` çağrısı bulunmadığı; motor durdurma çağrısı bulunduğu denetlendi.

Komutlar, `coderon-examples` klasöründen:

```text
node tools/verify-led-example.cjs
python tools/verify-led-android.py
```

Bu araçlar yerel PC/Android kaynaklarını yan yana bekler. GitHub CI'da tek başına uygulama kaynaklarının yerini tutmaz.

## Kullanıcı tarafından bildirilen gerçek kart sonucu

20 Ekim 2026 tarihli bu oturumda kullanıcı önce **“derleme tammalandı dedi”**, ardından karta yükleme denemesi sonrasında **“kırmızı yeşil mavi sırayla yanıyor yani işlem başarılı”** bilgisini verdi. Aynı mesajın tekrar gönderilmesi ikinci bir bağımsız test olarak sayılmadı.

Bu bildirim NEXTRON LED örneğinin kullanıcı tarafından başarılı derlendiği ve gerçek kartta kırmızı/yeşil/mavi döngüsünün görüldüğü şeklinde kaydedildi. Karta yükleme, bu çalışma sonucuyla kullanıcı tarafından doğrulanmış kabul edilir; USB/Bluetooth yöntemi belirtilmedi.

PC mi Android mi kullanıldığı, uygulama sürümü, kart revizyonu, derleme günlüğü, yüklenen ikili özeti ve test videosu alınmadı. Kapalı aşaması, 750 ms süre ölçümü, güç kesip açma ve iki platformda ayrı derleme/yükleme ayrıca doğrulanmadı. Ajan fiziksel karta erişmedi; kanıt kullanıcının bu sohbetteki bildirimidir.

Bu nedenle genel katalog `build` / `hardware` sonuçları kullanıcı bildirimiyle `passed`; NEXTRON uyumluluğu bu RGB davranışı için `verified` olarak güncellendi. Platforma özel PC/Android `compile` / `upload` durumları `unverified` kaldı.

## Yapılmayanlar ve yayın durumu

Ajan tarafından tam ESP32 firmware derlemesi ve bağlama veya fiziksel kart testi yapılmadı. Yerel Java kaynak hazırlama testleri bunların yerine geçmez. Kullanıcının yukarıdaki gerçek kart sonucu bu yerel kontrollerden ayrı tutulur.

Kullanıcı bu örnek için MIT lisansını seçti; örnek klasörüne `LICENSE` ve `.ron` içindeki dosyalara aynı metni taşıyan `LICENSE.txt` eklendi. LED `.ino` kodu ve davranışı değiştirilmedi. `.ron` paket boyutu/SHA-256 özeti lisans dosyası eklendiği için yeniden hesaplandı. Kullanıcının önceki kart bildirimi aynı LED kaynak koduna aittir; yeni ikili için ayrı fiziksel test iddiası yoktur. Canlı katalog ve uzak GitHub deposu henüz değiştirilmedi. Yayımlanmamış 1.0.0 adayının lisans/paket metadatası güncellendi.
## 20 Ekim 2026 — 1.0.1 anlatım güncellemesi (güncel)

Kullanıcı önceki yayından sonra örneğin uygulamada listelendiğini bildirdi. Platform ve yayımlanmış commit yerelde doğrulanmadı. Yukarıdaki henüz yayımlanmadı ifadeleri eski 1.0.0 adayını anlatır. Yerel catalog.json boş tarihsel kopyadır; canlı kataloğun yerine geçmez.

1.0.1 yalnız açıklama ve eğitim metadatasını yeniler: başlangıç seviyesinde README, kart görseli üzerindeki LED animasyon tanımı ve kaynakla eşleşen 52 satırlık açıklama kılavuzu. `.ino`, MIT'li `.ron` ve LICENSE.txt değişmedi. Animasyon fiziksel kart görüntüsü veya telemetri değildir. Yeni firmware/donanım testi yapılmadı; önceki kullanıcı bildirimi aynı kaynak için korunur.

Yerel kontroller: gerçek PC/Android proje ayrıştırma ve servis kaynak hazırlama; 52 satırın birebir kaynak eşleşmesi, kılavuz/paket SHA-256 ve boyut kontrolü, hatalı metadata reddi, güvenli metin gösterimi, oynat/durdur/adım/gizlenme/hareket azaltma testleri. Beş Python eğitim metadatası testi geçti. Bunlar gerçek uygulama görsel kabulü veya firmware derlemesi değildir. PC 1.34.0 / Android 1.24 kod36 yeni anlatım kaynaklarını içerir.

GitHub 1.0.1 yayını henüz yerelde yapılmadı. Katalog şemasına isteğe bağlı preview/codeGuide alanları eklenerek mevcut kayıt yükseltilmelidir. Yerelde jsonschema bağımlılığı bulunmadığından deponun eski dokuz şema testi bu oturumda çalıştırılmadı; web Codex yayın öncesi çalıştırmalıdır.
## 20 Ekim 2026 — 1.0.2 editör açıklamaları (en güncel)

Kullanıcı açıklamaları editörde de istedi. Her dolu `.ino` satırına Türkçe `//` yorumu eklendi; aynı içerik `.ron` kaynaklarına ve JSON kılavuzuna işlendi. MIT ve diğer proje ayarları korundu. Yorumlar çıkarılıp boşluklar normalize edildiğinde çalıştırılan kodun SHA-256 değeri, önceki gerçek kartta denenmiş 1.0.0 kaynağıyla aynıdır: `bc40b2d2d314862eef080393cb47691323c0c6c311fad86b432122f8c6cbcff7`. Test artık her dolu satırın yorum içermesini ve bu özeti denetler. Bu, yeni firmware derlemesi veya fiziksel kart denemesi değildir.

Paket ve kılavuz boyut/SHA-256 değerleri yeniden üretildi. Yerel PC/Android gerçek ayrıştırma/servis kaynak hazırlama ve kılavuz/satır eşleşme testleri geçti. 1.0.1 bölümündeki kaynak değişmedi ifadesi önceki aday içindir; 1.0.2'de yorum metinleri değişir, çalıştırılan komutlar değişmez. GitHub 1.0.2 yayını yerelde yapılmadı.

Mevcut kullanıcı projeleri otomatik değiştirilmez. Yeni yorumlar yalnız güncel örnek `.ron` dosyası açıldığında veya katalogda 1.0.2 yayımlandıktan sonra yeni bağımsız kopyaya eklenir. Kullanıcının sonradan yazdığı koda otomatik açıklama üretilmez.
