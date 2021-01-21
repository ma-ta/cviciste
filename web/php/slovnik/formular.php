<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Skript</title>
    <style>
        body {
            font-family: Verdana, Arial, sans-serif;
            margin: 50px;
            padding: 0;
        }
        form {
            width: 50%;
            min-width: 200px;
            margin: auto;
            background-color: #FAFAFA;
            border: 1px solid #CACACA;
            font-size: 14pt;
            padding: 20px;
        }
        form input {
            font-size: 14pt;
            width: 100%;
            text-align: center;
        }
        form input[type="file"] {
            text-align: left;
            width: 100%;
        }
        form select {
            height: 50px;
            width: 100%;
            padding: 10px;
            font-size: 14pt;
            text-align: center;
        }
        form input[type="submit"] {
            height: 50px;
        }
    </style>
</head>
<body>
<form action="skript.php" method="post" name="formular1" id="formular1">
    <h2>Výběr slov se zadanou délkou</h2>
    <label for="zdroj">Zdrojový soubor:</label><br />
    <input id="zdroj" type="file" name="zdroj" required />
    <br /><br />
    <label for="delka">Délka slova:</label><br />
    
    <select id="delka" name="delka" required >
    <?php
        for ($i = 1; $i <= 100; $i++) {
            echo("<option value=\"".$i."\">".$i."</option>\n");
        }
    ?>
    </select>

    <br /><br />
    <input type="submit" value="Spustit" />
</form>
</body>
</html>
