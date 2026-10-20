# Katalog sözleşmesi — öneri v1

Bu sözleşme CodeRon PC/Android uygulama tarafıyla henüz kesinleştirilmemiştir. `catalog.schema.json` makine tarafından denetlenebilir taslaktır; bu belge anlamsal kuralları tamamlar. Boş `examples` geçerlidir. Şablonlar örnek değildir.

## Alanlar

Aşağıda “isteğe bağlı” denmeyen alanlar zorunludur. Nesnelerde bilinmeyen alanlar bu sürümün yayın doğrulayıcısında reddedilir; diziler aksi belirtilmedikçe boş olabilir. Metinler boş olamaz.

| Alan | Tür ve anlam |
| --- | --- |
| `schemaVersion` | Tamsayı, şu anda yalnız `1`. |
| `examples` | Örnek nesneleri dizisi. |
| `id` | Kalıcı, katalog genelinde benzersiz küçük ASCII kimliği; harf/rakam, nokta ve tire. |
| `title`, `summary`, `topic` | Başlık, kısa açıklama, konu; metin. |
| `tags` | Benzersiz metin dizisi. |
| `difficulty` | `beginner`, `intermediate`, `advanced`. |
| `version` | `MAJOR.MINOR.PATCH`; negatif olmayan tamsayılar, ön ek/sonek yok. |
| `language` | BCP 47 dil etiketi önerilir (`tr`, `en`); taslak yalnız boş olmayan metni denetler. |
| `kind` | `general` veya `hardware`; genel kod ile donanım projesini ayırır. |
| `compatibleBoards` | `{id, name, status, notes}` dizisi. `status`: `unverified`, `verified`, `incompatible`. Kimlikler örnek içinde benzersizdir. Boş dizi “tüm kartlar” anlamına gelmez. `verified` iddiasının yöntemi ve sonucu açıklama dosyasında belgelenmelidir. |
| `hardware` | `{name, quantity, notes}` dizisi; miktar pozitif tamsayı. Genel örneklerde boş olabilir. Bağlantı/pin bilgisi yalnız doğrulanmışsa açıklamada verilir. |
| `libraries` | `{name, versionRange, sourceUrl?}` dizisi; `sourceUrl` isteğe bağlı URI. Boş dizi ek kütüphane bildirilmediğini gösterir. |
| `coderon.requirements` | `{platform, versionRange}` dizisi; platform `pc` veya `android`. Boşsa gereksinimler henüz bildirilmemiştir. |
| `coderon.support` | `{boardId, platform, coderonVersionRange, compile, upload}` dizisi. Kart aynı örneğin kart listesinde, platform gereksinim listesinde bulunmalıdır. Kart/platform/sürüm aralığı üçlüsü benzersizdir. Boşsa destek doğrulanmamıştır. |
| `descriptionPath` | Açıklama dosyasına depo köküne göreli yol. |
| `imagePaths` | Görsellere göreli yollar; boş olabilir. |
| `package` | `{path, format, sizeBytes, sha256}`. Yol gerçek dosyaya, biçim yayımlanan gerçek biçime karşılık gelir. Boyut pozitif tamsayı bayt; özet 64 küçük onaltılık karakter. `.ron` iç yapısı bu sözleşmede tanımlanmaz. |
| `license` | `{status, identifier?, path?}`. Durum `undecided` veya `declared`; beyan edilmişse identifier zorunlu (SPDX tanımlayıcısı önerilir). İsteğe bağlı path lisans dosyasına gider. `undecided` yeniden dağıtım izni değildir. |
| `validation` | `{build, hardware}`; ikisi de aşağıdaki kontrol nesnesidir. |

Kontrol nesnesi: `{status, details, evidencePath?}`. Durum `unverified`, `passed`, `failed` veya `not-applicable`; `details` koşulları, kullanılan araç/sürüm/kartı ve sınırları açıklar. `passed`/`failed` için gerçek test kaydına `evidencePath` zorunludur. Kanıt dosyasının varlığı testin doğru olduğunu otomatik kanıtlamaz. Hiç yapılmayan test `unverified` olur; `not-applicable` gerekçelendirilir. Kart uyumluluğu, proje derlemesi, gerçek donanım testi, CodeRon derlemesi ve CodeRon yüklemesi ayrı iddialardır.

`versionRange` ve `coderonVersionRange` bu aşamada yalnız insan tarafından okunur metindir. Aralık grameri, sürüm karşılaştırması ve kart kimlik kaydı uygulama ekibiyle kararlaştırılmalıdır. Uygulama bu metinlerden otomatik destek sonucu çıkarmamalıdır.

## Yollar ve indirme

Tüm dosya yolları **depo köküne** görelidir; katalog dosyasının veya örnek klasörünün konumuna göre değildir. POSIX `/` kullanılır. Mutlak yollar, boş bileşenler, `.`/`..`, ters eğik çizgi, URI/Windows sürücü sözdizimi, yüzde kodlaması, sorgu ve fragment reddedilir. Sembolik bağlantının çözülen hedefi de depo içinde gerçek dosya olmalıdır. Doğrulayıcı dış URL indirmez veya paket açmaz.

İstemci katalog ve dosyaları aynı değişmez Git commit'i/release içeriğinden almalıdır; hareketli `main` üzerinden ayrı zamanlarda almak tutarsız paket üretebilir. Temel GitHub içerik/dağıtım adresi istemci yapılandırmasıdır; katalogda sahte URL yoktur. Anonim indirme, CORS, hız limitleri ve PC/Android erişimi gerçek yayımdan sonra sınanmalıdır. SHA-256 bütünlük sağlar; tek başına yayıncı kimliğini doğrulamaz.

İndirme boyutu ve SHA-256 doğrulandıktan sonra içe aktarma yapılmalıdır. Paket açılırsa uygulama ayrıca arşiv içi traversal, sembolik bağlantı, boyut limitleri ve hedef çakışmalarını denetlemelidir; bu depo `.ron` ayrıştırıcısı sağlamaz.

## İstemci davranışı ve sürümleme

- Desteklenmeyen `schemaVersion`: kataloğu kullanma; anlaşılır hata ve varsa son doğrulanmış önbelleği göster.
- Eksik zorunlu alan, hatalı tür, güvensiz yol veya bütünlük uyuşmazlığı: etkilenen örneği içe aktarma; açıklanabilir hata göster. Yayın doğrulayıcısı kataloğun tamamını başarısız sayar.
- Eksik isteğe bağlı alanı varsayılan destek/izin olarak yorumlama. Bilinmeyen durum veya platformda güvenli biçimde destek “bilinmiyor” kabul edilir; otomatik derleme/yükleme başlatılmaz. İstemci bilinmeyen isteğe bağlı alanları yok sayabilir; yayıncı v1 şemasına uymalıdır.
- `id` başlık, kart veya klasör değişince değişmez; silinen kimlik başka projeye atanmaz. Esaslı farklı örneğe yeni kimlik verilir.
- Aynı kimlik ve sürümün yayımlanan içeriği değişmez. Paket, açıklama, görsel, destek veya lisans metadatası değişince örnek sürümünü artır. Geriye uyumsuz değişiklikte major, özellikte minor, düzeltmede patch önerilir.
- Sözleşmede uyumsuz alan/tür değişikliği yeni `schemaVersion` gerektirir. Katalog format sürümü örnek sürümünden bağımsızdır.
- “Projelerime ekle” yeni yerel proje kimliğiyle bağımsız kopya oluşturur; katalog klasörünü yerinde düzenletmez. Kaynak örnek kimliği, sürümü, commit ve paket özeti izleme için saklanabilir. Güncellemeler kullanıcının dosyalarını otomatik ezmez. Birleştirme/güncelleme UX'i uygulama tarafında kararlaştırılacaktır.

## Açık kararlar

`.ron` biçimi ve paket üreticisi; desteklenen gerçek kart kimlikleri; PC/Android minimum sürümleri ve doğrulama matrisi; sürüm aralığı grameri; dağıtım/önbellek politikası; katalog güven modeli; depo/örnek/görsel lisansları uygulama geliştirme oturumunda kesinleştirilmelidir. Bu taslak hiçbir kart API'si, pin bağlantısı veya doğrulanmış destek ilan etmez.

## İsteğe bağlı eğitim sunumu — 20 Ekim 2026

`preview`: `type=led-sequence`, `board=NEXTRON|GENERIC`, isteğe bağlı caption (en fazla 240 karakter), 2–16 steps. Her adım label (1–40 karakter), color (#RRGGBB), durationMs (200–10000 tam sayı) içerir; döngü toplamı en fazla 60000 ms. Bu yalnız görsel anlatımdır; donanım komutu değildir. Diğer kartların konumu tahmin edilmez, GENERIC soyut ışık gösterir.

`codeGuide`: güvenli depo yolu path, 1–128000 sizeBytes ve SHA-256 sha256. JSON şema sürümü 1; file ana `.ino` adı, source tam UTF-8 metin, sourceSha256 kaynak özeti, projectSha256 paket özeti, explanations her fiziksel satır için bir metindir. Her dolu satırın açıklaması gerekir; boş satırınki boş olabilir. 1000 satır ve açıklama başına 1000 karakter üst sınırı vardır. source paket files[file] ile birebir aynı olmalıdır. Kullanıcının değiştirdiği kod için otomatik açıklama anlamına gelmez. İstemci tüm metni kaçışlayarak gösterir; HTML/kod çalıştırmaz.

Alanlar isteğe bağlıdır; mevcut örnekler değişmeden geçerlidir. Yayın şeması ve `tools/validate_presentation.py` birlikte doğrular. `python tools/test_presentation.py` regresyonları çalıştırır. Yerel aday `--entry examples/nextron-led-cycle/catalog-entry.pending.json` ile canlı katalog değiştirilmeden denetlenebilir.
