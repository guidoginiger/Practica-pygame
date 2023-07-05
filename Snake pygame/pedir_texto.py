import pygame, sys
import colores

pygame.init()
tiempo = pygame.time.Clock()
celda_tamanio = 35
celda_numero = 20

pantalla = pygame.display.set_mode((celda_tamanio * celda_numero, celda_tamanio * celda_numero))
pygame.display.set_caption("Snake Game")


fuente = pygame.font.Font(None, 32)
ingresar_texto = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                ingresar_texto = ingresar_texto[:-1]
            else: 
                ingresar_texto += event.unicode

    pantalla.fill(colores.BLANCO)
    colocar_texto = fuente.render(ingresar_texto, True, colores.AZUL)
    pantalla.blit(colocar_texto, (10,10))

    pygame.display.flip()
    tiempo.tick(70)


