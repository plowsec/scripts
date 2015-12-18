<?php 
    
    if(isset($_POST['file_content']))   {

        $filename = date("d-m-y") + "_" + bin2hex(mcrypt_create_iv(22, MCRYPT_DEV_URANDOM));

        file_put_contents($filename, $_POST['file_content']);
    }

    else    {
        echo "<p>403 Forbidden</p>";
    }

?>
