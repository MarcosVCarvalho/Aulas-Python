def notas(*n,s=False):
   r = dict()
   r['total'] = len(n)
   r['maximo'] = max(n)
   r['minimo'] = min(n)
   r['media'] = sum(n) / len(n)
   if s:
        if r['media'] < 6:
             r['situação'] =  'ruim'
        elif r['media'] >= 6 and r['media'] < 8:
            r['situação'] =  'boa'
        else:
            r['situação'] =  'excelente'

   return(r)
resp = notas(6,10,10,s=True)
print(resp)
