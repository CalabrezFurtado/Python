try:

    def main ():
        global itens
        itens = {}
        global i
        i = 1
        item1 = str(input("What's the Item?")).upper()
        itens[item1]=i

        getitensloop(i, itens, item1)

    def getitensloop(i, itens, item1):

        while True:

            global itensloop
            itensloop = str(input("What's the Item?")).upper()

            if itensloop in itens:

                i += 1
                itens[itensloop]= i

            else:

                itens[itensloop]=i

    def printnewdict(itens):

        newdict = dict(sorted(itens.items()))

        for k, v in newdict.items():

            print (v, end = " ")
            print (k)

    main()

except EOFError:

    print ("")

    printnewdict(itens)
