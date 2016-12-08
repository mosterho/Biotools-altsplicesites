
# Create program to write alternative splice collection
# From the chrome database, read the gene and mrna collections
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

    #result = collect.find()
    #for x in result:
        #return_list = alt.get_altsplice(x['gene_id'])

    result_startendmrna = collect.aggregate([{'$unwind':"$exons"}, "$group":{"$start", "$end"}])


db.mrna.aggregate([{$unwind:"$exons"}])
db.mrna.aggregate([{ $project:{"gid":"$gene_id", "acc":"$accession"}}])
db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{"gid":"$gene_id", "acc":"$accession", "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonsstart":"$exons.start", "diffexonend":"$exons.end"}}]).pretty()
db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:"$diffexonstart"}}  ]).pretty()
db.mrna.aggregate([ {$unwind:"$exons"}, {$project:{gene_id:1, accession:1, "diffexonstart":"$exons.start", "diffexonend":"$exons.end"}}, {$group:{_id:{diffes:'$diffexonstart', diffee:'$diffexonend'}, total:{$sum:1}}}  ]).pretty()


#-------------------------------------------------------------------------
### mainline
#-------------------------------------------------------------------------

get_data('Y')
