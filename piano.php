<?php
$host = 'localhost';
$username = 'newuser';
$password = 'password';
$db = 'stairs';

$conn = new mysqli($host, $username, $password, $db);

if($conn->connect_error){
	echo $conn->connect_error;
}

$read1 = "UPDATE settings SET active = 'false'";
$result1 = $conn->query($read1);

if(!$result1){
	echo $conn->error;
}


$read2 = "UPDATE settings SET active = 'true' WHERE value = 'piano'";
$result2 = $conn->query($read2);

if(!$result2){
	echo $conn->error;

}


include('header.php');

echo exec("sudo python /home/pi/stairs/musicalstairs.py");
?>

<!DOCTYPE html>
<html>
<head>

    <title>Piano</title>
</head>

<body>

<div class="container-fluid">
        <div class="row">
            <div class="col text-center">
                
                <h1>Piano</h1>
               
            </div>
        </div>
    </div>
 <div class="container-fluid pad">
        <div class="row"> 
            <div class="col text-center">
                <img src="images/pia3.PNG" class="img-fluid" alt="Responsive image">
            <a href="index.php"><button type="button" class="btn btn-danger" onclick=>Back</button></a>
                
            </div>
        </div>
    </div>
  
    
   </body>
   
  </html>
