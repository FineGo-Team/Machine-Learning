# Categorizing Financial Status

Folder ini berisi file-file terkait model klasifikasi status keuangan berdasarkan data penghasilan, pengeluaran, dan faktor-faktor lainnya. Dataset yang digunakan dalam model ini dibuat dengan data asli dari **Badan Pusat Statistik (BPS)** tentang UMR (Upah Minimum Regional) setiap provinsi di Indonesia pada tahun 2020, yang dikembangkan lebih lanjut menggunakan Python untuk keperluan pelatihan dan pengujian model.

## **Isi Folder**
- `categorizing_financial_health_model.ipynb`: Notebook Jupyter yang berisi kode untuk preprocessing data, pelatihan model, dan evaluasi model klasifikasi status keuangan.
- `categorizing_financial_health_model.h5`: File model yang telah dilatih dalam format H5, digunakan untuk deployment atau inferensi.
- `categorizing_financial_health_model.keras`: File model yang disimpan dalam format Keras.
- `categorizing_financial_health_model.py`: Script Python mandiri untuk menjalankan pelatihan dan evaluasi model.
- `financial_data_indonesia.csv`: Dataset hasil pengembangan yang digunakan untuk pelatihan model.

## **Tentang Dataset**
Dataset yang digunakan dalam proyek ini adalah hasil pengembangan dari data asli UMR (Upah Minimum Regional) setiap provinsi di Indonesia pada tahun 2020 yang diterbitkan oleh Badan Pusat Statistik (BPS).  
- **Sumber asli:** Data UMR 2020 dari BPS.  
- **Proses pengembangan:**  
  Dataset ini dibuat dengan menambahkan beberapa kolom baru menggunakan Python, seperti pengeluaran untuk kebutuhan pokok (makanan, transportasi, perumahan), tagihan bulanan (air, listrik, internet), utang, tabungan, serta status keuangan berdasarkan penghitungan rasio pendapatan dan pengeluaran.

Dataset ini berfungsi sebagai data simulasi untuk pelatihan model klasifikasi status keuangan menjadi tiga kategori: **sehat**, **kurang sehat**, dan **tidak sehat**.

## **Penggunaan**
1. Jalankan file `categorizing_financial_health_model.ipynb` untuk melatih dan mengevaluasi model.
2. Gunakan file model yang telah dilatih (`.h5` atau `.keras`) untuk deployment.
3. Dataset (`financial_data_indonesia.csv`) dapat digunakan untuk eksperimen lebih lanjut atau validasi ulang model.

## **Lisensi**
Dataset ini dibuat dengan tujuan pembelajaran dan pengembangan model machine learning. Data asli berasal dari Badan Pusat Statistik (BPS), dan pengembangan lebih lanjut dilakukan secara independen. Pastikan untuk menghormati hak cipta dan kebijakan data saat menggunakan informasi ini.
