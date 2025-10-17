def sanitize_filename(filename):
    """
    Reemplaza los caracteres no permitidos en Windows por guion bajo.
    Caracteres prohibidos: < > : " / \ | ? *
    """
    forbidden_chars = '<>:"/\\|?*'
    for char in forbidden_chars:
        filename = filename.replace(char, "_")
    return filename


# Pruebas
test_cases = [
    "Undertale OST： sans Extended",
    "archivo<prueba>test",
    "path/to/file",
    "pregunta?respuesta",
    "pipe|symbol",
    "normal_filename",
    'comillas"dobles',
    "asterisco*test",
]

print("Pruebas de sanitización:\n")
for original in test_cases:
    sanitized = sanitize_filename(original)
    if original != sanitized:
        print(f"❌ '{original}'")
        print(f"✅ '{sanitized}'")
    else:
        print(f"✓ '{original}' (sin cambios)")
    print()
