import os


def sanitize_filename(filename):
    """
    Reemplaza los caracteres no permitidos en Windows por guion bajo.
    Caracteres prohibidos en Windows: < > : " / \\ | ? *
    Son exactamente 9 caracteres.
    """
    forbidden_chars = '<>:"/\\|?*'
    for char in forbidden_chars:
        filename = filename.replace(char, "_")
    return filename


# Simular el caso real
original = "Undertale OST： sans Extended"
sanitized = sanitize_filename(original)

print(f"Original:   '{original}'")
print(f"Sanitizado: '{sanitized}'")
print()

# Verificar cada carácter
print("Análisis de caracteres:")
for i, char in enumerate(original):
    code = ord(char)
    in_forbidden = char in '<>:"/\\|?*'
    print(
        f"  [{i:2d}] '{char}' → U+{code:04X} {'⚠️ PROHIBIDO' if in_forbidden else '✓'}"
    )
