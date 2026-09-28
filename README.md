# INFORME TÉCNICO DE PROYECTO

**Título del Proyecto:** Simulador CLI de Docker Asistido por Inteligencia Artificial

**Materia/Módulo:** Git & Docker - Clase 4 (Evaluación Práctica Integradora)

**Integrantes del Equipo:** Marcos y María

**Lenguaje de Programación:** Python 3

**Sistema de Control de Versiones:** Git & GitHub

---

## 1. RESUMEN EJECUTIVO

El presente proyecto consiste en el desarrollo colaborativo de un Simulador Interactivo de Línea de Comandos (CLI) para Docker ejecutado en entorno de consola. La herramienta replica el comportamiento interno, la sintaxis y el ciclo de vida de los contenedores Docker mediante comandos base como pull, run, ps, stop, rm y logs.

El desarrollo se gestionó mediante el flujo de trabajo en parejas (Pair Programming) alternando roles de Driver y Navigator, asistido por Modelos de Lenguaje (LLMs) para la aceleración y estructuración de código, y controlado mediante Git con un historial de commits atómicos subidos a un repositorio público en GitHub.

---

## 2. ARQUITECTURA DEL SISTEMA Y TECNOLOGÍA

Para la solución se seleccionó Python 3 debido a su legibilidad, facilidad de manejo de estructuras de datos en memoria (diccionarios y conjuntos) y ejecución directa en terminal sin necesidad de compilación.

### Estructura de Datos Principal:

* **Imágenes (self.images):** Un conjunto (set) que almacena los nombres de las imágenes descargadas en la memoria local.

* **Contenedores (self.containers):** Un diccionario (dict) indexado por un CONTAINER ID único de 6 caracteres alfanuméricos. Cada registro contiene:
  * name: Nombre asignado dinámicamente al contenedor.
  * image: Imagen base utilizada.
  * status: Estado del ciclo de vida (Up o Exited (0)).
  * ports: Puertos mapeados mediante la bandera -p.

---

## 3. PASO A PASO DEL DESARROLLO REALIZADO

### Paso 1: Configuración del Entorno de Trabajo Local

1. Se creó la estructura del proyecto en la carpeta local simulador-docker-cli.
2. Se inicializó el control de versiones local ejecutando git init.
3. Se parametrizó la identidad de los desarrolladores en la máquina de trabajo mediante git config user.name y git config user.email.
4. Se creó el archivo .gitignore para excluir archivos de caché de Python (__pycache__/) evitando subir archivos basura al repositorio.
5. Se creó el archivo README.md con la portada inicial del proyecto.

### Paso 2: Co-Creación Asistida por Inteligencia Artificial (LLM)

Haciendo uso de modelos de lenguaje (Gemini / DeepSeek / Qwen), el rol de Navigator diseñó y aplicó prompts de ingeniería precisa para obtener la lógica base y la validación de reglas:

* **Prompt 1 (Estructura CLI y Núcleo):** Se solicitó un script en Python con un bucle infinito interactivo (while True), un indicador de comandos docker-sim>, la generación de IDs de 6 caracteres y los métodos base para procesar argumentos.

* **Prompt 2 (Validación de Ciclo de Vida y Métodos Adicionales):** Se solicitó la incorporación de las funciones stop, logs y rm, programando la regla estricta de negocio donde un contenedor en estado Up rechaza su eliminación arrojando un mensaje de error.

### Paso 3: Desarrollo Incremental y Control de Commits (Git)

Se aplicó una metodología de integración continua local, realizando commits atómicos a medida que cada funcionalidad era probada y aprobada. El historial registrado refleja la siguiente progresión:

1. chore: configuracion inicial del repositorio y archivos base
2. feat: estructura base del bucle CLI interactivo
3. feat: agregar simulacion de comandos docker pull y docker run
4. feat: implementar comando docker ps y opcion -a
5. feat: agregar docker stop y docker rm con validacion de estado activo
6. feat: integracion de docker logs y actualizacion del README

### Paso 4: Pruebas y Validación de Funcionamiento

Se realizaron pruebas en consola verificando la cobertura total de los comandos exigidos:

* **docker pull:** Generó las líneas simuladas de descarga por capas y el Digest SHA256.
* **docker run:** Registró contenedores con asignación de ID corto y banderas opcionales de puertos (-p).
* **docker ps / -a:** Mostró la tabla alineada con las columnas CONTAINER ID, IMAGE, STATUS, PORTS y NAMES.
* **docker stop:** Cambió de forma efectiva el estado de Up a Exited (0).
* **docker rm:** Se validó que al intentar eliminar un contenedor activo en estado Up arrojara el mensaje: Error response from daemon: You cannot remove a running container.... Al detenerlo previamente con stop, la eliminación se completó de forma correcta.
* **docker logs:** Imprimió correctamente las líneas simuladas de respuesta de servidor.

### Paso 5: Publicación y Sincronización Remota con GitHub

1. Se creó el repositorio público en GitHub denominado simulador-super-vergatario-de-marcos-y-maria-100-real-no-fake-ia-opcional.
2. Se vinculó el repositorio remoto con el proyecto local mediante git remote add origin.
3. Se renombró la rama a main y se realizó la sincronización inicial con git push -u origin main.
4. Ante conflictos de divergencia con la rama remota, se ejecutó la sincronización y resolución mediante git pull origin main --rebase y posterior actualización de documentación.

---

## 4. RESULTADOS Y CONCLUSIONES

* Se logró construir un simulador de consola 100% funcional que cumple de manera estricta con todas las reglas de negocio descritas en la rúbrica del proyecto.
* La metodología de programación en pareja apoyada por IA demostró ser altamente eficiente para reducir los tiempos de desarrollo de la lógica sintáctica.
* El repositorio quedó documentado de forma completa en el archivo README.md con las instrucciones de ejecución, participantes y los prompts utilizados.
