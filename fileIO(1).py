def main():
    file = input("Type file name: ")
    fin = open(file)
    fout= open("myOutpt.txt",'w')
    # read lines from file one at a time and output to screen
    for line in fin:
        # strip removes leading and trailing spaces from line
        s_line = line.strip()
        print(s_line)
        fout.write(s_line+ '\n')
    # close the files
    fin.close()
    fout.close()
    
if __name__ == "__main__":
    main()
