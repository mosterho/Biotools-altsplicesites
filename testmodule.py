### test the retrieve as a module
### ensure this program can get the return
### Marty Osterhoudt

import sys
#import retrieve_altsplicesites as alt
import retrieve_altsplicesites_V4 as altV4

#-------------------------------------------------------------------------------
#### begin mainline

# try some of the following gene accession numbers for test data
# 820   # single mRNA
# 6402  # single mRNA
# 6003  # simple example of mixed exon start/end positions
# 6628  # for two mRNA, from exon pos. is same, but end pos. is different
# 862   # complex example of mixed exon start/end positions
# 8913  # probably the most complex, has 28 mRNA associated with this gene accession#

wrk_testlist = [820,6402,6003,6628,862,8913]
for x in wrk_testlist:
    rtn_list = altV4.get_altsplice(str(x), '')
    print('\n*---------------------------------------------------\n** From within testmodule, print:',rtn_list)
