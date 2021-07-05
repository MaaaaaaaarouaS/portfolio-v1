#!/usr/bin/python3
# coding:utf-8

##
#  Ecriture dans fichier "guestbook.html"
#  Paramètres reçus par méthode POST
#
 
import cgi, cgitb , datetime

# Lecture des données formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xville = form.getvalue('ville')
xcomment = form.getvalue('comment')

# Création du fichier si n'existe pas et ouverture en mode append 
gb = open("../../tp4/index.html", "a")


gb.write('<div class="ele">') 
gb.write('<p><em>Date</em>: '+str(datetime.date.today())+'</p>')
gb.write('<p><em>From</em>: '+str(xnom)+' '+str(xprenom)+'</p>')
gb.write('<p><em>Ville</em>: '+str(xville)+'</p>')
gb.write('<p><em>Mesg</em>: '+str(xcomment)+'</p>')
gb.write('</div>')

gb.close()

# Sortie sur UA de l'accusé de réception
print ("Content-type: text/html; charset=UTF-8\n")
a = """
<!DOCTYPE html>
<html>
<head>
<title>Merci!...</title>
</head>
<body>
<script>document.location.href='http://yasmina.emi.ac.ma/~houjari/tp4/index.html?reload'</script>
</body>
</html>
"""
print(a)
