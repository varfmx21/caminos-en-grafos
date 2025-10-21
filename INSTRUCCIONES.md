# Instrucciones para Configurar el Entorno Virtual

## 1. Crear el entorno virtual

```bash
python3 -m venv env
```

## 2. Activar el entorno virtual

### En Linux/macOS:
```bash
source env/bin/activate
```

### En Windows:
```bash
env\Scripts\activate
```

## 3. Instalar los paquetes desde requirements.txt

```bash
pip install -r requirements.txt
```

## 4. Ejecutar el script de visualización

```bash
python visualizar_grafo.py
```

## 5. Desactivar el entorno virtual

Cuando termines de trabajar:

```bash
deactivate
```

---

## Resumen de Comandos (Linux/macOS - zsh)

```bash
# Crear entorno
python3 -m venv env

# Activar
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python visualizar_grafo.py

# Desactivar
deactivate
```

---

## Notas adicionales

- El entorno virtual `env/` no debe subirse a Git (agrégalo al `.gitignore`)
- Las imágenes generadas se guardarán como `Grafo_Dirigido.png` y `Grafo_No_Dirigido.png`
- Si necesitas agregar más paquetes: `pip install <paquete>` y luego `pip freeze > requirements.txt`
