# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faço um programa que o ajude, lendo o nome dos alunos e mostrando o escolhido.
import random
n1 = input('Primeiro aluno ')
n2 = input ('Segundo aluno ')
n3 = input ('Terceiro aluno ')
n4 = input ('Quarta aluno ')
lista = [n1, n2, n3, n4]
e = random.choice(lista)
print(f'O aluno escolhido foi {e}')