<?php
$host = 'localhost';
$username = 'newuser';
$password = 'password';
$db = "stairs";

$conn = new mysqli($host, $username, $password, $db);

if($conn->connect_error) {
	echo $conn->connect_error;

}

$read = "UPDATE settings SET active = 'false'";
$result = $conn->query($read);

if(!$result){
	echo $conn->error;
}



include('header.php');
?>

<!DOCTYPE html>
<html>
<head>


    <title>Magic Stairs</title>
</head>

<body>

<div class="container-fluid">
        <div class="row">
            <div class="col text-center">
                
                <h1>Welcome to Magic Stairs!</h1>
               
            </div>
        </div>
    </div>

    <div class="container-fluid">
        <div class="row">
            <div class="col text-center">
                
                <h4>Please choose a setting...</h4>
               
            </div>
        </div>
    </div>

    <div class="container-fluid pad">
        <div class="row">
            <div class="col text-center">
                <img src="images/pia3.PNG" class="img-fluid" alt="Responsive image">
            <a href="piano.php"><button type="button" class="btn btn-danger" onclick=>Piano</button></a>
                
            </div>
        </div>
    </div>

    <div class="container-fluid pad">
        <div class="row">
            <div class="col text-center">
            <img src="images/drum1.png" class="img-fluid" alt="Responsive image">
            <a href="drum.php"><button type="button" class="btn btn-danger" onclick=>Drums</button></a>
            </div>
        </div>
    </div>

    <div class="container-fluid pad">
        <div class="row">
            <div class="col text-center">
            <img src="images/xy1.png" class="img-fluid" alt="Responsive image">
	    <a href="xylophone.php"><button type="button" class="btn btn-danger">Xylophone</button></a>
            </div>
        </div>

    </div>


</body>

</html>
