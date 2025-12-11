# 📋 Clipboard Manager

Windows için Python ile geliştirilmiş, hafif ve arkaplanda çalışan pano (clipboard) geçmişi yöneticisi.

Standart Windows panosunun aksine, kopyaladığınız son 20 öğeyi hafızada tutar. `Ctrl + Space` kısayolu ile dilediğiniz zaman arayüzü çağırabilir ve geçmiş öğeleri tekrar kopyalayabilirsiniz.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Özellikler

* **Arkaplanda Çalışma:** Uygulama kapatıldığında (X) kapanmaz, kendini gizler ve sistem tepsisinde (tray) çalışmaya devam eder.
* **Global Kısayol:** `Ctrl + Space` kombinasyonu ile nerede olursanız olun pencereyi çağırabilirsiniz.
* **Otomatik Başlatma:** Windows başlangıcına (Registry) kendini otomatik ekler, her seferinde elle başlatmanız gerekmez.
* **Pano Geçmişi:** Son 20 metin kopyalamasını saklar.
* **Hızlı Kopyalama:** Listeden bir öğeye çift tıkladığınızda panoya kopyalar ve pencereyi gizler.

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak veya geliştirmek için:

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/suleymanibis0/clipboard-manager.git](https://github.com/suleymanibis0/clipboard-manager.git)
    cd clipboard-manager
    ```

2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı başlatın:**
    ```bash
    python main.py
    ```

## 📦 EXE Oluşturma (Build)

Uygulamayı bağımsız bir `.exe` dosyasına dönüştürmek için PyInstaller kullanılmıştır. Aşağıdaki komut ile build alabilirsiniz:

```bash
pyinstaller --onefile --noconsole --name="MyClipboard" --icon="app.ico" main.py
```
**Not: --noconsole parametresi arka plandaki terminal penceresini gizlemek içindir.**

## 🧩 Kullanılan Teknolojiler

* **Tkinter:** Grafik arayüz (GUI).

* **Pyperclip:** Pano işlemleri.

* **Keyboard:** Global kısayol dinleme (Global Hooks).

* **Winreg:** Windows başlangıç kaydı entegrasyonu.

**Developed by Süleyman İbiş**
