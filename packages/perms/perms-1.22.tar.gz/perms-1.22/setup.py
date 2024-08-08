from setuptools import setup, Extension
import numpy as np

def main():
    setup(
        description = 'The perms package implements the algorithm proposed by Christensen (Inference for Bayesian Nonparametric Models with Binary Response Data via Permutation Counting, Bayesian Analysis, 1(1), 1-26,2023) for computing marginal likelihoods via permutation counting.',
        author = 'Dennis Christensen, Per August Jarval Moen',                  
        author_email = 'Dennis.Christensen@ffi.no, pamoen@math.uio.no',      
        name="perms",
        version="1.22",
        include_dirs=[np.get_include()],
        ext_modules=[Extension("perms", ["get_log_permanent.c", "help_functions.c", "get_alphabetagamma.c",\
                "methods_sparse.c", "methods.c", "xxhash.c"])],
        install_requires=["numpy>=1.18.0"],
        headers = ["xxhash.h", "header.h"])



if __name__ == "__main__":
    main()
