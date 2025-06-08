import os
from pathlib import Path
from datetime import datetime

SUPPORTED_EXTENSIONS = ['.pdf', '.epub']

def list_documents(base_dir):
    files_by_year = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in SUPPORTED_EXTENSIONS:
                full_path = os.path.join(root, file)
                year = Path(root).name if Path(root).name.isdigit() else "Desconhecido"
                files_by_year.setdefault(year, []).append((file, ext, full_path))
    return files_by_year

def add_document(source_path, target_dir, year):
    os.makedirs(os.path.join(target_dir, year), exist_ok=True)
    filename = os.path.basename(source_path)
    destination = os.path.join(target_dir, year, filename)
    os.rename(source_path, destination)
    return destination

def rename_document(file_path, new_name):
    dir_path = os.path.dirname(file_path)
    new_path = os.path.join(dir_path, new_name)
    os.rename(file_path, new_path)
    return new_path

def remove_document(file_path):
    os.remove(file_path)
    return f"{file_path} removido."

Cria file_manager.py com funções de manipulação de arquivos
