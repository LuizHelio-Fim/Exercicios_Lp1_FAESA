num_A = int(input("Digite um valor para A: "))
num_B = int(input("Digite um valor para B: "))

if num_A > num_B:
    print("{} é maior que {}".format(num_A, num_B))
elif num_B > num_A:
    print("{} é maior que {}".format(num_B, num_A))
else:
    print("A = B")