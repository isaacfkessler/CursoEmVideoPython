# Solicitando nome
# Upper transforma em Maiúsculo
# Strip remove espaços iniciais e finais
nome = str(input('Digite o nome: ')).upper().strip()

# Por fim, imprimindo o resultado
# Função "in" faz com que o programa verifique se existe o nome entre áspas, existe na String
# Caso sim, retorna TRUE, caso não, retorna FALSE.
print('A pessoa tem "SILVA" no nome? {}'.format('SILVA' in nome))