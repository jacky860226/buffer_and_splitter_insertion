module adder(a, b, c, cout, s);
  wire n_000_;
  wire n_001_;
  wire n_002_;
  wire n_003_;
  wire n_004_;
  wire n_005_;
  wire n_006_;
  wire n_007_;
  wire n_008_;
  wire n_009_;
  wire n_010_;
  wire n_011_;
  wire n_012_;
  wire n_013_;
  wire n_014_;
  wire n_015_;
  wire n_016_;
  wire n_017_;
  wire n_018_;
  wire n_019_;
  wire n_020_;
  wire n_021_;
  wire n_022_;
  wire n_023_;
  wire n_024_;
  wire n_025_;
  wire n_026_;
  wire n_027_;
  wire n_028_;
  wire n_029_;
  wire n_030_;
  wire n_031_;
  wire n_032_;
  wire n_033_;
  wire n_034_;
  wire n_035_;
  wire n_036_;
  wire n_037_;
  wire n_038_;
  wire n_039_;
  wire n_040_;
  wire n_041_;
  wire n_042_;
  wire n_043_;
  wire n_044_;
  wire n_045_;
  wire n_046_;
  wire n_047_;
  wire n_048_;
  wire n_049_;
  wire n_050_;
  wire n_051_;
  wire n_052_;
  wire n_053_;
  wire n_054_;
  wire n_055_;
  wire n_056_;
  wire n_057_;
  wire n_058_;
  wire n_059_;
  wire n_060_;
  wire n_061_;
  wire n_062_;
  wire n_063_;
  wire n_064_;
  wire n_065_;
  wire n_066_;
  wire n_067_;
  input a_0_;
  input a_1_;
  input a_2_;
  input a_3_;
  input a_4_;
  input a_5_;
  input a_6_;
  input a_7_;
  input b_0_;
  input b_1_;
  input b_2_;
  input b_3_;
  input b_4_;
  input b_5_;
  input b_6_;
  input b_7_;
  input c;
  output cout;
  output s_0_;
  output s_1_;
  output s_2_;
  output s_3_;
  output s_4_;
  output s_5_;
  output s_6_;
  output s_7_;
  and_bb n_068_ (
    .a(b_0_),
    .b(a_0_),
    .c(n_002_)
  );
  and_ii n_069_ (
    .a(b_0_),
    .b(a_0_),
    .c(n_003_)
  );
  or_bb n_070_ (
    .a(n_003_),
    .b(n_002_),
    .c(n_004_)
  );
  and_bi n_071_ (
    .a(c),
    .b(n_004_),
    .c(n_005_)
  );
  and_bi n_072_ (
    .a(n_004_),
    .b(c),
    .c(n_006_)
  );
  and_ii n_073_ (
    .a(n_006_),
    .b(n_005_),
    .c(s_0_)
  );
  or_ii n_074_ (
    .a(b_1_),
    .b(a_1_),
    .c(n_007_)
  );
  and_ii n_075_ (
    .a(b_1_),
    .b(a_1_),
    .c(n_008_)
  );
  and_bi n_076_ (
    .a(n_007_),
    .b(n_008_),
    .c(n_009_)
  );
  and_ii n_077_ (
    .a(n_005_),
    .b(n_002_),
    .c(n_010_)
  );
  or_bi n_078_ (
    .a(n_009_),
    .b(n_010_),
    .c(n_011_)
  );
  and_bi n_079_ (
    .a(n_009_),
    .b(n_010_),
    .c(n_012_)
  );
  and_bi n_080_ (
    .a(n_011_),
    .b(n_012_),
    .c(s_1_)
  );
  or_ii n_081_ (
    .a(n_009_),
    .b(n_005_),
    .c(n_013_)
  );
  or_ii n_082_ (
    .a(b_2_),
    .b(a_2_),
    .c(n_014_)
  );
  or_bb n_083_ (
    .a(b_2_),
    .b(a_2_),
    .c(n_015_)
  );
  or_ii n_084_ (
    .a(n_015_),
    .b(n_014_),
    .c(n_016_)
  );
  and_bi n_085_ (
    .a(n_002_),
    .b(n_008_),
    .c(n_017_)
  );
  and_bi n_086_ (
    .a(n_007_),
    .b(n_017_),
    .c(n_018_)
  );
  and_ii n_087_ (
    .a(n_018_),
    .b(n_016_),
    .c(n_019_)
  );
  and_bb n_088_ (
    .a(n_018_),
    .b(n_016_),
    .c(n_020_)
  );
  or_bb n_089_ (
    .a(n_020_),
    .b(n_019_),
    .c(n_021_)
  );
  or_bb n_090_ (
    .a(n_021_),
    .b(n_013_),
    .c(n_022_)
  );
  and_bb n_091_ (
    .a(n_021_),
    .b(n_013_),
    .c(n_023_)
  );
  and_bi n_092_ (
    .a(n_022_),
    .b(n_023_),
    .c(s_2_)
  );
  and_bi n_093_ (
    .a(n_014_),
    .b(n_019_),
    .c(n_024_)
  );
  and_bb n_094_ (
    .a(b_3_),
    .b(a_3_),
    .c(n_025_)
  );
  and_ii n_095_ (
    .a(b_3_),
    .b(a_3_),
    .c(n_026_)
  );
  or_bb n_096_ (
    .a(n_026_),
    .b(n_025_),
    .c(n_027_)
  );
  and_ii n_097_ (
    .a(n_027_),
    .b(n_024_),
    .c(n_028_)
  );
  and_bb n_098_ (
    .a(n_027_),
    .b(n_024_),
    .c(n_029_)
  );
  or_bb n_099_ (
    .a(n_029_),
    .b(n_028_),
    .c(n_030_)
  );
  or_bb n_100_ (
    .a(n_030_),
    .b(n_022_),
    .c(n_031_)
  );
  and_bb n_101_ (
    .a(n_030_),
    .b(n_022_),
    .c(n_032_)
  );
  and_bi n_102_ (
    .a(n_031_),
    .b(n_032_),
    .c(s_3_)
  );
  and_ii n_103_ (
    .a(n_028_),
    .b(n_025_),
    .c(n_033_)
  );
  and_bb n_104_ (
    .a(b_4_),
    .b(a_4_),
    .c(n_034_)
  );
  and_ii n_105_ (
    .a(b_4_),
    .b(a_4_),
    .c(n_035_)
  );
  or_bb n_106_ (
    .a(n_035_),
    .b(n_034_),
    .c(n_036_)
  );
  and_ii n_107_ (
    .a(n_036_),
    .b(n_033_),
    .c(n_037_)
  );
  and_bb n_108_ (
    .a(n_036_),
    .b(n_033_),
    .c(n_038_)
  );
  or_bb n_109_ (
    .a(n_038_),
    .b(n_037_),
    .c(n_039_)
  );
  or_bb n_110_ (
    .a(n_039_),
    .b(n_031_),
    .c(n_040_)
  );
  and_bb n_111_ (
    .a(n_039_),
    .b(n_031_),
    .c(n_041_)
  );
  and_bi n_112_ (
    .a(n_040_),
    .b(n_041_),
    .c(s_4_)
  );
  and_ii n_113_ (
    .a(n_037_),
    .b(n_034_),
    .c(n_042_)
  );
  and_bb n_114_ (
    .a(b_5_),
    .b(a_5_),
    .c(n_043_)
  );
  and_ii n_115_ (
    .a(b_5_),
    .b(a_5_),
    .c(n_044_)
  );
  or_bb n_116_ (
    .a(n_044_),
    .b(n_043_),
    .c(n_045_)
  );
  and_ii n_117_ (
    .a(n_045_),
    .b(n_042_),
    .c(n_046_)
  );
  and_bb n_118_ (
    .a(n_045_),
    .b(n_042_),
    .c(n_047_)
  );
  or_bb n_119_ (
    .a(n_047_),
    .b(n_046_),
    .c(n_048_)
  );
  or_bb n_120_ (
    .a(n_048_),
    .b(n_040_),
    .c(n_049_)
  );
  and_bb n_121_ (
    .a(n_048_),
    .b(n_040_),
    .c(n_050_)
  );
  and_bi n_122_ (
    .a(n_049_),
    .b(n_050_),
    .c(s_5_)
  );
  and_ii n_123_ (
    .a(n_046_),
    .b(n_043_),
    .c(n_051_)
  );
  and_bb n_124_ (
    .a(b_6_),
    .b(a_6_),
    .c(n_052_)
  );
  and_ii n_125_ (
    .a(b_6_),
    .b(a_6_),
    .c(n_053_)
  );
  or_bb n_126_ (
    .a(n_053_),
    .b(n_052_),
    .c(n_054_)
  );
  and_ii n_127_ (
    .a(n_054_),
    .b(n_051_),
    .c(n_055_)
  );
  and_bb n_128_ (
    .a(n_054_),
    .b(n_051_),
    .c(n_056_)
  );
  or_bb n_129_ (
    .a(n_056_),
    .b(n_055_),
    .c(n_057_)
  );
  or_bb n_130_ (
    .a(n_057_),
    .b(n_049_),
    .c(n_058_)
  );
  and_bb n_131_ (
    .a(n_057_),
    .b(n_049_),
    .c(n_059_)
  );
  and_bi n_132_ (
    .a(n_058_),
    .b(n_059_),
    .c(s_6_)
  );
  and_ii n_133_ (
    .a(n_055_),
    .b(n_052_),
    .c(n_060_)
  );
  and_bb n_134_ (
    .a(b_7_),
    .b(a_7_),
    .c(n_061_)
  );
  and_ii n_135_ (
    .a(b_7_),
    .b(a_7_),
    .c(n_062_)
  );
  or_bb n_136_ (
    .a(n_062_),
    .b(n_061_),
    .c(n_063_)
  );
  and_ii n_137_ (
    .a(n_063_),
    .b(n_060_),
    .c(n_064_)
  );
  and_bb n_138_ (
    .a(n_063_),
    .b(n_060_),
    .c(n_065_)
  );
  or_bb n_139_ (
    .a(n_065_),
    .b(n_064_),
    .c(n_066_)
  );
  and_ii n_140_ (
    .a(n_066_),
    .b(n_058_),
    .c(n_067_)
  );
  or_ii n_141_ (
    .a(n_066_),
    .b(n_058_),
    .c(n_000_)
  );
  and_bi n_142_ (
    .a(n_000_),
    .b(n_067_),
    .c(s_7_)
  );
  or_bb n_143_ (
    .a(n_064_),
    .b(n_061_),
    .c(n_001_)
  );
  or_bb n_144_ (
    .a(n_001_),
    .b(n_067_),
    .c(cout)
  );
endmodule
