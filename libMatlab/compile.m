% compile example.c
% mex -outdir ./libMatlab/ -I../include/ ./libMatlab/example.c ./src/example.c

% compile aspect.c
mex -I../include ./mex_aspect.c ../src/aspect.c

% done
fprintf('All source files compiled.\n');