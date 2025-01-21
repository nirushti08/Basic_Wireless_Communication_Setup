header = 86;
tail = 87;

fid = fopen ("image_bin1.txt", "r");
f = dlmread (fid);
fclose(fid);

m = rows(f);
n = columns(f);

g = reshape(f,1,[]);
g = [m,n,g];

for i=1:length(g)
  if or(g(i) == header, g(i) == tail)
     g(i) = bitshift (g(i), 1);
  endif
endfor

h = [header,g,tail];

fid2 = fopen ("image_bin1_2.txt","wb");
fwrite (fid2,h,"uint16");
fclose(fid2);

fid3 = fopen ("image_bin1_2.txt","rb");
l = fread(fid3,"uint16");
fclose(fid3);
