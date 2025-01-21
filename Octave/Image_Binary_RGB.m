pkg load image

[fname, fpath, fltidx] = uigetfile ({"*.jpg;*.png;*.jpeg;*.webp"}, "Select the picture to transmit");

I= imread (fname);

md = m = int2str(rows(I));
nd = n = int2str(columns(I));

m1 = [];
lm1 = length(m);
for i=1:lm1
  m1 = [m1;m(i);m(i);m(i)]; 
endfor
m = uint8(str2num(m1));

n1 = [];
ln1 = length(n);
for i=1:ln1
  n1 = [n1;n(i);n(i);n(i)]; 
endfor
n = uint8(str2num(n1));

ldim = uint8([lm1*3;ln1*3]);
ldim = [ldim;ldim;ldim];
dim = [m;n];

tid1 = fopen ("image_bin1.txt", "w");
t1 = I(:,:,1);
fwrite (tid1, t1);
fclose (tid1);

tid11 = fopen ("image_bin1.txt", "r");
t11 = padding(fread (tid11));
t11 = [ldim; dim; t11];
fclose (tid11);

tid12 = fopen ("image_bin1.txt", "w");
##t12 = [t11;t11];
fwrite (tid12, t11);
fclose (tid12);

tid2 = fopen ("image_bin2.txt", "w");
t2 = I(:,:,2);
fwrite (tid2, t2);
fclose (tid2);

tid21 = fopen ("image_bin2.txt", "r");
t21 = padding(fread (tid21));
t21 = [ldim; dim; t21];
fclose (tid21);

tid22 = fopen ("image_bin2.txt", "w");
##t22 = [t21;t21];
fwrite (tid22, t21);
fclose (tid22);

tid3 = fopen ("image_bin3.txt", "w");
t3 = I(:,:,3);
fwrite (tid3, t3);
fclose (tid3);

tid31 = fopen ("image_bin3.txt", "r");
t31 = padding(fread (tid31));
t31 = [ldim; dim; t31];
fclose (tid31);

tid32 = fopen ("image_bin3.txt", "w");
##t32 = [t31;t31];
fwrite (tid32, t31);
fclose (tid32);

disp(strcat("Binaries Generated. Dimensions : ",num2str(md)," x ",num2str(nd)))