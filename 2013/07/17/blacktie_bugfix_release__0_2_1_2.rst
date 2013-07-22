Blacktie BUGFIX release: 0.2.1.2
================================


.. image:: /_static/figs/basic_cummerbund_plots.png
    :width: 600px


- github repo: https://github.com/xguse/blacktie
- documentation: https://blacktie.readthedocs.org/en/latest/
- **issue tracking and feature requests:** https://github.com/xguse/blacktie/issues


The Bug:
------------------------

In short, on a Mac ``pprocess`` complained:

.. code-block:: python

    "AttributeError: 'module' object has no attribute 'poll'"
    
when trying to set up a queue.

This caused a fatal unhandled exception that was discovered on a Macintosh.
Version 0.2.1.2 should restore functionality of ``blacktie`` for people experiencing this problem.


For more detail see github issue: https://github.com/xguse/blacktie/issues/10

The Fix:
------------------------

This is a quick fix that looks for that exception and continues without using ``pprocess`` if it is encountered.
A more permanent fix will be included once I understand what is going on.


.. attention::

    - It is recommended that all users update to 0.2.1.2 to avoid this issue.
    - Anyone with knowledge of this issue is encouraged to comment on the `issues thread <https://github.com/xguse/blacktie/issues/10>`_ above or in the Comments section below. 


What is ``blacktie``? 
------------------------

``blacktie`` is a pipeline to streamline the deployment of the popular "Tuxedo Protocol" for RNA-seq analysis.
Please take a look at the `Project Summary <http://xguse.github.io/blacktie/project.html>`_ section of ``blacktie``'s documentation for more details. 


.. author:: default
.. categories:: My Code
.. tags:: blacktie, tophat, cufflinks, cummeRbund, python, open science, open source, RNA-seq, RNA
.. comments::
