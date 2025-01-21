pkg load image

I= imread ("th.jpeg");
m = int2str(rows(I));
n = int2str(columns(I));

m1 = [];
lm1 = length(m);
for i=1:lm1
  m1 = [m1;m(i)]; 
endfor
m = uint8(str2num(m1));

n1 = [];
ln1 = length(m);
for i=1:ln1
  n1 = [n1;n(i)]; 
endfor
n = uint8(str2num(n1));

ldim = uint8([lm1;ln1]);
dim = [m;n];

fid1 = fopen ("image_bin1.txt", "w");
##f0 = I(:,:,1);
f = reshape(I(:,:,1),[],1);
f = [ldim;dim;f];
f1 = padding(f);
fwrite (fid1, f1);
fclose (fid1);

fid2 = fopen ("image_bin2.txt", "w");
g = reshape(I(:,:,2),[],1);
g = [ldim;dim;g];
g1 = padding(g);
fwrite (fid2, g1);
fclose (fid2);

fid3 = fopen ("image_bin3.txt", "w");
h = reshape(I(:,:,3),[],1);
h = [ldim;dim;h];
h1 = padding(h);
fwrite (fid3, h1);
fclose (fid3);
