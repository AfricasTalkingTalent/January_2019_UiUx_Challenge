<!DOCTYPE html>
<html>
<head>
    <title>Verification Process</title>
    <script src="dist/sweetalert.min.js"></script>
    <link rel="stylesheet" type="text/css" href="dist/sweetalert.css">
</head>
<body>
    <?php
    session_start();

    session_destroy();

?>
    <div>
        <img src="images/success.gif">
        <h1>SignUp was Successful</h1>
    </div>

</body>
</html>
