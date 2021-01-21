<?php

function pocetCH($vstup, $kodovani) {
    
    mb_internal_encoding($kodovani);
    
    $string = mb_strtoupper($vstup);
                                                //echo("<strong>vstup = $vstup</strong><br />");
                                                //echo("string = $string<br /><br />");
    $pocet_ch = 0;
                                                //$i = 0;

    while (mb_strlen($string) > 0) {
                                                //$i++;
                                                //echo("<strong>$i.</strong><br />");

        $poz_c = mb_strpos($string, "C");
                                                //echo("poz_c: $poz_c<br />");
    
        if ($poz_c !== false) {
        
            $poz_h = mb_strpos($string, "H");
                                                //echo("poz_h: $poz_h<br />");
            if ($poz_h == $poz_c + 1) {
                                                //echo("nalezeno CH<br />");
                $pocet_ch++;
                                                //echo("pocet_ch = $pocet_ch<br />");
                $string = mb_substr($string, $poz_h+1);
                                                //echo("string = $string<br />");
            }
            else {
                $string = mb_substr($string, $poz_c+1);
                                                //echo("žádné CH<br />");
                                                //echo("string = $string<br />");
            }
        
        }
        else {
            return $pocet_ch;
        }
    }
    return $pocet_ch;

}

?>
