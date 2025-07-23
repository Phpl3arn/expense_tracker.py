# 💰 Python Komut Satırı Gider Takipçisi (CLI Expense Tracker)

Bu proje, Python'da geliştirilmiş basit bir komut satırı arayüzü (CLI) tabanlı gider takipçisi uygulamasıdır. Kullanıcıların giderlerini kolayca eklemesine, listelemesine ve toplam harcamalarını özetlemesine olanak tanır. Veriler `expenses.csv` adlı bir CSV dosyasına kaydedilir, bu sayede uygulama kapatılıp açılsa bile giderleriniz korunur.

## ✨ Özellikler

-   **Gider Ekleme:** Açıklama ve miktar belirterek yeni giderler ekleyin.
-   **Giderleri Listeleme:** Kaydedilmiş tüm giderleri ID, tarih, açıklama ve miktar bilgileriyle tablo halinde görüntüleyin.
-   **Toplam Özeti:** Tüm giderlerin toplam miktarını hesaplar ve gösterir.
-   **Gider Silme:** Belirtilen ID'ye sahip bir gideri silme yeteneği.
-   **Veri Kalıcılığı:** Giderler, basit ve okunabilir bir `expenses.csv` dosyasına kaydedilir.
-   **Kullanıcı Dostu Komut Satırı:** Basit komutlarla kolay etkileşim.

## 🚀 Nasıl Çalışır?

Uygulama, temel komutları kullanarak giderlerinizi yönetmenizi sağlar:

-   `add <açıklama> --amount <miktar>`: Yeni bir gider kaydı ekler.
    * Örnek: `add kahve --amount 15`
-   `list`: Kaydedilmiş tüm giderleri gösterir.
-   `summary`: Tüm giderlerin toplamını hesaplar.
-   `delete <ID>`: Belirtilen ID'ye sahip gideri siler.
    * Örnek: `delete 3`
-   `help`: Kullanılabilir komutların listesini gösterir.
-   `exit`: Uygulamadan çıkar.

## 💻 Kurulum ve Çalıştırma

Bu projeyi yerel bilgisayarınızda kurmak ve çalıştırmak oldukça basittir.

### Ön Koşullar

* Python 3.x yüklü olmalıdır. ([python.org](https://www.python.org/downloads/))

### Adımlar

1.  **Projeyi Klonlayın:**
    Terminalinizde veya komut istemcinizde aşağıdaki komutu kullanarak projeyi yerel bilgisayarınıza klonlayın:
    ```bash
    git clone [https://github.com/Phpl3arn/expense_tracker.py.git](https://github.com/Phpl3arn/expense_tracker.py.git)
    ```
    **Önemli Not:** Genellikle GitHub depo isimlerinde `.py` uzantısı kullanılmaz (örn: `expense-tracker-python`). Eğer deponuzu oluştururken `expense_tracker.py` olarak adlandırdıysanız bu komut doğrudur. Aksi takdirde, GitHub'daki gerçek depo adınıza göre klonlama URL'sini düzeltmeniz gerekebilir.

2.  **Proje Dizinine Girin:**
    ```bash
    cd expense_tracker.py
    ```
3.  **Uygulamayı Çalıştırın:**
    ```bash
    python expense_tracker.py
    ```

Artık gider takipçisi uygulamasını kullanmaya hazırsınız!

## 💡 Örnek Kullanım

İşte uygulamanın konsolda nasıl göründüğüne dair birkaç örnek:

```bash
💰 Komut Satırı Gider Takipçisine Hoş Geldiniz! 💰
Komutlar: add, list, summary, delete, help, exit
'expenses.csv' dosyası oluşturuldu.

Komut girin (örn: add öğle yemeği --amount 20): add kahve --amount 15
Gider başarıyla eklendi! [ID: 1]

Komut girin (örn: add öğle yemeği --amount 20): add akşam yemeği --amount 75.50
Gider başarıyla eklendi! [ID: 2]

Komut girin (örn: add öğle yemeği --amount 20): list

----------------------------------------------------
ID    Tarih        Açıklama                       Miktar (₺)
----------------------------------------------------
1     2025-07-24   kahve                            15.00
2     2025-07-24   akşam yemeği                     75.50
----------------------------------------------------

Komut girin (örn: add öğle yemeği --amount 20): summary

Toplam Gider: 90.50 ₺

Komut girin (örn: add öğle yemeği --amount 20): delete 1
Gider ID '1' başarıyla silindi.

Komut girin (örn: add öğle yemeği --amount 20): list

----------------------------------------------------
ID    Tarih        Açıklama                       Miktar (₺)
----------------------------------------------------
2     2025-07-24   akşam yemeği                     75.50
----------------------------------------------------

Komut girin (örn: add öğle yemeği --amount 20): exit
Uygulamadan çıkılıyor... Güle güle! 👋
