
class ChatBot:
	def chat(self, mensagem):
		resposta = "Resposta nao tratada"
		if "ola" in mensagem.lower():
			resposta = "ola "

		elif "não" in mensagem.lower():
			resposta = "você está negando algo"

		elif "sim" in mensagem.lower():
			resposta = "você está afirmando algo"


		return resposta