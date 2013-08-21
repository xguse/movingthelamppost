Lab meeting 2013-08-21
======================

1 Introduction
--------------------------------------------------------------
1.1 Purpose
************************************
Introduce core concepts relating to my project such as:

#. Importance of Dengue and Malaria
#. Transmission cycle dependant on Mosquitoes
#. Limited effectiveness (medical/finacial) of treatment of the diseases in rural poor human communities
#. Vector Control Strategies
#. How Transgenesis modifies the vector control landscape
#. Elements of Successful Transgenic Vector Control
#. Introduction to control of transcription and importance of CRE/CRMs

~~~~~~~~~~~~~~~~~~~~~~

2 Review of Literature Contributions and Development of Analytical Approach
--------------------------------------------------------------------------------
2.1 Purpose
*****************************************
Review a selection of my contributions to the literature that have informed the approach used in this project throughout my tenure as a member of the lab and explain the methods that I have used based on the lessons learned.

#. **Sieglaff, D. H., Dunn, W. A., Xie, X. S., Megy, K., Marinotti, O., & James, A. A. (2009). Comparative genomics allows the discovery of cis-regulatory elements in mosquitoes. Proceedings of the National Academy of Sciences of the United States of America, 106(9), 3053–8. doi:10.1073/pnas.0813264106**

    - Use of comparative genomics to discover putative CREs from orthologous promoter regions in mosquitoes that were able to be correlated with bloodmeal associated transcription control
    - For any specific transcription profile, typically a single motif was found to be significantly enriched in the corresponding promoter regions (modules not obvious)

#. **Bonizzoni, M., Dunn, W. A., Campbell, C. L., Olson, K. E., Dimon, M. T., Marinotti, O., & James, A. A. (2011). RNA-seq analyses of blood-induced changes in gene expression in the mosquito vector species, Aedes aegypti. BMC genomics, 12(1), 82. doi:10.1186/1471-2164-12-82**

    - Provided first experience in data handling and analysis of RNA-seq big data
    - Illustrated challenges to using flanking regions as putative promoters in genomes at this level of annotation completion/quality
        - annotation contains missed first exons and other incorrect feature definitions
        - upstream genes sometimes more likely to represent exon of downstream gene
    - Nevertheless using SCOPE, putative CRMs were able to be predicted

#. **Bonizzoni, M., Dunn, W. a., Campbell, C. L., Olson, K. E., Marinotti, O., James, a. a., & Kulathinal, R. (2012). Strain Variation in the Transcriptome of the Dengue Fever Vector, Aedes aegypti. G3: Genes|Genomes|Genetics, 2(1), 103–114. doi:10.1534/g3.111.001107**

    - Provided continued lessons on managing and analyzing RNAseq big data
    - Revealed that the transcriptomes of Ae. aegypti mosquitoes from distinct strains vary significantly in complexity and abundance of specific transcripts. This variation is evident in non- blood-fed mosquitoes and is enhanced after a bloodmeal.
    - differential use of paralogous genes
    - Support the need to take precautions when comparing differences in transcript abundance profiles between species that may have last shared a common ancestor as far back as 200 mya.

#. **Bonizzoni, M., Dunn, W. A., Campbell, C. L., Olson, K. E., Marinotti, O., & James, A. A. (2012). Complex Modulation of the Aedes aegypti Transcriptome in Response to Dengue Virus Infection. PloS one, 7(11), e50512. doi:10.1371/journal.pone.0050512**

    - Example of how results (CRE-discovery in this case) are sensitive to the gene-sets use for analysis.
#. Functional Genomics can be thought of as a problem of generating meaningful gene-sets

    - signal-to-noise is major challenge in generating useful gene-sets

#. This project aims to generate meaningful gene-sets through integration of multiple data-types

    - comparative genomics (N-way 1-to-1 orthologs)
    - comparative transcriptomics (identical RNA-seq experiements on divergent Mosquito species with shared trait: bloodfeeding)
    - phylogenetics (estimated divergence since last common ancestor)
    - existing knowledge about certain bloodmeal related transcriptional control programs (20E interacting TFBS motifs)

#. The last item presents analysis challenges that I addressed through custom graph-based analysis model (``gFunc``)


~~~~~~~~~~~~~~~~~~~~~~

3 Software Development to Support Analytical Approach
--------------------------------------------------------------------------
3.1 Purpose
*******************************************
Illustrate how lessons learned in previous chapter (as well as new lessons introduced here) are addressed through custom software solutions.

#. RNA-seq analysis, reproducibility, updating (``blacktie``)
#. Integration of multiple disparate Omics scale data types (``gFunc``)
#. Documentation of exactly how analyses were carried out (IPython notebooks and automated log keeping built in to ``blacktie``)



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Results
---------------

#. `PTCI score finalization <http://nbviewer.ipython.org/urls/raw.github.com/xguse/ipy_notebooks/master/PTCI_testing_rsrd_1.0_1.1_new_data_ecr_team.ipynb>`_
#. `Filtering of high-scoring N-way 1-to-1 ortholog sets <http://nbviewer.ipython.org/urls/raw.github.com/xguse/ipy_notebooks/master/Getting_and_using_filtered_gfunc_genes_v2.ipynb>`_
#. Motif discovery results with filtered gene-sets using STEME and TOMTOM
    - `STEME k9 vs JASPAR insect database <http://nbcr-222.ucsd.edu/opal-jobs/appTOMTOM_4.9.01377068911103-22439267/tomtom.html>`_
    - `STEME k13 vs JASPAR insect database <http://nbcr-222.ucsd.edu/opal-jobs/appTOMTOM_4.9.01377068109211-275022927/tomtom.html>`_





.. author:: default
.. categories:: none
.. tags:: none
.. comments::
