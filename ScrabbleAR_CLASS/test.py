from pattern.es import lexicon, spelling, split, parse
d = {1: '1', 2: '2', 3: 'q', 4: 'w'}
print(str().join(list(d.values())))
tipo = parse(str().join(list(d.values()))).split('/')[1]
print(tipo)
print(parse('SI'))
print({key: value if for key in [(1, 1), (2, ''), (3, 3)]})
# self._parametros.get_palabra() = d
# str().join(list(d.values()))
# print(parse('rgbrty').split('/')[1])	# 'JJ' ADJETIVO, 'VB' VERBO
