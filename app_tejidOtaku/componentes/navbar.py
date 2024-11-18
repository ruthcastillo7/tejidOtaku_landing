import reflex as rx

def navbar()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="camera"),
        rx.heading("TejidOtaku",size="6",weight="bold"),
      ),
      rx.hstack(
        rx.button(
          rx.hstack(
          rx.link("Contactanos",href="/#",size="3",weight="bold",color="white"),
          justify="end",
          spacing="5"
          )
        ),
        rx.button(
          rx.hstack(
            rx.link("Sobre nosotros",href="/#",size="3",weight="bold",color="white"),
            justify="end",
            spacing="5"
          )
        ),  
      ),
      
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      background="#e8ca61"
    )
