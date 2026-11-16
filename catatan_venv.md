# Catatan Virtual Environments

Virtual environment adalah folder terpisah untuk paket Python milik satu proyek, jadi paket di proyek ini tidak bercampur dengan proyek lain.

## Perintah yang dicoba (Windows PowerShell)

- Membuat venv: `python -m venv venv`
- Mengaktifkan: `venv\Scripts\Activate.ps1` (di CMD: `venv\Scripts\activate.bat`)
- Tanda aktif: tulisan `(venv)` di awal baris terminal
- Memasang paket: `pip install camelcase`
- Melihat daftar paket: `pip list`
- Menghapus paket: `pip uninstall asgiref`
- Menonaktifkan: `deactivate`

Di Linux atau Mac, mengaktifkan memakai `source venv/bin/activate`.

## Catatan

Folder venv ditulis di `.gitignore` supaya tidak ikut ke GitHub.