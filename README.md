# jrl-walkgen

[![Building Status](https://travis-ci.org/stack-of-tasks/jrl-walkgen.svg?branch=master)](https://travis-ci.org/stack-of-tasks/jrl-walkgen)
[![Pipeline status](https://gitlab.laas.fr/stack-of-tasks/jrl-walkgen/badges/master/pipeline.svg)](https://gitlab.laas.fr/stack-of-tasks/jrl-walkgen/commits/master)
[![Coverage report](https://gitlab.laas.fr/stack-of-tasks/jrl-walkgen/badges/master/coverage.svg?job=doc-coverage)](http://projects.laas.fr/gepetto/doc/stack-of-tasks/jrl-walkgen/master/coverage/)

This software provides a pattern generator for biped robots.

It relies on the [StackOfTasks/Pinocchio][StackOfTasks/Pinocchio]
specification to realize dynamics computation.


## Setup

To compile this package, it is recommended to create a separate build
directory:

    mkdir _build
    cd _build
    cmake [OPTIONS] ..
    make install

Please note that CMake produces a `CMakeCache.txt` file which should
be deleted to reconfigure a package from scratch.


### Dependencies

The matrix abstract layer depends on several packages which
have to be available on your machine.

 - Libraries:
   - [pinocchio][https://github.com/stack-of-tasks/pinocchio] (>= 1.1.0)
     The pattern generator uses dynamics provided by the pinocchio template
   programming interface.
   - [eigen-quadprog][https://github.com/jrl-umi3218/eigen-quadprog]

 - System tools:
   - CMake (>=3.1)
   - usual compilation tools (GCC/G++, make, etc.)



## Additional notes regarding compilation on Microsoft Windows

This package has been tested using Microsoft Visual Studio 8.

 - Install MinGW
 - Make sure all environment variables are set up properly.
 - Generate the Makefile using the NMake Makefile generator.
