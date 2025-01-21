pkg load image

rid1 = fopen ("recieved1.txt", "rb");
r1= dlmread(rid1);
fclose(rid1);

rid2 = fopen ("recieved2.txt", "rb");
r2= dlmread(rid2);
fclose(rid2);

rid3 = fopen ("recieved3.txt", "rb");
r3= dlmread(rid3);
fclose(rid3);

##J = uint8(zeros(m1,n1,3));
J(:,:,1) = r1;
J(:,:,2) = r2;
J(:,:,3) = r3;

