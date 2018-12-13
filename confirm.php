<?php
    session_start();

    extract($_POST);

    // $confirmation_code extracted from $_POST
    if ($confirmation_code == $_SESSION['confirmation_code']) {
       // success
        echo "SUCCESSFULLY SIGNED UP!";
    }else {
        echo "OOPS! CONFIRMATION FAILED";
    }

    session_abort();
?>
