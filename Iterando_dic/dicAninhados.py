# Top 10 software products with the most vulnerabilities in 2017
# (through August).  From www.cvedetails.com.
problemas2017 = {
    'Android': {'vendor': 'Google',
                'type': 'Operating System',
                'number': 564},
    'Linux Kernel': {'vendor': 'Linux',
                     'type': 'Operating System',
                     'number': 367},
    'Imagemagick': {'vendor': 'Imagemagick',
                    'type': 'Application',
                    'number': 307},
    'IPhone OS': {'vendor': 'Apple',
                  'type': 'Operating System',
                  'number': 290},
    'Mac OS X': {'vendor': 'Apple',
                 'type': 'Operating System',
                 'number': 210},
    'Windows 10': {'vendor': 'Microsoft',
                   'type': 'Operating System',
                   'number': 195},
    'Windows Server 2008': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 187},
    'Windows Server 2016': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 183},
    'Windows Server 2012': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 176},
    'Windows 7': {'vendor': 'Microsoft',
                  'type': 'Operating System',
                  'number': 174}
}

print('Produto               Vendedor      Tipo                Quantidade')
print('------------------------------------------------------------------')

for produto, valor in problemas2017.items():
    linha = "{:21} {:13} {:18} {:8}".format(produto,
                                            valor['vendor'],
                                            valor['type'],
                                            valor['number'])
    print(linha)

print()

# Procurando itens específicos
# Quantas vulnerabilidades teve o Windows 7?
print(
    f"Número de problemas do Windows 7: \
{problemas2017['Windows 7']['number']}")
print()

# Qual produto teve maior número de vulnerabilidades?
maxproduct = ''
maxnumber = -1

for produto, valores in problemas2017.items():
    if valores['number'] > maxnumber:
        maxnumber = valores['number']
        maxproduct = produto

print(f"O produto com mais vulnerabilidades foi: \
{maxproduct} com {maxnumber} vulnerabilides")
