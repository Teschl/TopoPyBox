#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void gradient8(int rows, int cols, int32_t *input_matrix, int32_t * output_matrix){

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            // Koordinaten der aktuellen Zelle
            int current_cell = i * cols + j;
            // Aktuelle Zelle sei erster minimaler Wert
            int min_neighbor = current_cell;

            // Nachbarn überprüfen
            for (int ni = -1; ni <= 1; ni++) {
                for (int nj = -1; nj <= 1; nj++) {
                    // Koordinaten angepasst mit jeweils +1, +0 oder -1
                    int ni_index = i + ni;
                    int nj_index = j + nj;

                    // Wenn Nachbar außerhalb des Arrays wäre überspringen.
                    if (ni_index >= 0 && ni_index < rows && nj_index >= 0 && nj_index < cols) {
                        // Koordinaten des Nachbars
                        int neighbor_index = ni_index * cols + nj_index;

                        // Gespeicherte Minimalwerte überschreiben falls neue Minimalwerte gefunden
                        if (input_matrix[neighbor_index] < input_matrix[min_neighbor]) {
                            min_neighbor = neighbor_index;
                        }
                    }
                }
            }
            // Die Koordinaten der aktuellen Zelle abziehen von den des kleinsten Nachbars 
            if (min_neighbor - current_cell > 1){
                output_matrix[current_cell] = min_neighbor - current_cell - cols +3;  
            } else if (min_neighbor - current_cell < -1){
                output_matrix[current_cell] = min_neighbor - current_cell + cols -3;  
            } else{
                output_matrix[current_cell] = min_neighbor - current_cell;  
            }
        }
    }
}