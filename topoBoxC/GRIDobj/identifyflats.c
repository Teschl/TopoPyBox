#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

void identifyflats(int rows, int cols, float *inputMatrix, bool *flatsMatrix, bool *sillsMatrix){
    //---------------- calc flats --------------------------
    // row = y axis, col = x axis
    for(int row = 0; row < rows; row++){
        for(int col = 0; col < cols; col++){

            // calculate location in matrix
            int index = row * cols + col;
            bool lower = false;

            // loop through all 8 neighbours
            for (int y = row-1; y <= row+1; y++){
                for (int x = col-1; x <= col+1; x++){

                    // calculate location in matrix
                    int neighbor = y * cols + x;
                    // Skip if out of bounds
                    if(x < 0 || x >= cols || y < 0 || y >= rows) continue; 
                    // Skip if current cell
                    if(neighbor == index) continue;
                    // check if neighbour is lower than current cell, if so break
                    if(inputMatrix[neighbor]<inputMatrix[index]){
                        lower = true;
                        break;
                    }
                }
                // break if neighbour is lower
                if(lower) break;
            }
            // assign result value to flats matrix
            flatsMatrix[index] = !lower;
        }
    }

    //--------------- calc sills -----------------------------
    // probably not working correctly!

    for(int row = 0; row < rows; row++){
        for(int col = 0; col < cols; col++){
            int index = row * cols + col;

            // skip if location is not flat
            if(flatsMatrix[index] == false) continue;

            for (int y = row-1; y <= row+1; y++){
                for (int x = col-1; x <= col+1; x++){
                    int neighbor = y * cols + x;
                    if(x < 0 || x >= cols || y < 0 || y >= rows) continue; 
                    if(neighbor == index) continue;

                    //
                    if(flatsMatrix[neighbor] == false){
                        sillsMatrix[neighbor] = true;
                    }

                }

            }
            // bla bla
        }
    }
}