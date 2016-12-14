
# Create program to write alternative splice site collection.

# arguments:
# 1. gene_id: can enter a single gene_id, or pass in an empty string
# 2. print flag: if "Y" will print debugging information

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

def get_data(arg_gene='', arg_print=''):

    # create objects required to access MongoDB
    from pymongo import MongoClient
    client = MongoClient()
    db = client.chrome
    collect = db.mrna
    collect_exons = db.exons

    return_list = []

    # 1. read mrna collection, group by gene and organism
    if(arg_gene == ''):
        result = collect.aggregate([{"$group":{"_id":{"gid":"$gene_id", "org":"$organism"}}}])
    else:
        result = collect.aggregate([{"$match":{"gene_id":{"$eq":arg_gene}}}, {"$group":{"_id":{"gid":"$gene_id", "org":"$organism"}}}])
    for x in result:

        # 2. retrieve alt splice site info for gene_id
        return_list = alt.get_altsplice(x['_id']['gid'])
        # if anything is returned, continue
        if(return_list):
            if(arg_print == 'Y'):
                print("\nEntire tuple returned from module:  ",x,"\nreturn_list:  ",return_list)

            # 3. get tuple info from module (determines flag for alternative splice site)
            for y in return_list[:]:
                if(arg_print == 'Y'):
                    print('Return list/tuple from module ',y[0],' ',y[1],' ', y[2],' ', y[3],' ',y[4])

                # 4. retrieve all mRNA collection document info by gene_id, also
                # unwind the exons to get multiple lines per gene and mRNA
                readthis = collect.aggregate([ {"$match":{"gene_id":{"$eq":y[1]}}}, {"$unwind":"$exons"} ])
                for z in readthis:
                    if(arg_print == 'Y'):
                        print("\nReturn list/tuple second loop with unwind: ",z)
                    #5. now roll-up exons with appropriate value for alt splice flag


#db.mrna.aggregate([{$unwind:"$exons"}])
#db.mrna.aggregate([{ $project:{"gid":"$gene_id", "acc":"$accession"}}])
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{"gid":"$gene_id", "acc":"$accession", "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:"$diffexonstart"}}  ]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:{diffes:'$diffexonstart', diffee:'$diffexonend'}, total:{$sum:1}}}  ]).pretty()


#-------------------------------------------------------------------------
### mainline
#-------------------------------------------------------------------------

tmp_gene = ''
tmp_input_print = ''
if(len(sys.argv) > 1):
    tmp_gene = sys.argv[1]
    if(sys.argv[2] != 'Y'):
        tmp_input_print = ''
    else:
        tmp_input_print = 'Y'

get_data(tmp_gene, tmp_input_print)
