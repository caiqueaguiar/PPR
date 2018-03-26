#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
clic=var.split("=")[0]

if clic == "serv":
	print("content-type: text/html")
	print("")
	f = open("menuserv.html", "r")
	pagina = f.read()
	f.close()
	print("pagina")
if clic == "stats":
	print("content-type: text/html")
	print("")
	f = open("status.html", "r")
	pagina = f.read()
	f.close()
	print("stats")
