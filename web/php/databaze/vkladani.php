<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="normalize.css" />
    <link rel="stylesheet" type="text/css" href="style.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <title>Práce s databází</title>
    
    <script>
        $(document).ready(function(){
            
        });
    </script>

</head>

<body>

<?php
include("db.php");
include("funkce.php");
?>

<div id="obsah">
    
    <h1>Vpisování do databáze</h1>

    <?php
    if(isset($_POST["potvrdit"])) {
        if((!empty($_POST["jmeno"])) && (!empty($_POST["email"])) && (isset($_POST["souhlas"]))) {
            
            //deklarace
            $jmeno = "";
            $email = "";
            $telefon = "";
            $profil = "";
            $heslo = nahodnyRetezec(10);
            $castka = null;
            $zprava = "";
            $souhlas = "";
            $ip = zjistiIP();
            
            $jmeno = htmlspecialchars(trim(chop($_POST["jmeno"])));
            $email = htmlspecialchars(trim(chop($_POST["email"])));
            
            if(isset($_POST["tel"]))
                $telefon = htmlspecialchars(trim(chop($_POST["telefon"])));
            
            if(isset($_POST["profil"]))
                $profil = htmlspecialchars(trim(chop($_POST["profil"])));            
            
            if(isset($_POST["castka"]))
                $castka = htmlspecialchars($_POST["castka"]);
            
            if(isset($_POST["zprava"]))
                $zprava = htmlspecialchars(trim(chop($_POST["zprava"])));
            
            if(isset($_POST["souhlas"]))
                $souhlas = $_POST["souhlas"];

            switch($souhlas) {
                case "on":
                    $souhlas = 1;
                    break;
                default:
                    $souhlas = 0;
            }
            
            $hashHesla = hash("sha256", $heslo);
            
            $sql_dotaz = "INSERT INTO uzivatele (jmeno, email, telefon, profil, heslo, castka, zprava, souhlas, ip) 
                VALUES (:jmeno, :email, :telefon, :profil, :heslo, :castka, :zprava, :souhlas, :ip)";
            $sql_vysledek = $db->prepare($sql_dotaz);
            $sql_vysledek->execute( array( ":jmeno"=>$jmeno, ":email"=>$email, ":telefon"=>$telefon, ":profil"=>$profil, ":heslo"=>$hashHesla, 
                ":castka"=>$castka, ":zprava"=>$zprava, ":souhlas"=>$souhlas, ":ip"=>$ip) );
        
            echo("<div style='padding: 15px; margin-bottom: 20px; background-color: #DDFFDD'><p class='hotovo' style='color: #00AA00; text-transform: uppercase;'><strong>Dokončeno</strong></p>
                <p class='hotovo'>Opište si prosím své heslo:&nbsp;<span style='font-weight: bold; text-decoration: underline; color: #00AA00; margin-left: 3px; margin-right: 3px;'>".$heslo."</span>!</p></div>");
            
            //zamezení opětovného odeslání
            /*$cesta = substr($_SERVER["PHP_SELF"], 0, strrpos($_SERVER["PHP_SELF"], "/"));
            header("Location: http://$_SERVER[SERVER_NAME]$cesta/vkladani.php", true, 303);*/
        }
        else {
            echo("<div style='padding: 15px; margin-bottom: 20px; background-color: #FFDDDD'><p class='hotovo' style='color: #AA0000;'><strong>Nevyplnili jste všechny potřebné údaje.</strong></p></div>");
        }
    }
    ?>

    <form action="#" method="post" id="zadavani" name="zadavani">
        <table>
            <tr>
                <td><label for="jmeno">Jméno, sdružení, strana<span class="poznamka">*</span>:</label></td>
                <td><input type="text" name="jmeno" id="jmeno" maxlength="200" required autofocus /></td>
            </tr>
            <tr>
                <td><label for="email">Kontaktní e-mail<span class="poznamka">*</span>:</label></td>
                <td><input type="email" name="email" id="email" value="@" placeholder="@" maxlength="200" required /></td>
            </tr>
            <tr>
                <td><label for="telefon">Telefon:</label></td>
                <td><input type="tel" name="telefon" id="telefon" value="+420" placeholder="+420123456789" maxlength="13" /></td>
            </tr>
            <tr>
                <td><label for="profil">Web (volební program):</label></td>
                <td><input type="text" name="profil" id="profil" maxlength="200" /></td>
            </tr>
            <tr>
                <td><label for="castka">Rámcová nabídka (CZK):</label></td>
                <td><input type="number" name="castka" id="castka" min="0" /></td>
            </tr>
            <tr>
                <td><label for="zprava">Zpráva:</label></td>
                <td><textarea name="zprava" id="zprava"></textarea></td>
            </tr>
            <tr>
                <td><label for="souhlas">Souhlasím s podmínkami<span class="poznamka">*</span>:</label></td>
                <td><input style="width: auto;" type="checkbox" name="souhlas" id="souhlas"  /></td>
            </tr>
            <tr>
                <td>Bezpečnostní prvek<span class="poznamka">*</span>:</td>
                <td></td>
            </tr>
            <tr>
                <td colspan="2"><input style="width: 100%;" type="submit" name="potvrdit" id="potvrdit" value="Potvrdit" /></td>
            </tr>
            <tr>
                <td colspan="2"><span class="poznamka">* Značí povinnou položku</span></td>
            </tr>
        </table>
    </form>

</div>

</body>

</html>
