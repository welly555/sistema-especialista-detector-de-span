import os

from dotenv import load_dotenv
from imap_tools import AND, MailBox

load_dotenv()

# pegar emails de um remetente para um destinatário
email = str(os.getenv("email"))
password = str(os.getenv("password"))


# lista de imaps: https://www.systoolsgroup.com/imap/
meu_email = MailBox('imap.gmail.com').login(email, password)
lista_remetentes = ["arthurmedeiros193@gmail.com", "weslley.ferreira@aluno.uepb.edu.br"]
palavras_chaves = ["100%", "Atenção", "Abra, por favor", "Acesso gratuito", "Apenas hoje",
                   "Assine agora", "Bilhão", "Bônus", "Cancelamento requerido", "Cartões aceitos",
                   "Cem por cento grátis", "Crédito pré-aprovado", "De graça", "Dinheiro Extra",
                   "Dinheiro rápido", "Economize agora", "eliminar a dívida", "Financie já",
                   "Fórmula milagrosa", "Ganhe $", "Ganhe dinheiro extra", "GRÁTIS", "Hospedagem grátis",
                   "Instalação gratuita", "Isso não é spam", "Isso não é um golpe", "Isto é um anúncio",
                   "Leia, por favor", "Ligue para nós", "Lucros", "Macbook grátis", "Melhor negócio",
                   "Melhor oferta", "Melhor preço", "Melhor promoção", "Menor preço",
                   "Menores taxas de seguro","Milhões de Dólares", "Milhões de Reais", "Milionário",
                   "Money", "MoneyBack", "Não é golpe", "Não é spam", "Nós odiamos spam",
                   "Oferta exclusiva", "Oferta fantástica", "Pague suas dívidas", "Por apenas",
                   "Presente gratuito", "Receba agora", "Receba de graça", "Receita milagrosa",
                   "Reembolso total", "Renda Extra", "Rolex", "se surpreenda", "Seja seu próprio patrão",
                   "Senhas", "SERASA", "Telefone celular gratuito", "tempo limitado", "Tempo limitado",
                   "Teste grátis", "Trabalhe em Casa", "Trabalhe de casa", "Última chance",
                   "Uma vez na vida", "Urgentes", "Vagas Limitadas", "Veja por si mesmo",
                   "Visite nosso site", "Zero chance", "dívida de empréstimo bancário", "clique no link",
                   "documento cancelado", "prometo revelar", "ganhou no sorteio", "informe seus dados"]
i = 0

# criterios: https://github.com/ikvk/imap_tools#search-criteria
lista_emails = meu_email.fetch(AND(to="t1525389@gmail.com"))
for email in lista_emails:
    test = email.text

    if (len(test) <= 2):
        print('Esse email está vazio e pode ser um spam!')
    if email.from_ not in lista_remetentes:
        print("esse email é suspeito")
    for i in range(len(palavras_chaves)):
        if palavras_chaves[i] in test:
            print("Palavras chaves spam no email!")
    print(email.from_)
    print(email.subject)
    print(email.text)
    print(len(email.subject))
    print(len(email.text))
    print(email.uid)

