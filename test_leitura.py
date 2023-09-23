import email
import imaplib
from email.header import decode_header

# Configurar suas informações de email
imap_server = 'imap.gmail.com'  # Substitua com o servidor IMAP do seu provedor de email
email_address = 't1525389@gmail.com'  # Seu endereço de email
password = 'uhrr sxew jfbv paaw'  # Sua senha
lista_remetentes = ["arthurmedeiros193@gmail.com", "weslley.ferreira@aluno.uepb.edu.br"]

emails_suspeitos = ["arthurmedeiros193@gmail.com"]

palavras_chaves = ["Grátis", "Atenção"]

# Conectar-se ao servidor IMAP
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

# Selecionar a caixa de entrada (inbox)
imap.select('inbox')

# Procurar por emails (por exemplo, todos os emails não lidos)
result, email_ids = imap.search(None, 'UNSEEN')

# Iterar pelos IDs dos emails e exibir o conteúdo
if result == 'OK':
    email_id_list = email_ids[0].split()
    for email_id in email_id_list:
        result, email_data = imap.fetch(email_id, '(RFC822)')
        if result == 'OK':
            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Exibir informações do email (remetente, assunto, data)
            subject, encoding = decode_header(email_message['Subject'])[0]
            sender, encoding = decode_header(email_message['From'])[0]
            date = email_message['Date']

            # print(len(subject))
            
            if len(subject) <= 2:
                print("O assunto está vazio!")

            for i in range(len(emails_suspeitos)):
                if emails_suspeitos[i] in sender:
                    print("Esse email é suspeito!")
            
            

            print(f'Remetente: {sender}')
            print(f'Assunto: {subject}')
            print(f'Data: {date}')

            # Exibir o corpo do email
            if email_message.is_multipart():
                for part in email_message.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if "attachment" not in content_disposition:
                        body = part.get_payload(decode=True)
                        if body is not None:
                            body = body.decode()
                            print(body)

                            for i in range(len(palavras_chaves)):
                                if palavras_chaves[i] in body:
                                    print("Esse body contem palavras chaves de spam!")
                                    result, data = imap.store(email_id, '+X-GM-LABELS', '(\Spam)')
                                    if result == 'OK':
                                        print(f'Email {email_id} marcado como spam com sucesso!')
                                    else:
                                        print(f'Erro ao marcar o email {email_id} como spam.')

            else:
                body = email_message.get_payload(decode=True)
                if body is not None:
                    body = body.decode()
                    print(body)

            print('-' * 40)  # Linha de separação entre os emails
else:
    print('Erro ao pesquisar emails.')

# Fechar a conexão com o servidor IMAP
imap.logout()