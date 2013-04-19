NEW RELEASE: Blacktie v0.2.0rc1
===============================

I have released a new version of blacktie (0.2.0rc1) which has a number of minor fixes and new features.

- github repo: https://github.com/xguse/blacktie
- documentation: http://xguse.github.io/blacktie/
- issue tracking and feature requests: https://github.com/xguse/blacktie/issues


.. warning:: One major gotcha will be that the yaml config file has been changed slightly to facilitate the inclusion of biological replicate data.  So please take a look at the demo config file in the docs posted at: http://xguse.github.io/blacktie/tutorial.html#the-configuration-file

Thanks and **please** let me know what you think.  I need your input to make improvements.

Gus


,,,,,,,,,,,,,,,,,,,,,,,,


News
----

0.2.0rc1
^^^^^^^^^^

*Release date: 2013-04-19*

* git tag: 'v0.2.0rc1'
* email_notification is now adjustable for other email servers
* Added support for handling biological replicates in cuffdiff runs.
* Major changes to yaml config:
    * condition_queue[index].group_id --> condition_queue[index].experiment_id
    * addition of condition_queue[index].replicate_id to track replicate data
    * condition_queue[index].name now represents description of an 'experimental condition' and will be shared by replicates.


.. author:: default
.. categories:: My Code
.. tags:: new release, blacktie, tophat, cufflinks, cuffmerge, cuffdiff, NGS, RNA-seq, python, open source, open science
.. comments::
