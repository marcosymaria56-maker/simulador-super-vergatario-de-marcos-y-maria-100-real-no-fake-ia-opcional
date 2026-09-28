import random
import string
import sys
import time


class DockerSimulator:

  def __init__(self):
    self.images = set()  # Almacena nombres de imágenes descargadas
    self.containers = {}  # ID -> dict(name, image, status, ports)

  def generate_id(self):
    """Genera un Hash ID corto único de 6 caracteres hex/alfanumerico"""
    return ''.join(random.choices(string.hexdigits.lower()[:16], k=6))

  def docker_pull(self, args):
    if not args:
      print('Error: Debe especificar el nombre de una imagen.')
      return
    image_name = args[0]
    print(f'Using default tag: latest')
    print(f'latest: Pulling from library/{image_name}')
    layers = ['a3ed95ca0b1e', '12c82960a631', '4f4fb700ef54']
    for layer in layers:
      print(f'{layer}: Pulling fs layer...')
      time.sleep(0.3)
      print(f'{layer}: Pull complete')
    digest = self.generate_id() + self.generate_id()
    print(f'Digest: sha256:{digest}...')
    print(f'Status: Downloaded newer image for {image_name}:latest')
    self.images.add(image_name)

  def docker_run(self, args):
    if not args:
      print('Error: Debe especificar una imagen para ejecutar.')
      return

    ports = "N/A"
    image_name = None

    # Parseo de opciones (-p)
    idx = 0
    while idx < len(args):
      if args[idx] == '-p' and idx + 1 < len(args):
        ports = args[idx + 1]
        idx += 2
      else:
        image_name = args[idx]
        idx += 1

    if not image_name:
      print('Error: Debe especificar el nombre de la imagen.')
      return

    # Auto-pull si la imagen no existe en memoria
    if image_name not in self.images:
      print(f"Unable to find image '{image_name}:latest' locally...")
      self.docker_pull([image_name])

    container_id = self.generate_id()
    container_name = f'focused_{self.generate_id()[:4]}'

    self.containers[container_id] = {
        'name': container_name,
        'image': image_name,
        'status': 'Up',
        'ports': ports,
    }
    print(container_id)

  def docker_ps(self, args):
    # Detecta la opción -a en cualquiera de sus posiciones
    show_all = any(arg == '-a' or arg == '-all' for arg in args)

    print(
        f"{'CONTAINER ID':<15} {'IMAGE':<15} {'STATUS':<15} {'PORTS':<15}"
        f" {'NAMES':<15}"
    )
    print('-' * 75)

    for cid, info in self.containers.items():
      # Si no se incluyó -a y el contenedor no está activo (Up), se ignora
      if not show_all and not info['status'].startswith('Up'):
        continue

      status_str = info['status']
      if status_str == 'Up':
        status_str = 'Up 2 minutes'
      elif status_str == 'Exited':
        status_str = 'Exited (0)'

      print(
          f"{cid:<15} {info['image']:<15} {status_str:<15}"
          f" {info['ports']:<15} {info['name']:<15}"
      )

  def _find_container(self, target):
    """Busca un contenedor por su ID (exacto o prefijo) o por su Nombre"""
    # 1. Búsqueda por ID exacto
    if target in self.containers:
      return target

    # 2. Búsqueda por Nombre exacto
    for cid, info in self.containers.items():
      if info['name'] == target:
        return cid

    # 3. Búsqueda por coincidencia parcial de ID (si el usuario escribe los primeros caracteres)
    for cid in self.containers:
      if cid.startswith(target):
        return cid

    return None

  def docker_stop(self, args):
    if not args:
      print('Error: Debe especificar ID o Nombre del contenedor.')
      return
    target = args[0]
    cid = self._find_container(target)
    if not cid:
      print(f'Error: No such container: {target}')
      return

    self.containers[cid]['status'] = 'Exited'
    print(target)

  def docker_rm(self, args):
    if not args:
      print('Error: Debe especificar ID o Nombre del contenedor.')
      return
    target = args[0]
    cid = self._find_container(target)
    if not cid:
      print(f'Error: No such container: {target}')
      return

    # Regla: Si está en ejecución (Up), genera un error
    if self.containers[cid]['status'].startswith('Up'):
      print(
          f'Error response from daemon: You cannot remove a running container'
          f' {cid}. Stop the container before attempting removal.'
      )
      return

    del self.containers[cid]
    print(target)

  def docker_logs(self, args):
    if not args:
      print('Error: Debe especificar ID o Nombre del contenedor.')
      return
    target = args[0]
    cid = self._find_container(target)
    if not cid:
      print(f'Error: No such container: {target}')
      return

    img = self.containers[cid]['image']
    print(f'[INFO] Initializing server logs for container {cid} ({img})...')
    print(f'[INFO] Server started on port 80...')
    print(f'[GET] /index.html 200 OK - 12ms')
    print(f'[POST] /api/v1/login 200 OK - 45ms')
    print(f'[INFO] Connection accepted from client 192.168.1.5')

  def run_cli(self):
    print('=== Simulador CLI de Docker (Escriba "exit" para salir) ===')
    while True:
      try:
        raw_input = input('docker-sim> ').strip()
        if not raw_input:
          continue
        if raw_input.lower() in ['exit', 'quit']:
          break

        tokens = raw_input.split()
        if tokens[0] != 'docker':
          print(f"Comando no reconocido: {tokens[0]}. Use 'docker ...'")
          continue

        if len(tokens) < 2:
          print('Uso: docker [comando] [opciones]')
          continue

        command = tokens[1]
        args = tokens[2:]

        if command == 'pull':
          self.docker_pull(args)
        elif command == 'run':
          self.docker_run(args)
        elif command == 'ps':
          self.docker_ps(args)
        elif command == 'stop':
          self.docker_stop(args)
        elif command == 'rm':
          self.docker_rm(args)
        elif command == 'logs':
          self.docker_logs(args)
        else:
          print(f'docker: "{command}" is not a docker command.')

      except KeyboardInterrupt:
        print('\nSaliendo...')
        break


if __name__ == '__main__':
  sim = DockerSimulator()
  sim.run_cli()
