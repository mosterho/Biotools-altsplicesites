
# Create program to write alternative splice site collection.

# arguments:
# 1. organism (e.g., Homo sapiens)
# 2. gene_id: can enter a single gene_id, or pass in an empty string
# 3. print flag: if "Y" will print debugging information

# process is as follows:
# From the chrome database,
# 1. read the gene collection, group by gene_id
# 2. call the "retrieve_altsplicesites" module using gene_id
# 3. loop though returned tuples to obtain gene
# 4. retrieve detailed mRNA collection info and unwind the exon data
#    (will now have multiple rows/documents for each mRNA)
# 5.
#
# create an "exons" collection.

### Marty Osterhoudt
### independent research project with Dr. Frees
### Fall 2016 semester
### Ramapo College of NJ

import sys, retrieve_altsplicesites as alt

def get_data(arg_organism, arg_gene='', arg_print=''):

    # create objects required to access MongoDB
    from pymongo import MongoClient
    client = MongoClient()
    db = client.chrome
    collect = db.mrna
    collect_altsplice = db.altsplicesites

    return_list = []
    switched_list = []

    # 1. read mrna collection, group by gene
    if(arg_gene == ''):
        result = collect.aggregate([{"$match":{"organism":arg_organism}}, {"$group":{"_id":{"gid":"$gene_id", "org":"$organism"}}}])
    else:
        result = collect.aggregate([{"$match":{"organism":arg_organism, "gene_id":arg_gene}}, {"$group":{"_id":{"gid":"$gene_id", "org":"$organism"}}}])
    for x in result:
        # 2. retrieve alt splice site info for gene_id
        return_list = alt.get_altsplice(x['_id']['gid'])
        # if anything is returned, continue
        if(return_list):
            if(arg_print == 'Y'):
                print("\nEntire tuple returned from retrieve_altsplicesites module: ",x,"\nreturn_list:\n  ",return_list)

            # 3. get tuple info from module (determines flag for alternative splice site)
            for y in return_list[:]:
                if(switched_list[y[1]][y[2]][y[3]][y[4]]):
                    switched_list[y[1]][y[2]][y[3]][y[4]].append(y[0])
                else:
                    switched_list[y[1]][y[2]][y[3]][y[4]].append(y[0])
                if(arg_print == 'Y'):
                    print('Return list/tuple from module ',y[0],' ',y[1],' ', y[2],' ', y[3],' ',y[4])
                    print('Switched list', switched_list)

                # 4. retrieve all mRNA collection document info by gene_id, also
                # unwind the exons to get multiple lines per gene and mRNA
                ################readthis = collect.aggregate([ {"$match":{"gene_id":str(y[1]), "accession":str(y[0]), "exons.start":int(y[2]), "exons.end":int(y[3])} }, {"$unwind":"$exons"} ])
                readthis = collect.find({"gene_id":str(y[1]), "accession":str(y[0]), "exons.start":int(y[2]), "exons.end":int(y[3])},{"_id":0, "gene_id":1, "accession":1, "exons.start":1, "exons.end":1})
                for z in readthis:
                    if(arg_print == 'Y'):
                        print("\nReturn list/tuple second loop: ",z)
                        #print("\nReturn list/tuple second loop with unwind: ")

                    #5. now roll-up and merge exons with appropriate value for alt splice flag
                    #insert_confirm = collect_altsplice.insert({"gene_id":str(y[1]), "accession":str(y[0]), "exons_start":int(y[2]), "exons_end":int(y[3])})


#-------------------------------------------------------------------------
### mainline
#-------------------------------------------------------------------------

tmp_organism = ''
tmp_gene = ''
tmp_input_print = ''
if(len(sys.argv) > 1):
    tmp_organism = sys.argv[1]
    tmp_gene = sys.argv[2]
    if(sys.argv[3] != 'Y'):
        tmp_input_print = ''
    else:
        tmp_input_print = 'Y'

get_data(tmp_organism, tmp_gene, tmp_input_print)
