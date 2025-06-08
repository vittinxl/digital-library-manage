import os
import shutil
from file_manager import *

def setup_module(module):
    os.makedirs("test_data/2022", exist_ok=True)
    with open("test_data/2022/teste.pdf", "w") as f:
        f.write("PDF de teste")

def teardown_module(module):
    shutil.rmtree("test_data")

def test_list_documents():
    result = list_documents("test_data")
    assert "2022" in result
    assert any(f[0] == "teste.pdf" for f in result["2022"])

def test_add_and_rename_document():
    path = add_document("test_data/2022/teste.pdf", "test_data", "2023")
    renamed = rename_document(path, "novo_nome.pdf")
    assert os.path.exists(renamed)

def test_remove_document():
    path = "test_data/2023/novo_nome.pdf"
    msg = remove_document(path)
    assert not os.path.exists(path)
    assert "removido" in msg
