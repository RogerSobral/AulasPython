from POO.associacao import Escritor, Ferramenta

#escritor1=Escritor("Carlos")
escritor2=Escritor("Pedro")

#f1=Ferramenta("Caneta")
f2=Ferramenta("Computador")

#escritor1.ferramenta=f1
escritor2.ferramenta=f2
#print(escritor1.ferramenta.escrever())
print(escritor2.ferramenta.nome)


# Crie uma aplicação que vai ter uma classe do tipo (Piloto) e outra do tipo (Carro)
# Faça a Associação deles, lembrando que queremos somente o nome de ambos,
# O Carro vai estar associado ao piloto.
# E a classe carro tem um metodo chamado andar() que mostra uma mensagem
# f"Estou dirigindo o carro {nome do carro}"