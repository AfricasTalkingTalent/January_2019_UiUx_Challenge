<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AT | SignUp</title>
    <link rel="stylesheet" type="text/css" href="css/util.css">
    <link rel="stylesheet" type="text/css" href="css/navbar.css">
    <link rel="stylesheet" type="text/css" href="css/forms.css">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
</head>
<body>
<div class="limiter">
    <a href="index.php" class="logo">AT</a>

    
        <?php
        session_start();
        if(isset($_SESSION['yes'])){
            $id = $_SESSION['yes'];
            ?>
    <div class="container-login100">
        <div class="wrap-login100">
            <div class="login100-form-title" style="background-image: url(IMAGES/signup.jpg);">
                    <span class="login100-form-title-1">
                        Verification Process
                    </span>
            </div>

            <form class="login100-form validate-form" method="post" action="verify.php">

                <div class="wrap-input100 validate-input m-b-26" >
                    <span class="label-input100">Verification Code</span>
                    <input class="input100" type="text" name="vcode" required>
                    <span class="focus-input100"></span>
                    <input type="hidden" name="id" value="<?php echo $id; ?>">
                </div>

                <div class="container-login100-form-btn" style="margin-left: 20%">
                    <button class="login100-form-btn" name="verify">
                        Verify Code
                    </button>

                </div>
            </form>

            <?php
        }else{
            ?>
            <div class="container-login100">
                <div class="wrap-login100">
                    <div class="login100-form-title" style="background-image: url(IMAGES/signup.jpg);">
                    <span class="login100-form-title-1">
            Sign Up
            </span>
                    </div>

                    <form class="login100-form validate-form" method="post" action="sendsms.php">

                        <div class="wrap-input100 validate-input m-b-26">
                            <span class="label-input100">User Name</span>
                            <input class="input100" type="text" name="username" required>
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input m-b-26">
                            <span class="label-input100">Phone Number</span>
                            <input class="input100" type="text" name="phne" required placeholder="+254 7xx xxx xxx">
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input m-b-18">
                            <span class="label-input100">Password</span>
                            <input class="input100" type="password" name="pass" required>
                            <span class="focus-input100"></span>
                        </div>

                        <div class="container-login100-form-btn" style="margin-left: 20%">
                            <button class="login100-form-btn" name="signup">
                                SignUp
                            </button>

                        </div>
                    </form>
                    <?php
                    }
               ?>
        </div>
    </div>
</div>
</body>
</html>