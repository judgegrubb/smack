[![Build Status](http://kepler.cs.utah.edu:8080/buildStatus/icon?job=smack)](http://kepler.cs.utah.edu:8080/job/smack/)

SMACK is a bounded software model checker, verifying the assertions in its
input programs up to a given bound on loop iterations and recursion depth.
SMACK can verify C programs, such as the following:

    // simple.c
    #include "smack.h"

    int incr(int x) {
      return x + 1;
    }

    int main(void) {
      int a, b;

      a = b = __VERIFIER_nondet_int();
      a = incr(a);
      assert(a == b + 1);
      return 0;
    }

The command

    smackverify.py simple.c

reports that the assertion `a == 2` cannot be violated. Besides the features of
this very simple example, SMACK handles every complicated feature of the C
language, including dynamic memory allocation, pointer arithmetic, and bitwise
operations.

Under the hood, SMACK is a translator from the [LLVM](http://www.llvm.org)
compiler’s popular intermediate representation (IR) into the
[Boogie](http://boogie.codeplex.com) intermediate verification language (IVL).
Sourcing LLVM IR exploits an increasing number of compiler front-ends,
optimizations, and analyses. Currently SMACK only supports the C language via
the [Clang](http://clang.llvm.org) compiler, though we are working on providing
support for additional languages. Targeting Boogie exploits a canonical
platform which simplifies the implementation of algorithms for verification,
model checking, and abstract interpretation. Currently, SMACK leverages the
[Boogie](http://boogie.codeplex.com) and [Corral](http://corral.codeplex.com)
verifiers.

For information about system requirements, installation, usage, and everything
else, please consult our [Wiki](https://github.com/smackers/smack/wiki).

*We are very interested in your experience using SMACK. Please do contact
[Zvonimir](mailto:zvonimir@cs.utah.edu) or
[Michael](mailto:michael.emmi@gmail.com) with any possible feedback.*
