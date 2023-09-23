import imaplib

# Configurar suas informações de email
imap_server = 'imap.gmail.com'  # Substitua com o servidor IMAP do seu provedor de email
email_address = 't1525389@gmail.com'  # Seu endereço de email
password = 'uhrr sxew jfbv paaw'  # Sua senha
remetente = 'weslley.ferreira@aluno.uepb.edu.br'




# Conectar-se ao servidor IMAP
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

# Selecionar a caixa de entrada (inbox)
imap.select('Inbox')

# Procurar por emails que correspondem a um critério específico (por exemplo, com base no assunto)
criteria = f'(FROM "{remetente}")'
result, email_ids = imap.search(None, criteria)

# Marcar os emails encontrados como spam (o comando exato pode variar dependendo do servidor de email)
if result == 'OK':
    email_id_list = email_ids[0].split()
    for email_id in email_id_list:
        result, data = imap.store(email_id, '+X-GM-LABELS', '(\Spam)')
        if result == 'OK':
            print(f'Email {email_id} marcado como spam com sucesso!')
        else:
            print(f'Erro ao marcar o email {email_id} como spam.')
else:
    print('Erro ao pesquisar emails.')

# Fechar a conexão com o servidor IMAP
imap.logout()