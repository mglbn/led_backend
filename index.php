<!DOCTYPE html>
<html lang="en">
<head>
    <script src="./requests.js"></script>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Led Kontrollzentrum</title>
</head>
<body>
    <?php 
        $effect = $_POST.effekt;
        exec("sudo touch /var/www/html/stop-script")
        if (effect=='rot'){
            exce("sudo python -c 'import mylib; rot()'")
        }
        if (effect=='blau'){
            exce("sudo python -c 'import mylib; blau()'")
        }
        if (effect=='rot'){
            exce("sudo python -c 'import mylib; aus'")
        }
    ?>

    <form action="/index.php" method="post">
        <h2>Farbe einstellen</h2>
        <div>
            <input type="radio" id="rot" name="effekt" value="rot" <?php echo ($effect=='rot')?'checked':''?>>
            <label for="rot">Rot</label>
        </div>
        <div>
            <input type="radio" id="blau" name="effekt" value="blau" <?php echo ($effect=='blau')?'checked':''?>>
            <label for="blau">Blau</label>
        </div>
        <div>
            <input type="radio" id="aus" name="effekt" value="aus" <?php echo ($effect=='aus')?'checked':''?>>
            <label for="ausschalten">Ausschalten</label>
        </div>
        <input type="submit"></input>
    </form>

</body>
</html>