import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.hstack(
        rx.vstack(
          rx.text("¿Te gustan los productos otakus?",
          rx.text("¿Quieres vender tus productos tejidos a"),
          rx.text("mano siendo un vendedor independiente y"),
          rx.text("generar ingresos por tus creaciones?"),
),  
        ),
        rx.image(src="https://images.unsplash.com/photo-1686151676893-c788695bbc8a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGFtaWd1cnVtaXMlMjB5JTIwbGFuYXN8ZW58MHx8MHx8fDA%3D",width="400px"),
      ),
      rx.link(
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="https://forms.gle/PvYHtu3D2NfWUq3f6",
          is_external=False,
      ),
      align="center",
      text_align="center",
      height="676px",
      background="#f3e5ab",
      
    )
  
  
  
        # rx.vstack(
        #   rx.heading(
        #     rx.text.span("tejidOtaku",color=rx.color("blue",7)),
        #     " la Aplicacion que te guia al tomarte fotos"
        #   ),
        #   rx.text("Mejora tus fotos con nuevas ideas",
        #   rx.text.em(" creativas y",color=rx.color("cyan",9)),
        #   rx.text.em(" novedosas,",color=rx.color("cyan",9)),
        #   " se la envidia de los demas con ",
        #   rx.text.quote("PIXIE.",color=rx.color("gold",9))),  
        # ),