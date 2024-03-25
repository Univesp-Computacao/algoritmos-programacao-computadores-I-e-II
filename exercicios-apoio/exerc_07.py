"Manipulação de strings."
# Comece executando as instruções de atribuição:

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
            
#Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:   
print(s1, s2, s3) 
# Output => 'ant bat cod'

print((s1 + " ") *10) 
# Output =>  ant ant ant ant ant ant ant ant ant ant'

print(s1, (s2 + " ")*2 + (s3+" ")*3)
# Output => 'ant bat bat cod cod cod'

print((s1 + " " + s2 + " ")*8) 
# Output => 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'

print((s2*2+s3 + " ")*5) 
# Output => 'batbatcod batbatcod batbatcod batbatcod batbatcod'