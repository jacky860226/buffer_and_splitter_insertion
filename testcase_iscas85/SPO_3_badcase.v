module SPO_3_badcase(i0,i1,i2,i3,i4,i5,i6,o0,o1,o2,o3);
  wire og0;
  wire og1;
  wire og2;
  wire og3;
  input i0;
  input i1;
  input i2;
  input i3;
  input i4;
  input i5;
  input i6;
  output o0;
  output o1;
  output o2;
  output o3;
  and_bb g0 (
    .a(i1),
    .b(i2),
    .c(og0)
  );
  and_bb g1 (
    .a(i4),
    .b(i5),
    .c(og1)
  );
  inv g2 (
    .din(og0),
    .dout(og2)
  );
  and_bb g3 (
    .a(i3),
    .b(og1),
    .c(og3)
  );
  maj_bbb g4 (
    .a(i0),
    .b(i3),
    .c(og2),
    .d(o0)
  );
  and_bb g5 (
    .a(i3),
    .b(og2),
    .c(o1)
  );
  and_bb g6 (
    .a(i3),
    .b(og3),
    .c(o2)
  );
  maj_bbb g7 (
    .a(i3),
    .b(og3),
    .c(i6),
    .d(o3)
  );
endmodule
