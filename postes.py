distancia_rua = int(input())*1000
espaco_postes = int(input())

qtd_postes = (distancia_rua + espaco_postes - 1) // espaco_postes + 1
ultimo_poste = distancia_rua%espaco_postes

print(" {:d} poste(s)." .format(qtd_postes))
print(" {:d} metro(s). " .format(ultimo_poste))