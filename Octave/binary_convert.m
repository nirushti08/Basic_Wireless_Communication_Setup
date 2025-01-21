##fid = fopen ("recieved2.txt", "r");
##f = fread(fid);
##f1 = padding(f);
##fclose(fid);
##fid2 = fopen ("empty.bin","wb");
##fwrite(fid2,f);
##fclose(fid);im2double
q = rep_find(t11(7:24,1))
##q1 = rep_find(q(1:3,1));