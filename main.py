from dotenv import load_dotenv
import os
from imap_tools import AND, MailBox

load_dotenv()

# pegar emails de um remetente para um destinatário
username = os.getenv("username")
password = os.getenv("password")

print(username)
print(password)

# lista de imaps: https://www.systoolsgroup.com/imap/
# meu_email = MailBox('imap.gmail.com').login(username, password)
# lista_remetentes = ["arthurmedeiros193@gmail.com","weslley.ferreira@aluno.uepb.edu.br"]
# palavras_chaves = ["Grátis", "Atenção"]
# i = 0

# criterios: https://github.com/ikvk/imap_tools#search-criteria
# lista_emails = meu_email.fetch(AND(to="t1525389@gmail.com"))
# for email in lista_emails:
#     test = email.text

#     if (len(test) <= 2):
#         print('Esse email está vazio e pode ser um spam!')
#     if email.from_ not in lista_remetentes:
#         print("esse email é suspeito")
#     for i in range(len(palavras_chaves)):
#         if palavras_chaves[i] in test:
#             print("Palavras chaves spam no email!")
#     print(email.from_)
#     print(email.subject)
#     print(email.text)
#     print(len(email.subject))
#     print(len(email.text))
    

# pegar emails com um anexo específico
# lista_emails = meu_email.fetch(AND(from_="remetente"))
# for email in lista_emails:
#     if len(email.attachments) > 0:
#         for anexo in email.attachments:
#             if "TituloAnexo" in anexo.filename:
#                 print(anexo.content_type)
#                 print(anexo.payload)
#                 with open("Teste.xlsx", 'wb') as arquivo_excel:
#                     arquivo_excel.write(anexo.payload)
