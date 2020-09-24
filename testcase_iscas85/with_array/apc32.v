/* Generated by Yosys 0.7 (git sha1 61f6811) */

module apc32bits(in, out);
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
  wire \apc16_1.adder1_lv1.a ;
  wire \apc16_1.adder1_lv1.b ;
  wire \apc16_1.adder1_lv1.cin ;
  wire \apc16_1.adder1_lv1.cout ;
  wire \apc16_1.adder1_lv1.d ;
  wire \apc16_1.adder1_lv1.m3.d ;
  wire \apc16_1.adder1_lv2.b ;
  wire \apc16_1.adder1_lv2.cin ;
  wire \apc16_1.adder1_lv2.cout ;
  wire \apc16_1.adder1_lv2.d ;
  wire \apc16_1.adder1_lv2.m3.d ;
  wire \apc16_1.adder2_lv1.a ;
  wire \apc16_1.adder2_lv1.b ;
  wire \apc16_1.adder2_lv1.cin ;
  wire \apc16_1.adder2_lv1.d ;
  wire \apc16_1.adder2_lv1.m3.d ;
  wire \apc16_1.adder2_lv2.cin ;
  wire \apc16_1.adder2_lv2.d ;
  wire \apc16_1.adder2_lv2.m3.d ;
  wire \apc16_1.half1.a ;
  wire \apc16_1.half1.cout ;
  wire \apc16_1.half1.s ;
  wire \apc16_1.half2.cout ;
  wire \apc16_1.half2.s ;
  wire \apc16_1.half3.cout ;
  wire \apc16_1.half3.s ;
  wire \apc16_2.adder1_lv1.a ;
  wire \apc16_2.adder1_lv1.b ;
  wire \apc16_2.adder1_lv1.cin ;
  wire \apc16_2.adder1_lv1.cout ;
  wire \apc16_2.adder1_lv1.d ;
  wire \apc16_2.adder1_lv1.m3.d ;
  wire \apc16_2.adder1_lv2.b ;
  wire \apc16_2.adder1_lv2.cin ;
  wire \apc16_2.adder1_lv2.cout ;
  wire \apc16_2.adder1_lv2.d ;
  wire \apc16_2.adder1_lv2.m3.d ;
  wire \apc16_2.adder2_lv1.a ;
  wire \apc16_2.adder2_lv1.b ;
  wire \apc16_2.adder2_lv1.cin ;
  wire \apc16_2.adder2_lv1.d ;
  wire \apc16_2.adder2_lv1.m3.d ;
  wire \apc16_2.adder2_lv2.cin ;
  wire \apc16_2.adder2_lv2.d ;
  wire \apc16_2.adder2_lv2.m3.d ;
  wire \apc16_2.half1.a ;
  wire \apc16_2.half1.cout ;
  wire \apc16_2.half1.s ;
  wire \apc16_2.half2.cout ;
  wire \apc16_2.half2.s ;
  wire \apc16_2.half3.cout ;
  wire \apc16_2.half3.s ;
  input [31:0] in;
  output [5:0] out;
  or_ii _031_ (
    .a(1'b0),
    .b(1'b0),
    .c(_000_)
  );
  and_ii _032_ (
    .a(1'b0),
    .b(1'b0),
    .c(_001_)
  );
  and_bi _033_ (
    .a(_000_),
    .b(_001_),
    .c(out[0])
  );
  or_ii _034_ (
    .a(\apc16_2.half1.s ),
    .b(\apc16_1.half1.s ),
    .c(_002_)
  );
  and_ii _035_ (
    .a(\apc16_2.half1.s ),
    .b(\apc16_1.half1.s ),
    .c(_003_)
  );
  and_bi _036_ (
    .a(_002_),
    .b(_003_),
    .c(_004_)
  );
  or_bi _037_ (
    .a(_000_),
    .b(_004_),
    .c(_005_)
  );
  and_bi _038_ (
    .a(_000_),
    .b(_004_),
    .c(_006_)
  );
  and_bi _039_ (
    .a(_005_),
    .b(_006_),
    .c(out[1])
  );
  maj_bii _040_ (
    .a(_000_),
    .b(\apc16_2.half1.s ),
    .c(\apc16_1.half1.s ),
    .d(_007_)
  );
  or_ii _041_ (
    .a(\apc16_2.half2.s ),
    .b(\apc16_1.half2.s ),
    .c(_008_)
  );
  and_ii _042_ (
    .a(\apc16_2.half2.s ),
    .b(\apc16_1.half2.s ),
    .c(_009_)
  );
  and_bi _043_ (
    .a(_008_),
    .b(_009_),
    .c(_010_)
  );
  or_bi _044_ (
    .a(_007_),
    .b(_010_),
    .c(_011_)
  );
  and_bi _045_ (
    .a(_007_),
    .b(_010_),
    .c(_012_)
  );
  and_bi _046_ (
    .a(_011_),
    .b(_012_),
    .c(out[2])
  );
  maj_bii _047_ (
    .a(_007_),
    .b(\apc16_2.half2.s ),
    .c(\apc16_1.half2.s ),
    .d(_013_)
  );
  or_ii _048_ (
    .a(\apc16_2.half3.s ),
    .b(\apc16_1.half3.s ),
    .c(_014_)
  );
  and_ii _049_ (
    .a(\apc16_2.half3.s ),
    .b(\apc16_1.half3.s ),
    .c(_015_)
  );
  and_bi _050_ (
    .a(_014_),
    .b(_015_),
    .c(_016_)
  );
  or_bi _051_ (
    .a(_013_),
    .b(_016_),
    .c(_017_)
  );
  and_bi _052_ (
    .a(_013_),
    .b(_016_),
    .c(_018_)
  );
  and_bi _053_ (
    .a(_017_),
    .b(_018_),
    .c(out[3])
  );
  maj_bii _054_ (
    .a(_013_),
    .b(\apc16_2.half3.s ),
    .c(\apc16_1.half3.s ),
    .d(_019_)
  );
  or_ii _055_ (
    .a(\apc16_2.half3.cout ),
    .b(\apc16_1.half3.cout ),
    .c(_020_)
  );
  and_ii _056_ (
    .a(\apc16_2.half3.cout ),
    .b(\apc16_1.half3.cout ),
    .c(_021_)
  );
  and_bi _057_ (
    .a(_020_),
    .b(_021_),
    .c(_022_)
  );
  or_bi _058_ (
    .a(_019_),
    .b(_022_),
    .c(_023_)
  );
  and_bi _059_ (
    .a(_019_),
    .b(_022_),
    .c(_024_)
  );
  and_bi _060_ (
    .a(_023_),
    .b(_024_),
    .c(out[4])
  );
  maj_bbi _061_ (
    .a(\apc16_2.half3.cout ),
    .b(\apc16_1.half3.cout ),
    .c(_019_),
    .d(out[5])
  );
  or_bb _062_ (
    .a(in[17]),
    .b(in[16]),
    .c(\apc16_1.adder1_lv1.a )
  );
  and_bb _063_ (
    .a(in[19]),
    .b(in[18]),
    .c(\apc16_1.adder1_lv1.b )
  );
  or_bb _064_ (
    .a(in[21]),
    .b(in[20]),
    .c(\apc16_1.adder1_lv1.cin )
  );
  and_bb _065_ (
    .a(in[23]),
    .b(in[22]),
    .c(\apc16_1.adder2_lv1.a )
  );
  or_bb _066_ (
    .a(in[25]),
    .b(in[24]),
    .c(\apc16_1.adder2_lv1.b )
  );
  and_bb _067_ (
    .a(in[27]),
    .b(in[26]),
    .c(\apc16_1.adder2_lv1.cin )
  );
  or_bb _068_ (
    .a(in[29]),
    .b(in[28]),
    .c(\apc16_1.adder2_lv2.cin )
  );
  and_bb _069_ (
    .a(in[31]),
    .b(in[30]),
    .c(\apc16_1.half1.a )
  );
  maj_bbb _070_ (
    .a(\apc16_1.adder1_lv1.cin ),
    .b(\apc16_1.adder1_lv1.b ),
    .c(\apc16_1.adder1_lv1.a ),
    .d(\apc16_1.adder1_lv1.cout )
  );
  maj_bbi _071_ (
    .a(\apc16_1.adder1_lv1.b ),
    .b(\apc16_1.adder1_lv1.a ),
    .c(\apc16_1.adder1_lv1.cin ),
    .d(\apc16_1.adder1_lv1.d )
  );
  maj_bbi _072_ (
    .a(\apc16_1.adder1_lv1.d ),
    .b(\apc16_1.adder1_lv1.cin ),
    .c(\apc16_1.adder1_lv1.cout ),
    .d(\apc16_1.adder1_lv1.m3.d )
  );
  maj_bbb _073_ (
    .a(\apc16_1.adder1_lv2.cin ),
    .b(\apc16_1.adder1_lv2.b ),
    .c(\apc16_1.adder1_lv1.cout ),
    .d(\apc16_1.adder1_lv2.cout )
  );
  maj_bbi _074_ (
    .a(\apc16_1.adder1_lv2.b ),
    .b(\apc16_1.adder1_lv1.cout ),
    .c(\apc16_1.adder1_lv2.cin ),
    .d(\apc16_1.adder1_lv2.d )
  );
  maj_bbi _075_ (
    .a(\apc16_1.adder1_lv2.d ),
    .b(\apc16_1.adder1_lv2.cin ),
    .c(\apc16_1.adder1_lv2.cout ),
    .d(\apc16_1.adder1_lv2.m3.d )
  );
  maj_bbb _076_ (
    .a(\apc16_1.adder2_lv1.cin ),
    .b(\apc16_1.adder2_lv1.b ),
    .c(\apc16_1.adder2_lv1.a ),
    .d(\apc16_1.adder1_lv2.b )
  );
  maj_bbi _077_ (
    .a(\apc16_1.adder2_lv1.b ),
    .b(\apc16_1.adder2_lv1.a ),
    .c(\apc16_1.adder2_lv1.cin ),
    .d(\apc16_1.adder2_lv1.d )
  );
  maj_bbi _078_ (
    .a(\apc16_1.adder2_lv1.d ),
    .b(\apc16_1.adder2_lv1.cin ),
    .c(\apc16_1.adder1_lv2.b ),
    .d(\apc16_1.adder2_lv1.m3.d )
  );
  maj_bbb _079_ (
    .a(\apc16_1.adder2_lv2.cin ),
    .b(\apc16_1.adder2_lv1.m3.d ),
    .c(\apc16_1.adder1_lv1.m3.d ),
    .d(\apc16_1.adder1_lv2.cin )
  );
  maj_bbi _080_ (
    .a(\apc16_1.adder2_lv1.m3.d ),
    .b(\apc16_1.adder1_lv1.m3.d ),
    .c(\apc16_1.adder2_lv2.cin ),
    .d(\apc16_1.adder2_lv2.d )
  );
  maj_bbi _081_ (
    .a(\apc16_1.adder2_lv2.d ),
    .b(\apc16_1.adder2_lv2.cin ),
    .c(\apc16_1.adder1_lv2.cin ),
    .d(\apc16_1.adder2_lv2.m3.d )
  );
  and_bb _082_ (
    .a(\apc16_1.adder2_lv2.m3.d ),
    .b(\apc16_1.half1.a ),
    .c(\apc16_1.half1.cout )
  );
  or_bb _083_ (
    .a(\apc16_1.adder2_lv2.m3.d ),
    .b(\apc16_1.half1.a ),
    .c(_025_)
  );
  and_bi _084_ (
    .a(_025_),
    .b(\apc16_1.half1.cout ),
    .c(\apc16_1.half1.s )
  );
  and_bb _085_ (
    .a(\apc16_1.half1.cout ),
    .b(\apc16_1.adder1_lv2.m3.d ),
    .c(\apc16_1.half2.cout )
  );
  or_bb _086_ (
    .a(\apc16_1.half1.cout ),
    .b(\apc16_1.adder1_lv2.m3.d ),
    .c(_026_)
  );
  and_bi _087_ (
    .a(_026_),
    .b(\apc16_1.half2.cout ),
    .c(\apc16_1.half2.s )
  );
  and_bb _088_ (
    .a(\apc16_1.half2.cout ),
    .b(\apc16_1.adder1_lv2.cout ),
    .c(\apc16_1.half3.cout )
  );
  or_bb _089_ (
    .a(\apc16_1.half2.cout ),
    .b(\apc16_1.adder1_lv2.cout ),
    .c(_027_)
  );
  and_bi _090_ (
    .a(_027_),
    .b(\apc16_1.half3.cout ),
    .c(\apc16_1.half3.s )
  );
  or_bb _091_ (
    .a(in[1]),
    .b(in[0]),
    .c(\apc16_2.adder1_lv1.a )
  );
  and_bb _092_ (
    .a(in[3]),
    .b(in[2]),
    .c(\apc16_2.adder1_lv1.b )
  );
  or_bb _093_ (
    .a(in[5]),
    .b(in[4]),
    .c(\apc16_2.adder1_lv1.cin )
  );
  and_bb _094_ (
    .a(in[7]),
    .b(in[6]),
    .c(\apc16_2.adder2_lv1.a )
  );
  or_bb _095_ (
    .a(in[9]),
    .b(in[8]),
    .c(\apc16_2.adder2_lv1.b )
  );
  and_bb _096_ (
    .a(in[11]),
    .b(in[10]),
    .c(\apc16_2.adder2_lv1.cin )
  );
  or_bb _097_ (
    .a(in[13]),
    .b(in[12]),
    .c(\apc16_2.adder2_lv2.cin )
  );
  and_bb _098_ (
    .a(in[15]),
    .b(in[14]),
    .c(\apc16_2.half1.a )
  );
  maj_bbb _099_ (
    .a(\apc16_2.adder1_lv1.cin ),
    .b(\apc16_2.adder1_lv1.b ),
    .c(\apc16_2.adder1_lv1.a ),
    .d(\apc16_2.adder1_lv1.cout )
  );
  maj_bbi _100_ (
    .a(\apc16_2.adder1_lv1.b ),
    .b(\apc16_2.adder1_lv1.a ),
    .c(\apc16_2.adder1_lv1.cin ),
    .d(\apc16_2.adder1_lv1.d )
  );
  maj_bbi _101_ (
    .a(\apc16_2.adder1_lv1.d ),
    .b(\apc16_2.adder1_lv1.cin ),
    .c(\apc16_2.adder1_lv1.cout ),
    .d(\apc16_2.adder1_lv1.m3.d )
  );
  maj_bbb _102_ (
    .a(\apc16_2.adder1_lv2.cin ),
    .b(\apc16_2.adder1_lv2.b ),
    .c(\apc16_2.adder1_lv1.cout ),
    .d(\apc16_2.adder1_lv2.cout )
  );
  maj_bbi _103_ (
    .a(\apc16_2.adder1_lv2.b ),
    .b(\apc16_2.adder1_lv1.cout ),
    .c(\apc16_2.adder1_lv2.cin ),
    .d(\apc16_2.adder1_lv2.d )
  );
  maj_bbi _104_ (
    .a(\apc16_2.adder1_lv2.d ),
    .b(\apc16_2.adder1_lv2.cin ),
    .c(\apc16_2.adder1_lv2.cout ),
    .d(\apc16_2.adder1_lv2.m3.d )
  );
  maj_bbb _105_ (
    .a(\apc16_2.adder2_lv1.cin ),
    .b(\apc16_2.adder2_lv1.b ),
    .c(\apc16_2.adder2_lv1.a ),
    .d(\apc16_2.adder1_lv2.b )
  );
  maj_bbi _106_ (
    .a(\apc16_2.adder2_lv1.b ),
    .b(\apc16_2.adder2_lv1.a ),
    .c(\apc16_2.adder2_lv1.cin ),
    .d(\apc16_2.adder2_lv1.d )
  );
  maj_bbi _107_ (
    .a(\apc16_2.adder2_lv1.d ),
    .b(\apc16_2.adder2_lv1.cin ),
    .c(\apc16_2.adder1_lv2.b ),
    .d(\apc16_2.adder2_lv1.m3.d )
  );
  maj_bbb _108_ (
    .a(\apc16_2.adder2_lv2.cin ),
    .b(\apc16_2.adder2_lv1.m3.d ),
    .c(\apc16_2.adder1_lv1.m3.d ),
    .d(\apc16_2.adder1_lv2.cin )
  );
  maj_bbi _109_ (
    .a(\apc16_2.adder2_lv1.m3.d ),
    .b(\apc16_2.adder1_lv1.m3.d ),
    .c(\apc16_2.adder2_lv2.cin ),
    .d(\apc16_2.adder2_lv2.d )
  );
  maj_bbi _110_ (
    .a(\apc16_2.adder2_lv2.d ),
    .b(\apc16_2.adder2_lv2.cin ),
    .c(\apc16_2.adder1_lv2.cin ),
    .d(\apc16_2.adder2_lv2.m3.d )
  );
  and_bb _111_ (
    .a(\apc16_2.adder2_lv2.m3.d ),
    .b(\apc16_2.half1.a ),
    .c(\apc16_2.half1.cout )
  );
  or_bb _112_ (
    .a(\apc16_2.adder2_lv2.m3.d ),
    .b(\apc16_2.half1.a ),
    .c(_028_)
  );
  and_bi _113_ (
    .a(_028_),
    .b(\apc16_2.half1.cout ),
    .c(\apc16_2.half1.s )
  );
  and_bb _114_ (
    .a(\apc16_2.half1.cout ),
    .b(\apc16_2.adder1_lv2.m3.d ),
    .c(\apc16_2.half2.cout )
  );
  or_bb _115_ (
    .a(\apc16_2.half1.cout ),
    .b(\apc16_2.adder1_lv2.m3.d ),
    .c(_029_)
  );
  and_bi _116_ (
    .a(_029_),
    .b(\apc16_2.half2.cout ),
    .c(\apc16_2.half2.s )
  );
  and_bb _117_ (
    .a(\apc16_2.half2.cout ),
    .b(\apc16_2.adder1_lv2.cout ),
    .c(\apc16_2.half3.cout )
  );
  or_bb _118_ (
    .a(\apc16_2.half2.cout ),
    .b(\apc16_2.adder1_lv2.cout ),
    .c(_030_)
  );
  and_bi _119_ (
    .a(_030_),
    .b(\apc16_2.half3.cout ),
    .c(\apc16_2.half3.s )
  );
endmodule
