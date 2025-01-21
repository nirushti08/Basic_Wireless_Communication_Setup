function fid = padding (fid)
  packet_len = 256; #bytes
  zero_pad = 64*256; #bytes
  pad = mod(length(fid),packet_len);
  if pad != 0
    fid = [fid;255*ones(256-pad,1)];
  endif
  fid =  [fid; 255*ones(zero_pad,1)];
endfunction