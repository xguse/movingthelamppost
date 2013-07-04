First pass Trinity Results for Anopheles stephensi midgut RNA-seq (non-bloodfed)
================================================================================



Exploration of the first set of results from a Trinity run with default settings on one library of Anopheles stephensi midgut RNA-seq (As\_00 lib one)
********************************************************************************************************************************************************


Analyze Lengths Of Assembled Contigs/Transcripts
------------------------------------------------


Function to count all transcripts of length *X*:

.. code:: python

    from collections import defaultdict
    from rSeq.utils.files import ParseFastA
    
    def measure_and_count_transcripts(fasta_path):
        
        tx_lens = defaultdict(list)
        
        p = ParseFastA(fasta_path)
        seqs = p.to_dict()
        
        for name,seq in seqs.iteritems():
            tx_lens[len(seq)].append(name)
                
        print "The number of different transcript sizes encountered: %s" % (len(tx_lens))
        return tx_lens


Now I count and plot the size data.


.. code:: python

    # Prep to plot a Histogram of the numbers of transcripts in each length bin
    
    trinity_tx_lens = measure_and_count_transcripts('/home/gus/Dropbox/common/projects/trinity_As_one_lib/Trinity.fasta')
    
    trinity_lengths = []
    
    for item in trinity_tx_lens.iteritems():
        trinity_lengths.extend([item[0]] * len(item[1]))
    
    trinity_lengths.sort()


.. parsed-literal::

    The number of different transcript sizes encountered: 4632


.. code:: python

    
    hist(trinity_lengths, bins=50, histtype='stepfilled')
    xlabel('transcript length')
    ylabel('number of transcripts')


.. parsed-literal::

    <matplotlib.text.Text at 0x645b290>


.. image:: /_static/As_midgut_RNAseq_lib_TRINITY_files/_fig_03.png

Now I calculate the N50*length* and N50*index* for the trinity assembly.

**N50*index*:** the number of largest contigs(transcripts) whose summed
lengths equal at least 50% of the sum of **ALL** contigs (smaller
numbers are 'better')

**N50*length*:** the length of the last added contig from above (larger
numbers are 'better')


.. code:: python

    def calc_N50s(lengths):
        total_length = sum(lengths)
        print "total_length:\t\t%s" % (total_length)
        
        running_total = 0
        collected_lengths = []
        n50_i = None
        
        for length in reversed(lengths): 
            running_total += length
            collected_lengths.append(length)
            
            if running_total >= total_length * 0.5:
                n50_i = len(collected_lengths)
                n50_l = length
                break
        
        print "running_total:\t\t%s" % (running_total) 
        print "N50_index:\t\t%s of %s" % (n50_i,len(lengths))
        print "N50_length:\t\t%s" % (n50_l)
        print "median contig length\t%s" % (median(lengths))



.. code:: python

    calc_N50s(trinity_lengths)


.. parsed-literal::

    total_length:		31858558
    running_total:		15931068
    N50_index:			3927 of 25167
    N50_length:			2469
    median contig length	647.0

Analyze Lengths Of Predicted Transcripts
----------------------------------------


1. AsteS1.0
~~~~~~~~~~~




.. code:: python

    asteS1_0_tx_lengths = measure_and_count_transcripts('/home/gus/genome_data/AsteS/Anopheles-stephensi-SDA-500_TRANSCRIPTS_AsteS1.0.fa')
    
    asteS1_0_lengths = []
    
    for item in asteS1_0_tx_lengths.iteritems():
        asteS1_0_lengths.extend([item[0]] * len(item[1]))
    
    asteS1_0_lengths.sort()


.. parsed-literal::

    The number of different transcript sizes encountered: 4058



.. code:: python

    hist(asteS1_0_lengths, bins=50, histtype='stepfilled',color='c')
    xlabel('transcript length')
    ylabel('number of transcripts')


.. parsed-literal::

    <matplotlib.text.Text at 0x3f2ced0>


.. image:: /_static/As_midgut_RNAseq_lib_TRINITY_files/_fig_08.png



.. code:: python

    calc_N50s(asteS1_0_lengths)


.. parsed-literal::

    total_length:		25155329
    running_total:		12580251
    N50_index:			2617 of 13251
    N50_length:			2838
    median contig length	1344.0

2. AsteI1.0
~~~~~~~~~~~



.. code:: python

    asteI1_0_tx_lengths = measure_and_count_transcripts('/home/gus/genome_data/AsteI/Anopheles-stephensi-Indian_TRANSCRIPTS_AsteI1.0.fa')
    
    asteI1_0_lengths = []
    
    for item in asteI1_0_tx_lengths.iteritems():
        asteI1_0_lengths.extend([item[0]] * len(item[1]))
    
    asteI1_0_lengths.sort()


.. parsed-literal::

    The number of different transcript sizes encountered: 5227


.. code:: python

    hist(asteI1_0_lengths, bins=50, histtype='stepfilled',color='g')
    xlabel('transcript length')
    ylabel('number of transcripts')


.. parsed-literal::

    <matplotlib.text.Text at 0x6d37710>


.. image:: /_static/As_midgut_RNAseq_lib_TRINITY_files/_fig_13.png


.. code:: python

    calc_N50s(asteI1_0_lengths)


.. parsed-literal::

    total_length:		35859205
    running_total:		17930131
    N50_index:			3231 of 23287
    N50_length:			3279
    median contig length	717.0


    




.. author:: default
.. categories:: My Research
.. tags:: RNA-seq, de novo transcriptome assembly, Trinity, Anopheles stephensi, midgut, non-bloodfed, blood feeding, ipython, python
.. comments::
