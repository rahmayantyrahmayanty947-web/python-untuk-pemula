import sys

print("Versi Python:", sys.version.split()[0])
print("Berjalan di venv:", sys.prefix != sys.base_prefix)