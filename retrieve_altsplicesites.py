### Determine which mRNA contain alternative splice sites
### from the mrna collection in chrome database
### pass in gene/accession number (numeric from NCBI) as argument to this script,
### determine if any of the exons'from and to positions
### are different and suggest an alternative splice site.
### return the result as tuples within an overall list that includes
### the accession#, mRNA, from/to exon positions, and
### alternative splice site flag (Y/'')

### Marty Osterhoudt
### independent research project with Dr. Frees
### Fall 2016 semester
### Ramapo College of NJ

import sys

class class_altsplice:
    wrk_mrnafromtoexon = []  # make this available to the entire class

    def __init__(self, arg_gene, arg_print=''):
        # create objects required to access MongoDB
        from pymongo import MongoClient
        client = MongoClient()
        db = client.chrome
        collect = db.mrna
        prm_gene = arg_gene

        # define work fields for this def
        #wrk_mrnafromtoexon = []
        wrk_dict_mrnafromtoexon = {} #used to track from/to positions and count
        wrk_tuple = ()  # tuple for "return"
        wrk_mrna_count = 0  # number/count of mRNA in gene

        ## gcursor should return a single row, which is the total number/count of mrna for a gene
        gcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$group": {"_id": {"gene_id":"$gene_id"}, "total_g":{"$sum":1}}} ])
        for g_row in gcursor:
            wrk_mrna_count = g_row['total_g']
            if(arg_print == 'Y'):
                print('gcursor full row: ',g_row)
        # keep the following outside of the "for" loop, it's possible gcursor count could be zero
        # (if an invalid gene accession# was passed in the argument)
        if(arg_print == 'Y'):
            print('Number of mRNA associated with gene ',prm_gene,' is: ',wrk_mrna_count)

        ## e.g., if the count is 3 there are 3 mRNA
        ## Next, read aggregate by gene, "from" exon position, and "to" exon position
        ## if row count grouped by from/to exon is less than the g_row count,
        ## there is likely an alternative splice site
        mcursor1 = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1,"exonend":1}}])
        for row1 in mcursor1:
            if(arg_print == 'Y'):
                print('full record row1: ', row1)
            ## create temporary dictionary of from/to exon positions and count
            wrk_dict_mrnafromtoexon[str(row1['_id']['exonstart']) + str(row1['_id']['exonend'])] = ('N' if(wrk_mrna_count == row1['total']) else 'Y')

        #if(arg_print == 'Y'):
            #print('** print list: ', [x for x in wrk_mrnafromtoexon])
            #print('** print dictionary: ', [x for x in wrk_dict_mrnafromtoexon])

        ## now retrieve each individual gene, mRNA, unwind exons' from/to positions to get a single row for each attribute
        mcursor2 = collect.aggregate([{'$match':{'gene_id':{'$eq':prm_gene}}} , {'$unwind':"$exons"}, {'$sort':{ "exons.start":1, "exons.end":1, 'accession':1}}, {'$project':{'_id':0,  'gene_id':1, 'accession':1, 'exons':1 }}])
        for row2 in mcursor2:
            if(arg_print == 'Y'):
                print('full record row2: ', row2)
            ## Build list of data to return, including "alternative splice (Y/N) flag"
            wrk_from = str(row2['exons']['start'])
            wrk_to =   str(row2['exons']['end'])
            wrk_tuple = (str(row2['accession']), str(row2['gene_id']), str(row2['exons']['start']), str(row2['exons']['end']), (wrk_dict_mrnafromtoexon[wrk_from + wrk_to]))
            self.wrk_mrnafromtoexon.append(wrk_tuple)

            if(arg_print == 'Y'):
                print('print most recent tuple entry (mRNA, gene, from, to, altsplicesite(Y,N) ): ', self.wrk_mrnafromtoexon[-1])

    def __str__(self):
        print("\n\nwithin __str__ ......")
        print("Gene accession# passed in as argument is: ", prm_gene)
        print('Resulting/final tuples within a single main list is:')
        print(self.wrk_mrnafromtoexon)
        return("End of __str__  -------------------\n\n")

#-------------------------------------------------------------------------------
#### begin mainline
## first argument is gene accession number
## second argument is optional, if "Y" print debugging info

### for coding, consider the following for debug:
### if 0, do not print any info
### if 1, print info in __str__ only
### if 2, print detailed info in __init__ and __str__
### if 3, write option 2, but to log file only (not to screen)


# try some of the following gene accession numbers for test data
#prm_gene = str('820')   # single mRNA
#prm_gene = str('6402')   # single mRNA
#prm_gene = str('6003')  # simple example of mixed exon start/end positions
#prm_gene = str('6628')  # for two mRNA, from exon pos. is same, but end pos. is different
#prm_gene = str('862')   # complex example of mixed exon start/end positions
#prm_gene = str('8913')   # probably the most complex, has 28 mRNA associated with this gene accession#

if(len(sys.argv) == 1):
    raise ValueError('Gene accession number is a mandatory for first argument for this program')
else:
    prm_gene = str(sys.argv[1])

prm_print, prm_print_summary = '', ''
# if second (print/debug) argument exists, but is not 'Y', just default to blank/empty string
if(len(sys.argv) == 3):
    if(sys.argv[2] != 'Y'):
        prm_print = ''
    else:
        prm_print = sys.argv[2]

s = class_altsplice(prm_gene, prm_print)

if(prm_print == 'Y'):
    print(s)
