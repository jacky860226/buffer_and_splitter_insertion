module c17(N1, N2, N3, N6, N7, N22, N23);
	wire _0_;
	wire new_net_0;
	wire new_net_2;
	wire new_net_6;
	wire new_net_7;
	wire new_net_8;
	wire new_net_9;
	wire new_net_10;
	wire _3_;
	wire new_net_4;
	wire new_net_11;
	wire new_net_15;
	wire _2_;
	wire new_net_1;
	wire new_net_3;
	wire _1_;
	wire new_net_5;
	wire new_net_13;
	wire new_net_14;
	input N1;
	input N2;
	input N3;
	input N6;
	input N7;
	output N22;
	output N23;

	and_bb _4_ (
		.a(new_net_4),
		.b(new_net_6),
		.c(_2_)
	);

	or_ii _5_ (
		.a(new_net_7),
		.b(new_net_5),
		.c(_3_)
	);

	and_bb _6_ (
		.a(new_net_0),
		.b(new_net_2),
		.c(_0_)
	);

	or_bb _7_ (
		.a(_0_),
		.b(new_net_8),
		.c(N22)
	);

	and_ii _8_ (
		.a(new_net_9),
		.b(new_net_3),
		.c(_1_)
	);

	and_bi _9_ (
		.a(new_net_1),
		.b(new_net_10),
		.c(new_net_11)
	);

	spl2 _3__v_fanout (
		.a(_3_),
		.b(new_net_1),
		.c(new_net_0)
	);

	spl2 N3_v_fanout (
		.a(N3),
		.b(new_net_5),
		.c(new_net_4)
	);

	bfr new_net_13_bfr_before (
		.din(new_net_13),
		.dout(new_net_2)
	);

	bfr new_net_14_bfr_before (
		.din(new_net_14),
		.dout(new_net_13)
	);

	spl2 N2_v_fanout (
		.a(N2),
		.b(new_net_3),
		.c(new_net_14)
	);

	bfr new_net_6_bfr_after (
		.din(N1),
		.dout(new_net_6)
	);

	bfr new_net_9_bfr_after (
		.din(N7),
		.dout(new_net_9)
	);

	bfr new_net_15_bfr_after (
		.din(_2_),
		.dout(new_net_15)
	);

	bfr new_net_8_bfr_after (
		.din(new_net_15),
		.dout(new_net_8)
	);

	bfr new_net_10_bfr_after (
		.din(_1_),
		.dout(new_net_10)
	);

	bfr new_net_7_bfr_after (
		.din(N6),
		.dout(new_net_7)
	);

	bfr N23_bfr_after (
		.din(new_net_11),
		.dout(N23)
	);

endmodule