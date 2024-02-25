from pathlib import Path

carpeta = Path('/Users/karenperalta/Desktop/prueba/hola.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.exists())

base = Path.home()
guia = Path(base,"Spain", Path("Barcelona", "Camp Nou"))
print(guia.parent.parent.parent)

guia = Path('/Users/karenperalta/Desktop/prueba/Europa')
for txt in guia.glob("*.txt"):
    print(txt)
print()
for txt in guia.glob("**/*.txt"):
    print(txt)