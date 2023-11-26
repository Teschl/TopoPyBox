#include "mex.h"
#include "aspect.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

void aspect(int rows, int cols, float *input, float *output);

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
    // Variable definitions
    float *matrix, *result;
    mwSize rows, cols;

    // Get input matrix
    matrix = (float *)mxGetData(prhs[0]);
    // Get dimensions
    rows = mxGetM(prhs[0]);
    cols = mxGetN(prhs[0]);

    // Create output matrix
    plhs[0] = mxCreateNumericMatrix(rows, cols, mxSINGLE_CLASS, mxREAL);
    result = (float *)mxGetData(plhs[0]);

    // Call the C function
    aspect(rows, cols, matrix, result);
}