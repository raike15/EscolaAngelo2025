nomes = ["Anos","paulo","Maria","Sofia","Fernada","Sofia"]

print(f"A primeira ocorrencia de sofia é no índice:{nomes.index("Sofia")}")

print(f"Sofia aparece {nomes.count("Sofia")}vezes na lista")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copiaNomes = nomes.copy()
print(f"Nomes copiados: {copiaNomes}")
