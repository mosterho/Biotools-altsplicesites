Biotools_marty

This shows the progression I've made in learning MongoDB


in MongoDB, start on terminal command line:

mongo chrome
db.mrna.find({}, {accession:1})  ## need empty set {} to include all rows, but just project the accession number
db.mrna.find({}, {accession:1,gene_id:1, _id:0}).sort({accession:1})  ## empty set for include, sort by accession number
db.mrna.find({}, { accession:1, gene_id:1, chrom:1, _id:0}).sort({chrom:1, gene_id:1})
db.mrna.find({gene_id:/^872/}, {gene_id: 1} )
db.mrna.find({gene_id:/^872/}, {gene_id: 1} ).sort({gene_id: -1})

###  
db.mrna.find({gene_id:"149628"}, {  _id:0}).pretty()

db.mrna.aggregate([ {$project:{gene_id:1}} ])
db.mrna.aggregate([ {$project:{gene_id:1, accession:1, _id:0}}  ])

db.mrna.aggregate([ {$group: {_id: "$gene_id", total: {$sum: 1 }}} ])
db.mrna.aggregate([ {$group: {_id: "$gene_id", total: {$sum: 1 }}}, {$match: {total: {$lte: 5}}}, {$sort : {total : -1 }} ])
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


## the following works well. Note that the documents print column info in the order of the original document,
##  regardless of how the $project is specified.
db.mrna.aggregate([  {$unwind :"$exons"}, {$project:{_id:0, gene_id:1, accession:1, exons:1}}  ])
db.mrna.aggregate([  {$unwind :"$exons"}, {$project:{_id:0, exons:1, gene_id:1, accession:1}}, {$match:{gene_id: {$eq:"522"}}}  ])
db.mrna.aggregate([  {$unwind :"$exons"}, {$match:{gene_id: {$eq:"522"}}}  , {$project:{_id:0, exons:1, gene_id:1, accession:1}}])
db.mrna.aggregate([  {$match:{gene_id: {$eq:"522"}}} , {$unwind:"$exons"},  {$project:{_id:0,  gene_id:1, accession:1, exons:1 }}])
{ "exons" : { "start" : 27107798, "end" : 27107965 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107626, "end" : 27107965 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107300, "end" : 27107965 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27107250, "end" : 27107965 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107164, "end" : 27107965 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003703.1", "gene_id" : "522" }

##  or... 
db.mrna.aggregate([  {$match:{gene_id: {$eq:"522"}}} , {$unwind:"$exons"}, {$sort:{"exons.start":1}}, {$project:{_id:0,  gene_id:1, accession:1, exons:1 }}   ])
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27096791, "end" : 27096988 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27097537, "end" : 27097661 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003697.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27101942, "end" : 27102112 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107164, "end" : 27107965 }, "accession" : "NM_001003703.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107250, "end" : 27107965 }, "accession" : "NM_001003701.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107300, "end" : 27107965 }, "accession" : "NM_001685.4", "gene_id" : "522" }
{ "exons" : { "start" : 27107626, "end" : 27107965 }, "accession" : "NM_001003696.1", "gene_id" : "522" }
{ "exons" : { "start" : 27107798, "end" : 27107965 }, "accession" : "NM_001003697.1", "gene_id" : "522" }

## different geneid, smaller result set, changed sort order
##  also use geneids 8913 (large result set), 7412  (moderate)
db.mrna.aggregate([  {$match:{gene_id: {$eq:"6003"}}} , {$unwind:"$exons"}, {$sort:{accession:1, "exons.start":1}}, {$project:{_id:0,  gene_id:1, accession:1, exons:1 }}   ])
{ "exons" : { "start" : 192605268, "end" : 192605447 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192606720, "end" : 192606790 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192607294, "end" : 192607333 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192613461, "end" : 192613529 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192617056, "end" : 192617117 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192627331, "end" : 192627497 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192628468, "end" : 192629441 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192605268, "end" : 192605447 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192606720, "end" : 192606790 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192613461, "end" : 192613529 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192617056, "end" : 192617117 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192627331, "end" : 192627497 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192628468, "end" : 192629441 }, "accession" : "NM_144766.2", "gene_id" : "6003" }


##  how to create a collection using "insert"
db.altsplicesitestest.insert({start: 0, end: 9999, accession:"NM_999999", gene_id:"9999", organism:"homo Sapiens", build:"37", altsplicesiteYN: "N"})
db.altsplicesitestest.find()
