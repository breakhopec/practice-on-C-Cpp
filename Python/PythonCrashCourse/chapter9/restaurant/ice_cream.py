#coding=utf-8
import restaurant

def main():
    ice = restaurant.IceCreamStand('Häagen-Dazs', 10)
    ice.read_flavors()

if __name__ == '__main__':
    main()