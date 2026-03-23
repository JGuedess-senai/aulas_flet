import flet as ft

def main(page: ft.Page):
    def mensagem(e):
        page.add(
            ft.Text("MF GHOST")
        )
    page.add(
        ft.Text("Carros em velocidade nas estradas do Japão"),
        ft.Image(
            src="images/mfGhost.jpg"
        ),
        ft.Button(
            content="CARROS",
            on_click=mensagem
        )
    )
ft.run(main)