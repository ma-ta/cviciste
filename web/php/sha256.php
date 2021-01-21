<?php
if ((isset($_GET["retezec"]) && (!empty($_GET["retezec"])))) {
    $retezec = htmlspecialchars($_GET["retezec"]);
}
else {
    $retezec = "";
}
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
        <title>SHA-256</title>
        <style type="text/css">
            body {
                padding: 0 0 30px 0;
                margin: 0;
                font-size: 14pt;
            }
        </style>
    </head>
    <body>
        <div style="text-align: center; width: 75%; margin: auto;">
        <h1>SHA-256</h1>
        <form action="#" method="get">
            <input autofocus required style="margin-bottom: 30px; padding: 10px; width: calc(100% - 22px); font-size: 120%" type="text" name="retezec" id="retezec" value="<?php echo($retezec) ?>" /><br />
            <input style="font-size: 105%; padding: 10px;" type="submit" value="Potvrdit" />
        </form>
        <?php
        if ((isset($_GET["retezec"]) && (!empty($_GET["retezec"])))) {
            $hash = hash("sha256", $retezec);
            echo("<div style='font-size: 120%; width: calc(100%-24px); word-wrap: break-word; border: 1px solid #00AA00; background-color: #DDFFDD; padding: 10px; margin-top: 30px;'><p>".$retezec.":</p><p style='color: #00AA00; font-weight: bold;'>".$hash."</p></div>");
        }
        ?>
        </div>
    </body>
</html>
