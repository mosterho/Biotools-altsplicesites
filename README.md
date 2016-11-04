Biotools_marty

in MongoDB, start on terminal command line:

mongo chrome
db.mrna.find({}, {accession:1})  ## need empty set {} to include all rows, but just project the accession number
db.mrna.find({}, {accession:1,gene_id:1, _id:0}).sort({accession:1})  ## empty set for include, sort by accession number
db.mrna.find({}, { accession:1, gene_id:1, chrom:1, _id:0}).sort({chrom:1, gene_id:1})
db.mrna.find({gene_id:/^872/}, {gene_id: 1} )
db.mrna.find({gene_id:/^872/}, {gene_id: 1} ).sort({gene_id: -1})

db.mrna.aggregate([ {$group: {_id: "$gene_id", total: {$sum: 1 }}} ])
db.mrna.aggregate([ {$group: {_id: "$gene_id", total: {$sum: 1 }}}, {$sort : {total : -1 }} ])
{ "_id" : "8913", "total" : 28 }
{ "_id" : "1390", "total" : 26 }
{ "_id" : "7404", "total" : 25 }
{ "_id" : "775", "total" : 23 }
{ "_id" : "27185", "total" : 23 }
{ "_id" : "1500", "total" : 22 }
{ "_id" : "5152", "total" : 20 }
{ "_id" : "4582", "total" : 20 }
{ "_id" : "7422", "total" : 18 }
{ "_id" : "1756", "total" : 18 }
{ "_id" : "10018", "total" : 18 }
{ "_id" : "6487", "total" : 18 }
{ "_id" : "3084", "total" : 17 }
{ "_id" : "1837", "total" : 17 }
{ "_id" : "627", "total" : 17 }
{ "_id" : "140690", "total" : 16 }
{ "_id" : "9643", "total" : 16 }
{ "_id" : "2104", "total" : 16 }
{ "_id" : "55638", "total" : 15 }
{ "_id" : "862", "total" : 15 }



###  
db.mrna.find({gene_id:"149628"}, {  _id:0}).pretty()


db.altsplicesitestest.insert({start: 0, end: 9999, accession:"NM_999999", gene_id:"9999", organism:"homo Sapiens", build:"37", altsplicesiteYN: "N"})
db.altsplicesitestest.find()
