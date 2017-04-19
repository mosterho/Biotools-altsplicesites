## Read the Mouse Alkaline Phosphatase Gene in all 6 possible reading frames, to
## determine the correct reading frame (i.e. the one with the
## longest open reading frame -- i.e. w/o stop codons)
## Your output should show the nucleic acid sequence with the amino acid (either 1 letter or 3 letter code) directly
## below the nucleotide sequence. (So you'd want to display a multiple of 3 nucleotides per line.)
## You should also report the length of the expected amino acid sequence.
## To split a sequence into codons remember your reg. exps.
## my $dna = 'agccctgatagcttagcgggatcg';
## my @codons = $dna =~ /(.{3})/g;
## say foreach (@codons);


#!usr/bin/perl
use strict;
use diagnostics;

my %CODON_TABLE = (
TCA => 'S',TCG => 'S',TCC => 'S',TCT => 'S',
TTT => 'F',TTC => 'F',TTA => 'L',TTG => 'L',
TAT => 'Y',TAC => 'Y',TAA => '*',TAG => '*',
TGT => 'C',TGC => 'C',TGA => '*',TGG => 'W',
CTA => 'L',CTG => 'L',CTC => 'L',CTT => 'L',
CCA => 'P',CCG => 'P',CCC => 'P',CCT => 'P',
CAT => 'H',CAC => 'H',CAA => 'Q',CAG => 'Q',
CGA => 'R',CGG => 'R',CGC => 'R',CGT => 'R',
ATT => 'I',ATC => 'I',ATA => 'I',ATG => 'M',
ACA => 'T',ACG => 'T',ACC => 'T',ACT => 'T',
AAT => 'N',AAC => 'N',AAA => 'K',AAG => 'K',
AGT => 'S',AGC => 'S',AGA => 'R',AGG => 'R',
GTA => 'V',GTG => 'V',GTC => 'V',GTT => 'V',
GCA => 'A',GCG => 'A',GCC => 'A',GCT => 'A',
GAT => 'D',GAC => 'D',GAA => 'E',GAG => 'E',
GGA => 'G',GGG => 'G',GGC => 'G',GGT => 'G'
);

my $record = '';   # used during read of each record in genbank file
my $origin_read = '0';   # flag to signal start of reading nucleotide sequence (ORIGIN)
my @tempdata = ();   # temporary array to hold nucleotide sequence
my $nucleotide_string = "";   # full nucleotide string read from genbank file
my @nucleotide_data = ();   # full nucleotide data as array

## read genbank file, find
## sequence data and store in string.
## data starts with "ORIGIN" (around line 99) of genbank file
## read and store nucleotide data until "//" is read.

my $filetouse = $ARGV[0];
open (GBFILE, $filetouse) or die "\n\n*** Cannot open genbank file: $! \n\n";

while(<GBFILE>) {
	chomp($record = $_);
	if(substr($record,0,6) eq 'ORIGIN') {
		$origin_read = '1';
	}
	elsif ($origin_read && substr($record,0,2) ne '//') {
		@tempdata = substr($record,10) =~ m/(\w+)/g; # include only words, no spaces
		foreach my $temprow (@tempdata) {
			$nucleotide_string = $nucleotide_string . $temprow; #build single nucleotide string
		}
	}
	elsif ($origin_read && substr($record,0,2) eq '//') {
		last;
	}
}

close GBFILE;
####   print full nucleotide string for easier reference
print "\nFull nucleotide string is:\n$nucleotide_string\n";

##############################
##  Setup 6 reading frames, 3 forward and 3 reverse.
##  Could have used a loop within a loop (F/R and frame),
##  but this seems more straightforward.
my $frameF1 = '';
my $frameF2 = '';
my $frameF3 = '';
my $frameR1 = '';
my $frameR2 = '';
my $frameR3 = '';
my $frame_longest = '';
my $frame_to_print = '';

##  sub_frame subroutine determines the longest reading frame
##  for the sequence passed in as argument.
##  arg0 = string  arg1 = Forward or Reverse  arg2 = offset of string
$frameF1 = sub_frame($nucleotide_string, 'F', 0);
$frameF2 = sub_frame($nucleotide_string, 'F', 1);
$frameF3 = sub_frame($nucleotide_string, 'F', 2);
$frameR3 = sub_frame($nucleotide_string, 'R', 0);
$frameR2 = sub_frame($nucleotide_string, 'R', 1);
$frameR1 = sub_frame($nucleotide_string, 'R', 2);

## find longest of the six frames
## initially set $frame_longest to first forward frame
$frame_longest = $frameF1;
$frame_to_print = 'Forward frame1';
if (length($frameF2) > length($frame_longest)) {
	$frame_longest = $frameF2;
	$frame_to_print = 'Forward frame2';
}
if (length($frameF3) > length($frame_longest)) {
	$frame_longest = $frameF3;
	$frame_to_print = 'Forward frame3';
}
if (length($frameR3) > length($frame_longest)) {
	$frame_longest = $frameR3;
	$frame_to_print = 'Reverse frame3';
}
if (length($frameR2) > length($frame_longest)) {
	$frame_longest = $frameR2;
	$frame_to_print = 'Reverse frame2';
}
if (length($frameR1) > length($frame_longest)) {
	$frame_longest = $frameR1;
	$frame_to_print = 'Reverse frame1';
}


######################################################################
## print nucleotides 60 residues per line, then
## for each line, determine the corresponding 1 letter codon
######################################################################

@nucleotide_data = $frame_longest =~ m/([atcg]{3})/g;
my @codonarray = ();   # tracks codons to print below nucleotide data
print "\n Longest ORF is: $frame_to_print";
##  remember: $# variables hold last index, add/multiply numbers to get true count.
print "\n Nucleotide length: " . ($#nucleotide_data * 3 + 3);
print "\n Amino acid sequence length: " . ($#nucleotide_data + 1) ;
print "\n The following is the longest open reading frame found:\n";

###  loop through longest ORF array, print each nucleotide up to 60 chars per line
###  Once 60 nucleotides printed, print corresponding single letter codon.
for (my $i = 0; $i <= $#nucleotide_data; $i++) {
	print "$nucleotide_data[$i] ";
	push(@codonarray, $CODON_TABLE{("\U$nucleotide_data[$i]\E")} );
	### if 60 nucleotides reached,
	### print the associated codons.
	if(($i+1)%20 == 0 and $i > 0) {
		printf "%5d", $i*3+3;   ## print nucleotide counter at end of line.
		print "\n";
		for (my $j = 0; $j < 20; $j++) {
			print "$codonarray[$j]   ";   ## print codons under their respective nucleotides
		}
		print "\n";
		@codonarray = ();  ## reset codon arrary for printing
	}
}
##### print last line of codons
print "\n";
for (my $j = 0; $j <= $#codonarray; $j++) {
	print "$codonarray[$j]   ";
}

print "\n\n";

##############################################################
### end of mainline
##############################################################

##############################################################
# find the best/longest ORF that is passed in
sub sub_frame {
	my $subarg = $_[0];   ## nucleotide string
	my $direction = $_[1];  ## Forward or Reverse
	my $offset = $_[2];   ## offset for substring
	my $currentpos = 0;   ## track current position.
	my $lastpos = 0;   ## keep last stop codon position encountered.
	my $beginningpos = 0; # keep track of longest pos, similar to currentpos
	my $longestlen = 0;   ## keep track of longest length ORF encountered

	##  if "R" is passed in as parm,
	##  reverse the nucleotide sequence (polyA tail now at beginning), then create
	##  the complementary sequence (polyA tail becomes a string of t's)
	##  using tr (translate).
	##  Using this technique allows the regex to work in a forward manner
	##  by using the %CODON_TABLE as it is.
	if ($direction eq 'R') {
		my $reverse_nucleotide = reverse($subarg);
		$reverse_nucleotide =~ tr/atcg/tagc/;
		$subarg = $reverse_nucleotide;
	}
	##  nucleotide string is correct sequence,
	##  now substring to length specified in 3rd argument
	$subarg = substr($subarg,$offset);

	##  begin real work --
	##  shift nucleotides to array to determine codon,
	##  then loop thru, looking for stop codon. If found,
	##  set counters and determine length of ORF.
	my @sub_nucleotide_data = $subarg =~ m/([atcg]{3})/g; ## trying something different with regex [atcg].
	foreach my $wrk_nucleotide (@sub_nucleotide_data) {
		if ($CODON_TABLE{("\U$wrk_nucleotide\E")} eq '*') {
			if ($currentpos - $lastpos  > $longestlen) {
				$longestlen = $currentpos - $lastpos ;  # new longest length
				$beginningpos = $lastpos;   # new beginning position
				$lastpos = $currentpos + 3;  # the +3 is to synch-up with the next $currentpos += 3
			}
		}
		$currentpos += 3;
	}

	##  once foreach is complete, check the last "chunk" of nucleotides read, compare and
	##  modify the longestlen and beginningpos if needed.
	if ($currentpos - $lastpos  > $longestlen) {
		$longestlen = $currentpos - $lastpos ;  # new longest length
		$beginningpos = $lastpos;   # new beginning position
	}

	##  return the substring of first argument (i.e. longest reading frame)
	return (substr($subarg, $beginningpos, $longestlen));
}

################################################################################
# Input: tri-nucleotide codon that tRNA reads
# Output: the 3 letter symbolic representation of the corresponding amino acid.
sub translate_codon {
	if ( $_ [ 0 ] =~ / GC[AGCU] /i ) { return 'Ala';} # Alanine;
	if ( $_ [ 0 ] =~ / UGC|UGU /i ) { return 'Cys';} # Cysteine
	if ( $_ [ 0 ] =~ / GAC|GAU /i ) { return 'Asp';} # Aspartic Acid;
	if ( $_ [ 0 ] =~ / GAA|GAG /i ) { return 'Glu';} # Glutamine;
	if ( $_ [ 0 ] =~ / UUC|UUU /i ) { return 'Phe';} # Phenylalanine;
	if ( $_ [ 0 ] =~ / GG[AGCU] /i ) { return 'Gly';} # Glycine;
	if ( $_ [ 0 ] =~ / CAC|CAU /i ) { return 'His';} # Histine (start codon);
	if ( $_ [ 0 ] =~ / AU[AUC] /i ) { return 'Ile';} # Isoleucine;
	if ( $_ [ 0 ] =~ / AAA|AAG /i ) { return 'Lys';} # Lysine;
	if ( $_ [ 0 ] =~ / UUA|UUG|CU[AGCU] /i ) { return 'Leu';} # Leucine;
	if ( $_ [ 0 ] =~ / AUG /i ) { return 'Met';} # Methionine;
	if ( $_ [ 0 ] =~ / AAC|AAU /i ) { return 'Asn';} # Asparagine;
	if ( $_ [ 0 ] =~ / CC[AGCU] /i ) { return 'Pro';} # Proline;
	if ( $_ [ 0 ] =~ / CAA|CAG /i ) { return 'Gln';} # Glutamine;
	if ( $_ [ 0 ] =~ / AGA|AGG|CG[AGCU] /i ) { return 'Arg';} # Arginine;
	if ( $_ [ 0 ] =~ / AGC|AGU|UC[AGCU] /i ) { return 'Ser';} # Serine;
	if ( $_ [ 0 ] =~ / AC[AGCU] /i ) { return 'Thr';} # Threonine;
	if ( $_ [ 0 ] =~ / GU[AGCU] /i ) { return 'Val';} # Valine;
	if ( $_ [ 0 ] =~ / UGG /i ) { return 'Trp';} # Tryptophan;
	if ( $_ [ 0 ] =~ / UAC|UAU /i ) { return 'Tyr';} # Tyrosine;
	if ( $_ [ 0 ] =~ / UAA|UGA|UAG /i ) { return "***" ;} # Stop Codons;
}
