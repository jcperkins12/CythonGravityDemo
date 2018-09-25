# CythonGravityDemo
This is an attempt to recreate the demo by Pauli Virtanen (https://python.g-node.org/python-summerschool-2011/_media/materials/cython/cython-slides.pdf)

Each directory labeled Cy0_, Cy1_, etc. is another step taken at the direction of the tutorial in converting regular python in Cy_0 into more efficient cython.

## A rough outline of how I set up my environment

1. Make sure that you have cython and line_profiler installed (assumes conda distribution but pip should work as well)
   ```
   conda install cython
   conda install line_profiler
   ```
2. Copy the kernprof.exe and kernprof-script.py from the Scripts dir of of the environment to the working directory (i.e from C:\Users\*JohnDoe*\AppData\Local\Continuum\anaconda3\Scripts\ to C:\Python\CythonGravityDemo\ )

3. Make sure that you are in the right conda environment - (my most up-to-date python 3 envinronment is called Py3x)
   ```
   conda activate Py3x
   ```
   
## Using the Profiler
- run the profiler with 
   ```
   python kernprof-script.py -l run_gravity.py
   ```
- view the results with
   ```
   python -m line_profiler run_gravity.py.lprof
   ```


## Compile cython
- with setup tools
   ```
   python setup_cy0.py build_ext -i
   ```
- with cython (only translates cython to C or C++)
   ```
   cython -a gravity_cy.pyx
   ```
