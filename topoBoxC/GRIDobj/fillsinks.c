#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

void fillsinks(int rows, int cols, float *input_matrix, float *output_matrix){
    bool changes = true;

    // fill sinks until there are no more sinks to fill
    while(changes){
        changes = false;

        // a cell is part of a sink, as long as all
        // neighbours are higher or part of a sink

        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                int index = row * cols + col;
                bool sink = true;
                float lowest = 8000; // bigger than biggest in matrix

                for (int y = row-1; y <= row+1; y++){
                    for (int x = col-1; x <= col+1; x++){
                        int neighbor = y * cols + x;
                        // continue if out of bounds
                        if(x < 0 || x >= cols || y < 0 || y >= rows) continue; 
                        if(neighbor == index) continue;

                        if(input_matrix[neighbor] < lowest) lowest = input_matrix[neighbor]; 
                        if(input_matrix[index] > input_matrix[neighbor]){
                            sink = false;
                            break;
                        }
                    }
                    if(!sink) break;
                }
                if(sink){
                    input_matrix[index] = lowest;
                }
            }
        }
    }
}