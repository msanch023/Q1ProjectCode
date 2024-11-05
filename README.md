Rising Edge Asymmetry Function

This repo contains 2 files that I wrote as part of my groups overall project. The file ending in '_plot' produces a visual, otherwise both files do the same thing.
They contain a function to be ran on a waveform that finds its rising edge asymmetry or skewness. It takes the waveform and the tp0 (the beginning of the rising edge) as inputs.

Required data: https://zenodo.org/records/8257027
1. Download any of the training files in the link and read it into the RSA.py file.
2. Install hp5y to be able to read the files. You will also need to install numpy, scipy, and matplotlib. Matplotlib is optional if you want to view the graph.
3. To use the function just call rsa(), with the waveform and tp0 as the inputs and it will return the skewness of the rising edge.
