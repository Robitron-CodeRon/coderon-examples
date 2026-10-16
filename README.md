# CodeRon örnek proje kütüphanesi

Bu depo, CodeRon içinde listelenmesi planlanan örneklerin açıklamalarını, kaynaklarını ve indirilebilir paketlerini GitHub üzerinden yönetmek içindir. CodeRon PC/Android uygulama kaynaklarını içermez; uygulama entegrasyonu henüz yapılmamıştır. İlk katalog boştur.

Hedef akışta kullanıcı GitHub hesabı olmadan açıklamaları okuyabilmeli ve yayımlanmış paketleri indirebilmelidir. “Projelerime ekle”, kullanıcının proje alanında bağımsız ve düzenlenebilir bir kopya oluşturmalıdır. Sonraki katalog güncellemeleri bu kopyayı ezmemelidir. Bu davranışın uygulamada geliştirilmesi ve anonim erişimin gerçek dağıtım adresleriyle sınanması gerekir.

Genel Arduino/C++ kod örnekleri belirli donanım gerektirmeyebilir. Donanım projeleri ise gerekli parçaları, doğrulanmış bağlantıları ve sınırları açıklamalıdır. NEXTRON, SPEEDRON ve diğer kartlar aynı katalog modelinde yer alabilir; bir örnek birden fazla kartla uyumlu olabilir. Donanım uyumluluğu, CodeRon’un ilgili platformda o karta derleme/yükleme desteğini kanıtlamaz. Doğrulanmamış destek açıkça işaretlenir.

## Düzen

- `catalog.json`: sürümlü, şu anda boş örnek listesi.
- `catalog.schema.json`: JSON Schema 2020-12 taslağı.
- `examples/<id>/`: her örneğin açıklaması, kaynakları, varsa görselleri ve gerçek paketi.
- `templates/PROJECT_README.tr.md`: boş proje açıklama şablonu; indirilebilir örnek değildir.
- `docs/catalog-contract.md`: uygulamayla görüşülecek katalog sözleşmesi.
- `CONTRIBUTING.md`: örnek ekleme ve doğrulama adımları.
- `tools/validate_catalog.py`, `tests/`: katalog doğrulaması ve testleri.

## Yerel doğrulama

Python 3.12 ile:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/validate_catalog.py
.venv/bin/python -m unittest discover -s tests -v
```

Doğrulayıcı yalnız katalog ve dosya bütünlüğünü denetler; proje kodunu çalıştırmaz, paket açmaz, derlemez veya karta yüklemez. `.ron` biçimi gerçek uygulama geliştirme oturumundan sağlanacaktır; bu depo biçim tanımlamaz.

## Lisans

Henüz depo lisansı seçilmedi. Her gerçek örneğin kodu, görselleri ve bağımlılıklarının paylaşım/dağıtım hakları ayrıca doğrulanmalıdır. Lisans kararı verilene kadar içerikleri yeniden kullanma izni varsaymayın.
