from tkinter import*
import tkinter as tk
import subprocess

window = tk.Tk()
window.title("MINI GAME")
window.geometry("800x500")

hangman_img = tk.PhotoImage(file="hang_Thum.png")  
boom_img = tk.PhotoImage(file="boom_Thum.png")       
snake_img = tk.PhotoImage(file="jirungi_Thum.png")

background_image = tk.PhotoImage(file="mini_background.png")

canvas = tk.Canvas(window, width=800, height=500)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor="nw", image=background_image)

canvas.create_text(400, 150, text="CUTE MINI GAME", font=("Press Start 2P", 32, "bold"), fill="black")

#hangman_img = hangman_img.subsample(1, 2)  # 이미지를 4배 축소
#boom_img = boom_img.subsample(1, 2)
#snake_img = snake_img.subsample(1, 2)


def run_hangman():
    subprocess.run(["Python", "hangman.py"])

def run_boom():
    subprocess.run(["Python", "boom.py"])

def run_snake():
    subprocess.run(["Python", "snake.py"])

def show_explanation():
    explanation_window = tk.Toplevel(window)
    explanation_window.title("Game Explanation")
    explanation_window.geometry("480x550")
    
    # 설명 텍스트
    explanation_text = """
    🎮 MINI GAME 🎮
    
    1. Hangman Game:
       숨겨진 단어를 가능한 적은 실수로
       맞추는 것이 목표입니다!
       
       실수할 때마다 행맨 그림이 점차 완성되며,
       6번의 기회를 다 쓰면 게임이 종료됩니다!

       행맨이 완성되기 전에 단어를 맞추면 승리!🥳🎉
       그렇지 않으면 패배입니다!

       *h키를 누르면 힌트를 볼 수 있습니다. (단, 한번만)
       *게임이 끝나고 r키를 누르면 다시 시작할 수 있습니다!

    2. Bomb Game:
       폭탄을 피하면서 최대한 오래 버티세요!
       하늘에서 떨어지는 폭탄을 피해서 점수를 얻습니다! 
       폭탄에 맞으면 폭발과 함께 게임이 오버되니 조심하세요😯

    3. Snake Game:
       지렁이를 조종해 먹이를 먹고 점수를 획득하세요!
       벽이나 자신과 충돌하면 게임 오버!
       적 지렁이와 부딫혀도 게임이 오버되니 잘 피해다니세요!🐍

    즐거운 시간 보내세요! 😊
    """
    label = tk.Label(explanation_window, text=explanation_text, font=("Arial", 12), justify="left")
    label.pack(pady=20, padx=20)




button1 = tk.Button(window, text="Hangman Game", font=("Press Start 2P", 10), image=hangman_img, command=run_hangman,compound="top", width=150, height=170)
button1.place(x=30, y=300)

button2 = tk.Button(window, text="Bomb Game", font=("Press Start 2P", 10), image=boom_img, command=run_boom, compound="top",width=150, height=170)
button2.place(x=230, y=300)

button3 = tk.Button(window, text="Snake Game", font=("Press Start 2P", 10),image=snake_img, command=run_snake, compound="top",width=150, height=170)
button3.place(x=430, y=300)

button4 = tk.Button(window, text="Explanation", font=("Press Start 2P", 10),image=snake_img, command=show_explanation, compound="top", width=150, height=170)
button4.place(x=630, y=300)

window.mainloop()
