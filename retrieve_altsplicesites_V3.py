### Determine which mRNA contain alternative splice sites
### from the mRNA collections
### pass in gene id/accession number (numeric from NCBI) to this script,
### count the number of mRNA, then determine if any of the exons'
### from and to positions are different and suggest an
### alternative splice site.

### Marty Osterhoudt
### for an independent research project with Dr. Frees
### Fall 2016 semester
### Ramapo College of NJ

#import urllib.request
#import shutil
#import requests
import pprint

class class_altsplice:
    def __init__(self, arg_gene):
        from pymongo import MongoClient
        self.client = MongoClient()
        self.db = self.client.chrome
        self.collect = self.db.mrna

        self.prm_gene = arg_gene
        self.prm_gene = 862
        #prm_gene = '820'
        #prm_gene = '6402'

        mcursor = collect.aggregate([ {"$match":{"gene_id":{"$eq": prm_gene}}}, {"$unwind":"$exons"}, {"$group": {"_id": {"gene_id":"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, "total":{"$sum":1}}}, {"$sort":{"exonstart":1, "exonend":1}} ])

        print("Start print of individual columns for mcursor")
        for record in mcursor:
            print("full record value is: ", record)

            print("\n\nStart print of full record mcursor1")
            mcursor1 = collect.aggregate([{'$match':{'gene_id': {'$eq':self.prm_gene}}} , {'$unwind':"$exons"}, {'$sort':{ "exons.start":1, "exons.end":1, 'accession':1}}, {'$project':{'_id':0,  'gene_id':1, 'accession':1, 'exons':1 }}])
            for record in mcursor1:
                print("full record: ",record)
        return rtn_tuple

    def __str__(self):
        print("nothing to see here... yet")

####### begin mainline

prm_gene = int(sys.argv[1])
print ("\n\nArgument passed in is: ", prm_gene)
rtn_result = class_altsplice(prm_gene)

return rtn_result
