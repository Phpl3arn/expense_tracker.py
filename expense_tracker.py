import csv
import os
from datetime import datetime

# Veri dosyasının adı
DATA_FILE = 'expenses.csv'
HEADERS = ['ID', 'Date', 'Description', 'Amount']

def initialize_data_file():
    """Veri dosyası yoksa oluşturur ve başlıkları yazar."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        print(f"'{DATA_FILE}' dosyası oluşturuldu.")

def get_next_id():
    """Giderler için bir sonraki uygun ID'yi döndürür."""
    if not os.path.exists(DATA_FILE):
        return 1 # Dosya yoksa ilk ID 1
    
    with open(DATA_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # Başlık satırını atla
        max_id = 0
        for row in reader:
            try:
                max_id = max(max_id, int(row[0])) # ID sütunu genellikle ilk sütundur (index 0)
            except (ValueError, IndexError):
                # Bozuk satırları veya ID olmayan satırları atla
                continue
        return max_id + 1

def add_expense(description, amount):
    """Yeni bir gider kaydı ekler."""
    if not isinstance(description, str) or not description.strip():
        return "Hata: Açıklama boş olamaz."
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Hata: Miktar pozitif bir sayı olmalıdır."

    expense_id = get_next_id()
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, current_date, description, amount])
    return f"Gider başarıyla eklendi! [ID: {expense_id}]"

def list_expenses():
    """Tüm giderleri listeler."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        return "Henüz hiç gider kaydı yok."

    expenses = []
    with open(DATA_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    
    if not expenses:
        return "Henüz hiç gider kaydı yok."
        
    print("\n----------------------------------------------------")
    print(f"{'ID':<5} {'Tarih':<12} {'Açıklama':<30} {'Miktar (₺)':>10}")
    print("----------------------------------------------------")
    for expense in expenses:
        try:
            print(f"{expense['ID']:<5} {expense['Date']:<12} {expense['Description']:<30} {float(expense['Amount']):>10.2f}")
        except KeyError:
            print(f"Uyarı: Bozuk satır tespit edildi: {expense}") # Eksik sütunları yakala
            continue
    print("----------------------------------------------------")
    return None # Liste başarılı olursa None döndürür

def summarize_expenses():
    """Toplam gider miktarını hesaplar ve gösterir."""
    if not os.os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        return "Henüz hiç gider kaydı yok."

    total_amount = 0.0
    with open(DATA_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                total_amount += float(row['Amount'])
            except (ValueError, KeyError):
                continue # Geçersiz miktar veya eksik sütunu atla
    
    return f"\nToplam Gider: {total_amount:.2f} ₺"

def delete_expense(expense_id):
    """Belirtilen ID'ye sahip gideri siler."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        return "Silinecek gider bulunamadı, dosya boş veya mevcut değil."

    expenses = []
    found = False
    with open(DATA_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == str(expense_id):
                found = True
            else:
                expenses.append(row)
    
    if not found:
        return f"Hata: ID '{expense_id}' bulunamadı."
        
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(expenses)
        
    return f"Gider ID '{expense_id}' başarıyla silindi."

def main():
    initialize_data_file() # Uygulama başladığında veri dosyasını kontrol et

    print("💰 Komut Satırı Gider Takipçisine Hoş Geldiniz! 💰")
    print("Komutlar: add, list, summary, delete, help, exit")

    while True:
        command_line = input("\nKomut girin (örn: add öğle yemeği --amount 20): ").strip()
        parts = command_line.split(' ', 1) # İlk boşluğa göre ayır
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ''

        if command == 'add':
            desc_parts = args.split('--amount', 1)
            if len(desc_parts) < 2:
                print("Hata: 'add' komutu için 'açıklama --amount miktar' formatını kullanın.")
                continue
            
            description = desc_parts[0].strip()
            amount_str = desc_parts[1].strip()
            try:
                amount = float(amount_str)
                result = add_expense(description, amount)
                print(result)
            except ValueError:
                print("Hata: Geçersiz miktar formatı. Lütfen bir sayı girin.")
            
        elif command == 'list':
            result = list_expenses()
            if result: # Eğer liste boşsa veya hata mesajı varsa
                print(result)
        
        elif command == 'summary':
            result = summarize_expenses()
            print(result)
            
        elif command == 'delete':
            try:
                expense_id = int(args.strip())
                result = delete_expense(expense_id)
                print(result)
            except ValueError:
                print("Hata: 'delete' komutu için geçerli bir ID girin (örn: delete 5).")
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")

        elif command == 'help':
            print("\nDesteklenen Komutlar:")
            print("  add <açıklama> --amount <miktar>  - Yeni bir gider ekler. (örn: add yemek --amount 35.50)")
            print("  list                             - Tüm giderleri listeler.")
            print("  summary                          - Tüm giderlerin toplamını gösterir.")
            print("  delete <ID>                      - Belirtilen ID'ye sahip gideri siler. (örn: delete 3)")
            print("  exit                             - Uygulamadan çıkar.")
            print("  help                             - Komut rehberini gösterir.")

        elif command == 'exit':
            print("Uygulamadan çıkılıyor... Güle güle! 👋")
            break
        else:
            print("❗ Geçersiz komut. 'help' yazarak komutları görebilirsiniz.")

if __name__ == "__main__":
    main()
