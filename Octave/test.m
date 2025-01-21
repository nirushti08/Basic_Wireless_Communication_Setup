
ldim = f1(1:2,1);
lm = ldim(1); ln = ldim(2);
dim_row = sum(ldim);
dim = f1(3:2+dim_row);
m4 = str2num(erase(num2str(reshape(dim(1:lm),1,[]))," "));
n4 = str2num(erase(num2str(reshape(dim(lm+1:lm+ln),1,[]))," "));
f2 = reshape(f1(3+dim_row:2+dim_row+m4*n4,1),m4,n4);
##m2 = num2str(m1);
##m3 = erase(m2," ");
##m4 = str2num(m3);