# 📦Divisor de Imagem em Blocos (com filtro de conteúdo)
Este script em Python divide uma imagem PNG em blocos de tamanho definido (por padrão 16x16 pixels) e salva somente os blocos que possuem conteúdo visível (ou seja, não totalmente brancos ou transparentes).


# 🖼️ Exemplo de uso

Suponha que você tenha uma imagem sprite_sheet.png de 128x128 pixels com ícones, este script irá gerar todos os blocos 16x16 que não estejam vazios, salvando-os como arquivos .png individuais.


# ⚙️ Configuração
Antes de rodar o script, edite as seguintes variáveis no topo do arquivo:

```PYTHON
# Tamanho do bloco em pixels
tamanho_bloco = 16

# Caminho da imagem de entrada
imagem_entrada = 'caminho/para/sua_imagem.png'

# Diretório onde os blocos serão salvos
diretorio_saida = 'blocos_saida'
```


# ▶️ Como executar
Abra o terminal na pasta do script e execute:

```PYTHON
python dividir_imagens_em_blocos.py
```


# 🧠 Requisitos
- Python 3.x

- Biblioteca Pillow para manipulação de imagens:
  
Instale com:

```PYTHON
pip install pillow
```


# 📁 Saída
Os blocos serão salvos como arquivos .png numerados sequencialmente no diretório especificado.

Exemplo de nomes de arquivos:

imagem_0000.png

imagem_0001.png

imagem_0002.png


# 🧪 Lógica de filtragem de blocos
Um bloco só será salvo se:

Contém ao menos um pixel visível (alpha > 0)

E não é completamente branco (RGB != 255,255,255)


# 📝 Licença
Sinta-se livre para usar e modificar!
