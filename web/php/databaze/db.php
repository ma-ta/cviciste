<?php
    
    // Připojení k databázi
    
    $host = "localhost";
    $jmeno = "root";
    $heslo = null;
    $databaze = "hrad";
    
    // PDO(mysql:host=localhost;dbname=test;charset=utf8", $user, $pass)
    try {
        $db = new PDO("mysql:host=".$host.";charset=utf8;dbname=".$databaze, $jmeno, $heslo);
        if ($db) {
            echo("<div class='status' style='background-color: #00AA00;'>
                Připojeno k databázi.</div>");
        }
    }
    catch (PDOException $e) {
        echo("<div class='status' style='background-color: #AA0000;'>
            Nepodařilo se připojit k databázi:<br />(".$e->getMessage().").</div>");
        exit;
    }

?>
