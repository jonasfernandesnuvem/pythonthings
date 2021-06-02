<?php
$con = mysqli_init();
require('credentials.php')
// Create connection
    if (!$con){
      die("mysqli_init failed");
    }
    mysqli_ssl_set($con,NULL,NULL,NULL,NULL,NULL); 
    $conn = new mysqli($servername, $username, $password,$db);
    if (!$conn->real_connect($con,$servername, $username, $password, $db)) {
      die('Connect Error (' . mysqli_connect_errno() . ') '. mysqli_connect_error());
    }
    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }
    echo "Database connected";
    printf("Client version: %d\n", mysqli_get_client_version());
 
    mysqli_close($con);
//     echo "Connected successfully";
//         if ($result = mysqli_query($conn, "SELECT * FROM mwp_orders WHERE store_id= 1071945")) {
//         echo "Returned rows are: " . mysqli_num_rows($result);
//         while ($row = mysqli_fetch_assoc($result)) {
//             print_r($row);
//         }
//         }
//     mysqli_close($con);
?>