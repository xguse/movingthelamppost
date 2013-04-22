Elements of transgenic disease-vector control (Part 1: setting the scene)
=========================================================================

Foreword
--------
This is the first installment in my endeavor to :doc:`"Blog My Dissertation" <../15/blogging_my_dissertation>`.  
I am afraid that I have not quite settled on a format for this project or even a solid governing theme on how to organize and execute the bloggification...
So I ask you to please bear with me as I experiment with how technical to be; how polished; how formal/informal; and "dissertation-ready" to make the prose etc.

This post will cover part of the dissertation's first chapter (Introduction and Background).
The long term goal of the Anthony James lab at UCI is to produce genetically modified mosquitoes that do not transmit :term:`malaria` or :term:`dengue fever` and will spread this trait swiftly through local mosquito populations.
In order to produce mosquitoes that will perform these functions, we use a process called :term:`transgenesis` that introduces a set of :term:`exogenous` genes into the mosquitoes' :term:`genome` and tells them when and where to be expressed.
All of my work should be interpreted in the scheme of aiding the lab's ability to improve this process; however, there is real basic science that it aims to further as well.

This is part one of a few posts that will discuss the fundamental elements of transgenic disease-\ :term:`vector` control.
It will set the scene by explaining what a disease-vector is and how our specific models of disease transmission influence how we can approach the problem of malaria and dengue fever by addressing the mosquitoes rather than treating the humans.

Mosquito borne disease
-----------------------

.. topic:: TL;DR:

	- there are many but we focus on Dengue Fever and Malaria
	- causative agents are RNA viruses and Plasmodium protists, respectively
	- people don't give people these two diseases
	- mosquitoes generally don't give mosquitoes these diseases

There are many mosquito borne diseases that afflict the world's population; however, the James Lab focuses on two of the major ones: dengue fever and malaria.
The causative agents of these two diseases are a suite of four species of RNA viruses (`Dengue Virus 1-4 <http://en.wikipedia.org/wiki/Dengue_fever#Virology>`_) and a suite of five species of protist from the genus |Plasmodium|_, respectively.
However, in any **single** location they are generally transmitted by a single species of mosquito: 


+------------------+------------+-----------------------+
| Disease          | Region     | Mosquito Vector       |
+==================+============+=======================+
| Dengue Viruses   | Worldwide  | *Aedes aeygypti*      |
+------------------+------------+-----------------------+
|                  | Africa     | *Anopheles gambiae*   |
| Human Malaria    +------------+-----------------------+
|                  | Asia       | *Anopheles stephensi* |
+------------------+------------+-----------------------+

|

.. Note:: The multiple species nature of these two diseases makes addressing the problem of preventing human disease caused by these pathogens quite difficult: especially when focusing on the human aspect.

.. seealso:: Other posts will go into more detail on the specifics of the distribution and effects of the actual diseases on local populations. Once completed, they will be linked to from here.

Another very important aspect of both of these diseases is that people do not become infected through interaction with other people, and mosquitoes do not become infected through interaction with other mosquitoes.
The :term:`transmission cycle` of both diseases requires that the pathogen be passed from human to mosquito or from mosquito to human.
We will soon see that this pattern has :ref:`important consequences that we can exploit <pub-health>` to prevent the transmission cycle from churning out infected individuals.

.. |Plasmodium| replace:: *Plasmodium*
.. _Plasmodium: http://en.wikipedia.org/wiki/Plasmodium


Transmission cycle
^^^^^^^^^^^^^^^^^^

.. topic:: TL;DR:
	
	1. a female mosquito bites infected person
	2. the pathogen is taken into mosquito midgut with bloodmeal
	3. the pathogen must escape the midgut and gain access to the mosquito's circulatory system *(the animal is now* **infected**\ *)*
	4. the pathogen must gain access to the mosquito's salivary glands *(the animal is now* **infectious**\ *)*
	5. the infectious female mosquito bites an uninfected human and pathogens in her saliva are introduced to the person's body

While the specifics of how viruses and protists live and reproduce in mosquitoes and humans are quite different, the transmission cycles of dengue and malaria are very similar in their major events.
The transmission of either pathogen from one infected human to another can both be summarized into five fundamental events.
First, a female mosquito feeds on an infected human's blood taking up the pathogen as well.
The bloodmeal is digested in the mosquito's :term:`midgut`, and as you might expect, the midgut is the first stop for the pathogen too.
Escape of the midgut is the first critical step for the survival of the pathogen inside the mosquito.
If it is trapped in the midgut, it will eventually be passed as waste after the bloodmeal is digested.
If it manages to escape to the :term:`hemolymph`, the pathogen must gain access to the mosquito's salivary glands if it is to infect another human.
If this step is unsuccessful, then the mosquito, while itself **infected**, is not **infectious** to other humans.
For this, the pathogen must be injected into the bloodstream of the next human along with the contents of the mosquito's saliva.

.. figure:: mosqXsection.png
	:width: 585px
	:align: center

	**Cross section of female mosquito with tissues important to the transmission cycle highlighted.**


.. _pub-health:

Public health: *multiple targets*
---------------------------------
.. topic:: TL;DR:

	- The specifics of the transmission cycle of these diseases provides multiple targets for public health interventions
	- focus on the human
	- focus on the vector

Because the arrow of transmission always\ [#nonhuman_transmission]_ points from mosquito to human or from human to mosquito, if either of those arrows are broken, the cycle will collapse and the area would eventually be cleared of the pathogen provided the intervention is maintained.
This model suggests that there are two primary targets for public health interventions aiming to reduce the :term:`incidence` (followed by :term:`prevalence`) of infection in a population.

	1. prevent mosquitoes from infecting humans
	2. prevent humans from infecting mosquitoes

However, many of the interventions can not be clearly divided into addressing purely the human or vector side of the cycle.
For example, any efforts to reduce the number of bites that humans receive from mosquitoes affects both the probabilities of the vector *and* the human becoming infected.  
This is one reason that vector control rather than purely human-based interventions are almost always part of prevention strategies. 
For the purposes of this document, I will define human-based interventions to be those that are directly administered to the human's body.
Essentially: medical interventions. 

.. note:: It should be noted that in this respect, the long term goals of public health are more focused on prevention than the treatment of acute cases. Of course sick people need to be treated, and finding and clearing people who are infected is a part of preventing mosquitoes from acquiring the pathogen from people.  However, in the long game it is much more effective to prevent the infection .  These efforts are what we will focus on.



Options for the humans
^^^^^^^^^^^^^^^^^^^^^^
Because of the definition of human-based interventions that I am using, there are relatively few effective options in this category for malaria and dengue fever.
Normally, this section would include vaccines and swift, effective patient identification and treatment to clear the infection.
For reasons that will be discussed in a later post, these interventions simply do not exist on the market or in a cost-effective form applicable to the isolated and impoverished areas that are most affected.

.. seealso:: This subject should also be given a deeper treatment in the future. Links to those posts will show up here.

Conventional options for the vectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Because medical options are generally quite scarce, most attention in the field is directed toward controlling access of the vector populations to human contact.
This can include removal of nearby mosquito breeding sites (usually standing water), spraying of insecticides, introduction of biological predators, and/or bed nets, etc. 
One fairly novel approach that has implications for the next post in this series is sterile insect technique.

.. topic:: Sterile Insect Technique:

	`Sterile insect technique (SIT) <http://en.wikipedia.org/wiki/Sterile_insect_technique>`_ exploits a peculiar aspect of some insects' reproductive behavior.  
	In many insects, it is only (or at least primarily) the first mating event that "matters".
	Subsequent mating events contribute little to no genetic material to the females progeny, **even when the first event involves a sterile male**.
	This means that if massive numbers of sterilized males are introduced into a native population, any wild female that mates first with one of the sterile males will be effectively sterilized herself.
	This can have dramatic effects on the local population.
	For a famously effective SIT campaign, look up `screwworm eradication <http://goo.gl/DF7bv>`_ on google. 


Transgenic options for the vectors
----------------------------------
As you saw above, most conventional vector control strategies involve what might be termed **vector population reduction**.  As we get into what transgenics can do for vector control, we will see that in addition to population reduction we have a new strategy available which has quite exciting implications to the sustainability of the vector control aspect of public health interventions for dengue and malaria.
This could be called **vector population conversion**.  Tune in next time to read all about it!





|
|
|

.. rubric:: **Footnotes:**

.. [#nonhuman_transmission] While some mosquito to non-human vertebrate transmission may occur, it is not thought to be sufficient to maintain the pathogen if the mosquito:human loop is broken.


.. author:: default
.. categories:: My Research, My Dissertation
.. tags:: mosquitoes, background, vector control, transgenic mosquitoes, GMO, GMM, Dissertation: Chapter One (Background)
.. comments::
