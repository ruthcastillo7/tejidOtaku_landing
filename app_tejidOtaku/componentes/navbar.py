import reflex as rx

def navbar()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="camera"),
        rx.heading("TejidOtaku",size="6",weight="bold"),
      ),
      rx.button(
      rx.hstack(
        rx.link("Iniciar sesion",href="/#",size="3",weight="bold"),
        justify="end",
        spacing="5"
#        background="#f3e5ab",
      )),
      rx.button(
      rx.hstack(
        rx.link("Sobre nosotros",href="/#",size="3",weight="bold"),
        justify="end",
        spacing="5"
      )),
      
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      background="#e8ca61"
    )
  
  
  
#   return rx.hstack(
#       rx.hstack(
#         rx.icon(tag="camera"),
#         rx.heading("TejidOtaku",size="6",weight="bold"),
#       ),
#       rx.hstack(
#         rx.link("Iniciar sesion",href="/#",size="3",weight="bold"),
#         justify="end",
#         spacing="5"
#       ),
#       justify="between",
#       align_items="center",
#       padding="1em",
#       width="100%",
#       background="#e8ca61"
#     )