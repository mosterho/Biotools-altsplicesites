#!/bin/bash

cd ../NCBIDownload/H_Sapiens_Chromosome
mv hs_ref_GRCh38.p7_chr1.fa chromosome01
mongofiles --host=mongodb -d=Chromosome -r put chromosome01
mv chromosome01 hs_ref_GRCh38.p7_chr1.fa
