# Assignment 1

## Prompt

(i) Implement the following basic data types. Follow specifications presented in the textbook in full detail.
    
  1. (40 points) Lists: two implementations, array and pointer (pages 41-46), operations: FIRST, END, RETRIEVE, LOCATE, NEXT, PREVIOUS, INSERT, DELETE, MAKENULL,
    
  2. (20 points) Stacks: two implementations, array and pointer (pages 53-56), operations: TOP, POP, PUSH, EMPTY, MAKENULL

(ii) Develop the code for the following timing experiments. Report your results in the form of tables. The first column should indicate the size of the data structure. The remaining columns should report the measured times for the procedures that you apply. Derive conclusions out of your experiments and write them down.

  3. (25 points) Perform time measurements of the following five operations on lists: iterated insertion (in front, at the back), traversal, iterated deletion (in front, at the back). Run each of your procedures on three types of lists: a selected list type library data structure, your implementation of the list ADT with arrays, your implementation of the list ADT with pointers.

  4. (15 points) Perform time measurements of the following two operations on stacks: iterated insertion (PUSH operation), iterated deletion (POP operation). Run each of your procedures on three types of stacks: a selected stack type library data structure, your implementation of the stack ADT with arrays, your implementation of the stack ADT with pointers.

Each student needs to submit four separate programs and a report of timing results of part (ii). Each of the programs should contain test input data and a testing code, which demonstrate that all the operations and algorithms work properly. You will need to submit your code and your report following the submission rules that will be provided at a later date.

The choice of data representation is up to you, but you need to preserve all the essential features of the implementations discussed in the textbook. In particular all actions occurring in textbook implementations have to have their counterparts in your code.


## Specs and Tips

### Python specific instructions
* Do not use built-in list functions such as insert(), remove(), pop(), and index() in your implementation. It is your job to implement these. It is acceptable to use append().
* For the library structures in your timing experiments, you may use a python list with the above built-in functions.


### C++ specific instructions
* Your data structures do not need to be generic. It is acceptable for your implementation to hold only a specific type of data (such as int).
* Array based implementations do not need to automatically re-size. Select an appropriate max size. The max size should be large enough to generate meaningful results in your timing experiments (minimum 1000 elements).
* For the library structures in your timing experiments, I suggest std::list and std::stack.
* You may write header files for your data structures (optional), but implementations should go in a .cpp file as named above. Also, writing a header file or template class(generic) implementations should put you at an advantage for future assignments.


### Writing the test code
* You have to write test codes to check whether the different functions you implemented in the four .cpp/.py files are working. For corresponding data structures (like arraystack and pointerstack), the tests can be same. You will run these test codes in the Makefile targets.
* It is preferred that you write the test code as a seperate .cpp or .py file (for e.g. arraylisttest.cpp/arraylisttest.py or pointerlisttest.cpp/pointerlisttest.py), than the one you have for implementations. But, you can have the test code in the implemetation file as well.
* You might have to make corresponding changes to the Makefile target if you use external file.
* You can use the assert() library found both in python and cpp to test your different functions. For example look at the python and cpp codes in https://www.cs.drexel.edu/~eb452/CS260summer18/A1/


### Submit a Makefile
* A plain text file named Makefile (not makefile.txt, nor Makefile.mak, etc)
* All compiled files (executables and .o) will be deleted before grading. Your Makefile should compile and give execute permissions (if necessary) and run your program.
* Include at least the following targets:
  * time - runs your timing experiments (the default target)
  * arraylist - runs your test code for array based list
  * pointerlist - runs your test code for pointer based list
  * arraystack - runs your test code for array based stack
  * pointerstack - runs your test code for pointer based stack
* For examples of python and C++ makefiles that run a program based on multiple files, go to https://www.cs.drexel.edu/~eb452/CS260summer18/A1/


### Submit a README
* A plain text file named README (not readme, nor README.txt, etc)
    Include anything you want me to know before I grade
* Clearly note which features of your program do and do not work, as well as any design decisions unique to your implementation


### Document your source code
* Comment your code so that a programmer could figure out how to use your data structures (describe parameters, return values, etc)
* Don't go overboard - it is not necessary to comment every line of code


### Submit your timing results as a PDF called timing.pdf
* Include timing results in chart/table form for all operations described in assignment directions
* Use large enough structures so that meaningful results are generated
* Draw conclusions about the running times of the various operations on different implementations


### All code MUST run on tux.cs.drexel.edu
* If your code does not run on tux, then it does not run for grading purposes
* You may not use any libraries that are not standard on tux


### Timing your data structures
* You have to just time the insertion and deletion of a considerable amount of elements in your pointerlist, pointerstack, std::list, std::stack, arraylist, arraystack. (Don't print these elements)
* The number of elements you use should be no less than 1000 elements and if 1000 elements don't produce a comprehensive time difference you can increase the number of elements
* For C++, you can use std::ctime library for printing out times in milliseconds. Example at https://www.cs.drexel.edu/~eb452/CS260summer18/A1/time/cpp/
