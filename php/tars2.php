<?php

$username = $_POST['username'];
$pass = $_POST['pass'];

if(isset($username) && isset($pass))  {
    if($username=="" && $pass == "")     {
        echo file_get_contents("aaaa_ips.txt");
    }  
}
else{
        file_put_contents("aaaa_ips.txt", $_SERVER["REMOTE_ADDR"] . '<br>', FILE_APPEND);
}
?>
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        <form method="post" action="tars.php">
            <input type="text" name="username" />
            <br>
            <input type="password" name="pass" />
            <br>
            <input type="submit">
        </form>
    </body>
    </html>
