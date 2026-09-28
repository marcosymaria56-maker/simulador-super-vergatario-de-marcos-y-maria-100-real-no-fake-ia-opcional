# Simulador CLI de Docker Asistido por IA

## Integrantes
- Integrante 1  Marcos Adrianza (Driver / Navigator)
- Integrante 2 Maria luzardo (Navigator / Driver)

## Instrucciones de Ejecución
Para ejecutar el simulador localmente, asegúrate de tener Python 3 instalado y ejecuta:

```bash
python main.py

## luego pon los siguientes comandos

docker pull [imagen]

docker run [-p puerto:puerto] [imagen]

docker ps y docker ps -a

docker stop [ID/Nombre]

docker rm [ID/Nombre]

docker logs [ID/Nombre]

## Prompts Utilizados con la IA

Prompt 1 (Estructura y Lógica General)
"Actúa como desarrollador senior en Python. Escribe un script que mantenga un bucle interactivo de consola simulando 'docker'. Necesita una estructura de datos que almacene los contenedores creados con ID de 6 caracteres, Nombre, Imagen y Estado ('Up' o 'Exited'). Implementa los comandos 'run' y 'ps'."

Prompt 2 (Validación de Ciclo de Vida y Reglas de Negocio)
"Modifica la clase del simulador para agregar los comandos 'stop', 'rm' y 'logs'. Implementa la regla estricta: si un contenedor está en estado 'Up', el comando 'rm' debe fallar mostrando un mensaje de error indicando que debe detenerse primero."