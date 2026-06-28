A = int(input("Informe um valor para a variável A: "))
B = int(input("Informe um valor para a variável B: "))

if  A>B:
    aux = A
    A=B
    B=aux
print ("O valor da variavel A agora é : ", A)
print ("O valor da variavel B agora é : ", B)