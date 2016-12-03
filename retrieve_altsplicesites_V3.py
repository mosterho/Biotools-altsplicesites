### Determine which mRNA contain alternative splice sites
### from the mrna collection in chrome database
### pass in gene/accession number (numeric from NCBI) to this script,
### determine if any of the exons'from and to positions
### are different and suggest an alternative splice site.
### return the result as a list (not tuple) that includes
### the accession#, mRNA, from/to exon positions, and
### alternative splice site flag (Y/'')

### Marty Osterhoudt
### for an independent research project with Dr. Frees
### Fall 2016 semester
### Ramapo College of NJ

import sys
#import os
#import urllib.request
#import shutil
#import requests

class class_altsplice:
    def __init__(self, arg_gene, arg_print=''):
        # create objects required to access MongoDB
        from pymongo import MongoClient
        client = MongoClient()
        db = client.chrome
        collect = db.mrna
        prm_gene = arg_gene

        rtn_list = []
        wrk_mrna_count = 0

        ## gcursor should have a single row, which is the count of mrna for a gene
        gcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$group": {"_id": {"gene_id":"$gene_id"}, "total_g":{"$sum":1}}} ])
        for g_row in gcursor:
            wrk_mrna_count = g_row['total_g']
            if(arg_print == 'Y'):
                print('gcursor full row: ',g_row)
        # keep indent here if printing, it's possible row count could be zero
        if(arg_print == 'Y'):
            print('Number of mRNA associated with gene ',prm_gene,' is: ',wrk_mrna_count)

        ###  if the count is greater than 1, there are two or more mrna
        ###  where there might be an alternative splice site
        if(wrk_mrna_count > 1):
            wrk_row_count = 0;
            #mcursor1 = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1,"exonend":1}}])
            mcursor1 = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$unwind":"$exons"}, {"$sort":{"exonstart":1,"exonend":1}}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}} ])
            for row1 in mcursor1:
                if(wrk_row_count == 0):
                    wrk_row_count = row1['total']
                # if the row counts don't match, possible alternative splice site
                if(wrk_row_count != row1['total']):
                    print
                if(arg_print == 'Y'):
                    print('full record row1: ', row1)

            mcursor2 = collect.aggregate([{'$match':{'gene_id':{'$eq':prm_gene}}} , {'$unwind':"$exons"}, {'$sort':{ "exons.start":1, "exons.end":1, 'accession':1}}, {'$project':{'_id':0,  'gene_id':1, 'accession':1, 'exons':1 }}])
            for row2 in mcursor2:
                if(arg_print == 'Y'):
                    print('full record row2: ', row2)

        #return rtn_list

    def __str__(self):
        print("\n\nIn __str__, nothing to see here... yet")
        return ("End of __str__ print  -------------------\n\n")


####### begin mainline
## pass in one argument as gene accessions number
## the second is optional, if "Y" print debugging

if(len(sys.argv) == 1):
    prm_gene = str('862')
    #prm_gene = str('820')
    #prm_gene = str('6402')
    #prm_gene = str('6003')  # nice example of mixed exon start/end positions

else:
    prm_gene = str(sys.argv[1])

prm_print = ''
if(len(sys.argv) == 3 and sys.argv[2] != ''):
    prm_print = sys.argv[2]
if(prm_print == 'Y'):
    print ("\nGene accession# passed in is: ", prm_gene)

s = class_altsplice(prm_gene, prm_print)
'''
if(prm_print == 'Y'):
    print(s)

return rtn_result
'''
