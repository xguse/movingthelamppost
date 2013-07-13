Installing PyQt... because it's too good for pip or easy_install.
=================================================================



This is a tutorial on installing ``PyQt`` and its dependency ``SIP``.
I am currently working on a Python package to integrate multiple disparate types of Omics data using a graph model.
Some of my code requires `ETE: a Python Environment for phylogenetic Tree Exploration <http://ete.cgenomics.org/>`_ which requires ``PyQt``.

Normally, I would simply use

.. code-block:: bash
    
    pip install -U package_name

to install ``package_name`` and ensure that all of its dependencies are installed and updated.
However, ``PyQt`` and ``SIP`` do not use the standard ``setup.py`` file for encoding the installation procedures.
They use ``configure.py``.
So ``pip`` and other `PyPI <https://pypi.python.org/pypi>`_ installer scripts will locate and download the code, but they will fail during the installation phase and complain that they can not be installed with ``setuptools``.

This was infuriating me since I know that I had these installed on my last system.
I just couldn't remember how I did it.
I must have done the whole thing manually.
In any case, thanks to a `post <http://problemssol.blogspot.com/2010/12/compile-and-install-pyqt4-for-python27.html>`_ I found using the google box at http://problemssol.blogspot.com, I found a slightly easier way to get the job done.
I am posting it here to maybe help others, but also so that I have it documented for myself the next time I have to do this.

I am borrowing **heavily** from the post above but adding some extras that I ran into on my `Arch Linux <https://www.archlinux.org/>`_ system.  

Installing assorted dependencies
-----------------------------------

Ubuntu: 
~~~~~~~~~
.. code-block:: bash

    sudo apt-get install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential


Arch:
~~~~~~~~~
As far as I can tell you should be pretty close with:

.. code-block:: bash

   sudo pacman -S base-devel qt4 python2-pip

However, you Arch folks are generally a pretty self-sufficient lot, so if there are more things you need, I am sure that you can look at the Ubuntu packages above and figure out what else you should try installing.


Installing ``PyQt`` and ``SIP``
------------------------------------

So we are going to cheat a bit and try to do the install with pip:

.. code-block:: bash

    pip install SIP

    pip install PyQt

These will both fail but the code will have been downloaded and left in the ``build`` location that ``pip`` uses.
If you are not using ``virtualenv`` (which you should be, btw), then the ``build`` is probably at 

.. code-block:: bash

    $HOME/build

If you **are** using ``virtualenv`` (good for you, btw), then your ``build`` directory will be in the root directory of whichever virtualenv you have activated.

From here on I will refer to your ``build`` directory as ``$BUILD``.
Now ``cd`` into the ``$BUILD/SIP/`` directory and build/install it with:

.. code-block:: bash

    cd $BUILD/SIP
    python configure.py
    make
    [sudo] make install

then

.. code-block:: bash

    cd $BUILD/PyQt
    python configure.py
    make
    [sudo] make install

Here is a place that I ran into a difference when doing this in Arch.
You need to specify the ``qmake`` path to ``configure.py`` since Arch names them based on the version of ``qt`` you are using (``qmake-qt4``).
So in Arch the configure line would look like this if you are using ``qt4``:

.. code-block:: bash

    python configure.py -q /usr/bin/qmake-qt4

.. warning::

    ``PyQt`` is a **big** package and a lot of compile/linking has to be done so be prepared to go get a cup of coffee or tea or scotch or whatever!


Testing your install
-------------------------
That **should** be it!
To make sure it worked fire up your `IPython <http://ipython.org/>`_ shell (you **are** using IPython aren't you?) and try to import some stuff!

.. code-block:: python

    from PyQt4 import QtCore, QtGui

If there are no errors, then you are all set!

Happy coding!




.. author:: default
.. categories:: Tutorials
.. tags:: Python, PyQt, pip, setup.py, configure.py, SIP
.. comments::
