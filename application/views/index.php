<?php defined('BASEPATH') or exit('No direct script access allowed');?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Jenga</title>

    <?php
        $base = 'assets/css/';
        $codebase = 'vendor/codebase/css/';
        $styles = array(
            $codebase.'codebase.min.css',
            $codebase.'earth.min.css',
            $base.'main.css'
        );
        foreach($styles as $style){
            echo link_tag($style);
        }
    ?>

</head>
<body>
    <!-- Page content -->
<main id="main-container">
    <div class="wrapper d-flex">
        <div class="left d-flex justify-content-center flex-column align-items-center">
            <h1 class="display-2 text-primary">Jenga</h1>
            <h2 class="display-4 font-size-md text-white">The new builders in town</h2>
        </div>
        <div class="right">
            <ul class="nav nav-tabs nav-tabs-block d-none" data-toggle="tabs" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" href="#signup_content">Signup</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#verification_content">Token</a>
                </li>
            </ul>

            <div class="block-content tab-content overflow-hidden">
                <!-- Signup tab -->
                <div class="tab-pane fade fade-right show active" id="signup_content" role="tabpanel">
                    <div class="content content-full pt-20">
                        <h4 class="font-w400 text-primary">Create a new account</h4>
                        <form  action="<?= base_url('main/signup_process');?>" class="signup_form" method="post">
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material">
                                        <input type="text" class="form-control" id="fname" name="fname" required>
                                        <label for="fname">First Name</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material">
                                        <input type="text" class="form-control" id="lname" name="lname" required>
                                        <label for="lname">Last Name</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material input-group">
                                        <div class="input-group-append">
                                            <span class="input-group-text">
                                                +254
                                            </span>
                                        </div>

                                        <input type="text" class="form-control" id="phone_number" name="phone_number" required>
                                        <label for="phone_number">Phone number</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material">
                                        <input type="password" class="form-control" id="pass" name="pass" required>
                                        <label for="pass">Password</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material">
                                        <input type="password" class="form-control" id="pass-conf" name="pass-conf" required>
                                        <label for="pass-conf">Password Confirmation</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="custom-control custom-checkbox">
                                        <input type="checkbox" class="custom-control-input" id="terms" name="terms" required>
                                        <label class="custom-control-label" for="terms">I agree to Terms &amp; Conditions</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <button type="submit" class="btn btn-sm btn-hero btn-alt-success">
                                    <i class="fa fa-plus mr-10"></i> Create Account
                                </button>
                            </div>
                        </form>
                    </div>                    
                </div>
                <!-- END Signup tab -->

                <!-- Verification tab -->
                <div class="tab-pane fade fade-right" id="verification_content" role="tabpanel">
                    <div class="content content-full pt-20">
                        <h4 class="font-w400 text-primary">Verify account creation</h4>
                        <!-- Primary Alert -->
                        <div class="alert alert-primary" role="alert">
                            <h3 class="alert-heading font-size-h4 font-w400">Authorization code</h3>
                            <p class="mb-0">A message has been sent to <span><?php if($this->session->phone_number) echo $this->session->phone_number;?></span> <br>
                                Didn't get message? <a class="alert-link text-info" href="javascript:void(0)" id="resend_token">Resend</a> <br>
                            </p>
                        </div>
                        <!-- END Primary Alert -->
                        <form action="<?= base_url('main/validate_auth_token');?>" id="auth_token_form" method="post">
                            <div class="form-group row">
                                <div class="col-12">
                                    <div class="form-material">
                                        <input type="text" class="form-control" id="auth_token" name="auth_token" required>
                                        <label for="auth_token">Enter code sent</label>
                                    </div>
                                </div>
                            </div>

                            <div class="form-group">
                                <button type="submit" class="btn btn-sm btn-hero btn-alt-success">
                                    <i class="fa fa-check mr-10"></i> Verify
                                </button>
                            </div>
                        </form>


                    </div>
                </div>
                <!-- END Verification tab -->
            </div>
        </div>
    </div>
</main>
    <!-- END page content -->
    <!-- Footer -->
<?php
    $codebase_script = 'vendor/codebase/js/';
    $base_js = 'assets/js/';
    $scripts = array(
        $codebase_script.'codebase.core.min.js',
        $codebase_script.'plugins/masked-inputs/jquery.maskedinput.min.js',
        $codebase_script.'plugins/jquery-validation/jquery.validate.min.js',
        $codebase_script.'plugins/jquery-validation/additional-methods.min.js',
        $codebase_script.'plugins/bootstrap-notify/bootstrap-notify.min.js',
        $codebase_script.'codebase.app.min.js',
        $base_js.'core.js',
        $base_js.'main.js'
    );
?>
    <script>
        var baseURL = '<?= base_url();?>';
    </script>
    <?php foreach($scripts as $script):?>
        <script src="<?= $script?>"></script>
    <?php endforeach; ?>
    <!-- END Footer -->
</body>
</html>