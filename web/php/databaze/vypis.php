<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="normalize.css" />
    <link rel="stylesheet" type="text/css" href="style.css" />
    <title>Výpis databáze</title>
</head>
<body>
    <?php
        include('db.php');
        define("TABULKA", "zajemci");
    ?>
    
    <br />
    <div id="obsah">
        
    <button onclick="location.reload()">Obnovit</button>
    <br />
    
    <h1>Výpis databáze<?php echo(" <em>".$databaze."</em>"); ?></h1>
    <table>
        <caption><?php echo("<em>".TABULKA."</em>"); ?></caption>
        <tr>
            <th>ID</th>
            <th>Datum registrace</th>
            <th>Jméno</th>
            <th>E-mail</th>
            <th>Telefon</th>
            <th>Profil</th>
            <th>Zpráva</th>
            <th>Částka</th>
            <th>IP adresa</th>
            <th>Referer</th>
            <!--<th>Heslo</th>
            <th>Souhlas</th>-->
        </tr>
        
        <?php
        $sql_dotaz = "SELECT * FROM ". TABULKA . " ORDER BY id DESC";
        $sql_vysledek = $db->prepare($sql_dotaz);
        $sql_vysledek->execute();
        
        foreach (($sql_vysledek->fetchAll(PDO::FETCH_ASSOC)) as $radek) {
            echo("<tr>");
            $i = 0;
            foreach ($radek as $sloupecek) {
                echo("<td id='td".++$i."'>" . nl2br(htmlspecialchars($sloupecek)) . "</td>");
            }
            echo("</tr>");
        }
        ?>
    </table>
        
    </div>
</body>
</html>
