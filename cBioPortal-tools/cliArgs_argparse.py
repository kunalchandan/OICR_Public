import sys, getopt

# DON'T do it this way, getopt is legacy


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    inputfile = ''
    outputfile= ''
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'HIHIHIHI'
    print inputfile
    print outputfile


if __name__ == "__main__":
    main(sys.argv[1:])