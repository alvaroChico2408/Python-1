'''
Created on 30 sept 2024

@author: alvaro
'''

import os.path
import urllib.request
import re


def abrir_url(url, archivo):
    try:
        if os.path.exists(archivo):
            recarga = input("La página ya ha sido cargada, ¿está seguro que quieres recargarla (s/n)?")
            if recarga == "s":
                urllib.request.urlretrieve(url, archivo)
        else:
            urllib.request.urlretrieve(url, archivo)
        return archivo
    except:
        print("Error en la página")
        return None
  
        
def extraer_lista(fichero):
    f = open (fichero, "r", encoding="utf-8")
    s = f.read()
    l1 = re.findall(r'<title>(.*)</title>\s*<link>(.*)</link>', s)
    l2 = re.findall(r'<pubDate>(.*)</pubDate>', s)
    l = [list(e1) for e1 in l1[1:]]
    for e1, e2 in zip(l, l2):
        e1.append(e2)
    f.close()
    return l


def formatear_fecha(fecha):
    meses = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    partes_bien = []
    partes = fecha.split()
    partes_bien.append(partes[1])
    partes_bien.append(partes[3])
    partes_bien.append(meses[partes[2]])
    return partes_bien


def imprimir_lista(lista):
    for t in lista:
        print("Título:", t[0])
        print("Link:", t[1])
        partes = formatear_fecha(t[2])
        print("fecha:", "{}/{}/{}".format(partes[0], partes[2], partes[1]))


def buscar_fecha(lista):
    mes = input("Introduzca el mes (mm):")
    dia = input("Introduzca el dia (dd):")
    encuentra = False
    for t in lista:
        partes = formatear_fecha(t[2])
        if mes == partes[2] and dia == partes[0]:
            print("Título:", t[0])
            print("Link:", t[1])
            partes = formatear_fecha(t[2])
            print("fecha:", "{}/{}/{}".format(partes[0], partes[2], partes[1]))
            encuentra = True
    if encuentra == False:
        print("No hay noticias para esa fecha")
        

if __name__ == '__main__':
    fichero = "noticias"
    if abrir_url("https://www.abc.es/rss/2.0/espana/andalucia/", fichero):
        lista = extraer_lista(fichero)
    if lista:
        imprimir_lista(lista)
        buscar_fecha(lista)
