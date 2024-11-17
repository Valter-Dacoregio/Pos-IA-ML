class BookStoreInventory:
    def __init__(self):
        self.inventory = {}
    
    def addBook(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
    
    def checkQuantity(self, title):
        if title in self.inventory:
            # return self.inventory[title]
            return self.inventory.get(title, 0)
        else:
            return 0
    
    def removeBook(self, title, quantity):
        if title in self.inventory and self.inventory[title]:
            self.inventory[title] -= quantity
            if self.inventory[title] == 0:
                del self.inventory[title]
            return True
        else:
            return False
    
    # PROTÓTIPO DE LLM
    def recommendBooks(self, description):
        # Esta é uma recomendação simulada baseada em palavras-chaves
        keywords = description.lower().split()
        recomendations = {
            'análise avançada': 'os elementos da aprendizagem estatística',
            'aventura': 'o Hobbit de J.R.R. Tolkien',
            'mistério': 'as aventuras de sherlock holmes de arthur conan doyle',
            'romance': 'orgulho e preconceito de jane austen',
            'ficção científica': 'duna de frank herbert',
            'fantasia': 'harry potter e a pedra filosofal de j.k. rowling',
            'história': 'sapiens: uma breve história da humanidade por yuval noah harari',
        }
        for keyword in keywords:
            if keyword in recomendations:
                return recomendations[keyword]
        return 'Sem recomendações para você no momento.'

# CLASSE MAIN
if __name__ == "__main__":
    bookstore = BookStoreInventory()

    # CARREGA OS LIVROS DA BIBLIOTECA
    bookstore.addBook("Sapiens: uma Breve História da Humanidade", 4)
    bookstore.addBook("Duna", 3)
    bookstore.addBook("O Hobbit", 1)
    bookstore.addBook("O senhor dos Anéis", 2)
    bookstore.addBook("Harry Potter e a Pedra Filosofal", 4)
    bookstore.addBook("As Aventuras de Sherlock Holmes", 3)

    # BUSCA RECOMENDAÇÃO COM BASE NA DESCRIÇÃO DO USUÁRIO
    descriptionUser = "Este livro é uma aventura sobre um Hobbit..."
    recomendation = bookstore.recommendBooks(descriptionUser)
    print("Recomendação....: ", recomendation)

    # VERIFICA O ESTOQUE DO LIVRO RECOMENDADO
    hobbitQuantity = bookstore.checkQuantity("O Hobbit")
    print("Quantidade de o Hobbit: " + str(hobbitQuantity))

    # INVENTÁRIO ANTES
    print("Inventário ANTES...: ", bookstore.inventory)

    # REMOVE DETERMINADA QUANTIDADE DO LIVRO DO ESTOQUE
    bookstore.removeBook("O Hobbit", 1)
    print("Qtd Antes..: ", hobbitQuantity, "\nLivro Recomendado: ", recomendation, "\nQtd Depois..: ", bookstore.checkQuantity("O Hobbit"))

    # INVENTÁRIO DEPOIS
    print("Inventário Depois...: ", bookstore.inventory)



