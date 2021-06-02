<?php
$servername = "mysql-balancer-eks-test.linkedstore.com";
$username = "wpmuprod";
$password = "mysqlwpmu4lombo";
$db = "tiendanube";
// Create connection
    $mysqli -> ssl_set(NULL, NULL, NULL, NULL, NULL);
    $conn = new mysqli($servername, $username, $password,$db);
    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";
        if ($result = mysqli_query($conn, "SELECT * FROM mwp_orders WHERE store_id= 1071945")) {
        echo "Returned rows are: " . mysqli_num_rows($result);
        while ($row = mysqli_fetch_assoc($result)) {
            print_r($row);
        }
        }
        // $result = $exec->fetchAll();
        // print_r($result);
?>