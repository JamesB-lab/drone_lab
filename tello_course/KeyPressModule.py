import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(key_name):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}' .format(key_name))

    if keyInput[mykey]:
        ans = True
    pygame.display.update()

    return ans


def main():
    if getKey("LEFT"):
        print("left key pressed")
    if getKey("RIGHT"):
        print("right key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()
