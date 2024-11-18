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
          href="https://forms.gle/pGqoBuULbmb6TRqs9",
          is_external=False,
      ),
      rx.link(
          rx.button(rx.icon(tag="airplay"),"Iniciar sesion",),
          href="https://forms.gle/vqYbrwcSbLUEPFTn9",
          is_external=False,
      ),      
      
      align="center",
      text_align="center",
      height="676px",
      background="#f3e5ab",
      
    )
