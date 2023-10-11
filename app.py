import os

diretorio_origem = "organização"
lista_arquivos = os.listdir(diretorio_origem)

for arquivo in lista_arquivos:
    if os.path.isfile(os.path.join(diretorio_origem, arquivo)):
        # Obtenha a extensão do arquivo
        _, extensao = os.path.splitext(arquivo)
        
        # Remova o ponto da extensão (por exemplo, ".exe" -> "exe")
        extensao = extensao.lstrip(".")
        
        # Crie o diretório com base na extensão, se ainda não existir
        diretorio_destino = os.path.join(diretorio_origem, extensao)
        os.makedirs(diretorio_destino, exist_ok=True)
        
        # Mova o arquivo para o diretório de destino
        os.rename(
            os.path.join(diretorio_origem, arquivo),
            os.path.join(diretorio_destino, arquivo)
        )
print("Arquivos foram organizados por extensão em subdiretórios.")