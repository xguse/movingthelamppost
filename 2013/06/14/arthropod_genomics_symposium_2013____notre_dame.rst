Arthropod Genomics Symposium 2013 -- Notre Dame
===============================================

My notes on talks from the `7th Annual Arthropod Genomics Symposium <http://globalhealth.nd.edu/7th-annual-arthropod-genomics-symposium/>`_  If you are interested, you can follow live tweets from `#13ArthGen <https://twitter.com/search?q=%2313arthgen&src=typd>`_.

.. note:: Obviously, my spelling is gonna suck on this.  Please don't hold it against me!?




General Session
-------------------
Dan Lawson
**************

- Federated curation and hosting of genomes plus standardized best practices and data formats needed for #i5k

Steven Richards (Fringy)
**************************

- ND50 10kb basic bar to reach for good annotation through Maker

Terence Murphy
********************
How to annotate 5000 genomes: lessons from NCBI genome annotation pipeline

Monica Munoz-Torres
*********************
*Web Apollo web based annotation editing platform*

- first realtime genome collaborative annotation editor on the web
- MANUAL annotation is NECESSARY not just desirable: without it many downstream experiments will be poisoned
- democratization of genome assembly and annotation require a new model of collaborative annotation

.. more::


Emerging Genomes
-----------------

Amy Toth
************
*Genome of primitively social wasp "Polistes dominula": insights/opportunity for understanding genomic basis of eusociality*

- low repetitive elements	
- even lower TE content
- genomic suspects for social evolution
    - genetic toolkits -- conserved gene sets
        - evo-devo approach --comparative
        - conservation of Hox genes etc
            - cis regulatory changes very important as changes in expression vs gene function important in evolution/speciation
        - transcriptomic look at
            - foraging
                - foraging transcriptome profiles agree with apis mellifera
            - dominance
                - compared transcriptomes of brains in dominant vs submissive individuals
                - found correlations of aggressive behavior in fruit flies and even mammals
    - epigenetics
        - controls wild diff in phenotypic models -- same genome gives VERY diff morphologies
        - cast related diff in DNA methylation are present
        - treatment with methyl inhibitor causes more worker like phenotypes
        - however dna meth not likely to be related to cast diff through diff expression, but maybe through splicing control
        - Dnmt3 (usually needed for DNA meth) not found yet in this genome
    - novel genes

Dave Denlinger (Ohio State)
*******************************
*Sequencing the Antarctic Midge, Belgica antarctica: the smallest insect genome*

- poly extremophile
    - cold -- frozen solid 8-9 months a year
    - 70% loss of body water
    - salinity
    - pH
    - UV EXPOSURE
- Heat shock proteins on almost constitutively
- Dessication 30% helps them survive low temps
- initial genome size of ~ 85 Mb?! -- then confirmed
- 13,500 protein encoding genes anyway
- uniqueness of the genome:
    - small size -- probly due to extremophile life
    - consistently small introns
    - few repetitive elements
    - few TEs -- usually old and probably inactive
    - 47% GC
    - function enrich:
        - up
            - membrane
            - ATP binding
        - dwn
            - oderant binding
            - oderant receptors
            - sensory perception of smell in general
- pathway of dessication protection
    - up regulation of autophagy
    - inhibit apoptosis
    - metabolism genes shutdown
- lead to focus on aquaporins as related to dehydration responses in diff tissues
- How does clock work in these extreme light/dark cycles
    - clock genes not correlated with light cycle at all
    - locomotor activity shows no diurnal bias
- genes still there and still expressed but the cyclic nature of transcription is NOT observed

     

Virpi Ahola
***************

*melitaea cinxia genome*



Epigenetics
-------------
Jennifer Brisson (U of Neb - Lincoln)
*****************************************

*Linking DNA methylation to phenotype in the pea aphid*

- meth found in gene bodies primarily in exons
- Methylation associated with higher expression (only at global level?)
- differences bt morphs:
	- methyl patterns plainly morph specific by PCA 2D
	- intron specific CHH methylation flat in wingless/asex but very pronounced in Sexual morphs
- function of intergenic DNA methylation:
	- skipped exons should have higher methylations bc CTCF cant bind the exon to slow down the machinerey to allow that exon to be recognized as NOT intron
	- this IS detected by the speaker
	- role for DNA methylation in dcerning paralogs?
		- example used is RNAi genes (Dicer etc)

Micheal Goodisman (GA Tech)
*******************************

*Function of DNA methylation in insects*

- DNA methylation lost in some insects
	- NO METHEYL IN DIPTERA?!  *Did I know that?*
- What is the function of methyl in insects?
- **Note:** look up CpG_o/e
- in Apis and Pea Aphid:
	- uniform expression between conditions = high methylation 
	- differential expression bt condition = low methylation
	- says its a strong repeating pattern
- fire ant diploid vs haploid males:
	- increased gene expression tends to track with increased DNAmeth
	- as variation in gene expression increases DNAmeth decreases
	- most DNAmeth seen in Haploid males... (not sure I got that right)
- Conservation of methylation and other epigenetic data (honey bee vs fire ant and Dmel [no DNAmeth but yes histone modification])
	- over all: within ants, correlatiuon of genes with DNAmeth are very high (r ~>0.7)
	- same in bees
	- between ants/bees: still relatively high correlation (r ~ 0.6)
	- are DNAmeth in genes in ants/bees correleated with specific histone mods in Dmel: 
		- Answer is YES
		- no time to document which hist mods he showed
- Summary:
	- phenoype specific genes are unmethylated
	- ubiquitously genes are methylated
	- DNAmeth associated with ploidy
	- Patterns of DNAmeth conserved within and bewtween species
	- DNAmeth tends to be associated with specific histone mods
	- DNAmeth tied to alternative splicing

Greg Hunt (Purdue)
********************

*Parent of origin effects in gene expression in honey bees*

- hybrids between african and european bees sting intermediate of the parents (but if the father is African hybrids are more similar to african bees?)  **NOT SURE I GOT THAT RIGHT**
- Used multiple different mapping methods but didnt say how -- *DONT LIKE THAT*
- Truethfully I dunno if I can talk about the rest because I can't tell if his biases are real or due to not using the same mapper in all conditions...

Susan Weiner (Iowa State Univ)
***********************************

*DNA methylation in the primitively social wasp *Polistes dominulus**

- primitavely eusocial = not morpholagical difference (queen/works look the same)
- independent origin of socialality? (Did i hear that right?)
- Polistes has way more DNAmeth than all other insects looked at
- is there a bias to sites DNAmeth in caste?
	- yes.... **but** PCA 2D was not **THAT** impressive
- Zebularine treatment (*inhibits DNAmeth*) in multiple replications and variations tend to cause individuals make them more worker-like (opposite as in honey bees)
- DNMT3 has not been found yet (DNAmethyltransferase i think)
- DNMT1 and 2 are there
- question asked: was zebularine validated that it is working uniformly
	- answer: working on that

Comparative Genomics
------------------------

Rob Waterhouse (Univ Geneva/MIT)
**************************************

*Orthology-based genome annotation and interpretation*

- where we have come since Dmel in early 2000s
- what is it you want from your genome BEFORE you start to make sure that you have the quality you need
- once your annotation is done:
    - how do you asses the completness of your annotation?
    - once complete, orthology becomes useful tool
- orthoDB: most comprehensive source for orthology amoung arthropods (>57 species)
- Assesing completion:
    - BUSCOs -> **needs definition later**
        - orthos with single copy ortho in 90% of other species
        - expectation:
            - most should be found in your assembly
            - most should be single copy
        - implementation:
            - blast
            - then:
                - best BLAST regions
                - next-best BLAST
                - homology based gene predictions
        - example:
            - 15 Mosquito species
            - fewer than 10 BUSCOs in most Mosq species
            - Aedes:
                - 16 missing
                - 244 multi copy
            - Culex:
                - 47 missing
                - 126 multi copy
            - also look at the length differentials between orthologs
                - helps see whether the fragmentation of assembly is affecting your assembly/gene models
    - mapping: new feature for orthoDB
        - allows new genomes to be mapped to current frozen set of orthologs
        - private interface if required
        - also allows you to predict how many of the BUSCOs are missing to decide whether to make current gene set public
- orthology to infer gene function:
    - functional traits
    - evolutionary traits
    - **CAVEAT EMPTOR**:
        - orthology does not strictly define function
    - Added a **BUNCH** of cool extra information including synteny blocks and relative evolutionary rate
    - **if:**
        - single copy
        - kept in most species
        - slow evolutionary rate
    - **then:**
        - functional assumptions are warranted


Chris Winchell (UC Berkley)
********************************

*Genome and germline of emerging genome of crustacean __Parhyale hawaiensis__*

- BAC library:
    - 129 024 clones
    - median insert ~140 kb
    - aprox coverage 5X
    - 70 have been seq'd: 53 genes found

- germline *REPLACEMENT?!*
    - you can ablate the original developing germline cells and they will MAKE MORE!! (convert somatic cells to germline?)
    - very elegant transgenic demonstration of where the new germline cells are originating in the blastoderm
- **not** a "normal" event, but may be a failsafe for rare germline loss of function in development


Michael Brewer (UC Berkley)
******************************
*Evolutionary transcriptomics associated with developmental color switching in an adaptive radiation of Hawaiian Tetragnatha spiders (Araneae: Tetragnathidae)*


- orb weavers that don't weave orbs anymore and adopt purely active hunting lifestyle
- 2 ecomorph:
    - green
    - maroon
- green individuals switch to maroon and their diet changes upon maturity
- they can control whether/when they shift?
- can date the species due to isolation on the islands
- METHOD:
    - RNAseq
    - trinity assembly
    - annotate by blast
    - trinity MM ORF
    - RecipBestBlast
    - Something else: slide change...
- ... got caught up in other things ...
- **He has many centipede/millipede RNA-seq libraries but they are being neglected in the community: if you are interested in the results from these libraries please contact him**

.. _piRNA:

Igor Sharakhov (Virgina Tech)
********************************
*Ornganization and evolution of piRNAs in _Anopheles gambiae_*

- in aedes piRNAs bind mostly to GENES not transposable elements
- tissue subcell localization:
    - Dmel:
        - diff localization for each piRNA protein
- composition of piRNA in Ag
    - aedes piRNA clusters overlap GENES
    - most piRNAs in Ag seem to have signiture of Ping Pong amplification
    - Localization in Ag seems mostly localized with transposable elements not genes
        - but on X many map with genes...

- Genomic chromosomal localization of piRNA in Ag
    - they have Abs for PIWI1
    - PIWI1 localization on chromo looks more like Dmel PIWI
    - PIWI2 (aub) not succeeded 
    - aedes: most piRNA clusters NOT near centromeres like Dmel
        - mostly in euchromatin
    - Ag: most piRNA peaks in centromereic but many outside of centromeric 
            - however still mostly in heterochromatic 
            - M and S forms look pretty similar in localization of clusters
            - again in X chromosome many more clusters mapping in euchromatin
            - M and S forms NOT as similar in X chromosome
    - aedes piRNAs clusters as much as 20% of genome


Systems Biology/Population Genomics
---------------------------------------

.. _andyclark:

Andy Clark (Cornell)
******************************************
*Population genomic and metabolic inference from a global diversity reference panel of _Drosophila melanogaster_*

- using flies as model for diabetes: insulin signaling and TOR
- lines isofemale lines (>90 lines):
    - Ithica
    - Netherlands 
    - Beijing
    - Zimbabwe
    - Tasmania
- significant metabolic phenotypic variation between the lines
- scored for MANY types of info:
    - enzyme activity
    - fat storage
    - more
- modeling objective:
    - fit models predicting endpoints like total fat storage from genome
    - assess sensitivity of component of models 
    - explain genetic architecture
- modeling:
    - multiple regression
        - observed vs expected: r^2 = 0.23
    - Flux balance Analysis (FBA)
    - Structural Equation MOodels (SEM)
        - obsvd vs exp: r^2 = 0.44
    - Bayesian hierarchical model
- 3 cam 120 frames/sec linked in 3D
- perturbations by flying through magnetic field with magnet glued to their back
- recovery from perturbation begins in a single wing beat
- **VERY COOL VIDEOS**
- Data suggesting that the Drosophila melanogaster population variance may mirror the human data supporting the idea that we brought Dmel with us as we left Africa and they follow similar variance constrictions as they followed the particular human population as they split
- New descriptions of hybrid dysgenesis through cross population mating allowing exploration of other mobile elements and their effects (similar to P-element)
- Wolbachia data suggests a single invasion of Dmel 

.. _petercherbas:

Peter Cherbas (Indiana Univ)
******************************************
*modENCODE and the potential of systems biology in _Drosophila_*

- 1938 new transcribed regions (not linked to any other gene model)
- almost every gene included new 5' or 3' UTR...
- promoter switching linked to certain lines where Broad in activated or deactivated by ecdysone
- environmental perturbations reveal totally new genes
- neural specific expressed isoforms have LONG 3' extensions
- 18 loci where there is almost exactly overlapped (sense/antisense) transcription (seems protein coding too but I am not sure)
- in general: the **least certain** part of any annotation is the non-coding regions
- **RESOURCE:** MANY cell lines used to produced transcriptomes for public use
- cell lines unique and represents different "test tubes" for biological questions
    - unique complement of transcription factors etc
    - sufficiently differentiated to be homologous in behavior and components

.. _jeremylynch:

Jeremy Lynch (Univ Illinois Chicago)
******************************************
*Global analysis of the dorsal-ventral patterning regulatory network in the wasp _Nasonia vitripennis_ using quantitative transcriptomics*

- opening statement: **DON'T BE AFRAID OF THE COMMAND LINE!!!!**
- Nasonia embryo layed out very similar to that of Dmel
    - morphology and gene expression
    - most likely convergent evolution
- Nasonia patterning systems more dynamic
- BMP provides most patterning information
- also once cells start migrating in the embryo there are major divergences from Dmel as well
- does Nasonia use the same genes as Dmel?
    - knock out BMP: lose dorsal gene expression
    - KO toll: lose ventral gene expression
- used tuxedo protocol 
- also used trinity to see what happened de novo followed by DESeq
    - works mostly ok but has a lot of nonsense as well


.. _sarahmitchell:

Sara Mitchell (Harvard Public Health)
******************************************
*Genetic pathways induced by mating have a key role in the reproductive biology of _Anopheles gambiae_*

- many discoveries regarding elements that are required for mating plug formation as well as signals effecting the female post mating changes (sperm is not required)
- found changes in the midgut after mating
- looking at early middle and late matting reponses (3, 12, 24 h)
- mostly induction of genes in mated vs virgins
- wow.  LOTS of information very fast!  Not keeping up with typing very well!



Ecological Genomics
-------------------------

Leslie Vosshall (The Rockefeller Univ)
**********************************************
*Dissecting mosquito host-seeking behavior through loss-of-function genetics*

- two clases of insect oder recepters
    - OR
    - IR
- each insect has different numbers of these receptors
- "Aedes has a 'horrifically' enormous genome"
- KO OR-coeffector effectively removes function of all ORs
- used Zinc Fingers to do the KO
- Behvior assay:
    - tube with a human scent at the end, see if the females choose the right tube.
    - ORCO-/- cant see human scent alone but can see if CO2 is added
    - IRs must also be involved
- given choice between human or guinee pig the double mutants are much less good at choosing the human
- ORco not needed to choose human over nothing but are important for choosing human vs non-human
- Vienette 2:
    - many cues moisture, heat, smell, C02 etc
    - moving on to gustatory receptors (GR)
    - GR3 knocks out all???
    - GR3-/- blind to CO2
    - CO2 + Heat causes biting
    - both needed
    - GR3- means no CO2 signal
    - mosqs need more than one signal to trigger feeding
    - mutants severly impaired in lab but in semi field conditions much LESS impaired






My Own Personal "Remember This" List
-----------------------------------------

- GMAP to map de novo assembled transcriptomes to the genome
    - plan to convert to GTF and merge with cufflinks GTF using cuffmerge to help define UTRs better for CRM/CRE discovery in my Mosquito species







.. author:: default
.. categories:: Conferences
.. tags:: ArthGen2013, genomics, arthropods, transcriptomics, twitter, science@twitter, live blogging
.. comments::
