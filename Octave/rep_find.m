function fid1 = rep_find (fid)
reps = length(fid)/3;
fid1 = [];

for j=1:reps
##  for 1=1:3
    if fid(1+(j-1)*3,1) == fid(1+(j-1)*3+1,1)
      fid1 = [fid1; fid(1+(j-1)*3,1)];
    elseif fid(1+(j-1)*3,1) == fid(1+(j-1)*3+2,1)
      fid1 = [fid1; fid(1+(j-1)*3,1)];
    elseif fid(1+(j-1)*3+1,1) == fid(1+(j-1)*3+2,1)
      fid1 = [fid1; fid(1+(j-1)*3+1,1)];
    else
      fid1 = [fid1; fid(1+(j-1)*3,1)];
    endif
##  endfor
endfor
endfunction