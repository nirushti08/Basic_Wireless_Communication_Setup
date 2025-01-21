pkg load image

##[fname, fpath, fltidx] = uigetfile ("*.txt", "Select the recievd image binaries IN ORDER", "MultiSelect", "on")

fid1 = "recieved1.txt";#fname{1,1};
fid2 = "recieved2.txt";#fname{1,2};
fid3 = "recieved3.txt";#fname{1,3};

fid1 = fopen (fid1, "r");
J1= fread(fid1);
fclose(fid1);
J11 = J1(2:end,1);
J11 = uint8(char(J11));

ldim1 = J11(1:2,1);
lm1 = ldim1(1); ln1 = ldim1(2);
dim_row1 = sum(ldim1);
dim1 = J11(3:2+dim_row1);
m1 = str2num(erase(num2str(reshape(dim1(1:lm1),1,[]))," "));
n1 = str2num(erase(num2str(reshape(dim1(lm1+1:lm1+ln1),1,[]))," "));
J12 = J11(2+dim_row1+1:2+dim_row1+m1*n1,1);
J13 = reshape(J12,m1,n1);

fid2 = fopen (fid2, "r");
J2= fread(fid2);
fclose(fid2);
J21 = J2(2:end,1);
J21 = uint8(char(J21));

ldim2 = J21(1:2,1);
lm2 = ldim2(1); ln2 = ldim2(2);
dim_row2 = sum(ldim2);
dim2 = J21(3:2+dim_row2);
m2 = str2num(erase(num2str(reshape(dim2(1:lm2),1,[]))," "));
n2 = str2num(erase(num2str(reshape(dim2(lm2+1:lm2+ln2),1,[]))," "));
J22 = J21(2+dim_row2+1:2+dim_row2+m2*n2,1);
J23 = reshape(J22,m1,n1);

fid3 = fopen (fid3, "r");
J3= fread(fid3);
fclose(fid3);
J31 = J3(2:end,1);
J31 = uint8(char(J31));

ldim3 = J31(1:2,1);
lm3 = ldim3(1); ln3 = ldim3(2);
dim_row3 = sum(ldim3);
dim3 = J31(3:2+dim_row3);
m3 = str2num(erase(num2str(reshape(dim3(1:lm3),1,[]))," "));
n3 = str2num(erase(num2str(reshape(dim3(lm3+1:lm3+ln3),1,[]))," "));
J32 = J31(2+dim_row3+1:2+dim_row3+m3*n3,1);
J33 = reshape(J32,m1,n1);

J = uint8(zeros(m1,n1,3));
J(:,:,1) = J13;
J(:,:,2) = J23;
J(:,:,3) = J33;

imwrite (J, "my_output_image.jpeg");