## jogo ping pong checar
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500/level

# atribuindo a variavel root uma tupla tk
root = Tk()
# acessando o titulo do objeto root e dando o titulo
root.title("Ping Pong")
# resizable é um método de root
# resizable permite aumentar o tamanho da tela que o tKinter proporciona
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# criação de um canvas
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
# pack posiciona o widget
# é a forma mais simples de place() e grid ()
canvas.pack()

# deve ta recarregando o root com o titulo e etc
root.update()

# Variável
count = 0
lost = False

# Se a classe é a forma e o objeto é o que vai ser encaixado
# então deve esta organizando a estrutura 
class Bola:
    # def é a declaração de uma função
    # os argumentos estão entre parentes
    # mas o que é retornado ? 
    # __init__ é o construtor - sempre que um novo obj for instanciado o que ta dentro de Bola será executado
    
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # starts_x é uma lista
        starts_x = [-3, -2, -1, 1, 2, 3]
        # escolhe aleatoriamente os numeros dentro de starts_x
        # shuffle reorganiza a ordem dos intems
        # então depois de ter posto os elementos em ordem crescente, escolhe "aleatoriamente"?
        random.shuffle(starts_x)
        
        # self REPRESENTA a instancia de uma classe 
        # self aponta para o objeto, faz referencia ao objeto
        # instanciei a classe x e atribui o atributo de indice 0 da lista
        # com self consigo acessar os atributos e métodos de uma classe 
        self.x = starts_x[0]
        
        # acessando um atributo de y 
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# inicializou sem o self ?
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()
