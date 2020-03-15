##

import sys
import re


search_this = '>gi|53828740|ref|NP_001005484.1| olfactory receptor 4F5 [Homo sapiens]'
wrk_fieldbreak  = re.findall('(?<=[|]).*?(?=[|])', search_this, re.DOTALL)
print('fieldbreak: ', wrk_fieldbreak)
wrk_fieldbreak  = re.findall('([^|]*)$', search_this, re.DOTALL)
print('fieldbreak: ', wrk_fieldbreak)


#>gi|53828740|ref|NP_001005484.1| olfactory receptor 4F5 [Homo sapiens]
#>gi|1034563939|ref|XP_016858498.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901762|ref|XP_011542108.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901764|ref|XP_011542109.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901766|ref|XP_011542110.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|1034563943|ref|XP_016858499.1| PREDICTED: putative ATP-dependent RNA helicase DDX12 isoform X2 [Homo sapiens]
#>gi|119943152|ref|NP_001005221.2| olfactory receptor 4F3/4F16/4F29 [Homo sapiens]
#>gi|767908050|ref|XP_011540840.1| PREDICTED: proline-rich extensin-like protein EPR1 isoform X1 [Homo sapiens]
