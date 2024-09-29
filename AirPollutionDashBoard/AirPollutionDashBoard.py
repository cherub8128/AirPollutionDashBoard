"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    show :bool = True
    no_x :float = 0.0
    so_x :float = 0.0
    pb :float = 0.0
    nh42so4 :float = 0.0
    nh4no3 :float = 0.0
    VOCs :float = 0.0
    
    brain :float = 0.0
    lungs :float = 0.0
    heart :float = 0.0
    stomach :float = 0.0
    intestine :float = 0.0
    
    def set_no_x(self, value: int):
        self.no_x = value[0] / 100
        self.lungs = (self.no_x+self.so_x+self.nh42so4+self.VOCs)/4
        self.stomach = self.no_x
        
    
    def set_so_x(self, value: int):
        self.so_x = value[0] / 100
        self.brain = (self.nh4no3+self.VOCs+self.so_x)/3
        self.lungs = (self.no_x+self.so_x+self.nh42so4+self.VOCs)/4
        
    
    def set_pb(self, value: int):
        self.pb = value[0] / 100
    
    def set_NH42SO4(self, value: int):
        self.nh42so4 = value[0] / 100
        self.lungs = (self.no_x+self.so_x+self.nh42so4+self.VOCs)/4
        
        
    def set_NH4NO3(self, value: int):
        self.nh4no3 = value[0] / 100
        self.brain = (self.nh4no3+self.VOCs+self.so_x)/3
        self.lungs = (self.no_x+self.so_x+self.nh42so4+self.VOCs)/4
        self.intestine = self.nh4no3
        
    def set_VOCs(self, value: int):
        self.VOCs = value[0] / 100
        self.brain = (self.nh4no3+self.VOCs+self.so_x)/3
        self.lungs = (self.no_x+self.so_x+self.nh42so4+self.VOCs)/4
        
        
        


def index() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("공기오염 대시보드", size="9", align="center",margin="20px",weight="bold", margin_top="50px"),
        rx.vstack(
            rx.card(
                rx.text("""폐암 확률 23.3% 증가!! 외출 금지🚶🚫
실내🏠에 머무르세요!!""",weight="bold",size="7",align="center", color_scheme="blue",white_space="pre-wrap"),
                padding="1em",
                width="100%",
                ),
            rx.card(
                rx.flex(
                    rx.image(src='/people.png',width="500px",position="absolute",top="0",left="0",z_index="0"),
                    rx.image(src='/heart.png',width="500px",position="absolute",top="0",left="0",z_index="1",opacity=State.heart),
                    rx.image(src='/lungs.png',width="500px",position="absolute",top="0",left="0",z_index="2",opacity=State.lungs),
                    rx.image(src='/brain.png',width="500px",position="absolute",top="0",left="0",z_index="3",opacity=State.brain),
                    rx.image(src='/stomach.png',width="500px",position="absolute",top="0",left="0",z_index="3",opacity=State.stomach),
                    rx.image(src='/intestine.png',width="500px",position="absolute",top="0",left="0",z_index="3",opacity=State.intestine),
                    width="500px",
                    height="500px",
                ),
                box_shadow="rgba(224, 224, 224, 0.8) 0 15px 30px -10px",
            ),
            rx.card(
                rx.text(f"NOx 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_no_x),
                rx.text(f"SOx 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_so_x),
                rx.text(f"Pb 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_pb),
                rx.text(f"(NH4)2SO4 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_NH42SO4),
                rx.text(f"NH4NO3 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_NH4NO3),
                rx.text(f"VOCs 농도"),
                rx.slider(width="500px",default_value=0,min=0,max=100,step=1,on_change=State.set_VOCs)
            )
        ),
        rx.color_mode_cond(
            light= rx.image(
            src="/background.png",
            width="100%",
            height="150vh",
            object_fit="cover",
            position="absolute",
            z_index="-1",
            ),
            dark=rx.image(
            src="/background_night.png",
            width="100%",
            height="150vh",
            object_fit="cover",
            position="absolute",
            z_index="-1",
            ),
        ),
        direction="column",
        justify="center",
        align="center",
        padding="1em",
        width="100%",
        height="100vh",    
    )

style = {
    "font_family": "Noto Sans KR, sans-serif"
}

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&display=swap",
    ],
    style=style,
    overlay_component=None
)
app.add_page(index)
