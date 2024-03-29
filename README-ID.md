<div align="center">
  <img src="https://raw.githubusercontent.com/FajarKim/pycx3/master/image/logo.svg" alt="PYCX3 Logo" width="140"/>
  <h1>PYCX3</h1>
  <p><a href="https://github.com/FajarKim/pycx3/blob/master/README-ID.md">Indonesia</a></p>
  <p><a href="https://github.com/FajarKim/pycx3/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml">Laporkan Bug</a> · <a href="https://github.com/FajarKim/pycx3/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml">Ajukan Fitur</a></p>
  <p>
    <a href="https://pypi.org/project/pycx3"><img src="https://img.shields.io/pypi/v/pycx3?label=PyPI&labelColor=302d41&color=8aadf4&logoColor=d9e0ee&logo=pypi&style=for-the-badge" alt="PyPI Version"/></a>
    <a href="https://github.com/FajarKim/pycx3/stargazers/"><img src="https://custom-icon-badges.demolab.com/github/stars/FajarKim/pycx3?label=Stars&logo=star&labelColor=302d41&color=c9cbff&logoColor=d9e0ee&style=for-the-badge" alt="Stars"></a>
    <a href="https://github.com/FajarKim/pycx3/network/members/"><img src="https://custom-icon-badges.demolab.com/github/forks/FajarKim/pycx3?label=Forks&logo=fork&labelColor=302d41&color=b5e8e0&logoColor=d9e0ee&style=for-the-badge" alt="Forks"/></a>
    <a href="https://github.com/FajarKim/pycx3/issues"><img src="https://custom-icon-badges.demolab.com/github/issues/FajarKim/pycx3?label=Issues&labelColor=302d41&color=f5a97f&logoColor=d9e0ee&logo=issue&style=for-the-badge" alt="Issues"/></a>
    <a href="https://github.com/FajarKim/pycx3/archive/refs/heads/master.zip"><img src="https://custom-icon-badges.demolab.com/github/languages/code-size/FajarKim/pycx3?label=Download&logo=download&labelColor=302d41&color=b7bdf8&logoColor=d9e0ee&style=for-the-badge" alt="Download Size"/></a>
  </p>
</div>

## Daftar Isi

1. [Pendahuluan](#pendahuluan)
2. [Fitur](#fitur)
3. [Instalasi](#instalasi)
4. [Penggunaan](#penggunaan)
5. [Lisensi](#lisensi)
6. [Donasi](#donasi)
7. [Catatan Perubahan](#catatan-perubahan)

## Pendahuluan

PYCX3 adalah kompiler kode Python 3 yang menggunakan Cython untuk peningkatan kinerja. Ini menyediakan cara yang mudah untuk mengkompilasi kode Python 3.8 keatas, bertujuan untuk meningkatkan kecepatan dan efisiensi eksekusi, terutama untuk optimalisasi kode Python lama.

## Fitur

- **Dukungan Python >=3.8:** Dirancang khusus untuk mengkompilasi kode Python 3.8 ketas.
- **Integrasi Cython:** Menggunakan Cython untuk menghasilkan ekstensi C demi peningkatan kinerja.
- **Antarmuka Baris Perintah:** CLI yang mudah digunakan untuk mengkompilasi kode Python 3.

## Instalasi

Anda dapat menginstal `pycx3` menggunakan `pip`:

```bash
pip install pycx3
```

## Penggunaan

Penggunaan dasar dengan perintah CLI:

```bash
pycx3 source_file.py
```

Menggunakan modul impor:

```python
from pycx3 import compile as compile_

compile_.compile("source_file.py" #, True/False for enable verbose mode)
```

## Lisensi

PYCX3 dirilis di bawah lisensi AGPL-3.0, yang memberikan izin berikut:
- Penggunaan komersial
- Modifikasi
- Distribusi
- Penggunaan paten
- Penggunaan pribadi

Untuk bahasa yang lebih lanjut, lihat [LISENSI](https://github.com/FajarKim/pycx3/blob/master/LICENSE).

## Donasi

Suka proyek ini? Harap pertimbangkan untuk berdonasi untuk membantu meningkatkannya!

[![GitHub](https://img.shields.io/badge/GitHub-Sponsor-blue?labelColor=302d41&color=f5bde6&logo=github&logoColor=d9e0ee&style=for-the-badge)](https://github.com/sponsors/FajarKim/)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-blue?labelColor=302d41&color=eed49f&logo=buymeacoffee&logoColor=d9e0ee&style=for-the-badge)](https://buymeacoffee.com/fajarkim/)
[![Trakteer](https://custom-icon-badges.demolab.com/badge/Trakteer-Donate-blue?labelColor=302d41&color=ed8796&logo=trakteerid&logoColor=d9e0ee&style=for-the-badge)](https://trakteer.id/fajarkim/)

## Catatan Perubahan

Terus ikuti perubahan dan pembaruan terbaru PYCX3 dengan mengacu ke [Catatan Perubahan](https://github.com/FajarKim/pycx3/releases).

Terima kasih telah memilih PYCX3! Kami bertujuan untuk memberikan solusi yang aman dan andal untuk mengenkripsi sumber file Python.

<div align="center">
  <img src="https://raw.githubusercontent.com/FajarKim/FajarKim/master/images/line.svg?sanitize=true"/>
</div>

<p align="center">Dibuat dengan ❤️ dan Python</p>
<p align="center">Copyright © 2024 Rangga Fajar Oktariansyah</p>
<div align="center">
  <a href="https://github.com/FajarKim/pycx3/blob/master/LICENSE"><img src="https://custom-icon-badges.demolab.com/github/license/FajarKim/pycx3?label=License&labelColor=302d41&color=91d7e3&logo=law&logoColor=d9e0ee&style=for-the-badge" alt="License"></a>
</div>
