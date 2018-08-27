# Conexion-Nem-Blockchain

Clase python para la conexíón con la [Blockchain NEM](https://nemproject.github.io). 

### Prerequisitos

Instalar la siguiente dependencia:

`pip install git+https://github.com/semolex/nis-python-client`

### Métodos

  - conectBlockchain("IP-NIS")
  - get_balance_entrante('address')
  - get_balance_saliente('address')
  - get_address_from_pkey('address')

### Ejemplos de uso

```
  connection = conectBlockchain("153.122.112.137")
  entrante = connection.get_balance_entrante('TD6GWFFBJ5OO4MNTXXZEJ2SAMNP4U2MYQ37VK7S7')
  saliente = connection.get_balance_saliente('TD6GWFFBJ5OO4MNTXXZEJ2SAMNP4U2MYQ37VK7S7')
  addres = connection.get_address_from_pkey('')
  data = conectBlockchain("153.122.112.137").get_balance_saliente("de49e258ff650a185f5ae0d7ec05a345d120277042fb0f68ef40984b8b0e8d99")
```
