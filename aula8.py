#Abrindo texto de outro arquivo
'''ts=open('albumsts.txt')
print(ts.read())
print(ts.readline())'''

'''newalbums = open('albumsts.txt', 'r+')
print(newalbums.read())
newalbums.write('\n The Life of a showgirl')
newalbums = open('albumsts.txt', 'r')
#fechando arquivo'''

'''newalbums.close()'''
#Quando tentamos escrever qualquer coisa após o texto fechado, teremos um erro, pois estamos tentando escrever algo em um arquivo fechado. 
'''newalbums.write('Karma')'''
#prática
'''compromissos = open('compromissos.txt', 'r+')
print(compromissos.read())
compromissos.write('\n - Ir para faculdade \n - Estudar para as atividades \n - corrigir homework')
compromissos.read()
compromissos.close()'''
#comando with
'''with open('compromissos.txt') as compromissos: 
    print(compromissos.readline())
    print(compromissos.readline())
print(compromissos.readline())'''

compromissos = open('compromissos.txt', 'r')
for x in compromissos:
    print(x)