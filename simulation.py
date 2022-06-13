import pygame
import numpy as np
import pandas as pd
import time
import market

#pd.Timestamp.now().round(freq='min')

mymarket = market.Supermarket()
mymarket.init_layout()
mymarket.add_customers(23)

cust1 = mymarket.customers[5]
cust1.to_df()


df = mymarket.get_customer_df()
df.sort_values(by=["global time"])


pygame.init()
display = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
theFont = pygame.font.Font(None,32)

layout = mymarket.layout
surf = pygame.surfarray.make_surface(layout.transpose(1, 0, 2))

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.blit(surf, (0, 0))
    for custom in mymarket.customers:
        print(custom.time)
    print("time")
    clock.tick(1)
    print("time 2")
    theTime = time.strftime("%H:%M:%S", time.localtime())
    timeText = theFont.render(str(theTime), True,(0, 0, 0),(176, 226, 255))
    display.blit(timeText, (500,370))
    pygame.display.update()



pygame.quit()




