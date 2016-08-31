Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> class Pan:
	def __init__(self, tam,sabor,precio):
		self.tam=tam
		self.sabor=sabor
		self.precio=precio
	def desplegarC(self):
		print (self.tam),
		print (self.sabor),
		print (self.precio)
		
>>> pan1 = Pan(Grande,queso,50)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    pan1 = Pan(Grande,queso,50)
NameError: name 'Grande' is not defined
>>> pan1 = Pan("Grande","Queso","25")
>>> pan2 = Pan("Pequeno","Chocolate","10")
>>> pan3 = Pan("Grande","Dulce","500")
>>> pan1.desplegarC()
Grande
Queso
25
>>> pan2.desplegarC()
Pequeno
Chocolate
10
>>> pan3.desplegarC()
Grande
Dulce
500
>>> raw_imput()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    raw_imput()
NameError: name 'raw_imput' is not defined
>>> 
