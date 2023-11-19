import gradio as gr
from langchain.llms import Ollama

# Crie uma instância do Ollama
ollama = Ollama(base_url='http://localhost:11434', model="metalurgico")

# Verifique a documentação da biblioteca para confirmar o método correto
def ollama_response(message, history):
    # Substitua 'generate_response' pelo método correto se necessário
    response = ollama.generate_response(message)

    # Concatene as partes da resposta e retorne
    generated_response = ''.join(chunk['text'] for chunk in response['choices'][0]['text'])
    return generated_response

# Crie uma instância da interface de chat Gradio com a função do Ollama
demo = gr.ChatInterface(ollama_response)

# Lance a interface de chat
demo.launch()
