header = uint16(86);
tail = uint16(87);

fid = fopen ("transmitted.txt", "rb");
k=fread(fid);

for i=1:length(f)
  if f(i)==header
    break
  endif
endfor
  

##for i=1:length(f)
##  up=bitshift(f(i),-4);
##  low=bitshift(f(i),4)/16;
##  nextup=low;
##  if 
##endfor