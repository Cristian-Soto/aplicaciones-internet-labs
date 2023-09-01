
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $conn = mysqli_connect('db', 'root', 'test', 'dbname');

    $nombre = $_POST['Nombre'];
    $apellido = $_POST['Apellido'];

    $query = "INSERT INTO personas (Nombre, Apellido) VALUES ('$nombre', '$apellido')";
    $result = mysqli_query($conn, $query);

    if ($result) {
        echo "Registro insertado correctamente.";
    } else {
        echo "Error al insertar el registro: " . mysqli_error($conn);
    }

    mysqli_close($conn);
}
?>
<html>
    <head>
        <title>Aplicaciones de Internet</title>
        <meta charset="utf-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <h1>Aplicaciones de Internet</h1>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                        </tr>
                    </thead>
                    <?php

                        $conn = mysqli_connect('db', 'root', 'test', "dbname");

                        $query = 'SELECT * From personas';
                        $result = mysqli_query($conn, $query);

                        while($value = $result->fetch_array(MYSQLI_ASSOC)){
                            echo '<tr>';
                            echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
                            foreach($value as $element){
                                echo '<td>' . $element . '</td>';
                            }

                            echo '</tr>';
                        }

                        $result->close();
                        mysqli_close($conn);
                    ?>
                    </table>
            </div>
        </div>
        <form action="index.php" method="post">
            <h1>Ingresa tu nombre</h1>
            <input type="text" name="Nombre">
            <h2>Ingresa tu apellido</h2>
            <input type="text" name="Apellido">

            <button type="submit">Enviar</button>

        </form>    
    </body>
</html>
