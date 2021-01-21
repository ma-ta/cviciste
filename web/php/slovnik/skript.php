<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Skript</title>
</head>
<body>

<?php

include("funkce.php");

$delka_slova = $_POST["delka"];
$soubor = $_POST["zdroj"];
$i = 0;

try {
    if (file_exists($soubor)) {
        $vystup = fopen("vystup.txt", "w");
        $soubor = fopen($soubor, "r");
        echo("<div style='font-family: Consolas, monospace;'><table>");
        
        while(!feof($soubor)) {
           $radek = trim(fgets($soubor));
           
           $delka = mb_strlen($radek, "UTF-8");
           $pocet_ch = pocetCH($radek, "UTF-8");
           $delka -= $pocet_ch;
           
           if ($delka == $delka_slova) {
               $i++;
               fwrite($vystup, mb_convert_case($radek, MB_CASE_TITLE, "UTF-8").PHP_EOL);
               echo("<tr><td>".$radek."</td><td style='padding-left: 20px;'>zn.: ".$delka." | pol. ".$i." | CH: ".$pocet_ch."x</td></tr>");
           }
        }
        fclose($soubor);
        fclose($vystup);
        echo("</table></div>");
        echo("<p style='font-size: 14pt; font-family: Verdana; background-color: #F0F0F0; border: 1px solid #D0D0D0; padding: 20px;'><strong>HOTOVO</strong><br />Počet výskytů: ".$i."</p>");
    }
    else {
        echo("Soubor neexistuje");
    }
}
catch(Exception $e) {
    echo("Něco se nezdařilo:<br />".$e->Message);
}

?>

</body>
</html>
