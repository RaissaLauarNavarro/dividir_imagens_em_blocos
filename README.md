# 📦Divisor de Imagem em Blocos (com filtro de conteúdo e múltiplos arquivos)

Este script em Python percorre **todas as imagens PNG** dentro de uma pasta, divide cada imagem em blocos de tamanho definido (por padrão 16x16 pixels) e salva **apenas os blocos que possuem conteúdo visível** (não totalmente brancos ou transparentes).

Para melhor organização, cada imagem processada gera **uma subpasta** com o mesmo nome da imagem original, onde serão salvos os blocos correspondentes.

# 🖼️ Exemplo de uso

Suponha que você tenha uma pasta `imagensEntrada` com:

```
personagem.png
itens.png
tileset.png
```

O script irá gerar, dentro da pasta de saída (`imagens_divididas`), subpastas como:

```
imagens_divididas/
  personagem/
    personagem_0000.png
    personagem_0001.png
    ...
  itens/
    itens_0000.png
    itens_0001.png
    ...
  tileset/
    tileset_0000.png
    tileset_0001.png
    ...

```

# ⚙️ Configuração

Antes de rodar o script, edite as seguintes variáveis no topo do arquivo:

```PYTHON
# Tamanho do bloco em pixels
tamanho_bloco = 16

# Pasta de entrada contendo as imagens PNG
pasta_entrada = 'imagensEntrada/'

# Diretório onde os blocos serão salvos
diretorio_saida = 'imagens_divididas'

# Fator de escala (opcional) — aumenta o tamanho dos blocos na saída
# Ex.: fator_escala = 32 transforma blocos 16x16 em imagens 512x512
fator_escala = 32

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

* Cada imagem PNG da pasta de entrada será processada separadamente.
* Os blocos serão salvos na pasta de saída, dentro de uma **subpasta** com o nome da imagem original (sem extensão).
* Arquivos nomeados no formato:

  ```
  nomeOriginal_0000.png
  nomeOriginal_0001.png
  ...

  ```

# 🧪 Lógica de filtragem de blocos

Um bloco só será salvo se:

Contém ao menos um pixel visível (alpha > 0)

E não é completamente branco (RGB != 255,255,255)

# 📝 Licença

Sinta-se livre para usar e modificar!
