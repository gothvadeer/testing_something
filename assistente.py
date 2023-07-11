from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from os import system

class Comandos:
    def assistente_ouvir(self):
        rec = Recognizer()
        with Microphone() as source:
            print('Fale...')
            rec.pause_threshold = 0.6
            audio = rec.listen(source)
            try:
                print('Reconhecendo voz...')
                palavras = (rec.recognize_google(audio, language='pt-br')).lower()
                print(f'Frase dita: {palavras}')
            except:
                print('Não estou ouvindo...')
                return 'None'
            return palavras

    def assistente_falar(self, falar):
        engine = init('sapi5')
        engine.say(falar)
        engine.runAndWait()

    def assistente_acoes(self):
        frase = self.assistente_ouvir()
        if frase != 'None':
            palavras_desligar = ['desligar', 'desligue', 'desliga']
            if any(palavra in frase for palavra in palavras_desligar):
                print('Quer mesmo desligar? Ruama?')
                self.assistente_falar('Quer mesmo desligar, Ruama?')
                decisao = self.assistente_ouvir()
                if 'sim' in decisao:
                    print('Desligando o computador...')
                    self.assistente_falar('Desligando o computador...')
                    system("shutdown /s /t 300")
                else:
                    print('Ok, não irei')
                    self.assistente_falar('Ok, não irei, o cancelado com sucesso')
            elif 'bloco de notas' in frase:
                print('Abrindo bloco de notas...')
                self.assistente_falar('Abrindo bloco de notas!')
                system('start notepad')
            elif 'chrome' in frase:
                print('Abrindo o navegador chrome...')
                self.assistente_falar('Abrindo o navegador chrome!')
                system('start chrome')
            elif 'firefox' in frase:
                print('Abrindo navegador firefox...')
                self.assistente_falar('Abrindo navegador firefox!')
                system('start firefox')
            elif 'cmd' in frase:
                print('Abrindo cmd...')
                self.assistente_falar('Abrindo prompt de comando!')
                system('start cmd')
            elif 'cancelar' in frase:
                print('Cancelando o desligamento...')
                self.assistente_falar('Cancelando o desligamento...')
                system("shutdown /a")
            else:
                print('Desculpe, não entendi!')
                self.assistente_falar('Desculpe, não entendi!')


if __name__ == '__main__':
    assistente = Comandos()
    assistente.assistente_acoes()

