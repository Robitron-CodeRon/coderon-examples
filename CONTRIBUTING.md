# Örnek ekleme

1. Paylaşmaya yetkili olduğunuz kod, belge ve görselleri kullanın. Üçüncü taraf lisanslarını ve yeniden dağıtım koşullarını kontrol edin. Depo lisansı henüz seçilmemiştir; içerik yayımlamadan önce lisans kararını sahipleriyle netleştirin.
2. Kalıcı, benzersiz kimlik seçin. `examples/<id>/` oluşturun; `templates/PROJECT_README.tr.md` dosyasını açıklama olarak kopyalayın. Kaynakları `src/`, görselleri isteğe bağlı `assets/`, gerçek paketi `dist/` altında tutun. Kart başına klasör gerekmez.
3. Amacı, malzemeleri, doğrulanmış bağlantıları, kurulumu, kullanımı, sonucu ve sınırları doldurun. Yapılmayan derleme/donanım testlerini açıkça yazın; pin veya firmware API'si tahmin etmeyin. Genel kod için donanım bölümlerine gerekçeli “uygulanamaz” yazılabilir.
4. Gerçek paket ve biçim yerel CodeRon geliştirme oturumundan gelmelidir. `.ron` dosyası uydurmayın; şablonları kataloğa eklemeyin. Gerçek paket gelene kadar katalog boş kalabilir.
5. `docs/catalog-contract.md` ve JSON şemasına göre katalog kaydı ekleyin. Boyutu bayt olarak, SHA-256 özetini gerçek paket üzerinden hesaplayın (`python` hashlib veya `sha256sum`). Kart uyumluluğu ve CodeRon derleme/yükleme kanıtlarını ayrı kaydedin. Test kanıtları gizli bilgi içermemelidir.
6. README'deki doğrulayıcı ve test komutlarını çalıştırın. Katalog kontrolü derleme veya donanım testi yerine geçmez. Gerçek testleri yalnız uygun araçlar/donanım ve açık kullanıcı eylemiyle yapın; otomatik karta yükleme eklemeyin.
7. PR'de değişen örnek kimliği/sürümü, lisanslar, çalıştırılan testler ve yapılmayan kontrolleri yazın. Yayımlanmış aynı sürümü yerinde değiştirmeyin.

Token, parola, imzalama anahtarı, kullanıcı projeleri veya CodeRon uygulama kaynaklarını bu herkese açık depoya eklemeyin. CI yalnız katalog metadatasını ve dosya bütünlüğünü denetler.
