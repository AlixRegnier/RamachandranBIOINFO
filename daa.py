import sys


if __name__=="__main__":

    if sys.argv[1] != '-k' and sys.argv[1] != '-d':
        print("python daa.py [-d|-k] [k|e] [minpoints] [-phipsi|-chi] filename.pdb\n" + \
                "-d : dbscan clustering / -k : kmeans clustering\n"+\
                    " [k|e] number above 0\n"+\
                         " minpoint : number above 0 - this parameter exist only if you have selecter dbscan\n"+\
                         "\n ")
    
    try:
        while int(sys.argv[2]) <= 0:
            value=input("Please select a correct value for k or  ɛ, it has to be above 0 :")
            sys.argv[2]=value
    except ValueError:
        value=input("the second argument has to be number above 0")
    except IndexError:
        print("Please give a second argument : a number above 0")

    

