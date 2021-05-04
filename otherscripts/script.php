<?php
$servername = "zapdos2.ckt7jl13k34z.us-east-1.rds.amazonaws.com";
$username = "wpmuprod";
$password = "mysqlwpmu4lombo";
$dbname = "tiendanube";
$options = array(
	PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
	PDO::MYSQL_ATTR_SSL_CA => '/home/ubuntu/rds-ca-2019-root.pem',
	PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => false,
);

    $conn = new PDO("mysql:host=$servername;port=3306;dbname=$dbname", $username, $password, $options);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $exec = $conn->query('SELECT * FROM mwp_orders WHERE store_id= "1071945"');
    $result = $exec->fetchAll();
    print_r($result);