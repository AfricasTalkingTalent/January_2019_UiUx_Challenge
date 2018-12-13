<!DOCTYPE html>
<html>
<head>
	<title>Verification Process</title>
	 <script src="dist/sweetalert.min.js"></script>
    <link rel="stylesheet" type="text/css" href="dist/sweetalert.css">
</head>
<body>
 <?php
require "DBConnect.php";
global $db;

    $code = $_POST['vcode'];
    $id = $_POST['id'];

 $key = 'wejsgbvnb78sgvxc8FYY68JSD6xvxv';
 $token = crypt($code, $key);

    $sql= "SELECT * FROM `user` WHERE `userName`='$id'";
    $result = mysqli_query($db,$sql);

    while ($row = mysqli_fetch_array($result)) {
        $res = $row['verificationToken'];
 
 if ($res == $token) {
     
     ?> 
        <script>
            swal({
                title: "Success",
                type: "success",
                timer: 1500,
                showConfirmButton: false
            });
            setTimeout(function () {
                location.href = "success.php"
            }, 1000);
        </script>
             <?php
}
else{
             ?>
     <script>
         swal({
             title: "Verification Fail",
             type: "error",
             timer: 1500,
             showConfirmButton: false
         });
         setTimeout(function () {
             location.href = "index.php"
         }, 1000);
     </script>
     <?php
 }
    }

?>



</body>
</html>
