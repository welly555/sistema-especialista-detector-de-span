import email
import imaplib
from email.header import decode_header


class Spam:
    def __init__(self,):
        # Configurar suas informações de email
        self.imap_server = 'imap.gmail.com'  # Substitua com o servidor IMAP do seu provedor de email
        self.email_address = 't1525389@gmail.com'  # Seu endereço de email
        self.password = 'uhrr sxew jfbv paaw'  # Sua senha
        self.lista_remetentes = ["arthurmedeiros193@gmail.com", "weslley.ferreira@aluno.uepb.edu.br"]
        self.emails_suspeitos = ["arthurmedeiros193@gmail.com"]
        self.palavras_chaves = ["Grátis", "Atenção"]

        # Conectar-se ao servidor IMAP
        self.imap = imaplib.IMAP4_SSL(self.imap_server)
        self.imap.login(self.email_address, self.password)

        # Selecionar a caixa de entrada (inbox)
        self.imap.select('inbox')

    def iniciar(self,):
        self.ChecarEmail()
        self.Logout()

    def ChecarEmail(self,):
        # Procurar por emails (por exemplo, todos os emails não lidos)
        result, email_ids = self.imap.search(None, 'UNSEEN')

        if result == 'OK':
            email_id_list = email_ids[0].split()
            for self.email_id in email_id_list:
                result, email_data = self.imap.fetch(self.email_id, '(RFC822)')
                if result == 'OK':
                    raw_email = email_data[0][1]
                    email_message = email.message_from_bytes(raw_email)

                    # Exibir informações do email (remetente, assunto, data)
                    self.subject, encoding = decode_header(email_message['Subject'])[0]
                    self.sender, encoding = decode_header(email_message['From'])[0]
                    self.date = email_message['Date']

                    # print(len(subject))

                    print(f'Remetente: {self.sender}')
                    print(f'Assunto: {self.subject}')
                    print(f'Data: {self.date}')

                    self.ExibirEmail(email_message)

                  
                    print('-' * 40)  # Linha de separação entre os emails
        else:
            print('Erro ao pesquisar emails.')
    
    def ChecarEmailVazio(self, body):
        if len(body) <= 2:
            print("O assunto está vazio!")
            self.MoverSpam()
            return True
        return False
    
    def ChecarEmailSuspeito(self,):
        for i in range(len(self.emails_suspeitos)):
            if self.emails_suspeitos[i] in self.sender:
                print("Esse email é suspeito!")
                self.MoverSpam()
                return True
        return False
    
    def ChecarPalavrasChaves(self, body):
        for i in range(len(self.palavras_chaves)):
            if self.palavras_chaves[i] in body:
                print("Esse body contem palavras chaves de spam!")
                self.MoverSpam()
                return True
        return False

    def ExibirEmail(self, email_message):
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    body = part.get_payload(decode=True)
                    if body is not None:
                        body = body.decode()
                        print(body)

                        if self.ChecarEmailVazio(body):    
                            pass
                        elif self.ChecarEmailSuspeito():
                            pass
                        elif self.ChecarPalavrasChaves(body):
                            pass
        else:
            body = email_message.get_payload(decode=True)
            if body is not None:
                body = body.decode()
                print(body)
    
    def MoverSpam(self,):
        result, self.data = self.imap.store(self.email_id, '+X-GM-LABELS', '(\Spam)')
        if result == 'OK':
            print(f'Email {self.email_id} marcado como spam com sucesso!')
        else:
            print(f'Erro ao marcar o email {self.email_id} como spam.')
    
    def Logout(self,):
        self.imap.logout()



inicar = Spam()

inicar.iniciar()