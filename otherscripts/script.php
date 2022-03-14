<?php
$servername = "<instance-database-hostname>";
$username = "<username>";
$password = "<db-password>";
$dbname = "<database-name";
$options = array(
	PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
	PDO::MYSQL_ATTR_SSL_CA => '<path>/proxysql-ca.pem',
    PDO::MYSQL_ATTR_SSL_CERT=>'<path>/proxysql-cert.pem',
    PDO::MYSQL_ATTR_SSL_KEY    =>'<path>/proxysql-key.pem',
    PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => false,
);
    $conn = new PDO("mysql:host=$servername;port=3306;dbname=$dbname", $username, $password, $options);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $exec = $conn->query('SELECT * FROM '<table-name>' WHERE store_id= "1071945"');
    $result = $exec->fetchAll();
    print_r($result); 