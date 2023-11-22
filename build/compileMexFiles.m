% compileMexFiles.m

% compile aspect.c
% how to build new compile command:
%%%  mex -outdir ./libMatlab/ -I../include/ ./libMatlab/<mexFileName>.c ./src/<cFileName>.c

% compile aspect.c
mex -outdir ../libMatlab/ -I../include ../libMatlab/mex_aspect.c ../src/aspect.c

% done
fprintf('All source files compiled.\n');