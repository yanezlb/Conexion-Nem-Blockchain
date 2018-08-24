#-*- conding:utf-8 -*-
__copyright__ = "2018  PtariSoft"
__license__ = "License: MIT."
__version__ = "0.0.1"
__author__ = "Luis Yanez"
__email__ = "yanezln@pdvsa.com"

"""
	connectBlockchain
	-----------------
	Implementa conexiones con distintas blockchain
"""

from nemnis import Client, Account

__all__=['conectBlockchain']

class conectBlockchain():
	"""
	Conecta con la blockchain de NEM
	"""
	def __init__(self, server):
		"""
		Inicializa la conexion con la blockchain de NEM
		"""
		self.server = str(server)
		self.nis = Client("http://"+self.server+":7890")
		self.account = Account(self.nis)


	def get_balance_entrante(self,address):
		"""
		Retorna JSON las transsacciones entrastes a la direccion
		:param
		@address: Direccion
		"""
		return  self.account.transfers_incoming(address).json()


	def get_balance_saliente(self,address):
		"""
		Retorna JSON las transsacciones entrastes a la direccion
		:param
		@address: Direccion
		"""
		return  self.account.transfers_outgoing(address).json()


	def get_address_from_pkey(self,pkey):
		"""
		Retorna JSON las transsacciones entrastes a la direccion
		:param
		@pkey: clave publica de la cuenta a consultar
		"""
		return self.account.get_from_public_key(pkey).json()['account']['address']

