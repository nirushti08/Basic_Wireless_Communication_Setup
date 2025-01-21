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

tid1 = fopen ("image_bin1.txt", "wb");
t1 = I(:,:,1);
dlmwrite (tid1, t1);
fclose (tid1);

tid2 = fopen ("image_bin2.txt", "wb");
t2 = I(:,:,2);
dlmwrite (tid2, t2);
fclose (tid2);

tid3 = fopen ("image_bin3.txt", "wb");
t3 = I(:,:,3);
dlmwrite (tid3, t3);
fclose (tid3);