<?php
// Ejecuta como root, el script python encargado de controlar el sensor ultrasonido
echo exec('sudo python3 /var/www/html/cinematik/python/calcular_v9.py');
// La salida la imprime con el echo
?>
