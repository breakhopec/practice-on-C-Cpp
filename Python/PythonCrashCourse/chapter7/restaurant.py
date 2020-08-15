#coding=utf-8

def main():
    sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'pastrami', 'pastrami', 'pastrami']
    finished_sandwich = []
    out_of_stock = ['pastrami']

    for out in out_of_stock:
        print('%s is out of stock' % (out))
        while out in sandwich_orders:
            sandwich_orders.remove(out)

    while sandwich_orders:
        doing = sandwich_orders.pop()
        print('making %s' % (doing))
        finished_sandwich.append(doing)

if __name__ == '__main__':
    main()