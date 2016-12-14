
# Create program to write alternative splice site collection.

# From the chrome database,
# 1. read the gene collection, group by gene_id
# 2. call the "retrieve_altsplicesites" module using
# 3. loop though returned tuple,
#
# create an "exons" collection.

### Marty Osterhoudt
### independent research project with Dr. Frees
### Fall 2016 semester
### Ramapo College of NJ

import sys, retrieve_altsplicesites as alt

def get_data(arg_print=''):

    # create objects required to access MongoDB
    from pymongo import MongoClient
    client = MongoClient()
    db = client.chrome
    collect = db.mrna
    collect_exons = db.exons

    return_list = []

    # read mrna collection, group by gene and organism
    result = collect.aggregate([{"$group":{"_id":{"gid":"$gene_id", "org":"$organism"}}}])
    for x in result:
        return_list = alt.get_altsplice(x['_id']['gid'])
        # if anything is returned, continue
        if(return_list):
            if(arg_print == 'Y'):
                print("\nfirst loop: ",x,"\nreturn_list:  ",return_list)

            # get tuple info from module that was called
            for y in return_list[:]:
                if(arg_print == 'Y'):
                    print(y[0],' ',y[1],' ', y[2],' ', y[3],' ',y[4])

                # retrieve whole mRNA collection row/document by gene_id
                # (the initial aggregate in the first line only retrieved the gene_id)
                readthis = collect.aggregate([ {"$match":{"gene_id":{"$eq":y[1]}}} ])
                for z in readthis:
                    if(arg_print == 'Y'):
                        print("\nsecond loop: ",z)


#db.mrna.aggregate([{$unwind:"$exons"}])
#db.mrna.aggregate([{ $project:{"gid":"$gene_id", "acc":"$accession"}}])
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{"gid":"$gene_id", "acc":"$accession", "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:"$diffexonstart"}}  ]).pretty()
#db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:{diffes:'$diffexonstart', diffee:'$diffexonend'}, total:{$sum:1}}}  ]).pretty()


#-------------------------------------------------------------------------
### mainline
#-------------------------------------------------------------------------
tmp_input_print = ''
if(len(sys.argv) > 1):
    if(sys.argv[1] != 'Y'):
        tmp_input_print = ''
    else:
        tmp_input_print = 'Y'

get_data(tmp_input_print)
