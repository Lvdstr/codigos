def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Exemplo de uso
hex_color = input("digite a cor em hex + o #:")
rgb_color = hex_to_rgb(hex_color)
print(f"A cor hexadecimal {hex_color} em RGB é: {rgb_color}")
