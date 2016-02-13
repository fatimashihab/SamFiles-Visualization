import pysam
import matplotlib.pyplot as plt
import os

try:
    os.chdir("/home/fatma/Desktop/samtools/lib")
    file= pysam.AlignmentFile("ex2_sorted.sorted.bam", "rb")
except IOError:
    try:
        file_path= raw_input ("Please enter file path: \n")
        os.chdir(file_path)

        file= raw_input("\nPlease enter the bamfile (ex: file_name.bam): \n")
        file=pysam.AlignmentFile(file, "rb")

    except OSError:
        print("Path or File Name Error.")
    else:
        position= []
        number_of_reads=[]

        for pileupcolumn in file.pileup(until_eof=True):
            number_of_reads.append(pileupcolumn.n)
            position.append(pileupcolumn.pos)

        #print (number_of_reads)
        #print ("\n %s" %position)

        plt.plot(position, number_of_reads)
        plt.show()

        file.close()


else:
    position= []
    number_of_reads=[]

    for pileupcolumn in file.pileup(until_eof=True):
        number_of_reads.append(pileupcolumn.n)
        position.append(pileupcolumn.pos)

    #print (number_of_reads)
    #print ("\n %s" %position)

    plt.plot(position, number_of_reads)
    plt.show()

    file.close()
