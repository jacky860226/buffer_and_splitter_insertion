/* Generated by Yosys 0.7 (git sha1 61f6811) */

module apc64bits(in, out);
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
  wire _031_;
  wire _032_;
  wire _033_;
  wire _034_;
  wire _035_;
  wire _036_;
  wire _037_;
  wire _038_;
  wire _039_;
  wire _040_;
  wire _041_;
  wire _042_;
  wire _043_;
  wire _044_;
  wire _045_;
  wire _046_;
  wire _047_;
  wire _048_;
  wire _049_;
  wire _050_;
  wire _051_;
  wire _052_;
  wire _053_;
  wire _054_;
  wire _055_;
  wire _056_;
  wire _057_;
  wire _058_;
  wire _059_;
  wire _060_;
  wire _061_;
  wire _062_;
  wire _063_;
  wire _064_;
  wire _065_;
  wire _066_;
  wire _067_;
  wire _068_;
  wire _069_;
  wire _070_;
  wire _071_;
  wire _072_;
  wire _073_;
  wire _074_;
  wire _075_;
  wire _076_;
  wire _077_;
  wire _078_;
  wire _079_;
  wire _080_;
  wire _081_;
  wire _082_;
  wire _083_;
  wire _084_;
  wire _085_;
  wire _086_;
  wire _087_;
  wire _088_;
  wire _089_;
  wire _090_;
  wire _091_;
  wire _092_;
  wire \apc32_1.apc16_1.adder1_lv1.a ;
  wire \apc32_1.apc16_1.adder1_lv1.b ;
  wire \apc32_1.apc16_1.adder1_lv1.cin ;
  wire \apc32_1.apc16_1.adder1_lv1.cout ;
  wire \apc32_1.apc16_1.adder1_lv1.d ;
  wire \apc32_1.apc16_1.adder1_lv1.m3.d ;
  wire \apc32_1.apc16_1.adder1_lv2.b ;
  wire \apc32_1.apc16_1.adder1_lv2.cin ;
  wire \apc32_1.apc16_1.adder1_lv2.cout ;
  wire \apc32_1.apc16_1.adder1_lv2.d ;
  wire \apc32_1.apc16_1.adder1_lv2.m3.d ;
  wire \apc32_1.apc16_1.adder2_lv1.a ;
  wire \apc32_1.apc16_1.adder2_lv1.b ;
  wire \apc32_1.apc16_1.adder2_lv1.cin ;
  wire \apc32_1.apc16_1.adder2_lv1.d ;
  wire \apc32_1.apc16_1.adder2_lv1.m3.d ;
  wire \apc32_1.apc16_1.adder2_lv2.cin ;
  wire \apc32_1.apc16_1.adder2_lv2.d ;
  wire \apc32_1.apc16_1.adder2_lv2.m3.d ;
  wire \apc32_1.apc16_1.half1.a ;
  wire \apc32_1.apc16_1.half1.cout ;
  wire \apc32_1.apc16_1.half1.s ;
  wire \apc32_1.apc16_1.half2.cout ;
  wire \apc32_1.apc16_1.half2.s ;
  wire \apc32_1.apc16_1.half3.cout ;
  wire \apc32_1.apc16_1.half3.s ;
  wire \apc32_1.apc16_2.adder1_lv1.a ;
  wire \apc32_1.apc16_2.adder1_lv1.b ;
  wire \apc32_1.apc16_2.adder1_lv1.cin ;
  wire \apc32_1.apc16_2.adder1_lv1.cout ;
  wire \apc32_1.apc16_2.adder1_lv1.d ;
  wire \apc32_1.apc16_2.adder1_lv1.m3.d ;
  wire \apc32_1.apc16_2.adder1_lv2.b ;
  wire \apc32_1.apc16_2.adder1_lv2.cin ;
  wire \apc32_1.apc16_2.adder1_lv2.cout ;
  wire \apc32_1.apc16_2.adder1_lv2.d ;
  wire \apc32_1.apc16_2.adder1_lv2.m3.d ;
  wire \apc32_1.apc16_2.adder2_lv1.a ;
  wire \apc32_1.apc16_2.adder2_lv1.b ;
  wire \apc32_1.apc16_2.adder2_lv1.cin ;
  wire \apc32_1.apc16_2.adder2_lv1.d ;
  wire \apc32_1.apc16_2.adder2_lv1.m3.d ;
  wire \apc32_1.apc16_2.adder2_lv2.cin ;
  wire \apc32_1.apc16_2.adder2_lv2.d ;
  wire \apc32_1.apc16_2.adder2_lv2.m3.d ;
  wire \apc32_1.apc16_2.half1.a ;
  wire \apc32_1.apc16_2.half1.cout ;
  wire \apc32_1.apc16_2.half1.s ;
  wire \apc32_1.apc16_2.half2.cout ;
  wire \apc32_1.apc16_2.half2.s ;
  wire \apc32_1.apc16_2.half3.cout ;
  wire \apc32_1.apc16_2.half3.s ;
  wire [5:0] \apc32_1.out ;
  wire \apc32_2.apc16_1.adder1_lv1.a ;
  wire \apc32_2.apc16_1.adder1_lv1.b ;
  wire \apc32_2.apc16_1.adder1_lv1.cin ;
  wire \apc32_2.apc16_1.adder1_lv1.cout ;
  wire \apc32_2.apc16_1.adder1_lv1.d ;
  wire \apc32_2.apc16_1.adder1_lv1.m3.d ;
  wire \apc32_2.apc16_1.adder1_lv2.b ;
  wire \apc32_2.apc16_1.adder1_lv2.cin ;
  wire \apc32_2.apc16_1.adder1_lv2.cout ;
  wire \apc32_2.apc16_1.adder1_lv2.d ;
  wire \apc32_2.apc16_1.adder1_lv2.m3.d ;
  wire \apc32_2.apc16_1.adder2_lv1.a ;
  wire \apc32_2.apc16_1.adder2_lv1.b ;
  wire \apc32_2.apc16_1.adder2_lv1.cin ;
  wire \apc32_2.apc16_1.adder2_lv1.d ;
  wire \apc32_2.apc16_1.adder2_lv1.m3.d ;
  wire \apc32_2.apc16_1.adder2_lv2.cin ;
  wire \apc32_2.apc16_1.adder2_lv2.d ;
  wire \apc32_2.apc16_1.adder2_lv2.m3.d ;
  wire \apc32_2.apc16_1.half1.a ;
  wire \apc32_2.apc16_1.half1.cout ;
  wire \apc32_2.apc16_1.half1.s ;
  wire \apc32_2.apc16_1.half2.cout ;
  wire \apc32_2.apc16_1.half2.s ;
  wire \apc32_2.apc16_1.half3.cout ;
  wire \apc32_2.apc16_1.half3.s ;
  wire \apc32_2.apc16_2.adder1_lv1.a ;
  wire \apc32_2.apc16_2.adder1_lv1.b ;
  wire \apc32_2.apc16_2.adder1_lv1.cin ;
  wire \apc32_2.apc16_2.adder1_lv1.cout ;
  wire \apc32_2.apc16_2.adder1_lv1.d ;
  wire \apc32_2.apc16_2.adder1_lv1.m3.d ;
  wire \apc32_2.apc16_2.adder1_lv2.b ;
  wire \apc32_2.apc16_2.adder1_lv2.cin ;
  wire \apc32_2.apc16_2.adder1_lv2.cout ;
  wire \apc32_2.apc16_2.adder1_lv2.d ;
  wire \apc32_2.apc16_2.adder1_lv2.m3.d ;
  wire \apc32_2.apc16_2.adder2_lv1.a ;
  wire \apc32_2.apc16_2.adder2_lv1.b ;
  wire \apc32_2.apc16_2.adder2_lv1.cin ;
  wire \apc32_2.apc16_2.adder2_lv1.d ;
  wire \apc32_2.apc16_2.adder2_lv1.m3.d ;
  wire \apc32_2.apc16_2.adder2_lv2.cin ;
  wire \apc32_2.apc16_2.adder2_lv2.d ;
  wire \apc32_2.apc16_2.adder2_lv2.m3.d ;
  wire \apc32_2.apc16_2.half1.a ;
  wire \apc32_2.apc16_2.half1.cout ;
  wire \apc32_2.apc16_2.half1.s ;
  wire \apc32_2.apc16_2.half2.cout ;
  wire \apc32_2.apc16_2.half2.s ;
  wire \apc32_2.apc16_2.half3.cout ;
  wire \apc32_2.apc16_2.half3.s ;
  wire [5:0] \apc32_2.out ;
  input [63:0] in;
  output [6:0] out;
  or_ii _093_ (
    .a(\apc32_2.out [0]),
    .b(\apc32_1.out [0]),
    .c(_000_)
  );
  or_ii _094_ (
    .a(\apc32_2.out [1]),
    .b(\apc32_1.out [1]),
    .c(_001_)
  );
  and_ii _095_ (
    .a(\apc32_2.out [1]),
    .b(\apc32_1.out [1]),
    .c(_002_)
  );
  and_bi _096_ (
    .a(_001_),
    .b(_002_),
    .c(_003_)
  );
  or_bi _097_ (
    .a(_000_),
    .b(_003_),
    .c(_004_)
  );
  and_bi _098_ (
    .a(_000_),
    .b(_003_),
    .c(_005_)
  );
  and_bi _099_ (
    .a(_004_),
    .b(_005_),
    .c(out[1])
  );
  maj_bii _100_ (
    .a(_000_),
    .b(\apc32_2.out [1]),
    .c(\apc32_1.out [1]),
    .d(_006_)
  );
  or_ii _101_ (
    .a(\apc32_2.out [2]),
    .b(\apc32_1.out [2]),
    .c(_007_)
  );
  and_ii _102_ (
    .a(\apc32_2.out [2]),
    .b(\apc32_1.out [2]),
    .c(_008_)
  );
  and_bi _103_ (
    .a(_007_),
    .b(_008_),
    .c(_009_)
  );
  or_bi _104_ (
    .a(_006_),
    .b(_009_),
    .c(_010_)
  );
  and_bi _105_ (
    .a(_006_),
    .b(_009_),
    .c(_011_)
  );
  and_bi _106_ (
    .a(_010_),
    .b(_011_),
    .c(out[2])
  );
  maj_bii _107_ (
    .a(_006_),
    .b(\apc32_2.out [2]),
    .c(\apc32_1.out [2]),
    .d(_012_)
  );
  or_ii _108_ (
    .a(\apc32_2.out [3]),
    .b(\apc32_1.out [3]),
    .c(_013_)
  );
  and_ii _109_ (
    .a(\apc32_2.out [3]),
    .b(\apc32_1.out [3]),
    .c(_014_)
  );
  and_bi _110_ (
    .a(_013_),
    .b(_014_),
    .c(_015_)
  );
  or_bi _111_ (
    .a(_012_),
    .b(_015_),
    .c(_016_)
  );
  and_bi _112_ (
    .a(_012_),
    .b(_015_),
    .c(_017_)
  );
  and_bi _113_ (
    .a(_016_),
    .b(_017_),
    .c(out[3])
  );
  maj_bii _114_ (
    .a(_012_),
    .b(\apc32_2.out [3]),
    .c(\apc32_1.out [3]),
    .d(_018_)
  );
  or_ii _115_ (
    .a(\apc32_2.out [4]),
    .b(\apc32_1.out [4]),
    .c(_019_)
  );
  and_ii _116_ (
    .a(\apc32_2.out [4]),
    .b(\apc32_1.out [4]),
    .c(_020_)
  );
  and_bi _117_ (
    .a(_019_),
    .b(_020_),
    .c(_021_)
  );
  or_bi _118_ (
    .a(_018_),
    .b(_021_),
    .c(_022_)
  );
  and_bi _119_ (
    .a(_018_),
    .b(_021_),
    .c(_023_)
  );
  and_bi _120_ (
    .a(_022_),
    .b(_023_),
    .c(out[4])
  );
  maj_bii _121_ (
    .a(_018_),
    .b(\apc32_2.out [4]),
    .c(\apc32_1.out [4]),
    .d(_024_)
  );
  or_ii _122_ (
    .a(\apc32_2.out [5]),
    .b(\apc32_1.out [5]),
    .c(_025_)
  );
  and_ii _123_ (
    .a(\apc32_2.out [5]),
    .b(\apc32_1.out [5]),
    .c(_026_)
  );
  and_bi _124_ (
    .a(_025_),
    .b(_026_),
    .c(_027_)
  );
  or_bi _125_ (
    .a(_024_),
    .b(_027_),
    .c(_028_)
  );
  and_bi _126_ (
    .a(_024_),
    .b(_027_),
    .c(_029_)
  );
  and_bi _127_ (
    .a(_028_),
    .b(_029_),
    .c(out[5])
  );
  maj_bbi _128_ (
    .a(\apc32_2.out [5]),
    .b(\apc32_1.out [5]),
    .c(_024_),
    .d(out[6])
  );
  and_ii _129_ (
    .a(\apc32_2.out [0]),
    .b(\apc32_1.out [0]),
    .c(_030_)
  );
  and_bi _130_ (
    .a(_000_),
    .b(_030_),
    .c(out[0])
  );
  or_ii _131_ (
    .a(1'b0),
    .b(1'b0),
    .c(_031_)
  );
  or_ii _132_ (
    .a(\apc32_1.apc16_2.half1.s ),
    .b(\apc32_1.apc16_1.half1.s ),
    .c(_032_)
  );
  and_ii _133_ (
    .a(\apc32_1.apc16_2.half1.s ),
    .b(\apc32_1.apc16_1.half1.s ),
    .c(_033_)
  );
  and_bi _134_ (
    .a(_032_),
    .b(_033_),
    .c(_034_)
  );
  or_bi _135_ (
    .a(_031_),
    .b(_034_),
    .c(_035_)
  );
  and_bi _136_ (
    .a(_031_),
    .b(_034_),
    .c(_036_)
  );
  and_bi _137_ (
    .a(_035_),
    .b(_036_),
    .c(\apc32_1.out [1])
  );
  maj_bii _138_ (
    .a(_031_),
    .b(\apc32_1.apc16_2.half1.s ),
    .c(\apc32_1.apc16_1.half1.s ),
    .d(_037_)
  );
  or_ii _139_ (
    .a(\apc32_1.apc16_2.half2.s ),
    .b(\apc32_1.apc16_1.half2.s ),
    .c(_038_)
  );
  and_ii _140_ (
    .a(\apc32_1.apc16_2.half2.s ),
    .b(\apc32_1.apc16_1.half2.s ),
    .c(_039_)
  );
  and_bi _141_ (
    .a(_038_),
    .b(_039_),
    .c(_040_)
  );
  or_bi _142_ (
    .a(_037_),
    .b(_040_),
    .c(_041_)
  );
  and_bi _143_ (
    .a(_037_),
    .b(_040_),
    .c(_042_)
  );
  and_bi _144_ (
    .a(_041_),
    .b(_042_),
    .c(\apc32_1.out [2])
  );
  maj_bii _145_ (
    .a(_037_),
    .b(\apc32_1.apc16_2.half2.s ),
    .c(\apc32_1.apc16_1.half2.s ),
    .d(_043_)
  );
  or_ii _146_ (
    .a(\apc32_1.apc16_2.half3.s ),
    .b(\apc32_1.apc16_1.half3.s ),
    .c(_044_)
  );
  and_ii _147_ (
    .a(\apc32_1.apc16_2.half3.s ),
    .b(\apc32_1.apc16_1.half3.s ),
    .c(_045_)
  );
  and_bi _148_ (
    .a(_044_),
    .b(_045_),
    .c(_046_)
  );
  or_bi _149_ (
    .a(_043_),
    .b(_046_),
    .c(_047_)
  );
  and_bi _150_ (
    .a(_043_),
    .b(_046_),
    .c(_048_)
  );
  and_bi _151_ (
    .a(_047_),
    .b(_048_),
    .c(\apc32_1.out [3])
  );
  maj_bii _152_ (
    .a(_043_),
    .b(\apc32_1.apc16_2.half3.s ),
    .c(\apc32_1.apc16_1.half3.s ),
    .d(_049_)
  );
  or_ii _153_ (
    .a(\apc32_1.apc16_2.half3.cout ),
    .b(\apc32_1.apc16_1.half3.cout ),
    .c(_050_)
  );
  and_ii _154_ (
    .a(\apc32_1.apc16_2.half3.cout ),
    .b(\apc32_1.apc16_1.half3.cout ),
    .c(_051_)
  );
  and_bi _155_ (
    .a(_050_),
    .b(_051_),
    .c(_052_)
  );
  or_bi _156_ (
    .a(_049_),
    .b(_052_),
    .c(_053_)
  );
  and_bi _157_ (
    .a(_049_),
    .b(_052_),
    .c(_054_)
  );
  and_bi _158_ (
    .a(_053_),
    .b(_054_),
    .c(\apc32_1.out [4])
  );
  and_ii _159_ (
    .a(1'b0),
    .b(1'b0),
    .c(_055_)
  );
  and_bi _160_ (
    .a(_031_),
    .b(_055_),
    .c(\apc32_1.out [0])
  );
  maj_bbi _161_ (
    .a(\apc32_1.apc16_2.half3.cout ),
    .b(\apc32_1.apc16_1.half3.cout ),
    .c(_049_),
    .d(\apc32_1.out [5])
  );
  or_bb _162_ (
    .a(in[49]),
    .b(in[48]),
    .c(\apc32_1.apc16_1.adder1_lv1.a )
  );
  and_bb _163_ (
    .a(in[51]),
    .b(in[50]),
    .c(\apc32_1.apc16_1.adder1_lv1.b )
  );
  or_bb _164_ (
    .a(in[53]),
    .b(in[52]),
    .c(\apc32_1.apc16_1.adder1_lv1.cin )
  );
  and_bb _165_ (
    .a(in[55]),
    .b(in[54]),
    .c(\apc32_1.apc16_1.adder2_lv1.a )
  );
  or_bb _166_ (
    .a(in[57]),
    .b(in[56]),
    .c(\apc32_1.apc16_1.adder2_lv1.b )
  );
  and_bb _167_ (
    .a(in[59]),
    .b(in[58]),
    .c(\apc32_1.apc16_1.adder2_lv1.cin )
  );
  or_bb _168_ (
    .a(in[61]),
    .b(in[60]),
    .c(\apc32_1.apc16_1.adder2_lv2.cin )
  );
  and_bb _169_ (
    .a(in[63]),
    .b(in[62]),
    .c(\apc32_1.apc16_1.half1.a )
  );
  maj_bbb _170_ (
    .a(\apc32_1.apc16_1.adder1_lv1.cin ),
    .b(\apc32_1.apc16_1.adder1_lv1.b ),
    .c(\apc32_1.apc16_1.adder1_lv1.a ),
    .d(\apc32_1.apc16_1.adder1_lv1.cout )
  );
  maj_bbi _171_ (
    .a(\apc32_1.apc16_1.adder1_lv1.b ),
    .b(\apc32_1.apc16_1.adder1_lv1.a ),
    .c(\apc32_1.apc16_1.adder1_lv1.cin ),
    .d(\apc32_1.apc16_1.adder1_lv1.d )
  );
  maj_bbi _172_ (
    .a(\apc32_1.apc16_1.adder1_lv1.d ),
    .b(\apc32_1.apc16_1.adder1_lv1.cin ),
    .c(\apc32_1.apc16_1.adder1_lv1.cout ),
    .d(\apc32_1.apc16_1.adder1_lv1.m3.d )
  );
  maj_bbb _173_ (
    .a(\apc32_1.apc16_1.adder1_lv2.cin ),
    .b(\apc32_1.apc16_1.adder1_lv2.b ),
    .c(\apc32_1.apc16_1.adder1_lv1.cout ),
    .d(\apc32_1.apc16_1.adder1_lv2.cout )
  );
  maj_bbi _174_ (
    .a(\apc32_1.apc16_1.adder1_lv2.b ),
    .b(\apc32_1.apc16_1.adder1_lv1.cout ),
    .c(\apc32_1.apc16_1.adder1_lv2.cin ),
    .d(\apc32_1.apc16_1.adder1_lv2.d )
  );
  maj_bbi _175_ (
    .a(\apc32_1.apc16_1.adder1_lv2.d ),
    .b(\apc32_1.apc16_1.adder1_lv2.cin ),
    .c(\apc32_1.apc16_1.adder1_lv2.cout ),
    .d(\apc32_1.apc16_1.adder1_lv2.m3.d )
  );
  maj_bbb _176_ (
    .a(\apc32_1.apc16_1.adder2_lv1.cin ),
    .b(\apc32_1.apc16_1.adder2_lv1.b ),
    .c(\apc32_1.apc16_1.adder2_lv1.a ),
    .d(\apc32_1.apc16_1.adder1_lv2.b )
  );
  maj_bbi _177_ (
    .a(\apc32_1.apc16_1.adder2_lv1.b ),
    .b(\apc32_1.apc16_1.adder2_lv1.a ),
    .c(\apc32_1.apc16_1.adder2_lv1.cin ),
    .d(\apc32_1.apc16_1.adder2_lv1.d )
  );
  maj_bbi _178_ (
    .a(\apc32_1.apc16_1.adder2_lv1.d ),
    .b(\apc32_1.apc16_1.adder2_lv1.cin ),
    .c(\apc32_1.apc16_1.adder1_lv2.b ),
    .d(\apc32_1.apc16_1.adder2_lv1.m3.d )
  );
  maj_bbb _179_ (
    .a(\apc32_1.apc16_1.adder2_lv2.cin ),
    .b(\apc32_1.apc16_1.adder2_lv1.m3.d ),
    .c(\apc32_1.apc16_1.adder1_lv1.m3.d ),
    .d(\apc32_1.apc16_1.adder1_lv2.cin )
  );
  maj_bbi _180_ (
    .a(\apc32_1.apc16_1.adder2_lv1.m3.d ),
    .b(\apc32_1.apc16_1.adder1_lv1.m3.d ),
    .c(\apc32_1.apc16_1.adder2_lv2.cin ),
    .d(\apc32_1.apc16_1.adder2_lv2.d )
  );
  maj_bbi _181_ (
    .a(\apc32_1.apc16_1.adder2_lv2.d ),
    .b(\apc32_1.apc16_1.adder2_lv2.cin ),
    .c(\apc32_1.apc16_1.adder1_lv2.cin ),
    .d(\apc32_1.apc16_1.adder2_lv2.m3.d )
  );
  and_bb _182_ (
    .a(\apc32_1.apc16_1.adder2_lv2.m3.d ),
    .b(\apc32_1.apc16_1.half1.a ),
    .c(\apc32_1.apc16_1.half1.cout )
  );
  or_bb _183_ (
    .a(\apc32_1.apc16_1.adder2_lv2.m3.d ),
    .b(\apc32_1.apc16_1.half1.a ),
    .c(_056_)
  );
  and_bi _184_ (
    .a(_056_),
    .b(\apc32_1.apc16_1.half1.cout ),
    .c(\apc32_1.apc16_1.half1.s )
  );
  and_bb _185_ (
    .a(\apc32_1.apc16_1.half1.cout ),
    .b(\apc32_1.apc16_1.adder1_lv2.m3.d ),
    .c(\apc32_1.apc16_1.half2.cout )
  );
  or_bb _186_ (
    .a(\apc32_1.apc16_1.half1.cout ),
    .b(\apc32_1.apc16_1.adder1_lv2.m3.d ),
    .c(_057_)
  );
  and_bi _187_ (
    .a(_057_),
    .b(\apc32_1.apc16_1.half2.cout ),
    .c(\apc32_1.apc16_1.half2.s )
  );
  and_bb _188_ (
    .a(\apc32_1.apc16_1.half2.cout ),
    .b(\apc32_1.apc16_1.adder1_lv2.cout ),
    .c(\apc32_1.apc16_1.half3.cout )
  );
  or_bb _189_ (
    .a(\apc32_1.apc16_1.half2.cout ),
    .b(\apc32_1.apc16_1.adder1_lv2.cout ),
    .c(_058_)
  );
  and_bi _190_ (
    .a(_058_),
    .b(\apc32_1.apc16_1.half3.cout ),
    .c(\apc32_1.apc16_1.half3.s )
  );
  or_bb _191_ (
    .a(in[33]),
    .b(in[32]),
    .c(\apc32_1.apc16_2.adder1_lv1.a )
  );
  and_bb _192_ (
    .a(in[35]),
    .b(in[34]),
    .c(\apc32_1.apc16_2.adder1_lv1.b )
  );
  or_bb _193_ (
    .a(in[37]),
    .b(in[36]),
    .c(\apc32_1.apc16_2.adder1_lv1.cin )
  );
  and_bb _194_ (
    .a(in[39]),
    .b(in[38]),
    .c(\apc32_1.apc16_2.adder2_lv1.a )
  );
  or_bb _195_ (
    .a(in[41]),
    .b(in[40]),
    .c(\apc32_1.apc16_2.adder2_lv1.b )
  );
  and_bb _196_ (
    .a(in[43]),
    .b(in[42]),
    .c(\apc32_1.apc16_2.adder2_lv1.cin )
  );
  or_bb _197_ (
    .a(in[45]),
    .b(in[44]),
    .c(\apc32_1.apc16_2.adder2_lv2.cin )
  );
  and_bb _198_ (
    .a(in[47]),
    .b(in[46]),
    .c(\apc32_1.apc16_2.half1.a )
  );
  maj_bbb _199_ (
    .a(\apc32_1.apc16_2.adder1_lv1.cin ),
    .b(\apc32_1.apc16_2.adder1_lv1.b ),
    .c(\apc32_1.apc16_2.adder1_lv1.a ),
    .d(\apc32_1.apc16_2.adder1_lv1.cout )
  );
  maj_bbi _200_ (
    .a(\apc32_1.apc16_2.adder1_lv1.b ),
    .b(\apc32_1.apc16_2.adder1_lv1.a ),
    .c(\apc32_1.apc16_2.adder1_lv1.cin ),
    .d(\apc32_1.apc16_2.adder1_lv1.d )
  );
  maj_bbi _201_ (
    .a(\apc32_1.apc16_2.adder1_lv1.d ),
    .b(\apc32_1.apc16_2.adder1_lv1.cin ),
    .c(\apc32_1.apc16_2.adder1_lv1.cout ),
    .d(\apc32_1.apc16_2.adder1_lv1.m3.d )
  );
  maj_bbb _202_ (
    .a(\apc32_1.apc16_2.adder1_lv2.cin ),
    .b(\apc32_1.apc16_2.adder1_lv2.b ),
    .c(\apc32_1.apc16_2.adder1_lv1.cout ),
    .d(\apc32_1.apc16_2.adder1_lv2.cout )
  );
  maj_bbi _203_ (
    .a(\apc32_1.apc16_2.adder1_lv2.b ),
    .b(\apc32_1.apc16_2.adder1_lv1.cout ),
    .c(\apc32_1.apc16_2.adder1_lv2.cin ),
    .d(\apc32_1.apc16_2.adder1_lv2.d )
  );
  maj_bbi _204_ (
    .a(\apc32_1.apc16_2.adder1_lv2.d ),
    .b(\apc32_1.apc16_2.adder1_lv2.cin ),
    .c(\apc32_1.apc16_2.adder1_lv2.cout ),
    .d(\apc32_1.apc16_2.adder1_lv2.m3.d )
  );
  maj_bbb _205_ (
    .a(\apc32_1.apc16_2.adder2_lv1.cin ),
    .b(\apc32_1.apc16_2.adder2_lv1.b ),
    .c(\apc32_1.apc16_2.adder2_lv1.a ),
    .d(\apc32_1.apc16_2.adder1_lv2.b )
  );
  maj_bbi _206_ (
    .a(\apc32_1.apc16_2.adder2_lv1.b ),
    .b(\apc32_1.apc16_2.adder2_lv1.a ),
    .c(\apc32_1.apc16_2.adder2_lv1.cin ),
    .d(\apc32_1.apc16_2.adder2_lv1.d )
  );
  maj_bbi _207_ (
    .a(\apc32_1.apc16_2.adder2_lv1.d ),
    .b(\apc32_1.apc16_2.adder2_lv1.cin ),
    .c(\apc32_1.apc16_2.adder1_lv2.b ),
    .d(\apc32_1.apc16_2.adder2_lv1.m3.d )
  );
  maj_bbb _208_ (
    .a(\apc32_1.apc16_2.adder2_lv2.cin ),
    .b(\apc32_1.apc16_2.adder2_lv1.m3.d ),
    .c(\apc32_1.apc16_2.adder1_lv1.m3.d ),
    .d(\apc32_1.apc16_2.adder1_lv2.cin )
  );
  maj_bbi _209_ (
    .a(\apc32_1.apc16_2.adder2_lv1.m3.d ),
    .b(\apc32_1.apc16_2.adder1_lv1.m3.d ),
    .c(\apc32_1.apc16_2.adder2_lv2.cin ),
    .d(\apc32_1.apc16_2.adder2_lv2.d )
  );
  maj_bbi _210_ (
    .a(\apc32_1.apc16_2.adder2_lv2.d ),
    .b(\apc32_1.apc16_2.adder2_lv2.cin ),
    .c(\apc32_1.apc16_2.adder1_lv2.cin ),
    .d(\apc32_1.apc16_2.adder2_lv2.m3.d )
  );
  and_bb _211_ (
    .a(\apc32_1.apc16_2.adder2_lv2.m3.d ),
    .b(\apc32_1.apc16_2.half1.a ),
    .c(\apc32_1.apc16_2.half1.cout )
  );
  or_bb _212_ (
    .a(\apc32_1.apc16_2.adder2_lv2.m3.d ),
    .b(\apc32_1.apc16_2.half1.a ),
    .c(_059_)
  );
  and_bi _213_ (
    .a(_059_),
    .b(\apc32_1.apc16_2.half1.cout ),
    .c(\apc32_1.apc16_2.half1.s )
  );
  and_bb _214_ (
    .a(\apc32_1.apc16_2.half1.cout ),
    .b(\apc32_1.apc16_2.adder1_lv2.m3.d ),
    .c(\apc32_1.apc16_2.half2.cout )
  );
  or_bb _215_ (
    .a(\apc32_1.apc16_2.half1.cout ),
    .b(\apc32_1.apc16_2.adder1_lv2.m3.d ),
    .c(_060_)
  );
  and_bi _216_ (
    .a(_060_),
    .b(\apc32_1.apc16_2.half2.cout ),
    .c(\apc32_1.apc16_2.half2.s )
  );
  and_bb _217_ (
    .a(\apc32_1.apc16_2.half2.cout ),
    .b(\apc32_1.apc16_2.adder1_lv2.cout ),
    .c(\apc32_1.apc16_2.half3.cout )
  );
  or_bb _218_ (
    .a(\apc32_1.apc16_2.half2.cout ),
    .b(\apc32_1.apc16_2.adder1_lv2.cout ),
    .c(_061_)
  );
  and_bi _219_ (
    .a(_061_),
    .b(\apc32_1.apc16_2.half3.cout ),
    .c(\apc32_1.apc16_2.half3.s )
  );
  or_ii _220_ (
    .a(1'b0),
    .b(1'b0),
    .c(_062_)
  );
  or_ii _221_ (
    .a(\apc32_2.apc16_2.half1.s ),
    .b(\apc32_2.apc16_1.half1.s ),
    .c(_063_)
  );
  and_ii _222_ (
    .a(\apc32_2.apc16_2.half1.s ),
    .b(\apc32_2.apc16_1.half1.s ),
    .c(_064_)
  );
  and_bi _223_ (
    .a(_063_),
    .b(_064_),
    .c(_065_)
  );
  or_bi _224_ (
    .a(_062_),
    .b(_065_),
    .c(_066_)
  );
  and_bi _225_ (
    .a(_062_),
    .b(_065_),
    .c(_067_)
  );
  and_bi _226_ (
    .a(_066_),
    .b(_067_),
    .c(\apc32_2.out [1])
  );
  maj_bii _227_ (
    .a(_062_),
    .b(\apc32_2.apc16_2.half1.s ),
    .c(\apc32_2.apc16_1.half1.s ),
    .d(_068_)
  );
  or_ii _228_ (
    .a(\apc32_2.apc16_2.half2.s ),
    .b(\apc32_2.apc16_1.half2.s ),
    .c(_069_)
  );
  and_ii _229_ (
    .a(\apc32_2.apc16_2.half2.s ),
    .b(\apc32_2.apc16_1.half2.s ),
    .c(_070_)
  );
  and_bi _230_ (
    .a(_069_),
    .b(_070_),
    .c(_071_)
  );
  or_bi _231_ (
    .a(_068_),
    .b(_071_),
    .c(_072_)
  );
  and_bi _232_ (
    .a(_068_),
    .b(_071_),
    .c(_073_)
  );
  and_bi _233_ (
    .a(_072_),
    .b(_073_),
    .c(\apc32_2.out [2])
  );
  maj_bii _234_ (
    .a(_068_),
    .b(\apc32_2.apc16_2.half2.s ),
    .c(\apc32_2.apc16_1.half2.s ),
    .d(_074_)
  );
  or_ii _235_ (
    .a(\apc32_2.apc16_2.half3.s ),
    .b(\apc32_2.apc16_1.half3.s ),
    .c(_075_)
  );
  and_ii _236_ (
    .a(\apc32_2.apc16_2.half3.s ),
    .b(\apc32_2.apc16_1.half3.s ),
    .c(_076_)
  );
  and_bi _237_ (
    .a(_075_),
    .b(_076_),
    .c(_077_)
  );
  or_bi _238_ (
    .a(_074_),
    .b(_077_),
    .c(_078_)
  );
  and_bi _239_ (
    .a(_074_),
    .b(_077_),
    .c(_079_)
  );
  and_bi _240_ (
    .a(_078_),
    .b(_079_),
    .c(\apc32_2.out [3])
  );
  maj_bii _241_ (
    .a(_074_),
    .b(\apc32_2.apc16_2.half3.s ),
    .c(\apc32_2.apc16_1.half3.s ),
    .d(_080_)
  );
  or_ii _242_ (
    .a(\apc32_2.apc16_2.half3.cout ),
    .b(\apc32_2.apc16_1.half3.cout ),
    .c(_081_)
  );
  and_ii _243_ (
    .a(\apc32_2.apc16_2.half3.cout ),
    .b(\apc32_2.apc16_1.half3.cout ),
    .c(_082_)
  );
  and_bi _244_ (
    .a(_081_),
    .b(_082_),
    .c(_083_)
  );
  or_bi _245_ (
    .a(_080_),
    .b(_083_),
    .c(_084_)
  );
  and_bi _246_ (
    .a(_080_),
    .b(_083_),
    .c(_085_)
  );
  and_bi _247_ (
    .a(_084_),
    .b(_085_),
    .c(\apc32_2.out [4])
  );
  and_ii _248_ (
    .a(1'b0),
    .b(1'b0),
    .c(_086_)
  );
  and_bi _249_ (
    .a(_062_),
    .b(_086_),
    .c(\apc32_2.out [0])
  );
  maj_bbi _250_ (
    .a(\apc32_2.apc16_2.half3.cout ),
    .b(\apc32_2.apc16_1.half3.cout ),
    .c(_080_),
    .d(\apc32_2.out [5])
  );
  or_bb _251_ (
    .a(in[17]),
    .b(in[16]),
    .c(\apc32_2.apc16_1.adder1_lv1.a )
  );
  and_bb _252_ (
    .a(in[19]),
    .b(in[18]),
    .c(\apc32_2.apc16_1.adder1_lv1.b )
  );
  or_bb _253_ (
    .a(in[21]),
    .b(in[20]),
    .c(\apc32_2.apc16_1.adder1_lv1.cin )
  );
  and_bb _254_ (
    .a(in[23]),
    .b(in[22]),
    .c(\apc32_2.apc16_1.adder2_lv1.a )
  );
  or_bb _255_ (
    .a(in[25]),
    .b(in[24]),
    .c(\apc32_2.apc16_1.adder2_lv1.b )
  );
  and_bb _256_ (
    .a(in[27]),
    .b(in[26]),
    .c(\apc32_2.apc16_1.adder2_lv1.cin )
  );
  or_bb _257_ (
    .a(in[29]),
    .b(in[28]),
    .c(\apc32_2.apc16_1.adder2_lv2.cin )
  );
  and_bb _258_ (
    .a(in[31]),
    .b(in[30]),
    .c(\apc32_2.apc16_1.half1.a )
  );
  maj_bbb _259_ (
    .a(\apc32_2.apc16_1.adder1_lv1.cin ),
    .b(\apc32_2.apc16_1.adder1_lv1.b ),
    .c(\apc32_2.apc16_1.adder1_lv1.a ),
    .d(\apc32_2.apc16_1.adder1_lv1.cout )
  );
  maj_bbi _260_ (
    .a(\apc32_2.apc16_1.adder1_lv1.b ),
    .b(\apc32_2.apc16_1.adder1_lv1.a ),
    .c(\apc32_2.apc16_1.adder1_lv1.cin ),
    .d(\apc32_2.apc16_1.adder1_lv1.d )
  );
  maj_bbi _261_ (
    .a(\apc32_2.apc16_1.adder1_lv1.d ),
    .b(\apc32_2.apc16_1.adder1_lv1.cin ),
    .c(\apc32_2.apc16_1.adder1_lv1.cout ),
    .d(\apc32_2.apc16_1.adder1_lv1.m3.d )
  );
  maj_bbb _262_ (
    .a(\apc32_2.apc16_1.adder1_lv2.cin ),
    .b(\apc32_2.apc16_1.adder1_lv2.b ),
    .c(\apc32_2.apc16_1.adder1_lv1.cout ),
    .d(\apc32_2.apc16_1.adder1_lv2.cout )
  );
  maj_bbi _263_ (
    .a(\apc32_2.apc16_1.adder1_lv2.b ),
    .b(\apc32_2.apc16_1.adder1_lv1.cout ),
    .c(\apc32_2.apc16_1.adder1_lv2.cin ),
    .d(\apc32_2.apc16_1.adder1_lv2.d )
  );
  maj_bbi _264_ (
    .a(\apc32_2.apc16_1.adder1_lv2.d ),
    .b(\apc32_2.apc16_1.adder1_lv2.cin ),
    .c(\apc32_2.apc16_1.adder1_lv2.cout ),
    .d(\apc32_2.apc16_1.adder1_lv2.m3.d )
  );
  maj_bbb _265_ (
    .a(\apc32_2.apc16_1.adder2_lv1.cin ),
    .b(\apc32_2.apc16_1.adder2_lv1.b ),
    .c(\apc32_2.apc16_1.adder2_lv1.a ),
    .d(\apc32_2.apc16_1.adder1_lv2.b )
  );
  maj_bbi _266_ (
    .a(\apc32_2.apc16_1.adder2_lv1.b ),
    .b(\apc32_2.apc16_1.adder2_lv1.a ),
    .c(\apc32_2.apc16_1.adder2_lv1.cin ),
    .d(\apc32_2.apc16_1.adder2_lv1.d )
  );
  maj_bbi _267_ (
    .a(\apc32_2.apc16_1.adder2_lv1.d ),
    .b(\apc32_2.apc16_1.adder2_lv1.cin ),
    .c(\apc32_2.apc16_1.adder1_lv2.b ),
    .d(\apc32_2.apc16_1.adder2_lv1.m3.d )
  );
  maj_bbb _268_ (
    .a(\apc32_2.apc16_1.adder2_lv2.cin ),
    .b(\apc32_2.apc16_1.adder2_lv1.m3.d ),
    .c(\apc32_2.apc16_1.adder1_lv1.m3.d ),
    .d(\apc32_2.apc16_1.adder1_lv2.cin )
  );
  maj_bbi _269_ (
    .a(\apc32_2.apc16_1.adder2_lv1.m3.d ),
    .b(\apc32_2.apc16_1.adder1_lv1.m3.d ),
    .c(\apc32_2.apc16_1.adder2_lv2.cin ),
    .d(\apc32_2.apc16_1.adder2_lv2.d )
  );
  maj_bbi _270_ (
    .a(\apc32_2.apc16_1.adder2_lv2.d ),
    .b(\apc32_2.apc16_1.adder2_lv2.cin ),
    .c(\apc32_2.apc16_1.adder1_lv2.cin ),
    .d(\apc32_2.apc16_1.adder2_lv2.m3.d )
  );
  and_bb _271_ (
    .a(\apc32_2.apc16_1.adder2_lv2.m3.d ),
    .b(\apc32_2.apc16_1.half1.a ),
    .c(\apc32_2.apc16_1.half1.cout )
  );
  or_bb _272_ (
    .a(\apc32_2.apc16_1.adder2_lv2.m3.d ),
    .b(\apc32_2.apc16_1.half1.a ),
    .c(_087_)
  );
  and_bi _273_ (
    .a(_087_),
    .b(\apc32_2.apc16_1.half1.cout ),
    .c(\apc32_2.apc16_1.half1.s )
  );
  and_bb _274_ (
    .a(\apc32_2.apc16_1.half1.cout ),
    .b(\apc32_2.apc16_1.adder1_lv2.m3.d ),
    .c(\apc32_2.apc16_1.half2.cout )
  );
  or_bb _275_ (
    .a(\apc32_2.apc16_1.half1.cout ),
    .b(\apc32_2.apc16_1.adder1_lv2.m3.d ),
    .c(_088_)
  );
  and_bi _276_ (
    .a(_088_),
    .b(\apc32_2.apc16_1.half2.cout ),
    .c(\apc32_2.apc16_1.half2.s )
  );
  and_bb _277_ (
    .a(\apc32_2.apc16_1.half2.cout ),
    .b(\apc32_2.apc16_1.adder1_lv2.cout ),
    .c(\apc32_2.apc16_1.half3.cout )
  );
  or_bb _278_ (
    .a(\apc32_2.apc16_1.half2.cout ),
    .b(\apc32_2.apc16_1.adder1_lv2.cout ),
    .c(_089_)
  );
  and_bi _279_ (
    .a(_089_),
    .b(\apc32_2.apc16_1.half3.cout ),
    .c(\apc32_2.apc16_1.half3.s )
  );
  or_bb _280_ (
    .a(in[1]),
    .b(in[0]),
    .c(\apc32_2.apc16_2.adder1_lv1.a )
  );
  and_bb _281_ (
    .a(in[3]),
    .b(in[2]),
    .c(\apc32_2.apc16_2.adder1_lv1.b )
  );
  or_bb _282_ (
    .a(in[5]),
    .b(in[4]),
    .c(\apc32_2.apc16_2.adder1_lv1.cin )
  );
  and_bb _283_ (
    .a(in[7]),
    .b(in[6]),
    .c(\apc32_2.apc16_2.adder2_lv1.a )
  );
  or_bb _284_ (
    .a(in[9]),
    .b(in[8]),
    .c(\apc32_2.apc16_2.adder2_lv1.b )
  );
  and_bb _285_ (
    .a(in[11]),
    .b(in[10]),
    .c(\apc32_2.apc16_2.adder2_lv1.cin )
  );
  or_bb _286_ (
    .a(in[13]),
    .b(in[12]),
    .c(\apc32_2.apc16_2.adder2_lv2.cin )
  );
  and_bb _287_ (
    .a(in[15]),
    .b(in[14]),
    .c(\apc32_2.apc16_2.half1.a )
  );
  maj_bbb _288_ (
    .a(\apc32_2.apc16_2.adder1_lv1.cin ),
    .b(\apc32_2.apc16_2.adder1_lv1.b ),
    .c(\apc32_2.apc16_2.adder1_lv1.a ),
    .d(\apc32_2.apc16_2.adder1_lv1.cout )
  );
  maj_bbi _289_ (
    .a(\apc32_2.apc16_2.adder1_lv1.b ),
    .b(\apc32_2.apc16_2.adder1_lv1.a ),
    .c(\apc32_2.apc16_2.adder1_lv1.cin ),
    .d(\apc32_2.apc16_2.adder1_lv1.d )
  );
  maj_bbi _290_ (
    .a(\apc32_2.apc16_2.adder1_lv1.d ),
    .b(\apc32_2.apc16_2.adder1_lv1.cin ),
    .c(\apc32_2.apc16_2.adder1_lv1.cout ),
    .d(\apc32_2.apc16_2.adder1_lv1.m3.d )
  );
  maj_bbb _291_ (
    .a(\apc32_2.apc16_2.adder1_lv2.cin ),
    .b(\apc32_2.apc16_2.adder1_lv2.b ),
    .c(\apc32_2.apc16_2.adder1_lv1.cout ),
    .d(\apc32_2.apc16_2.adder1_lv2.cout )
  );
  maj_bbi _292_ (
    .a(\apc32_2.apc16_2.adder1_lv2.b ),
    .b(\apc32_2.apc16_2.adder1_lv1.cout ),
    .c(\apc32_2.apc16_2.adder1_lv2.cin ),
    .d(\apc32_2.apc16_2.adder1_lv2.d )
  );
  maj_bbi _293_ (
    .a(\apc32_2.apc16_2.adder1_lv2.d ),
    .b(\apc32_2.apc16_2.adder1_lv2.cin ),
    .c(\apc32_2.apc16_2.adder1_lv2.cout ),
    .d(\apc32_2.apc16_2.adder1_lv2.m3.d )
  );
  maj_bbb _294_ (
    .a(\apc32_2.apc16_2.adder2_lv1.cin ),
    .b(\apc32_2.apc16_2.adder2_lv1.b ),
    .c(\apc32_2.apc16_2.adder2_lv1.a ),
    .d(\apc32_2.apc16_2.adder1_lv2.b )
  );
  maj_bbi _295_ (
    .a(\apc32_2.apc16_2.adder2_lv1.b ),
    .b(\apc32_2.apc16_2.adder2_lv1.a ),
    .c(\apc32_2.apc16_2.adder2_lv1.cin ),
    .d(\apc32_2.apc16_2.adder2_lv1.d )
  );
  maj_bbi _296_ (
    .a(\apc32_2.apc16_2.adder2_lv1.d ),
    .b(\apc32_2.apc16_2.adder2_lv1.cin ),
    .c(\apc32_2.apc16_2.adder1_lv2.b ),
    .d(\apc32_2.apc16_2.adder2_lv1.m3.d )
  );
  maj_bbb _297_ (
    .a(\apc32_2.apc16_2.adder2_lv2.cin ),
    .b(\apc32_2.apc16_2.adder2_lv1.m3.d ),
    .c(\apc32_2.apc16_2.adder1_lv1.m3.d ),
    .d(\apc32_2.apc16_2.adder1_lv2.cin )
  );
  maj_bbi _298_ (
    .a(\apc32_2.apc16_2.adder2_lv1.m3.d ),
    .b(\apc32_2.apc16_2.adder1_lv1.m3.d ),
    .c(\apc32_2.apc16_2.adder2_lv2.cin ),
    .d(\apc32_2.apc16_2.adder2_lv2.d )
  );
  maj_bbi _299_ (
    .a(\apc32_2.apc16_2.adder2_lv2.d ),
    .b(\apc32_2.apc16_2.adder2_lv2.cin ),
    .c(\apc32_2.apc16_2.adder1_lv2.cin ),
    .d(\apc32_2.apc16_2.adder2_lv2.m3.d )
  );
  and_bb _300_ (
    .a(\apc32_2.apc16_2.adder2_lv2.m3.d ),
    .b(\apc32_2.apc16_2.half1.a ),
    .c(\apc32_2.apc16_2.half1.cout )
  );
  or_bb _301_ (
    .a(\apc32_2.apc16_2.adder2_lv2.m3.d ),
    .b(\apc32_2.apc16_2.half1.a ),
    .c(_090_)
  );
  and_bi _302_ (
    .a(_090_),
    .b(\apc32_2.apc16_2.half1.cout ),
    .c(\apc32_2.apc16_2.half1.s )
  );
  and_bb _303_ (
    .a(\apc32_2.apc16_2.half1.cout ),
    .b(\apc32_2.apc16_2.adder1_lv2.m3.d ),
    .c(\apc32_2.apc16_2.half2.cout )
  );
  or_bb _304_ (
    .a(\apc32_2.apc16_2.half1.cout ),
    .b(\apc32_2.apc16_2.adder1_lv2.m3.d ),
    .c(_091_)
  );
  and_bi _305_ (
    .a(_091_),
    .b(\apc32_2.apc16_2.half2.cout ),
    .c(\apc32_2.apc16_2.half2.s )
  );
  and_bb _306_ (
    .a(\apc32_2.apc16_2.half2.cout ),
    .b(\apc32_2.apc16_2.adder1_lv2.cout ),
    .c(\apc32_2.apc16_2.half3.cout )
  );
  or_bb _307_ (
    .a(\apc32_2.apc16_2.half2.cout ),
    .b(\apc32_2.apc16_2.adder1_lv2.cout ),
    .c(_092_)
  );
  and_bi _308_ (
    .a(_092_),
    .b(\apc32_2.apc16_2.half3.cout ),
    .c(\apc32_2.apc16_2.half3.s )
  );
endmodule
