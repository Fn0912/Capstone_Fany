
data_Karyawan=[]

def validasi_field(field):
      field = field.strip().upper()
      if field not in ['NAMA', 'GENDER','DIVISI','GAJI']:
        print("Data yang akan diubah tidak sesuai")
        return False
      return True

def validasi_nik(nik):
      if not nik.isdigit():
        print("❌ NIK harus berupa angka.")
        return False
      if len(nik) != 6:
        print("❌ NIK harus 6 angka.")
        return False
      return True

def validasi_nama(nama):
      if not nama.replace(" ", "").isalpha():
        print("❌ Nama hanya boleh mengandung huruf dan spasi.")
        return False
      if isinstance(nama, int):
        return False
      return True

def validasi_gender(Gender):
      Gender = Gender.strip().upper()
      if Gender not in ['F', 'M']:
        print("Gender harus 'F' atau 'M'")
        return False
      return True

def validasi_Divisi(Divisi):
      Divisi = Divisi.strip().upper()
      if Divisi not in ['IT', 'CS' , 'FN' , 'GA']:
        print("Divisi hanya dapat diisi dengan IT , CS(Cutomer Service), GA(General Affair) dan FN(Finance)")
        return False
      return True

def validasi_Gaji(Gaji):
      if not Gaji.isdigit():
        print("❌ Gaji harus berupa angka.")
        return False
      elif int(Gaji) < 3000000:
        print("❌ Gaji harus diatas UMR.")
        return False
      return True

def validasi_confirm(Confirm):
      Confirm = Confirm.strip().upper()
      if Confirm not in ['Y', 'N']:
        print("pilihan tidak sesuai")
        return False
      return True

def tambah_karyawan():
 
    while True:
        nik = input("Masukkan NIK Karyawan: ")
        if validasi_nik(nik):
            break
    
    while True:
        nama = input("Masukkan nama Karyawan: ")
        if validasi_nama(nama):
            break
        
    while True:
        Gender = input("Masukkan Gender Karyawan[F/M]: ")
        if validasi_gender(Gender):
            break

    while True:
        Divisi = input("Masukkan Divisi Karyawan[IT,CS,GA,FN]: ")
        if validasi_Divisi(Divisi):
            break
        
    while True:
        Gaji = input("Masukkan Gaji Karyawan: ")
        if validasi_Gaji(Gaji):
            break
        
    
    Karyawan_Baru = {
        "NAMA": nama,
        "NIK": nik.upper(),
        "GENDER": Gender.upper(),
        "DIVISI" : Divisi.upper(),
        "GAJI" : Gaji
    }

    data_Karyawan.append(Karyawan_Baru)
    print("Data Karyawan berhasil ditambahkan!\n")

def tampilkan_data_biasa(data):
    print(f"{'NIK':<15}{'NAMA':<25}{'GENDER':<10}{'DIVISI':<10}{'GAJI':<15}")
    print("-" * 75)
    for k in data:
        print(f"{k['NIK']:<15}{k['NAMA']:<25}{k['GENDER']:<10}{k['DIVISI']:<10}{k['GAJI']:<15}")

def tampilkan_data_filtered(data,field,value_filter):
    if field == "NAMA":
        filtered = [k for k in data if k["NAMA"] == value_filter.upper()] 
    elif field== "GENDER": 
        filtered = [k for k in data if k["GENDER"] == value_filter.upper()]
    elif field == "DIVISI":
        filtered = [k for k in data if k["DIVISI"] == value_filter.upper()]  
    elif field== "NIK": 
        filtered = [k for k in data if k["NIK"] == value_filter] 

    print(f"{'NIK':<15}{'NAMA':<25}{'GENDER':<10}{'DIVISI':<10}{'GAJI':<15}")
    print("-" * 75)
    for k in filtered:
        print(f"{k['NIK']:<15}{k['NAMA']:<25}{k['GENDER']:<10}{k['DIVISI']:<10}{k['GAJI']:<15}")

def edit_karyawan(nik, field, new_value):
      
    for karyawan in data_Karyawan:
        if karyawan['NIK'] != nik:
            print(f"Error: Karyawan dengan NIK {nik} tidak ditemukan.")
            break
        else :
            karyawan[field] = new_value
            print(f"Data '{field}' karyawan NIK {nik} berhasil diperbarui.")
            tampilkan_data_biasa(data_Karyawan)

def hapus_karyawan(data,nik):
        for i, karyawan in enumerate(data):
            if karyawan['NIK'] != nik:
                print(f"Error: Karyawan dengan NIK {nik} tidak ditemukan.")
            else :
                del data[i]
                tampilkan_data_biasa(data)

def menu_1_1():
    while True:
        print("================== Report Data Karyawan PT X ==================")
        print("1. Report seluruh data Karyawan")
        print("2. Report Data Karayawan berdasarkan Gender")
        print("3. Report Data Karayawan berdasarkan Divisi")
        print("4. Kembali Ke Menu Utama")
        Choise1 = input("Silahkan Pilih Sub Menu Report[1-3] : ")

        if Choise1 == "1":
            tampilkan_data_biasa(data_Karyawan)
            menu_1_1()
            break
        elif Choise1 == "2":
            while True:
                Gender = input("Masukkan Gender Karyawan[F/M]: ")
                if validasi_gender(Gender):
                    break
            
            tampilkan_data_filtered(data_Karyawan,"GENDER",Gender)
            menu_1_1()            
            break
        elif Choise1 == "3":
            while True:
                Divisi = input("Masukkan Divisi Karyawan[IT,CS,GA,FN]: ")
                if validasi_Divisi(Divisi):
                    break

            tampilkan_data_filtered(data_Karyawan,"DIVISI",Divisi)
            menu_1_1()
            break
        elif Choise1 == "4":
            menu_1()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_1_2():
    while True:
        print("================== Tambah Data Karyawan PT X ==================")
        print("1. Tambah data Karyawan")
        print("2. Kembali Ke Menu Utama")
        Choise2 = input("Silahkan Pilih Sub Menu Tambah[1-2] : ")

        if Choise2 == "1":
            tambah_karyawan()
        elif Choise2 == "2":
            menu_1()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_1_3():
    while True:
        print("================== Edit Data Karyawan PT X ==================")
        print("1. Edit data Karyawan")
        print("2. Kembali Ke Menu Utama")
        Choise2 = input("Silahkan Pilih Sub Menu Edit[1-2] : ")

        if Choise2 == "1":
            while True:
                  nik = input("Masukkan NIK Karyawan yang akan diubah: ")
                  if validasi_nik(nik):
                        break

            while True:
                  field = input("Masukkan Jenis data yang akan diubah: ")
                  field = field.upper()
                  if validasi_field(field):
                   break

            if field =="NAMA":
                  while True:
                        nama = input("Masukkan nama Karyawan: ")
                        if validasi_nama(nama):
                              break
                  new_value=nama
            elif field == "DIVISI":
                  while True:
                        Divisi = input("Masukkan Divisi Karyawan[IT,CS,GA,FN]: ")
                        if validasi_Divisi(Divisi):
                              break
                  new_value=Divisi
            elif field =="GENDER":
                  while True:
                        Gender = input("Masukkan Gender Karyawan[F/M]: ")
                        if validasi_gender(Gender):
                              break
                  new_value=Gender
            elif field =="GAJI":
                  while True:
                        Gaji = input("Masukkan Gaji Karyawan: ")
                        if validasi_Gaji(Gaji):
                              break
                  new_value=Gaji
            
            tampilkan_data_filtered(data_Karyawan,"NIK",nik)
            while True:
                Confirm = input("Apakah anda yakin akan mengubah data[Y/N]: ")
                if validasi_confirm(Confirm):
                    break

            if Confirm == "Y" or Confirm == "y":
                edit_karyawan(nik, field, new_value)
                menu_1_3()
                break
            elif Confirm =="N" or Confirm == "n":
                menu_1_3()
                break
            
        elif Choise2 == "2":
            menu_1()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_1_4():
    while True:
        print("================== Hapus Data Karyawan PT X ==================")
        print("1. Hapus data Karyawan")
        print("2. Kembali Ke Menu Utama")
        Choise2 = input("Silahkan Pilih Sub Menu Hapus[1-2] : ")

        if Choise2 == "1":
            while True:
                nik = input("Masukkan NIK Karyawan yang akan Hapus: ")
                if validasi_nik(nik):
                    break
            tampilkan_data_filtered(data_Karyawan,"NIK",nik)
            while True:
                Confirm = input("Apakah anda yakin akan mengubah data[Y/N]: ")
                if validasi_confirm(Confirm):
                    break

            if Confirm == "Y" or Confirm == "y":
                hapus_karyawan(data_Karyawan,nik)
                break
            elif Confirm =="N" or Confirm == "n":
                menu_1_4()
                break
        elif Choise2 == "2":
            menu_1()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_1():
    while True:
        print("================== Report Data Karyawan PT X ==================")
        print("1. Report Data Karyawan")
        print("2. Menambahkan Data Karyawan")
        print("3. Mengubah Data Karyawan")
        print("4. Menghapus Data Karyawan")
        print("5. Exit")
        Choise = input("Silahkan Pilih Main_Menu[1-5] : ")

        if Choise == "1":
            menu_1_1()
            break
        elif Choise == "2":
            menu_1_2()
            break
        elif Choise == "3":
            menu_1_3()
            break
        elif Choise == "4":
            menu_1_4()
        elif Choise == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


menu_1()

