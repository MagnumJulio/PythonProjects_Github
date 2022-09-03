#!/usr/bin/python3

'''
    Programa que tira todas quebras de linhas de alguma string 
    copiada para o clipboard. Muito útil para textos grandes
    copiados diretamente de pdfs.
'''
import pyperclip


text = pyperclip.paste().splitlines()
text = ' '.join(text)
pyperclip.copy(text)
print("   ")
#print(f'String in clipboard had its \\n removed')


