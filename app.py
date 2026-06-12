def enviar_prompt(prompt):
    return f"Resposta simulada: {prompt}"

if __name__ == "__main__":
    texto = input("Digite algo: ")
    print(enviar_prompt(texto))