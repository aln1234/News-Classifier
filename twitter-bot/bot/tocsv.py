def text2csva(screenname):
    t = ""
    data_file = open("bot\corpus1.csv", 'w')
    for s in screenname:
        if(s != ',' and s != '\n'):
            t = t+s
    data_file.write(t+'.')


def text2csvb(screenname):
    t = ""
    data_file = open("bot\corpus2.csv", 'w')
    for s in screenname:
        if(s != ',' and s != '\n'):
            t = t+s
    data_file.write(t+'.')


def text2csvc(screenname):
    t = ""
    data_file = open("bot\corpus3.csv", 'w')
    for s in screenname:
        if(s != ',' and s != '\n'):
            t = t+s
    data_file.write(t+'.')


def text2csvd(screenname):
    t = ""
    data_file = open("bot\demo.csv", 'a')
    for s in screenname:
        if(s != ',' and s != '\n'):
            t = t+s
    data_file.write(' \n'+t)
