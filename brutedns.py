import dns.resolver
import sys
try:
   dominio = sys.argv[1]
   nome_arquivo = sys.argv[2]
except:
    print "Argumentos invalidos!"
    print "Como usar: dnsbrute.py <dominio> <wordlist.txt>"
    sys.exit(1)
try:
    arq = open(nome_arquivo)
    listas = arq.read().splitlines()
except:
      print "Arquivo nao encotrado"
      sys.exit(1)

for lista in listas:
    subdom = lista + "." + dominio
    try:
        resultados = dns.resolver.query(subdom, "a")
        for resultado in resultados:
            print subdom, resultado
    except:
        pass
