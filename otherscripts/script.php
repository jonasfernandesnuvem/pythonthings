<?php
$servername = "mysql-balancer-eks-test.linkedstore.com";
$username = "wpmuprod";
$password = "mysqlwpmu4lombo";
$dbname = "tiendanube";
$options = array(
	PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
	PDO::MYSQL_ATTR_SSL_CA => '/Users/jonasfernandes/pythonthings/otherscripts/proxysql-ca.pem',
    PDO::MYSQL_ATTR_SSL_CERT=>'/Users/jonasfernandes/pythonthings/otherscripts/proxysql-cert.pem',
    PDO::MYSQL_ATTR_SSL_KEY    =>'/Users/jonasfernandes/pythonthings/otherscripts/proxysql-key.pem',
    PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => false,
);
    $conn = new PDO("mysql:host=$servername;port=3306;dbname=$dbname", $username, $password, $options);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $exec = $conn->query('SELECT * FROM mwp_orders WHERE store_id= "1071945"');
    $result = $exec->fetchAll();
    print_r($result); 