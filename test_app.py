from app import enviar_prompt

def test_envio():
    resposta = enviar_prompt("Olá")
    assert resposta is not None

def test_retorno_string():
    resposta = enviar_prompt("Teste")
    assert isinstance(resposta, str)