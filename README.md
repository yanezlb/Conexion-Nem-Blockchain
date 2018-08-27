# Conexion-Nem-Blockchain
Clases para agilizar el proceso de extracción de información de la blockchain de NEM

- ```conectBlockchain("IP-SERVER")``` 
- ```conectBlockchain("IP-SERVER").get_balance_entrante('address')``` 
- ```conectBlockchain("IP-SERVER").get_balance_saliente('address')```  
- ```conectBlockchain("IP-SERVER").get_address_from_pkey('address')``` 

```connection = conectBlockchain("153.122.112.137").get_balance_saliente("TD6GWFFBJ5OO4MNTXXZEJ2SAMNP4U2MYQ37VK7S7")```
