import tkinter as tk
from tkinter import ttk,messagebox

class GorevTakipUygulaması:
    # Constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Görev Takip Uygulaması")

        # Label'lar
        self.gorev_adi_label = tk.Label(root, text="Görev Adı :",font="Coolvetica 16 bold")
        self.gorev_adi_label.place(x=10,y=300)

        self.gorev_icerigi_label = tk.Label(root, text="Görev İçeriği :",font="Coolvetica 16 bold")
        self.gorev_icerigi_label.place(x=10,y=340)

        self.gorev_saati_label = tk.Label(root, text="Görev Saati :",font="Coolvetica 16 bold")
        self.gorev_saati_label.place(x=10,y=380)

        self.gorev_dakikasi_label = tk.Label(root, text="Görev Dakikası :",font="Coolvetica 16 bold")
        self.gorev_dakikasi_label.place(x=10,y=420)

        self.GorevListesi_label = tk.Label(root, text="Görevler",font="Coolvetica 27 ",fg="red")
        self.GorevListesi_label.place(x=775,y=15)

        self.TamamlandıListe_label = tk.Label(root, text="Tamamlandı",font="Coolvetica 27 ",fg="red")
        self.TamamlandıListe_label.place(x=750,y=415)

        # Entry'ler
        self.gorev_adi_entry = tk.Entry(root,font="Coolvetica 14 bold")
        self.gorev_adi_entry.place(x=160,y=302)

        self.gorev_icerigi_entry = tk.Entry(root,font="Coolvetica 14 bold")
        self.gorev_icerigi_entry.place(x=160,y=342)

        self.gorev_saati_entry = tk.Entry(root,font="Coolvetica 14 bold")
        self.gorev_saati_entry.place(x=160,y=382)

        self.gorev_dakikasi_entry = tk.Entry(root,font="Coolvetica 14 bold")
        self.gorev_dakikasi_entry.place(x=160,y=422)


        # Butonlar
        self.bilgilendirme_button = tk.Button(root, text="Bilgi",font="Coolvetica 14 bold",fg='blue', command=self.bilgilendirme)
        self.bilgilendirme_button.place(x=10,y=10)

        self.gorev_ekle_button = tk.Button(root, text="Görev Ekle",font="Coolvetica 14 bold",width=17, command=self.gorevEkle)
        self.gorev_ekle_button.place(x=160,y=470)

        self.gorev_sil_button = tk.Button(root, text="Görev Sil",font="Coolvetica 14 bold",width=11, command=self.gorevSil)
        self.gorev_sil_button.place(x=428,y=80)  

        self.gorev_tamamla_button = tk.Button(root, text="Görev Tamamla",font="Coolvetica 14 bold", command=self.gorevTamamla)
        self.gorev_tamamla_button.place(x=430,y=150) 

        self.asagi_ok_button = tk.Button(root, text="↓",font="Coolvetica 24 bold", command=self.gorevTamamla)
        self.asagi_ok_button.place(x=760,y=320)  

        self.gorev_duzenle_button = tk.Button(root, text="Görev Düzenle",font="Coolvetica 14 bold", command=self.gorevDuzenle)
        self.gorev_duzenle_button.place(x=433,y=220)

        self.geri_dondur_button = tk.Button(root, text="Geri Döndür",font="Coolvetica 14 bold",width=10, command=self.geriDondur)
        self.geri_dondur_button.place(x=439,y=490) 

        self.yukari_ok_button = tk.Button(root, text="↑",font="Coolvetica 24 bold", command=self.geriDondur)
        self.yukari_ok_button.place(x=840,y=320)

        self.tamamlanan_gorev_sil_button = tk.Button(root, text="Görev Sil",font="Coolvetica 14 bold",width=10, command=self.tamamlandiSil)
        self.tamamlanan_gorev_sil_button.place(x=439,y=560) 

        self.cikis_button = tk.Button(root, text="Çıkış",font="Coolvetica 18 bold",fg="red", command=self.cıkıs)
        self.cikis_button.place(x=10,y=680)

        # Treeview'ler
        self.gorev_listesi_treeview = ttk.Treeview(root, columns=("Görev Adı", "Görev İçeriği", "Görev Saati", "Görev Dakikası"), show="headings")
        self.gorev_listesi_treeview.heading("Görev Adı", text="Görev Adı")
        self.gorev_listesi_treeview.heading("Görev İçeriği", text="Görev İçeriği")
        self.gorev_listesi_treeview.heading("Görev Saati", text="Saat")
        self.gorev_listesi_treeview.heading("Görev Dakikası", text="Dakika")

        # Sütunların genişlik ayarı      
        self.gorev_listesi_treeview.column("Görev Adı",width=100)
        self.gorev_listesi_treeview.column("Görev İçeriği",width=300)
        self.gorev_listesi_treeview.column("Görev Saati",width=45)
        self.gorev_listesi_treeview.column("Görev Dakikası",width=45)

        self.gorev_listesi_treeview.place(x=580,y=50)
        

        self.tamamlanan_gorevler_treeview = ttk.Treeview(root, columns=("Görev Adı", "Görev İçeriği", "Görev Saati", "Görev Dakikası"), show="headings")
        self.tamamlanan_gorevler_treeview.heading("Görev Adı", text="Görev Adı")
        self.tamamlanan_gorevler_treeview.heading("Görev İçeriği", text="Görev İçeriği")
        self.tamamlanan_gorevler_treeview.heading("Görev Saati", text="Saat")
        self.tamamlanan_gorevler_treeview.heading("Görev Dakikası", text="Dakika")

        # Sütunların genişlik ayarı
        self.tamamlanan_gorevler_treeview.column("Görev Adı",width=100)
        self.tamamlanan_gorevler_treeview.column("Görev İçeriği",width=300)
        self.tamamlanan_gorevler_treeview.column("Görev Saati",width=45)
        self.tamamlanan_gorevler_treeview.column("Görev Dakikası",width=45)

        self.tamamlanan_gorevler_treeview.place(x=580,y=450)

        # Başlangıçta treeview'leri güncelle
        self.listeleriYenile()




    def gorevEkle(self):
        try:
            gorev_adi = self.gorev_adi_entry.get()
            gorev_icerigi = self.gorev_icerigi_entry.get()
            gorev_saati = self.gorev_saati_entry.get()
            gorev_dakikasi = self.gorev_dakikasi_entry.get()

            # Giriş alanlarının boş olup olmadığını kontrol et
            if not gorev_adi or not gorev_icerigi or not gorev_saati or not gorev_dakikasi:
                raise ValueError("Tüm alanları doldurunuz.")

            # Saat ve dakika değerlerine sayı dışında bir şey girilip girilmediğini kontrol et
            try:
                saat = int(gorev_saati)
                dakika = int(gorev_dakikasi)
            except ValueError:
                raise ValueError("Saat ve dakika değeri sayı olmalıdır.")

            # Saat ve dakika sınırlarını kontrol et
            if not (0 <= saat <= 23) or not (0 <= dakika <= 59):
                raise ValueError("Saat 0-23 arasında, dakika 0-59 arasında olmalıdır.")

            # Saat ve dakika değeri 10'dan küçükse başlarına 0 ekleyerek düzelt
            if saat < 10:
                gorev_saati = "0" + gorev_saati
            if dakika < 10:
                gorev_dakikasi = "0" + gorev_dakikasi


            # Doğrulama sorusu
            soru = f"Görev eklemek istiyor musunuz?\n\nGörev Adı: {gorev_adi}\nGörev İçeriği: {gorev_icerigi}\nGörev Saati: {gorev_saati}\nGörev Dakikası: {gorev_dakikasi}"
            cevap = messagebox.askyesno("Doğrulama", soru)

            if cevap:
                yeni_gorev = f"{gorev_adi},{gorev_icerigi},{gorev_saati},{gorev_dakikasi}\n"

                with open("PROJE/GörevListesi.txt", "a") as dosya:
                    dosya.write(yeni_gorev)

                # Treeview'leri güncelle
                self.listeleriYenile()

            # Entry'leri temizle
            self.gorev_adi_entry.delete(0, tk.END)
            self.gorev_icerigi_entry.delete(0, tk.END)
            self.gorev_saati_entry.delete(0, tk.END)
            self.gorev_dakikasi_entry.delete(0, tk.END)

        # Uyarıları yakala
        except ValueError as e:
            messagebox.showwarning("Hata", str(e))




    # Görev silme fonksiyonu          
    def gorevSil(self):
        try:
            secilen_item = self.gorev_listesi_treeview.selection()

            if not secilen_item:
                raise ValueError("Silinecek bir görev seçiniz.")

            secilen_gorev = self.gorev_listesi_treeview.item(secilen_item, "values")

            # Doğrulama sorusu
            soru = f"Görevi silmek istediğinize emin misiniz?\n\nGörev Adı: {secilen_gorev[0]}\nGörev İçeriği: {secilen_gorev[1]}\nGörev Saati: {secilen_gorev[2]}\nGörev Dakikası: {secilen_gorev[3]}"
            cevap = messagebox.askyesno("Doğrulama", soru)

            # Cevap true değer ise silme işlemini gerçekleştir.
            if cevap:
                with open("PROJE/GörevListesi.txt", "r") as dosya:
                    satırlar = dosya.readlines()

                with open("PROJE/GörevListesi.txt", "w") as dosya:
                    for satır in satırlar:
                        if satır.strip() != ",".join(secilen_gorev):
                            dosya.write(satır)

                # Treeview'leri güncelle
                self.listeleriYenile()

        # Uyarıları yakala
        except ValueError as e:
            messagebox.showwarning("Hata", str(e))




    # Görev tamamlama fonksiyonu
    def gorevTamamla(self):
        try:
            # Seçimi al
            secilen_item = self.gorev_listesi_treeview.selection()

            # Seçim yapılıp yapılmadığını kontrol et
            if not secilen_item:
                raise ValueError("Tamamlanacak bir görev seçiniz.")

            secilen_gorev = self.gorev_listesi_treeview.item(secilen_item, "values")

            # Doğrulama sorusu
            soru = f"Seçilen görevi tamamlamak istiyor musunuz?\n\nGörev Adı: {secilen_gorev[0]}\nGörev İçeriği: {secilen_gorev[1]}\nGörev Saati: {secilen_gorev[2]}\nGörev Dakikası: {secilen_gorev[3]}"
            cevap = messagebox.askyesno("Doğrulama", soru)

            # Cevap true değer ise tamamlama işlemini gerçekleştir.
            if cevap:
                with open("PROJE/GörevListesi.txt", "r") as dosya:
                    satırlar = dosya.readlines()

                with open("PROJE/GörevListesi.txt", "w") as dosya:
                    for satır in satırlar:
                        if satır.strip() != ",".join(secilen_gorev):
                            dosya.write(satır)

                with open("PROJE/Tamamlandı.txt", "a") as dosya:
                    dosya.write(",".join(secilen_gorev) + "\n")

                # Treeview'leri güncelle
                self.listeleriYenile()

        # Uyarıları yakala
        except ValueError as e:
            messagebox.showwarning("Hata", str(e))

    # Tamamlanmış görevleri eski haline getirme fonksiyonu
    def geriDondur(self):
        try:
            # Seçimi al
            secilen_item = self.tamamlanan_gorevler_treeview.selection()

            # Seçim yapılıp yapılmadığını kontrol et
            if not secilen_item:
                raise ValueError("Geri döndürülecek bir görev seçiniz.")

            secilen_gorev = self.tamamlanan_gorevler_treeview.item(secilen_item, "values")

            # Doğrulama sorusu
            soru = f"Tamamlanan görevi tamamlanmadı olarak işaretlemek istediğinize emin misiniz?\n\nGörev Adı: {secilen_gorev[0]}\nGörev İçeriği: {secilen_gorev[1]}\nGörev Saati: {secilen_gorev[2]}\nGörev Dakikası: {secilen_gorev[3]}"
            cevap = messagebox.askyesno("Doğrulama", soru)

            # Cevap true değer ise işlemi gerçekleştir.
            if cevap:
                with open("PROJE/Tamamlandı.txt", "r") as file:
                    lines = file.readlines()

                with open("PROJE/Tamamlandı.txt", "w") as file:
                    for line in lines:
                        if line.strip() != ",".join(secilen_gorev):
                            file.write(line)

                with open("PROJE/GörevListesi.txt", "a") as file:
                    file.write(",".join(secilen_gorev) + "\n")

                # Treeview'leri güncelle
                self.listeleriYenile()

        # Uyarıları yakala
        except ValueError as e:
            messagebox.showwarning("Hata", str(e))





    # Görev düzenleme fonksiyonu
    def gorevDuzenle(self):
        try:
            # Seçimi al
            secilen_item = self.gorev_listesi_treeview.selection()

            # Seçim yapılıp yapılmadığını kontroll et
            if not secilen_item:
                raise ValueError("Düzenlenecek bir görev seçiniz.")

            secilen_gorev = self.gorev_listesi_treeview.item(secilen_item, "values")

            # Pop-up penceresini oluştur
            pop_up = tk.Toplevel(self.root)
            pop_up.geometry("350x250+200+280")
            pop_up.title("Görev Düzenle")

            # Pop-up penceresini ana pencerenin önüne getir
            pop_up.grab_set()

            # Label'lar ve entry'ler için çerçeve
            frame = tk.Frame(pop_up)
            frame.pack(padx=10, pady=10)

            # Label'lar
            tk.Label(frame, text="Görev Adı:",font="Coolvetica 11 bold").grid(row=0, column=0, sticky="w")
            tk.Label(frame, text="Görev İçeriği:",font="Coolvetica 11 bold").grid(row=1, column=0, sticky="w")
            tk.Label(frame, text="Görev Saati:",font="Coolvetica 11 bold").grid(row=2, column=0, sticky="w")
            tk.Label(frame, text="Görev Dakikası:",font="Coolvetica 11 bold").grid(row=3, column=0, sticky="w")

            # Entry'ler
            gorev_adi_var = tk.StringVar(value=secilen_gorev[0])
            gorev_adi_entry = tk.Entry(frame, textvariable=gorev_adi_var,font="Coolvetica 11 bold")
            gorev_adi_entry.grid(row=0, column=1, pady=5)

            gorev_icerigi_var = tk.StringVar(value=secilen_gorev[1])
            gorev_icerigi_entry = tk.Entry(frame, textvariable=gorev_icerigi_var,font="Coolvetica 11 bold")
            gorev_icerigi_entry.grid(row=1, column=1, pady=5)

            gorev_saati_var = tk.StringVar(value=secilen_gorev[2])
            gorev_saati_entry = tk.Entry(frame, textvariable=gorev_saati_var,font="Coolvetica 11 bold")
            gorev_saati_entry.grid(row=2, column=1, pady=5)

            gorev_dakikasi_var = tk.StringVar(value=secilen_gorev[3])
            gorev_dakikasi_entry = tk.Entry(frame, textvariable=gorev_dakikasi_var,font="Coolvetica 11 bold")
            gorev_dakikasi_entry.grid(row=3, column=1, pady=5)

            
            # Değişiklikleri kaydetme metodu
            def kaydet():
                try:
                    # Boş alan kontrolü
                    if not gorev_adi_var.get() or not gorev_icerigi_var.get() or not gorev_saati_var.get() or not gorev_dakikasi_var.get():
                        raise ValueError("Tüm alanları doldurunuz.")

                    # Kontrol edilmek üzere saat ve dakika değerlerini oku
                    saat = gorev_saati_var.get()
                    dakika = gorev_dakikasi_var.get()

                    # Saat ve dakika değerlerine sayı dışında bir şey girilip girilmediğini kontrol et
                    try:
                        saat = int(saat)
                        dakika = int(dakika)
                    except ValueError:
                        raise ValueError("Saat ve dakika değeri sayı olmalıdır.")

                    # Saat ve dakika değerlerinin uygun olup olmadığını kontrol et
                    if not (0 <= int(saat) <= 23) or not (0 <= int(dakika) <= 59):
                        raise ValueError("Saat 0-23 arasında, dakika 0-59 arasında olmalıdır.")
                    
                    
                    # Saat ve dakika değeri 10'dan küçükse başlarına 0 ekleyerek düzelt
                    if int(saat) < 10:
                        saat = "0" + saat
                    if int(dakika) < 10:
                        dakika = "0" + dakika



                    yeni_gorev = f"{gorev_adi_var.get()},{gorev_icerigi_var.get()},{saat},{dakika}\n"

                    with open("PROJE/GörevListesi.txt", "r") as dosya:
                        satırlar = dosya.readlines()

                    with open("PROJE/GörevListesi.txt", "w") as dosya:
                        for satır in satırlar:
                            if satır.strip() == ",".join(secilen_gorev):
                                dosya.write(yeni_gorev)
                            else:
                                dosya.write(satır)

                    pop_up.destroy()
                    self.listeleriYenile()

                except ValueError as e:
                    messagebox.showwarning("Hata", str(e))

            tk.Button(frame, text="Kaydet",font="Coolvetica 11 bold",fg="blue", command=kaydet).grid(row=4, columnspan=2, pady=10)

            # Çıkış butonu
            tk.Button(frame, text="Geri",font="Coolvetica 11 bold",fg="red", command=pop_up.destroy).grid(row=5, columnspan=2, pady=10)

        except ValueError as e:
            messagebox.showwarning("Hata", str(e))



     # Tamamlanan görev silme metodu   
    def tamamlandiSil(self):
        try:
            # Seçimi al
            selected_item = self.tamamlanan_gorevler_treeview.selection()

            # Seçim yapılıp yapılmadığını kontrol et
            if not selected_item:
                raise ValueError("Silinecek bir tamamlanan görev seçiniz.")

            selected_gorev = self.tamamlanan_gorevler_treeview.item(selected_item, "values")

            # Doğrulama sorusu
            soru = f"Seçilen tamamlanan görevi silmek istediğinize emin misiniz?\n\nGörev Adı: {selected_gorev[0]}\nGörev İçeriği: {selected_gorev[1]}\nGörev Saati: {selected_gorev[2]}\nGörev Dakikası: {selected_gorev[3]}"
            cevap = messagebox.askyesno("Doğrulama", soru)

            # Cevap true değer ise işlemi gerçekleştir.
            if cevap:
                with open("PROJE/Tamamlandı.txt", "r") as file:
                    lines = file.readlines()

                with open("PROJE/Tamamlandı.txt", "w") as file:
                    for line in lines:
                        if line.strip() != ",".join(selected_gorev):
                            file.write(line)

                # Treeview'leri güncelle
                self.listeleriYenile()

        # Uyarıları yakala
        except ValueError as e:
            messagebox.showwarning("Hata", str(e))


    

    # Treeview listelerini yenileme fonksiyonu
    def listeleriYenile(self):
        # Temizle
        self.gorev_listesi_treeview.delete(*self.gorev_listesi_treeview.get_children())
        self.tamamlanan_gorevler_treeview.delete(*self.tamamlanan_gorevler_treeview.get_children())

        # Dosyalardan gelen görevleri saat ve dakika değerlerine göre sırala
        gorev_listesi = self.siraliGorevListesi("PROJE/GörevListesi.txt")
        tamamlanan_gorevler = self.siraliGorevListesi("PROJE/Tamamlandı.txt")

        # Sıralanmış görev listesini treeview'e ekle
        for degerler in gorev_listesi:
            self.gorev_listesi_treeview.insert("", "end", values=degerler)

        # Sıralanmış tamamlanan görev listesini treeview'e ekle
        for degerler in tamamlanan_gorevler:
            self.tamamlanan_gorevler_treeview.insert("", "end", values=degerler)

    # Dosyadan gelen görevleri saat ve dakika değerlerine göre sıralayan yardımcı metot
    def siraliGorevListesi(self, dosya_adi):
        with open(dosya_adi, "r") as dosya:
            # Satırları oku, temizle ve saat/dakika değerlerine göre sırala
            satirlar = sorted((satır.strip().split(",") for satır in dosya), key=lambda x: (int(x[2]), int(x[3])))

        return satirlar




    # Bilgilendirme metodu
    def bilgilendirme(self):
        try:
            # Pop-up penceresini oluştur
            popup = tk.Toplevel(self.root)
            popup.geometry("600x350+260+100")
            popup.title("Bilgi")

            # Pop-up penceresini ana pencerenin önüne getir
            popup.grab_set()

            # Bilgi metni
            bilgi_metni = (
                "Görev Takip Uygulaması\n\n"
                "Bu uygulama, görevleri eklemenizi, silmenizi, tamamlamanızı, düzenlemenizi\n"
                "ve takip etmenizi sağlayan basit bir görev takip uygulamasıdır.\n\n"
                "Kullanım:\n"
                "- 'Görev Ekle' butonu ile yeni görev ekleyebilirsiniz.\n"
                "- 'Görev Sil' butonu ile seçili görevi silebilirsiniz.\n"
                "- 'Görev Tamamla' veya '↓' butonları ile seçili görevi tamamlayabilirsiniz.\n"
                "- 'Görev Düzenle' butonu ile seçili görevi düzenleyebilirsiniz.\n"
                "- 'Geri Döndür' veya '↑' butonları ile tamamlanmış görevi geri döndürebilirsiniz.\n"
                "- 'Bilgi' butonu ile bu bilgi penceresini görüntüleyebilirsiniz.\n"
                "\nÇıkış butonları ile uygulamadan çıkabilirsiniz."
            )

            # Bilgi metnini gösteren etiket
            bilgi_etiket = tk.Label(popup, text=bilgi_metni, justify="left", font="Coolvetica 15 bold")
            bilgi_etiket.pack(pady=10)

            # Çıkış butonu
            cikis_butonu = tk.Button(popup, text="Geri", font="Coolvetica 11 bold", fg="red", command=popup.destroy)
            cikis_butonu.pack(pady=10)

        except Exception as e:
            messagebox.showwarning("Hata", str(e))


    # Çıkış butonu doğrulama sorusu için fonksiyon
    def cıkıs(self):
        # Doğrulama sorusu
        cıkıs = messagebox.askquestion("Çıkış","Çıkış yapmak istediğinize emin misiniz?")

        # Cevap true değer ise işlemi gerçekleştir.
        if cıkıs == "yes":
            root.destroy()


# Arayüzün başlatılması
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1100x750+200+20")
    uygulama = GorevTakipUygulaması(root) # Nesne oluşturma
    root.mainloop()
