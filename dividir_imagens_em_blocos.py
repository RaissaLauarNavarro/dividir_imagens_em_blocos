#---------------------- INFORMAÇÕES EDITÁVEIS ----------------------------------------------------------------
# defina aqui as informações sobre os imagens que você deseja dividir em blocos
# Lembre de rodar o comando: pip install pillow

# Tamanho do bloco em pixels:
tamanho_bloco = 16

# diretório da imagem de entrada: (coloque na pasta imagensEntrada para melhor organização)
imagem_entrada = 'imagensEntrada/'

# Diretório onde os blocos serão salvos:
diretorio_saida = '' 

# Fator de escala (1 = mantém o tamanho original, 2 = dobra, etc.)
#  Recomendado usar potências de 2 (2, 4, 8, 16, 32...) para manter proporção da pixel art.
# Ex.: bloco de 16x16 → fator 32 = imagem final 512x512, fator 16 = 256x256.
fator_escala = 32




#---------------------- COMANDO DE CHAMADA ----------------------------------------------------------------
# Para executar este script, você pode usar o seguinte comando no terminal:
# python dividir_imagens_em_blocos.py



#---------------------- CÓDIGO (NÃO ALTERAR) ----------------------------------------------------------------
from PIL import Image
import os

def dividir_imagem_em_blocos(imagem_entrada, tamanho_bloco, diretorio_saida, fator_escala):

    if not imagem_entrada.strip():
        print("ATENÇÃO!")
        print(f"A imagem não foi encontrada, verifique o caminho da imagem de entrada")
        return
  
    imagem = Image.open(imagem_entrada).convert('RGBA')
    largura, altura = imagem.size

    if not diretorio_saida.strip():
        print(f"Diretório de saída não encontrado. Criando diretório como imagens_divididas...")
        diretorio_saida = "imagens_divididas"

    if largura % tamanho_bloco != 0 or altura % tamanho_bloco != 0:
        print("ATENÇÃO!")
        print("A largura e a altura da imagem devem ser múltiplos do tamanho do bloco")
        return

    os.makedirs(diretorio_saida, exist_ok=True)

    contador = 0
    for y in range(0, altura, tamanho_bloco):
        for x in range(0, largura, tamanho_bloco):
            bloco = imagem.crop((x, y, x + tamanho_bloco, y + tamanho_bloco))

            if bloco_contem_conteudo(bloco):
                if fator_escala > 1:
                    bloco = bloco.resize(
                        (tamanho_bloco * fator_escala, tamanho_bloco * fator_escala),
                        Image.NEAREST  # mantém os pixels "quadrados"
                    )

                nome_arquivo = f'{diretorio_saida}/imagem_{contador:04}.png'
                bloco.save(nome_arquivo)
                contador += 1

    print(f'{contador} blocos salvos em "{diretorio_saida}"')


def bloco_contem_conteudo(bloco):
    for pixel in bloco.getdata():
        r, g, b, a = pixel
        if a > 0 and (r, g, b) != (255, 255, 255):  
            return True
    return False


dividir_imagem_em_blocos(imagem_entrada, tamanho_bloco, diretorio_saida, fator_escala)