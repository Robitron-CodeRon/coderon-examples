# Kartın ışığını renk renk yak

Bu örnekte NEXTRON kartının üzerindeki küçük ışık, yani **LED**, sırayla **kırmızı, yeşil ve mavi** yanar. Sonra kısa bir süre söner ve aynı sıra yeniden başlar.

Kod yazmayı bilmen gerekmiyor. Örneği olduğu gibi projelerine ekleyip deneyebilirsin. Bu örnek motorları hareket ettiren bir komut içermez.

## Neye ihtiyacın var?

- Bir **NEXTRON kartı**.
- Kartı normal kullandığın güç kaynağı.
- CodeRon'un PC veya Android uygulaması.
- Yükleme yöntemine göre uygun USB veri kablosu veya hazır Bluetooth bağlantısı.

Kartın kendi ışığını kullanıyoruz. **Ek LED veya kablo bağlantısı yapmana gerek yok.**

## Nasıl çalıştırırım?

1. Bu sayfadaki **İndir** düğmesine dokun.
2. İndirme bitince **Projelerime ekle** düğmesine dokun. Örnek, sana ait ayrı bir proje olarak açılır.
3. Kartın **NEXTRON**, çalışma profilinin **NEXTRON OTA / Serbest kod** olduğunu kontrol et. Bu profil, kartın kablosuz yükleme özelliğini korur.
4. **Derle** düğmesine bas. Derleme, kodu kartın çalıştırabileceği dosyaya dönüştürür. Başarılı mesajını bekle.
5. Kartını normal kullandığın yöntemle bağla ve **Karta yükle** düğmesine bas.
6. Yükleme bitince kartı yeniden başlat. Kartın dört küçük anahtarının **tamamı ON konumunda olmasın**. Tamamı ON olursa normal örnek yerine bağlantı ve güncelleme modu açılır.
7. Başlangıç için yaklaşık **3–4 saniye bekle**. Ardından renk döngüsünü izle.

Örneği daha önce `.ron` dosyası olarak aldıysan, **.ron aç** ile açıp üçüncü adımdan devam edebilirsin.

## Ne görmeliyim?

**Kırmızı → Yeşil → Mavi → Işık kapalı → Yeniden kırmızı**

Her adım yaklaşık **0,75 saniye** sürer. Sayfadaki animasyon bu sırayı anlamana yardımcı olur. Animasyon, gerçek kartın görüntüsü veya canlı ölçümü değildir.

Bu örneğin kırmızı, yeşil ve mavi sırası NEXTRON kartında denenmiş ve çalıştığı bildirilmiştir.

## Kodu editörde nasıl okuyacağım?

Örneği **Projelerime ekle** ile açtığında, kodun her dolu satırında `//` işaretinden sonra Türkçe açıklama görürsün. `//` sonrasındaki yazılar kartın çalıştırdığı komutlar değildir; sana o satırın ne yaptığını anlatır. Editörde satır numaralarını izleyerek kodu baştan sona okuyabilirsin. Açıklama uzun olduğunda satırın devamına bak.

Örneğin `nextronStop(); // Motorları durdurur.` satırında soldaki komut çalışır, sağındaki yazı açıklamadır. Örnek sayfasındaki **Kodu satır satır öğren** bölümünde de kod ve açıklama ayrı sütunlarda gösterilir. Kendi yeni yazdığın satırlara otomatik açıklama eklenmez.

## Hızı veya parlaklığı değiştirebilir miyim?

Evet. Projedeki `NextronLed.ino` dosyasını aç. Başlangıçta şu iki satırı göreceksin:

```cpp
constexpr uint32_t COLOR_INTERVAL_MS = 750;
constexpr uint8_t LED_LEVEL = 32;
```

- **Renk değiştirme hızı:** `750` değerini `1500` yaparsan her renk 1,5 saniye görünür; ışık daha yavaş değişir. `500` yaparsan her renk yarım saniye görünür.
- **Parlaklık:** `32` değerini artırırsan ışık daha parlak, azaltırsan daha loş olur. İzin verilen aralık **0–255**; `0` ışığı kapatır.

Değişiklikten sonra yeniden **Derle** ve **Karta yükle** adımlarını uygula. Buradaki animasyon, sen kodu değiştirdiğinde otomatik değişmez; paylaşılan örneğin ilk halini gösterir.

## Işık beklediğim gibi yanmıyorsa

- Yalnız indirmek yetmez; projeyi derleyip **karta yüklediğinden** emin ol.
- Dört anahtarın tamamının ON olmadığını kontrol et ve kartı yeniden başlat.
- Kart seçiminin NEXTRON, profilin NEXTRON OTA / Serbest kod olduğunu kontrol et.
- Ekranda hata varsa hata mesajını kaydet; yardım isterken hangi adımda çıktığını belirt.

## Bu örneği kullanabilir miyim?

Evet. Örnek **MIT lisansıyla** paylaşılır. Kullanabilir, değiştirebilir ve paylaşabilirsin. Paylaştığın kopyalarda telif ve lisans bildirimini koru. Projedeki `LICENSE.txt` dosyası bu bildirimi içerir.
