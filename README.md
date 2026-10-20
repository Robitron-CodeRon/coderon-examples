# CodeRon örnek projeleri

Kartına ne yaptırabileceğini örneklerle öğren. Hazır projeyi aç, kodunu incele, küçük değişiklikler yap ve kendi kartında dene. Yeni başladıysan **Başlangıç** seviyesindeki örneklerden başlayabilirsin.

## Uygulamada nasıl açarım?

1. PC veya Android CodeRon'da **Örnek Projeler** ekranını aç.
2. **Yenile** ile yayımlanan örnekleri getir ve bir örneği seç.
3. Hangi kartın ve parçaların gerektiğini oku. Her örnek bütün kartlara uygun değildir.
4. Örneği indir ve **Projelerime ekle** ile kendi kopyanı oluştur.
5. Kartı ve profili kontrol et. Sonra **Derle** ve **Karta yükle** adımlarını kendin başlat.

PC **1.35.0** / Android **1.25** ve sonraki sürümlerde indirdiğin örnekte **Projeyi aç**, yeni sürüm gelirse **Güncelle** düğmesi görünür. Güncelleme yeni bir proje kopyası oluşturur; kendi düzenlediğin eski proje korunur. **Kayıtlı örneği sil** ile indirme kaydını kaldırabilirsin. Yerel proje kopyasını da silmek istersen silme ekranında ayrıca seçmelisin.

Örneği açmak kartına kendiliğinden komut göndermez. Önceden indirilmiş içerik çevrimdışı kullanılabilir; karta yükleme için normal bağlantı koşulları gerekir. Örnekleri okumak ve yerelde çalışmak için CodeRon veya GitHub hesabı gerekmez.

## İlk örnek: NEXTRON'un ışığını renk renk yak

[NEXTRON LED örneğinin anlatımını oku](examples/nextron-led-cycle/README.md).

Kartın kendi ışığı kırmızı, yeşil, mavi yanar; kısa süre söner ve tekrar başlar. Harici LED veya ek kablo gerekmez. Kaynakta `//` işaretinden sonraki Türkçe yorumlar satırların ne yaptığını anlatır. Kullanıcı kırmızı, yeşil ve mavi sırasını gerçek NEXTRON kartında gördüğünü bildirdi; ayrıntılar ve doğrulanmamış kısımlar [test kaydında](examples/nextron-led-cycle/verification.md).

Yeni CodeRon sürümleri örneği kart görselindeki LED gösterimi ve satır açıklamalarıyla anlatır. Bu gösterim bağlı kartın canlı görüntüsü değildir; kodu değiştirdiğinde otomatik değişmez. Gereken uygulama sürümü örneğin ayrıntısında belirtilir.

## Kart ve lisans bilgisi

Örnekler farklı kartlar için hazırlanabilir. Belirtilen kartı, profilini ve bağlantıları kullan; bilinmeyen pinleri tahmin etme. NEXTRON LED örneğinin lisansı [MIT](examples/nextron-led-cycle/LICENSE)'dir. Bu izin yalnız o örnek ve beraberindeki metinler içindir. Başka örneklerin lisanslarını ayrıca kontrol et; CodeRon uygulaması ve firmware'i için genel bir lisans verilmez.

<details>
<summary>Örnek hazırlamak ve katkı vermek isteyenler için</summary>

[Katkı yönergeleri](CONTRIBUTING.md) ve [katalog sözleşmesi](docs/catalog-contract.md), örnek ekleme biçimini açıklar. `catalog.json` uygulamanın okuduğu listedir; `catalog.schema.json` metadata şemasıdır. Gerçek `.ron` paketi, kullanım açıklaması, lisans ve doğrulama kaydı birlikte hazırlanmalıdır.

Python 3.12 ile:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/validate_catalog.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/validate_presentation.py
.venv/bin/python tools/test_presentation.py
```

Windows'ta `.venv/bin/python` yerine `.venv\Scripts\python` kullanılır. Bu kontroller kaynak kodu derlemez veya karta yüklemez. Test edilmemiş donanım desteğini doğrulanmış gibi yazma.

</details>
