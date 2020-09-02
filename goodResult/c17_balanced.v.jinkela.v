module c17(N6,N3,N2,N7,N1);
    wire new_Jinkela_wire_6;
    wire new_Jinkela_wire_5;
    wire new_Jinkela_wire_1;
    wire new_Jinkela_wire_8;
    wire new_Jinkela_wire_9;
    wire new_Jinkela_wire_11;
    wire new_Jinkela_wire_3;
    wire new_Jinkela_wire_0;
    wire new_Jinkela_wire_12;
    wire new_Jinkela_wire_10;
    wire new_Jinkela_wire_14;
    wire _3_;
    wire _1_;
    wire new_Jinkela_wire_4;
    wire new_Jinkela_wire_2;
    wire new_Jinkela_wire_13;
    wire _2_;
    wire new_Jinkela_wire_7;
    wire _0_;
    wire new_net_11;
    input N6;
    input N3;
    input N2;
    input N7;
    input N1;
    output N22;
    output N23;

    and_ii _8_ (
        .a(new_Jinkela_wire_7),
        .b(new_Jinkela_wire_3),
        .c(_1_)
    );

    bfr new_Jinkela_buffer_8 (
        .din(new_net_11),
        .dout(new_Jinkela_wire_14)
    );

    bfr new_Jinkela_buffer_7 (
        .din(new_Jinkela_wire_12),
        .dout(new_Jinkela_wire_13)
    );

    and_bi _9_ (
        .a(new_Jinkela_wire_10),
        .b(new_Jinkela_wire_11),
        .c(new_net_11)
    );

    spl2 new_Jinkela_splitter_0 (
        .a(N3),
        .c(new_Jinkela_wire_1),
        .b(new_Jinkela_wire_2)
    );

    bfr new_Jinkela_buffer_0 (
        .din(N6),
        .dout(new_Jinkela_wire_0)
    );

    spl2 new_Jinkela_splitter_1 (
        .a(N2),
        .c(new_Jinkela_wire_3),
        .b(new_Jinkela_wire_4)
    );

    bfr new_Jinkela_buffer_3 (
        .din(N7),
        .dout(new_Jinkela_wire_7)
    );

    bfr new_Jinkela_buffer_1 (
        .din(new_Jinkela_wire_4),
        .dout(new_Jinkela_wire_5)
    );

    bfr new_Jinkela_buffer_4 (
        .din(N1),
        .dout(new_Jinkela_wire_8)
    );

    spl2 new_Jinkela_splitter_2 (
        .a(_3_),
        .c(new_Jinkela_wire_9),
        .b(new_Jinkela_wire_10)
    );

    bfr new_Jinkela_buffer_2 (
        .din(new_Jinkela_wire_5),
        .dout(new_Jinkela_wire_6)
    );

    or_bb _7_ (
        .a(_0_),
        .b(new_Jinkela_wire_13),
        .c(N22)
    );

    bfr new_Jinkela_buffer_5 (
        .din(_1_),
        .dout(new_Jinkela_wire_11)
    );

    or_ii _5_ (
        .a(new_Jinkela_wire_0),
        .b(new_Jinkela_wire_2),
        .c(_3_)
    );

    bfr new_Jinkela_buffer_6 (
        .din(_2_),
        .dout(new_Jinkela_wire_12)
    );

    and_bb _6_ (
        .a(new_Jinkela_wire_9),
        .b(new_Jinkela_wire_6),
        .c(_0_)
    );

    and_bb _4_ (
        .a(new_Jinkela_wire_1),
        .b(new_Jinkela_wire_8),
        .c(_2_)
    );

endmodule
