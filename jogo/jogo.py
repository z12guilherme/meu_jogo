import tkinter as tk
from random import randint
from PIL import Image, ImageTk

class JogoAdventure:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo de Aventura")
        self.janela.geometry("800x600")

        self.player_nome = "Player"
        self.player_vida = 300
        self.player_forca = 10
        self.player_inteligencia = 5
        self.player_agilidade = 8

        self.inimigo_nome = "Dragão"
        self.inimigo_vida = 500
        self.inimigo_forca = 15
        self.inimigo_inteligencia = 3
        self.inimigo_agilidade = 12

        self.player_image = ImageTk.PhotoImage(Image.open(r"C:\Users\USUARIO\Desktop\jogo\player.jpg"))
        self.dragao_image = ImageTk.PhotoImage(Image.open(r"C:\Users\USUARIO\Desktop\jogo\dragao.jpg"))

        self.criar_interface_player()
        self.criar_interface_dragao()
        self.criar_interface_batalha()

        self.janela.mainloop()

    def criar_interface_player(self):
        self.frame_player_stats = tk.Frame(self.janela, bg="#333")
        self.frame_player_stats.pack(fill="x")

        self.label_player_nome = tk.Label(self.frame_player_stats, text=f"Nome: {self.player_nome}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_player_nome.pack(side=tk.LEFT, padx=10)

        self.label_player_vida = tk.Label(self.frame_player_stats, text=f"Vida: {self.player_vida}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_player_vida.pack(side=tk.LEFT, padx=10)

        self.label_player_forca = tk.Label(self.frame_player_stats, text=f"Força: {self.player_forca}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_player_forca.pack(side=tk.LEFT, padx=10)

        self.label_player_inteligencia = tk.Label(self.frame_player_stats, text=f"Inteligência: {self.player_inteligencia}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_player_inteligencia.pack(side=tk.LEFT, padx=10)

        self.label_player_agilidade = tk.Label(self.frame_player_stats, text=f"Agilidade: {self.player_agilidade}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_player_agilidade.pack(side=tk.LEFT, padx=10)

        self.label_player_image = tk.Label(self.frame_player_stats, image=self.player_image, bg="#333")
        self.label_player_image.pack(side=tk.LEFT, padx=10)

    def criar_interface_dragao(self):
        self.frame_dragao_stats = tk.Frame(self.janela, bg="#333")
        self.frame_dragao_stats.pack(fill="x")

        self.label_dragao_nome = tk.Label(self.frame_dragao_stats, text=f"Nome: {self.inimigo_nome}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_dragao_nome.pack(side=tk.LEFT, padx=10)

        self.label_dragao_vida = tk.Label(self.frame_dragao_stats, text=f"Vida: {self.inimigo_vida}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_dragao_vida.pack(side=tk.LEFT, padx=10)

        self.label_dragao_forca = tk.Label(self.frame_dragao_stats, text=f"Força: {self.inimigo_forca}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_dragao_forca.pack(side=tk.LEFT, padx=10)

        self.label_dragao_inteligencia = tk.Label(self.frame_dragao_stats, text=f"Inteligência: {self.inimigo_inteligencia}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_dragao_inteligencia.pack(side=tk.LEFT, padx=10)

        self.label_dragao_agilidade = tk.Label(self.frame_dragao_stats, text=f"Agilidade: {self.inimigo_agilidade}", font=("Arial", 12), bg="#333", fg="#fff")
        self.label_dragao_agilidade.pack(side=tk.LEFT, padx=10)

        self.label_dragao_image = tk.Label(self.frame_dragao_stats, image=self.dragao_image, bg="#333")
        self.label_dragao_image.pack(side=tk.LEFT, padx=10)

    def criar_interface_batalha(self):
        self.frame_batalha = tk.Frame(self.janela, bg="#333")
        self.frame_batalha.pack(fill="x")

        self.label_batalha = tk.Label(self.frame_batalha, text="Batalha", font=("Arial", 24), bg="#333", fg="#fff")
        self.label_batalha.pack(side=tk.LEFT, padx=10)

        self.button_atacar = tk.Button(self.frame_batalha, text="Atacar", font=("Arial", 12), bg="#333", fg="#fff", command=self.atacar)
        self.button_atacar.pack(side=tk.LEFT, padx=10)

        self.button_defender = tk.Button(self.frame_batalha, text="Defender", font=("Arial", 12), bg="#333", fg="#fff", command=self.defender)
        self.button_defender.pack(side=tk.LEFT, padx=10)

    def atacar(self):
     dano = randint(1, self.player_forca)
     self.inimigo_vida -= dano
     self.label_dragao_vida['text'] = f"Vida: {self.inimigo_vida}"
     if self.inimigo_vida <= 0:
        self.label_batalha['text'] = "Você venceu!"
        self.button_atacar['state'] = 'disabled'
        self.button_defender['state'] = 'disabled'

    def defender(self):
        dano = randint(1, self.inimigo_forca)
        self.player_vida -= dano
        self.label_player_vida['text'] = f"Vida: {self.player_vida}"
        if self.player_vida <= 0:
         self.label_batalha['text'] = "Você perdeu!"
         self.button_atacar['state'] = 'disabled'
         self.button_defender['state'] = 'disabled'

JogoAdventure()