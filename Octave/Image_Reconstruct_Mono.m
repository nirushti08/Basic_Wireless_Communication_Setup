pkg load image

##[fname, fpath, fltidx] = uigetfile ("*.txt", "Select the recievd image binaries IN ORDER", "MultiSelect", "on")

fid1 = "transmitted.txt";#fname{1,1};

fid1 = fopen (fid1, "r");
J1= fread(fid1);
fclose(fid1);
J11 = J1(2:end,1);
J11 = uint8(char(J11));

ldim1 = rep_find(J11(1:6,1));
lm1 = ldim1(1)/3;
ln1 = ldim1(2)/3;
dim_row1 = sum(ldim1);
dim1 = J11(7:6+dim_row1);
dim1 = rep_find(dim1);
m1 = str2num(erase(num2str(reshape(dim1(1:lm1),1,[]))," "));
n1 = str2num(erase(num2str(reshape(dim1(lm1+1:lm1+ln1),1,[]))," "));
J12 = J11(6+dim_row1+1:6+dim_row1+m1*n1,1);
J13 = reshape(J12,m1,n1);


J = J13;

all(J11==t11(1:length(J11),1));
all(and(J13,t1));
idx = find (not(J11==t11(1:length(J11),1)));
idx = uint32(idx);

imwrite (J, "my_output_image.jpeg");
disp(strcat("Image Recreated. Dimensions : ",num2str(m1)," x ",num2str(n1)))
