def to_camel_case(text):
    import re
    if(len(text)>0):
        indice = 0
        cadena = ''
        for x in re.split('_|-',text):
            if(indice==0):
                cadena += x
            else:
                cadena += x.capitalize()
            indice += 1
        return cadena   
    else:
        return ''
