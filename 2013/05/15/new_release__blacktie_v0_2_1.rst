NEW RELEASE: Blacktie v0.2.1
============================
I have released a new version of blacktie (0.2.1) which has a number of minor fixes and **NOW INCLUDES** `cummeRbund <http://compbio.mit.edu/cummeRbund/>`_ **SUPPORT!!!**

.. image:: /_static/figs/basic_cummerbund_plots.png
	:width: 600px


- github repo: https://github.com/xguse/blacktie
- documentation: http://xguse.github.io/blacktie/
- **issue tracking and feature requests:** https://github.com/xguse/blacktie/issues




Thanks and again **please** let me know what you think.  I need your input to make blacktie better and easier to use.

Gus

.. warning:: One major change was introduced in v0.2.0rc1: the yaml config file was changed slightly to facilitate the inclusion of biological replicate data.  So please take a look at the demo config file in the docs posted at: http://xguse.github.io/blacktie/tutorial.html#the-configuration-file
	
	This is the last time that this warning will be included.


News
----------

0.2.1
^^^^^^^^^^^^
*Release date: 2013-05-15*

* git tag: 'v0.2.1'
* added new script named blacktie-cummerbund to run cummeRbund
* added new class in calls.py CummerbundCall to use blacktie-cummerbund script to add cummeRbund plots to blacktie script
* checks for R and rpy2 installations
* if cummeRbund R library not found, it walks you through installing it
* ``src/blacktie/utils/calls.py``: - fixed _flag_out_dir() so that if the outdir has not been created yet it gracefully moves on
* ``examples/blacktie_config_example.yaml``: - added cummerbund_options
* ``requirements.txt``: - added rpy2
* updated docs

0.2.0rc1
^^^^^^^^^^^^

*Release date: 2013-04-19*

* git tag: 'v0.2.0rc1'
* Added support for handling biological replicates in cuffdiff runs.
* Major changes to yaml config:
    * condition_queue[index].group_id --> condition_queue[index].experiment_id
    * addition of condition_queue[index].replicate_id to track replicate data
    * condition_queue[index].name now represents description of an 'experiemental condition' and will be shared by replicates.



    
.. author:: default
.. categories:: My Code
.. tags:: new release, blacktie, tophat, cufflinks, cuffmerge, cuffdiff, NGS, RNA-seq, python, open source, open science, cummeRbund, R, bioinformatics
.. comments::

