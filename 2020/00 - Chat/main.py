import random
import string

from chat.bot import ChatBot

arquivoLog = "log.txt"


def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


nomeBot = randomString(8)

class Chat(object):
	def __init__(self):
		mensagem = "msg incial"

	def PegarMensagem(self):
		self.mensagem = input()
		self.resposta = ChatBot().chat(str(self.mensagem))
		print(self.resposta)

		self.SalvarMensagem(">>>"+str(self.mensagem))
		self.SalvarMensagem("<<<"+str(self.resposta))


	def SalvarMensagem(self, mensagem):
		f = open(arquivoLog, "+a")
		f.write(mensagem+"\n")
		f.close()
		
print("Converse com " + randomString(8))
while (True):
	chat = Chat()
	chat.PegarMensagem()

	if chat.mensagem == "sair":
		break
