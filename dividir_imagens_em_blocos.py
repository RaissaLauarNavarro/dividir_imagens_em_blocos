#---------------------- INFORMAÇÕES EDITÁVEIS ----------------------------------------------------------------
# defina aqui as informações sobre os imagens que você deseja dividir em blocos
# Lembre de rodar o comando: pip install pillow

# Tamanho do bloco em pixels:
tamanho_bloco = 16

# Diretório da pasta de entrada (com as imagens PNG):
pasta_entrada = 'imagensEntrada/'

# Diretório onde os blocos serão salvos:
diretorio_saida = 'imagensEditadas/'

# Fator de escala (1 = mantém o tamanho original, 2 = dobra, etc.)
#  Recomendado usar potências de 2 (2, 4, 8, 16, 32...) para manter proporção da pixel art.
fator_escala = 32


#---------------------- COMANDO DE CHAMADA ----------------------------------------------------------------
# Para executar este script, você pode usar o seguinte comando no terminal:
# python dividir_imagens_em_blocos.py


#---------------------- CÓDIGO (NÃO ALTERAR) ----------------------------------------------------------------
from PIL import Image
import os

def dividir_todas_as_imagens(pasta_entrada, tamanho_bloco, diretorio_saida, fator_escala):
    if not os.path.isdir(pasta_entrada):
        print(f"ATENÇÃO! A pasta '{pasta_entrada}' não foi encontrada.")
        return

    os.makedirs(diretorio_saida, exist_ok=True)

    # Lista apenas arquivos PNG
    arquivos = [f for f in os.listdir(pasta_entrada) if f.lower().endswith('.png')]

    if not arquivos:
        print("Nenhuma imagem PNG encontrada na pasta de entrada.")
        return

    for arquivo in arquivos:
        caminho_imagem = os.path.join(pasta_entrada, arquivo)
        nome_base = os.path.splitext(arquivo)[0] 

        pasta_saida_imagem = os.path.join(diretorio_saida, nome_base)
        os.makedirs(pasta_saida_imagem, exist_ok=True)

        dividir_imagem_em_blocos(
            caminho_imagem, tamanho_bloco, pasta_saida_imagem, fator_escala, nome_base
        )


def dividir_imagem_em_blocos(caminho_imagem, tamanho_bloco, diretorio_saida, fator_escala, nome_base):
    imagem = Image.open(caminho_imagem).convert('RGBA')
    largura, altura = imagem.size

    if largura % tamanho_bloco != 0 or altura % tamanho_bloco != 0:
        print(f"ATENÇÃO! '{caminho_imagem}' ignorada: dimensões não são múltiplos do tamanho do bloco.")
        return

    contador = 0
    for y in range(0, altura, tamanho_bloco):
        for x in range(0, largura, tamanho_bloco):
            bloco = imagem.crop((x, y, x + tamanho_bloco, y + tamanho_bloco))

            if bloco_contem_conteudo(bloco):
                if fator_escala > 1:
                    bloco = bloco.resize(
                        (tamanho_bloco * fator_escala, tamanho_bloco * fator_escala),
                        Image.NEAREST 
                    )

                nome_arquivo = os.path.join(diretorio_saida, f'{nome_base}_{contador:04}.png')
                bloco.save(nome_arquivo)
                contador += 1

    print(f'{contador} blocos salvos para "{nome_base}" em "{diretorio_saida}"')


def bloco_contem_conteudo(bloco):
    for pixel in bloco.getdata():
        r, g, b, a = pixel
        if a > 0 and (r, g, b) != (255, 255, 255):
            return True
    return False


dividir_todas_as_imagens(pasta_entrada, tamanho_bloco, diretorio_saida, fator_escala)
