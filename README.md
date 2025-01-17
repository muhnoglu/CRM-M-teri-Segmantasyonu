
![images](https://github.com/user-attachments/assets/3c5d3966-e256-4a90-a80d-5b5cd75ec0a0)

# CRM Müşteri Segmentasyonu Projesi

Bu proje, CRM (Customer Relationship Management) sisteminde yer alan müşteri verilerinin segmentasyonunu yapmak amacıyla oluşturulmuştur. Proje kapsamında MSSQL veri tabanındaki **CRM_System** veritabanını Docker kullanarak bir konteynırda çalıştırdım ve Python ortamında bu veritabanına bağlandım. SQL sorguları ve veri görselleştirme yöntemlerini kullanarak anlamlı içgörüler elde ettim.

## Proje Adımları

### 1. Veri Tabanının Docker'da Çalıştırılması
- MSSQL veritabanını bir Docker konteynırında çalıştırdım.
- `docker-compose` kullanarak veri tabanını hızlıca kurdum ve erişilebilir hale getirdim.

### 2. Python Ortamına Bağlantı
- Python'da `pyodbc` kütüphanesini kullanarak Docker konteynırındaki MSSQL veri tabanına bağlantı sağladım.
- SQL sorgularını Python üzerinden çalıştırarak gerekli verileri çektim.

### 3. Verilerin Analizi ve Görselleştirilmesi
- Verileri Pandas ile işledim ve temizledim.
- Müşteri segmentasyonu için SQL ve Python kullanarak analizler yaptım.
- Elde edilen sonuçları Matplotlib ve Seaborn kullanarak görselleştirdim.

### 4. Python Image'ının Oluşturulması
- Proje için özel bir Python image'ı oluşturdum ve tüm gerekli kütüphaneleri bu image'a dahil ettim.
- Image Docker Hub'a yüklenebilir şekilde yapılandırıldı.

## Kullanılan Teknolojiler ve Araçlar
- **MSSQL**: Veri tabanı yönetimi.
- **Docker**: Veri tabanını konteynırda çalıştırmak için.
- **Python**: Veri analizi ve görselleştirme.
  - `pyodbc`, `pandas`, `matplotlib`, `seaborn` kütüphaneleri.
- **Docker Compose**: Çok konteynırlı ortam kurulumları için.

## Projeyi Çalıştırma

### Gereksinimler
- Docker ve Docker Compose yüklü olmalıdır.
- Python 3.9 veya daha yeni bir sürüm yüklü olmalıdır.
- MSSQL (SSMS)
