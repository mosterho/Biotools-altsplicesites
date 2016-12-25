#Biotools/Alternative Splice Sites: Marty Osterhoudt's contribution to Dr. Bagga and Dr. Frees' Bioinformatics project
##Fall semester, 2016, Ramapo College of NJ

**Biotools** is a project of Ramapo College of NJ professors Dr. Frees and Dr. Bagga (convener of the Bioinformatics program). Throughout the duration of the project, contributions were made by three of my fellow students over the course of a couple semesters.

The existing project currently consists of a single MongoDB database "chrome" with several collections. These collections include "alignments", "gene", "mrna", "seedlog", and "seq". My contribution to the project was to create a collection of alternative splice sites named "exons".

##The deliverables for this portion of the project:
* The definition for the new "exon" collection was created by Dr. Frees. The attributes are similar to the "mrna" collection, but more conducive to finding alternative splice sites;
* create a Python3 module that can retrieve "mrna" data, including an "alternative splice flag Y/N", and return the values to the calling program;
* create a Python3 module that reads the "mrna" data, calls the module above, and inserts data into the new "exons" collection.

##Learning objectives/requirements:
* Create a Linux environment to house my portion of the project;
* Follow the instructions to successfully install the current version of Biotools in the Linux environment;
* Utilize Github to share my contributions ("exons" collection, programs, etc.);
* Update existing documentation where necessary;
* Keep Dr. Frees apprised of my progress with weekly status updates (minimum), either in-person or email.

##The steps taken during the project:
* Meet with Dr. Frees for a "kickoff" to the semester;
* Create a VMware guest "Mint64bit01" on my personal computer;
* Create my own repository on Github;
* Follow the instructions and install the main components of the Biotools (note: please see the results of each step of the installation process below);
* Document each step taken, noting where the steps did not work (previous installs were performed on Windows and Apple);
* Consider using dbSNP and EST databases from NCBI, elected to use existing mrna collection;
* Pseudocode was written that describes how an alternative splice splice site could be determined from the mrna collection:

  1. Allow a single gene passed in as an argument, along with the ability to print debugging information;
  2. read mrna collection, retrieve gene#, mrna accession#, and individual exon beginning and ending positions;
  3. rearrange the data collected for each mRNA, gene, exon from position, exon to position, and altsplicesite(Y,N), using count of each start/end position to determine if an alternative splice site;
  4. return the information as tuples within a list.

* Go through MongoDB website, observe examples;
* Create a series of trial and error steps of learning MongoDB using the mrna collection;
* Create the program above in Python3 called "retrieve_altsplicesite.py";
* Create "test_retrievealtsplicesites.py" that tests use of "retrieve" program as a separate module.
* Create "seed_altsplice.py" program that utilizes the retrieve program/module to write to the "exons" collection
* Create "purge_altsplicesites.py" that will perform Mongo "remove" of "exons" documents based on organism and geneid arguments
* Found bug in "seed_altsplice.py" (was writing too many documents for each mrna), fixed.
* Continuous debugging and updates to documentation

##Examples of running programs
The following screen capture shows the result of calling the "retrieve_altsplicesite.py" module.

![screen cap of retrieving alternative splice site data](/docs/retrieve_altsplicesite.jpg)

The following two screen captures shows the result of calling the "seed_altsplice.py" module, but for one gene. (needed two screen caps due to the size of the output)

![screen cap of the seed process for the "exons" collection](/docs/exons_seed1.jpg)
![screen cap of the seed process for the "exons" collection](/docs/exons_seed2.jpg)



---
The following is an ad hoc "diary" of the various commands I ran while learning MongoDB

in MongoDB, start on terminal command line:

`db.mrna.find({}, {accession:1})  ## need empty set {} to include all rows, but just project the accession number
db.mrna.find({}, {accession:1,gene_id:1, _id:0}).sort({accession:1})  
db.mrna.find({}, { accession:1, gene_id:1, chrom:1, _id:0}).sort({chrom:1, gene_id:1})
db.mrna.find({gene_id:/^872/}, {gene_id: 1} )
db.mrna.find({gene_id:/^872/}, {gene_id: 1} ).sort({gene_id: -1})

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


the following works well.

db.mrna.aggregate([  {$unwind :"$exons"}, {$project:{_id:0, gene_id:1, accession:1, exons:1}}  ])
db.mrna.aggregate([  {$unwind :"$exons"}, {$project:{_id:0, exons:1, gene_id:1, accession:1}}, {$match:{gene_id: {$eq:"522"}}}  ])
db.mrna.aggregate([  {$unwind :"$exons"}, {$match:{gene_id: {$eq:"522"}}}  , {$project:{_id:0, exons:1, gene_id:1, accession:1}}])

db.mrna.aggregate([  {$match:{gene_id: {$eq:"522"}}} , {$unwind:"$exons"},  {$project:{_id:0,  gene_id:1, accession:1, exons:1}}])
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

or...
db.mrna.aggregate([  {$match:{gene_id: {$eq:"522"}}} , {$unwind:"$exons"}, {$sort:{"exons.start":1}}, {$project:{_id:0,gene_id:1, accession:1, exons:1 }}   ])


different geneid, smaller result set, changed sort order
also use geneids 8913 (large result set), 7412  (moderate)

db.mrna.aggregate([  {$match:{gene_id: {$eq:"6003"}}} , {$unwind:"$exons"}, {$sort:{accession:1, "exons.start":1}}, {$project:{_id:0,  gene_id:1, accession:1, exons:1 }} ])


best sort to determine if gene/exon positions have alternative splice sites, but must
join with a summary (gene/accession#)

db.mrna.aggregate([  {$match:{gene_id: {$eq:"6003"}}} , {$unwind:"$exons"}, {$sort:{ "exons.start":1, "exons.end":1, accession:1}}, {$project:{_id:0,  gene_id:1, accession:1, exons:1 }} ])
{ "exons" : { "start" : 192605268, "end" : 192605447 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192605268, "end" : 192605447 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192606720, "end" : 192606790 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192606720, "end" : 192606790 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192607294, "end" : 192607333 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192613461, "end" : 192613529 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192613461, "end" : 192613529 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192617056, "end" : 192617117 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192617056, "end" : 192617117 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192627331, "end" : 192627497 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192627331, "end" : 192627497 }, "accession" : "NM_144766.2", "gene_id" : "6003" }
{ "exons" : { "start" : 192628468, "end" : 192629441 }, "accession" : "NM_002927.4", "gene_id" : "6003" }
{ "exons" : { "start" : 192628468, "end" : 192629441 }, "accession" : "NM_144766.2", "gene_id" : "6003" }


db.mrna.aggregate([ {$match:{gene_id:{$eq:"6003"}}}, {$unwind:"$exons"}, {$group: {_id: {gene_id:"$gene_id", "exonstart":"$exons.start", "exonend":"$exons.end"}, total:{$sum: 1 }}}, {$sort:{exonstart:1, exonend:1}} ])
{ "_id" : { "gene_id" : "6003", "exonstart" : 192607294, "exonend" : 192607333 }, "total" : 1 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192628468, "exonend" : 192629441 }, "total" : 2 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192627331, "exonend" : 192627497 }, "total" : 2 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192613461, "exonend" : 192613529 }, "total" : 2 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192606720, "exonend" : 192606790 }, "total" : 2 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192617056, "exonend" : 192617117 }, "total" : 2 }
{ "_id" : { "gene_id" : "6003", "exonstart" : 192605268, "exonend" : 192605447 }, "total" : 2 }


how to create a collection using "insert"
db.altsplicesitestest.insert({start: 0, end: 9999, accession:"NM_999999", gene_id:"9999", organism:"homo Sapiens", build:"37", altsplicesiteYN: "N"})
db.altsplicesitestest.find()
`
