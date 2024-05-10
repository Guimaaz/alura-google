#!pip install -q -U google-generativeai

import google.generativeai as genai


#implementando minha api key
GOOGLE_API_KEY="Inserir a api key aqui"
genai.configure(api_key=GOOGLE_API_KEY)

#listar modelos 
# for i in genai.list_models():
#     if 'generateContent' in i.supported_generation_methods:
#         print(i.name)

#config

Config = {
  "candidate_count": 1,
  "temperature": 1,
}

config_seguranca=[
   
     {
    "category": "HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HATE",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "SEXUAL",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "DANGEROUS",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },

]
    

model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    generation_config=Config,
    safety_settings=config_seguranca
     )

#pergunta chumbada
# response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
# print(response.text)

chat = model.start_chat(history=[])
prompt = input('Olá, você está em um ChatBot!, para encerrar esta conversa digite \"Fim\", caso contrario estarei ao seu dispor\nComando: ')

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n')
  prompt = input('Comando: ')
