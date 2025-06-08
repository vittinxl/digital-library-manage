import argparse
from file_manager import list_documents, add_document, rename_document, remove_document

parser = argparse.ArgumentParser(description="Sistema de Gerenciamento da Biblioteca Digital")

subparsers = parser.add_subparsers(dest="command")

# Listar
subparsers.add_parser("listar")

# Adicionar
add = subparsers.add_parser("adicionar")
add.add_argument("source")
add.add_argument("target_dir")
add.add_argument("ano")

# Renomear
rename = subparsers.add_parser("renomear")
rename.add_argument("file_path")
rename.add_argument("novo_nome")

# Remover
remove = subparsers.add_parser("remover")
remove.add_argument("file_path")

args = parser.parse_args()

if args.command == "listar":
    docs = list_documents("biblioteca")
    for ano, arquivos in docs.items():
        print(f"\nAno {ano}:")
        for nome, ext, path in arquivos:
            print(f" - {nome} ({ext})")
elif args.command == "adicionar":
    print(add_document(args.source, args.target_dir, args.ano))
elif args.command == "renomear":
    print(rename_document(args.file_path, args.novo_nome))
elif args.command == "remover":
    print(remove_document(args.file_path))
