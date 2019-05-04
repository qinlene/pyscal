pybop
=================================

**pybop** is a python module for calculation of Steinhardt's bond order parameters [#]_. The core functionality of **pybop** is written in C++ with python wrappers using `pybind11 <https://pybind11.readthedocs.io/en/stable/intro.html>`_ . This allows for fast calculations with possibilities for seamless expansion in python. 

Stenhardt's order parameters or local bond order parameters are widely used in simulations to determine crystal structure of atoms. They are also used to identify if an atom is solid or liquid and the identify the solid atoms in a liquid, which is often used an order parameter to study progress of reaction during solidification. Additionally **pybop** provides an easy environment for reading in snapshots from molecular dynamics trajectories, allowing for easy post-processing of simulation data. **pybop** is inspired by `BondOrderAnalysis <https://homepage.univie.ac.at/wolfgang.lechner/bondorderparameter.html>`_ code, but has since incorporated many additions and modifications. The main highlights of **pybop** are given below.

Highlights
----------

* Fast and efficient library using C++.
* Calculation of Steinhardts order parameters and their averaged version [#]_.
* Links with `Voro++ <http://math.lbl.gov/voro++/>`_ code, to enable weighted calculation of local bond order parameters [#]_.
* An environment for easy processing of simulation data.
* Distinction of solid and liquid atoms using q6 parameter [#]_.
* Cluster algorithms of solid atoms to find largest cluster of solid atoms in liquid [#]_.


.. [#]  Steinhardt, PJ, Nelson, DR, Ronchetti, M. PRB 28, 1983.
.. [#]  Lechner, W, Dellago, C. JCP 129, 2008.
.. [#]  Mickel, W, kapfer, SC, Shroder-Turk, GE, Mecke, K. JCP 138, 2013.
.. [#]  Auer, S, Frenkel, D. APS 173, 2005., Diaz Leines, G, Drautz, R, Rogal, J. JCP 146, 2017.
.. [#]  Diaz Leines, G, Drautz, R, Rogal, J. JCP 146, 2017.