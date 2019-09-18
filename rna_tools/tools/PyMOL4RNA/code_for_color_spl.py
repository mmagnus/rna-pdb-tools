
try:
    from pymol import cmd
except ImportError:
    print("PyMOL Python lib is missing")
    # sys.exit(0)

def spl_color():
 for name in cmd.get_names("all"):
  # cmd.do('color grey50') # off gray
  if name in ['5zwo', '5gm6', '5lj3', '5mps', '6exn', '5ylz', '5y88', '3jb9', '6icz', '6ff7', '5yzg', '5xjc']: # this should be auto
    print(" \ Extracting mode for %s" % name)
    if '5zwo' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5zwo")
        cmd.do("color skyblue, PRP8_B5zwo")
        #BRR2
        cmd.do("color grey60, chain D and 5zwo")
        cmd.do("color grey60, BRR2_B5zwo")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 5zwo")
        cmd.do("color dirtyviolet, BUD31_B5zwo")
        #CEF1
        cmd.do("color raspberry, chain nan and 5zwo")
        cmd.do("color raspberry, CEF1_B5zwo")
        #CLF1
        cmd.do("color raspberry, chain nan and 5zwo")
        cmd.do("color raspberry, CLF1_B5zwo")
        #CWC15
        cmd.do("color orange, chain nan and 5zwo")
        cmd.do("color orange, CWC15_B5zwo")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5zwo")
        cmd.do("color lightteal, CWC16/YJU2_B5zwo")
        #CWC2_hRBM22
        cmd.do("color ruby, chain nan and 5zwo")
        cmd.do("color ruby, CWC2_hRBM22_B5zwo")
        #CWC21
        cmd.do("color violetpurple, chain nan and 5zwo")
        cmd.do("color violetpurple, CWC21_B5zwo")
        #CWC22
        cmd.do("color bluewhite, chain nan and 5zwo")
        cmd.do("color bluewhite, CWC22_B5zwo")
        #CWC25
        cmd.do("color deepteal, chain nan and 5zwo")
        cmd.do("color deepteal, CWC25_B5zwo")
        #Intron_2
        cmd.do("color black, chain nan and 5zwo")
        cmd.do("color black, Intron_2_B5zwo")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5zwo")
        cmd.do("color dirtyviolet, ISY1_B5zwo")
        #LEA1
        cmd.do("color palegreen, chain o and 5zwo")
        cmd.do("color palegreen, LEA1_B5zwo")
        #Msl1
        cmd.do("color palegreen, chain p and 5zwo")
        cmd.do("color palegreen, Msl1_B5zwo")
        #PRP45
        cmd.do("color lightpink, chain nan and 5zwo")
        cmd.do("color lightpink, PRP45_B5zwo")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5zwo")
        cmd.do("color smudge, PRP16_hDHX38_B5zwo")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 5zwo")
        cmd.do("color dirtyviolet, CDC40_B5zwo")
        #PRP19
        cmd.do("color grey70, chain nan and 5zwo")
        cmd.do("color grey70, PRP19_B5zwo")
        #PRP46
        cmd.do("color lightblue, chain nan and 5zwo")
        cmd.do("color lightblue, PRP46_B5zwo")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 5zwo")
        cmd.do("color chocolate, SLT11/ECM2_B5zwo")
        #SNT309
        cmd.do("color grey70, chain nan and 5zwo")
        cmd.do("color grey70, SNT309_B5zwo")
        #SNU114
        cmd.do("color slate, chain C and 5zwo")
        cmd.do("color slate, SNU114_B5zwo")
        #SYF2
        cmd.do("color brightorange, chain nan and 5zwo")
        cmd.do("color brightorange, SYF2_B5zwo")
        #SYF1
        cmd.do("color brightorange, chain nan and 5zwo")
        cmd.do("color brightorange, SYF1_B5zwo")
        #U2
        cmd.do("color forest, chain H and 5zwo")
        cmd.do("color forest, U2_B5zwo")
        #U5
        cmd.do("color density, chain B and 5zwo")
        cmd.do("color density, U5_B5zwo")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5zwo")
        cmd.do("color deepblue, U5_SmRNP_B5zwo")
        #U6
        cmd.do("color firebrick, chain F and 5zwo")
        cmd.do("color firebrick, U6_B5zwo")
        #5EXON
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, 5EXON_B5zwo")
        #U4
        cmd.do("color brown, chain I and 5zwo")
        cmd.do("color brown, U4_B5zwo")
        #Intron
        cmd.do("color black, chain G and 5zwo")
        cmd.do("color black, Intron_B5zwo")
        #Exon
        cmd.do("color yellow, chain nan and 5zwo")
        cmd.do("color yellow, Exon_B5zwo")
        #exon-3
        cmd.do("color yellow, chain nan and 5zwo")
        cmd.do("color yellow, exon-3_B5zwo")
        #exon-5
        cmd.do("color yellow, chain nan and 5zwo")
        cmd.do("color yellow, exon-5_B5zwo")
        #PRP4
        cmd.do("color grey50, chain K and 5zwo")
        cmd.do("color grey50, PRP4_B5zwo")
        #PRP31
        cmd.do("color grey50, chain L and 5zwo")
        cmd.do("color grey50, PRP31_B5zwo")
        #PRP6
        cmd.do("color grey50, chain N and 5zwo")
        cmd.do("color grey50, PRP6_B5zwo")
        #PRP3
        cmd.do("color grey50, chain J and 5zwo")
        cmd.do("color grey50, PRP3_B5zwo")
        #DIB1
        cmd.do("color grey50, chain E and 5zwo")
        cmd.do("color grey50, DIB1_B5zwo")
        #SNU13
        cmd.do("color grey50, chain M and 5zwo")
        cmd.do("color grey50, SNU13_B5zwo")
        #LSM8
        cmd.do("color grey50, chain z and 5zwo")
        cmd.do("color grey50, LSM8_B5zwo")
        #LSM2
        cmd.do("color grey50, chain q and 5zwo")
        cmd.do("color grey50, LSM2_B5zwo")
        #LSM3
        cmd.do("color grey50, chain r and 5zwo")
        cmd.do("color grey50, LSM3_B5zwo")
        #LSM6
        cmd.do("color grey50, chain x and 5zwo")
        cmd.do("color grey50, LSM6_B5zwo")
        #LSM5
        cmd.do("color grey50, chain t and 5zwo")
        cmd.do("color grey50, LSM5_B5zwo")
        #LSM7
        cmd.do("color grey50, chain y and 5zwo")
        cmd.do("color grey50, LSM7_B5zwo")
        #LSM4
        cmd.do("color grey50, chain s and 5zwo")
        cmd.do("color grey50, LSM4_B5zwo")
        #SNU66
        cmd.do("color grey50, chain O and 5zwo")
        cmd.do("color grey50, SNU66_B5zwo")
        #RNA
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, RNA_B5zwo")
        #BUD13
        cmd.do("color grey60, chain Y and 5zwo")
        cmd.do("color grey60, BUD13_B5zwo")
        #CLF2
        cmd.do("color rasberry, chain nan and 5zwo")
        cmd.do("color rasberry, CLF2_B5zwo")
        #Cus1
        cmd.do("color palegreen, chain 2 and 5zwo")
        cmd.do("color palegreen, Cus1_B5zwo")
        #CWC24
        cmd.do("color grey60, chain nan and 5zwo")
        cmd.do("color grey60, CWC24_B5zwo")
        #CWC27
        cmd.do("color grey60, chain nan and 5zwo")
        cmd.do("color grey60, CWC27_B5zwo")
        #HSH155
        cmd.do("color smudge, chain 1 and 5zwo")
        cmd.do("color smudge, HSH155_B5zwo")
        #HSH49
        cmd.do("color sand, chain 4 and 5zwo")
        cmd.do("color sand, HSH49_B5zwo")
        #PML1
        cmd.do("color grey60, chain Z and 5zwo")
        cmd.do("color grey60, PML1_B5zwo")
        #PRP11
        cmd.do("color palegreen, chain v and 5zwo")
        cmd.do("color palegreen, PRP11_B5zwo")
        #PRP2
        cmd.do("color palegreen, chain nan and 5zwo")
        cmd.do("color palegreen, PRP2_B5zwo")
        #RDS3
        cmd.do("color palegreen, chain 5 and 5zwo")
        cmd.do("color palegreen, RDS3_B5zwo")
        #RSE1
        cmd.do("color smudge, chain 3 and 5zwo")
        cmd.do("color smudge, RSE1_B5zwo")
        #SNU17
        cmd.do("color grey60, chain X and 5zwo")
        cmd.do("color grey60, SNU17_B5zwo")
        #Ysf3
        cmd.do("color palegreen, chain 6 and 5zwo")
        cmd.do("color palegreen, Ysf3_B5zwo")
        #cwc23
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, cwc23_B5zwo")
        #SPP382
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, SPP382_B5zwo")
        #NTR2
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, NTR2_B5zwo")
        #PRP43
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, PRP43_B5zwo")
        cmd.do("color grey50, chain a and 5zwo")
        cmd.do("color grey50, chain P and 5zwo")
        cmd.do("color grey50, chain h and 5zwo")
        cmd.do("color grey50, chain e and 5zwo")
        cmd.do("color grey50, chain T and 5zwo")
        cmd.do("color grey50, chain i and 5zwo")
        cmd.do("color grey50, chain f and 5zwo")
        cmd.do("color grey50, chain U and 5zwo")
        cmd.do("color grey50, chain j and 5zwo")
        cmd.do("color grey50, chain g and 5zwo")
        cmd.do("color grey50, chain V and 5zwo")
        cmd.do("color grey50, chain k and 5zwo")
        cmd.do("color grey50, chain d and 5zwo")
        cmd.do("color grey50, chain S and 5zwo")
        cmd.do("color grey50, chain l and 5zwo")
        cmd.do("color grey50, chain b and 5zwo")
        cmd.do("color grey50, chain Q and 5zwo")
        cmd.do("color grey50, chain m and 5zwo")
        cmd.do("color grey50, chain c and 5zwo")
        cmd.do("color grey50, chain R and 5zwo")
        cmd.do("color grey50, chain n and 5zwo")
        #PRP22
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, PRP22_B5zwo")
        #PRP18
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, PRP18_B5zwo")
        #SLU7
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, SLU7_B5zwo")
        #SMF
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, SMF_B5zwo")
        #SMG
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, SMG_B5zwo")
        #PRP9
        cmd.do("color grey50, chain u and 5zwo")
        cmd.do("color grey50, PRP9_B5zwo")
        #PRP21
        cmd.do("color grey50, chain w and 5zwo")
        cmd.do("color grey50, PRP21_B5zwo")
        #SNU23
        cmd.do("color grey50, chain W and 5zwo")
        cmd.do("color grey50, SNU23_B5zwo")
        #PRP38
        cmd.do("color grey50, chain 0 and 5zwo")
        cmd.do("color grey50, PRP38_B5zwo")
        #SPP381
        cmd.do("color grey50, chain 9 and 5zwo")
        cmd.do("color grey50, SPP381_B5zwo")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, unknown_unassigned_B5zwo")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, Spp42_yPrp8_B5zwo")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5zwo")
        cmd.do("color orange, CWF15_yCWC15_B5zwo")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5zwo")
        cmd.do("color grey50, PRKRIP1_B5zwo")
    if '5gm6' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5gm6")
        cmd.do("color skyblue, PRP8_Ba5gm6")
        #BRR2
        cmd.do("color grey60, chain B and 5gm6")
        cmd.do("color grey60, BRR2_Ba5gm6")
        #BUD31
        cmd.do("color dirtyviolet, chain T and 5gm6")
        cmd.do("color dirtyviolet, BUD31_Ba5gm6")
        #CEF1
        cmd.do("color raspberry, chain c and 5gm6")
        cmd.do("color raspberry, CEF1_Ba5gm6")
        #CLF1
        cmd.do("color raspberry, chain nan and 5gm6")
        cmd.do("color raspberry, CLF1_Ba5gm6")
        #CWC15
        cmd.do("color orange, chain S and 5gm6")
        cmd.do("color orange, CWC15_Ba5gm6")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5gm6")
        cmd.do("color lightteal, CWC16/YJU2_Ba5gm6")
        #CWC2_hRBM22
        cmd.do("color ruby, chain R and 5gm6")
        cmd.do("color ruby, CWC2_hRBM22_Ba5gm6")
        #CWC21
        cmd.do("color violetpurple, chain X and 5gm6")
        cmd.do("color violetpurple, CWC21_Ba5gm6")
        #CWC22
        cmd.do("color bluewhite, chain Z and 5gm6")
        cmd.do("color bluewhite, CWC22_Ba5gm6")
        #CWC25
        cmd.do("color deepteal, chain nan and 5gm6")
        cmd.do("color deepteal, CWC25_Ba5gm6")
        #Intron_2
        cmd.do("color black, chain nan and 5gm6")
        cmd.do("color black, Intron_2_Ba5gm6")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5gm6")
        cmd.do("color dirtyviolet, ISY1_Ba5gm6")
        #LEA1
        cmd.do("color palegreen, chain nan and 5gm6")
        cmd.do("color palegreen, LEA1_Ba5gm6")
        #Msl1
        cmd.do("color palegreen, chain nan and 5gm6")
        cmd.do("color palegreen, Msl1_Ba5gm6")
        #PRP45
        cmd.do("color lightpink, chain P and 5gm6")
        cmd.do("color lightpink, PRP45_Ba5gm6")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5gm6")
        cmd.do("color smudge, PRP16_hDHX38_Ba5gm6")
        #CDC40
        cmd.do("color dirtyviolet, chain n and 5gm6")
        cmd.do("color dirtyviolet, CDC40_Ba5gm6")
        #PRP19
        cmd.do("color grey70, chain f and 5gm6")
        cmd.do("color grey70, PRP19_Ba5gm6")
        #PRP46
        cmd.do("color lightblue, chain O and 5gm6")
        cmd.do("color lightblue, PRP46_Ba5gm6")
        #SLT11/ECM2
        cmd.do("color chocolate, chain Q and 5gm6")
        cmd.do("color chocolate, SLT11/ECM2_Ba5gm6")
        #SNT309
        cmd.do("color grey70, chain t and 5gm6")
        cmd.do("color grey70, SNT309_Ba5gm6")
        #SNU114
        cmd.do("color slate, chain C and 5gm6")
        cmd.do("color slate, SNU114_Ba5gm6")
        #SYF2
        cmd.do("color brightorange, chain f and 5gm6")
        cmd.do("color brightorange, SYF2_Ba5gm6")
        #SYF1
        cmd.do("color brightorange, chain v and 5gm6")
        cmd.do("color brightorange, SYF1_Ba5gm6")
        #U2
        cmd.do("color forest, chain 2 and 5gm6")
        cmd.do("color forest, U2_Ba5gm6")
        #U5
        cmd.do("color density, chain 5 and 5gm6")
        cmd.do("color density, U5_Ba5gm6")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5gm6")
        cmd.do("color deepblue, U5_SmRNP_Ba5gm6")
        #U6
        cmd.do("color firebrick, chain 6 and 5gm6")
        cmd.do("color firebrick, U6_Ba5gm6")
        #5EXON
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, 5EXON_Ba5gm6")
        #U4
        cmd.do("color brown, chain nan and 5gm6")
        cmd.do("color brown, U4_Ba5gm6")
        #Intron
        cmd.do("color black, chain M and 5gm6")
        cmd.do("color black, Intron_Ba5gm6")
        #Exon
        cmd.do("color yellow, chain N and 5gm6")
        cmd.do("color yellow, Exon_Ba5gm6")
        #exon-3
        cmd.do("color yellow, chain nan and 5gm6")
        cmd.do("color yellow, exon-3_Ba5gm6")
        #exon-5
        cmd.do("color yellow, chain nan and 5gm6")
        cmd.do("color yellow, exon-5_Ba5gm6")
        #PRP4
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP4_Ba5gm6")
        #PRP31
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP31_Ba5gm6")
        #PRP6
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP6_Ba5gm6")
        #PRP3
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP3_Ba5gm6")
        #DIB1
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, DIB1_Ba5gm6")
        #SNU13
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SNU13_Ba5gm6")
        #LSM8
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM8_Ba5gm6")
        #LSM2
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM2_Ba5gm6")
        #LSM3
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM3_Ba5gm6")
        #LSM6
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM6_Ba5gm6")
        #LSM5
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM5_Ba5gm6")
        #LSM7
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM7_Ba5gm6")
        #LSM4
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, LSM4_Ba5gm6")
        #SNU66
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SNU66_Ba5gm6")
        #RNA
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, RNA_Ba5gm6")
        #BUD13
        cmd.do("color grey60, chain W and 5gm6")
        cmd.do("color grey60, BUD13_Ba5gm6")
        #CLF2
        cmd.do("color rasberry, chain d and 5gm6")
        cmd.do("color rasberry, CLF2_Ba5gm6")
        #Cus1
        cmd.do("color palegreen, chain H and 5gm6")
        cmd.do("color palegreen, Cus1_Ba5gm6")
        #CWC24
        cmd.do("color grey60, chain a and 5gm6")
        cmd.do("color grey60, CWC24_Ba5gm6")
        #CWC27
        cmd.do("color grey60, chain b and 5gm6")
        cmd.do("color grey60, CWC27_Ba5gm6")
        #HSH155
        cmd.do("color smudge, chain G and 5gm6")
        cmd.do("color smudge, HSH155_Ba5gm6")
        #HSH49
        cmd.do("color sand, chain e and 5gm6")
        cmd.do("color sand, HSH49_Ba5gm6")
        #PML1
        cmd.do("color grey60, chain U and 5gm6")
        cmd.do("color grey60, PML1_Ba5gm6")
        #PRP11
        cmd.do("color palegreen, chain I and 5gm6")
        cmd.do("color palegreen, PRP11_Ba5gm6")
        #PRP2
        cmd.do("color palegreen, chain Y and 5gm6")
        cmd.do("color palegreen, PRP2_Ba5gm6")
        #RDS3
        cmd.do("color palegreen, chain J and 5gm6")
        cmd.do("color palegreen, RDS3_Ba5gm6")
        #RSE1
        cmd.do("color smudge, chain F and 5gm6")
        cmd.do("color smudge, RSE1_Ba5gm6")
        #SNU17
        cmd.do("color grey60, chain V and 5gm6")
        cmd.do("color grey60, SNU17_Ba5gm6")
        #Ysf3
        cmd.do("color palegreen, chain K and 5gm6")
        cmd.do("color palegreen, Ysf3_Ba5gm6")
        #cwc23
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, cwc23_Ba5gm6")
        #SPP382
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SPP382_Ba5gm6")
        #NTR2
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, NTR2_Ba5gm6")
        #PRP43
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP43_Ba5gm6")
        #SMB1
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMB1_Ba5gm6")
        #SME1
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SME1_Ba5gm6")
        #SMX3
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMX3_Ba5gm6")
        #SMX2
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMX2_Ba5gm6")
        #SMD3
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMD3_Ba5gm6")
        #SMD1
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMD1_Ba5gm6")
        #SMD2
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMD2_Ba5gm6")
        #PRP22
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP22_Ba5gm6")
        #PRP18
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP18_Ba5gm6")
        #SLU7
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SLU7_Ba5gm6")
        #SMF
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMF_Ba5gm6")
        #SMG
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SMG_Ba5gm6")
        #PRP9
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP9_Ba5gm6")
        #PRP21
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP21_Ba5gm6")
        #SNU23
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SNU23_Ba5gm6")
        #PRP38
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRP38_Ba5gm6")
        #SPP381
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, SPP381_Ba5gm6")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, unknown_unassigned_Ba5gm6")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, Spp42_yPrp8_Ba5gm6")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5gm6")
        cmd.do("color orange, CWF15_yCWC15_Ba5gm6")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5gm6")
        cmd.do("color grey50, PRKRIP1_Ba5gm6")
    if '5lj3' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5lj3")
        cmd.do("color skyblue, PRP8_C5lj3")
        #BRR2
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, BRR2_C5lj3")
        #BUD31
        cmd.do("color dirtyviolet, chain L and 5lj3")
        cmd.do("color dirtyviolet, BUD31_C5lj3")
        #CEF1
        cmd.do("color raspberry, chain O and 5lj3")
        cmd.do("color raspberry, CEF1_C5lj3")
        #CLF1
        cmd.do("color raspberry, chain S and 5lj3")
        cmd.do("color raspberry, CLF1_C5lj3")
        #CWC15
        cmd.do("color orange, chain P and 5lj3")
        cmd.do("color orange, CWC15_C5lj3")
        #CWC16/YJU2
        cmd.do("color lightteal, chain D and 5lj3")
        cmd.do("color lightteal, CWC16/YJU2_C5lj3")
        #CWC2_hRBM22
        cmd.do("color ruby, chain M and 5lj3")
        cmd.do("color ruby, CWC2_hRBM22_C5lj3")
        #CWC21
        cmd.do("color violetpurple, chain R and 5lj3")
        cmd.do("color violetpurple, CWC21_C5lj3")
        #CWC22
        cmd.do("color bluewhite, chain H and 5lj3")
        cmd.do("color bluewhite, CWC22_C5lj3")
        #CWC25
        cmd.do("color deepteal, chain F and 5lj3")
        cmd.do("color deepteal, CWC25_C5lj3")
        #Intron_2
        cmd.do("color black, chain nan and 5lj3")
        cmd.do("color black, Intron_2_C5lj3")
        #ISY1
        cmd.do("color dirtyviolet, chain G and 5lj3")
        cmd.do("color dirtyviolet, ISY1_C5lj3")
        #LEA1
        cmd.do("color palegreen, chain W and 5lj3")
        cmd.do("color palegreen, LEA1_C5lj3")
        #Msl1
        cmd.do("color palegreen, chain Y and 5lj3")
        cmd.do("color palegreen, Msl1_C5lj3")
        #PRP45
        cmd.do("color lightpink, chain K and 5lj3")
        cmd.do("color lightpink, PRP45_C5lj3")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5lj3")
        cmd.do("color smudge, PRP16_hDHX38_C5lj3")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 5lj3")
        cmd.do("color dirtyviolet, CDC40_C5lj3")
        #PRP19
        cmd.do("color grey70, chain nan and 5lj3")
        cmd.do("color grey70, PRP19_C5lj3")
        #PRP46
        cmd.do("color lightblue, chain J and 5lj3")
        cmd.do("color lightblue, PRP46_C5lj3")
        #SLT11/ECM2
        cmd.do("color chocolate, chain N and 5lj3")
        cmd.do("color chocolate, SLT11/ECM2_C5lj3")
        #SNT309
        cmd.do("color grey70, chain nan and 5lj3")
        cmd.do("color grey70, SNT309_C5lj3")
        #SNU114
        cmd.do("color slate, chain C and 5lj3")
        cmd.do("color slate, SNU114_C5lj3")
        #SYF2
        cmd.do("color brightorange, chain nan and 5lj3")
        cmd.do("color brightorange, SYF2_C5lj3")
        #SYF1
        cmd.do("color brightorange, chain T and 5lj3")
        cmd.do("color brightorange, SYF1_C5lj3")
        #U2
        cmd.do("color forest, chain Z and 5lj3")
        cmd.do("color forest, U2_C5lj3")
        #U5
        cmd.do("color density, chain U and 5lj3")
        cmd.do("color density, U5_C5lj3")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5lj3")
        cmd.do("color deepblue, U5_SmRNP_C5lj3")
        #U6
        cmd.do("color firebrick, chain V and 5lj3")
        cmd.do("color firebrick, U6_C5lj3")
        #5EXON
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, 5EXON_C5lj3")
        #U4
        cmd.do("color brown, chain nan and 5lj3")
        cmd.do("color brown, U4_C5lj3")
        #Intron
        cmd.do("color black, chain I and 5lj3")
        cmd.do("color black, Intron_C5lj3")
        #Exon
        cmd.do("color yellow, chain E and 5lj3")
        cmd.do("color yellow, Exon_C5lj3")
        #exon-3
        cmd.do("color yellow, chain nan and 5lj3")
        cmd.do("color yellow, exon-3_C5lj3")
        #exon-5
        cmd.do("color yellow, chain nan and 5lj3")
        cmd.do("color yellow, exon-5_C5lj3")
        #PRP4
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP4_C5lj3")
        #PRP31
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP31_C5lj3")
        #PRP6
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP6_C5lj3")
        #PRP3
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP3_C5lj3")
        #DIB1
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, DIB1_C5lj3")
        #SNU13
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SNU13_C5lj3")
        #LSM8
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM8_C5lj3")
        #LSM2
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM2_C5lj3")
        #LSM3
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM3_C5lj3")
        #LSM6
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM6_C5lj3")
        #LSM5
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM5_C5lj3")
        #LSM7
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM7_C5lj3")
        #LSM4
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, LSM4_C5lj3")
        #SNU66
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SNU66_C5lj3")
        #RNA
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, RNA_C5lj3")
        #BUD13
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, BUD13_C5lj3")
        #CLF2
        cmd.do("color rasberry, chain nan and 5lj3")
        cmd.do("color rasberry, CLF2_C5lj3")
        #Cus1
        cmd.do("color palegreen, chain nan and 5lj3")
        cmd.do("color palegreen, Cus1_C5lj3")
        #CWC24
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, CWC24_C5lj3")
        #CWC27
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, CWC27_C5lj3")
        #HSH155
        cmd.do("color smudge, chain nan and 5lj3")
        cmd.do("color smudge, HSH155_C5lj3")
        #HSH49
        cmd.do("color sand, chain nan and 5lj3")
        cmd.do("color sand, HSH49_C5lj3")
        #PML1
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, PML1_C5lj3")
        #PRP11
        cmd.do("color palegreen, chain nan and 5lj3")
        cmd.do("color palegreen, PRP11_C5lj3")
        #PRP2
        cmd.do("color palegreen, chain nan and 5lj3")
        cmd.do("color palegreen, PRP2_C5lj3")
        #RDS3
        cmd.do("color palegreen, chain nan and 5lj3")
        cmd.do("color palegreen, RDS3_C5lj3")
        #RSE1
        cmd.do("color smudge, chain nan and 5lj3")
        cmd.do("color smudge, RSE1_C5lj3")
        #SNU17
        cmd.do("color grey60, chain nan and 5lj3")
        cmd.do("color grey60, SNU17_C5lj3")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5lj3")
        cmd.do("color palegreen, Ysf3_C5lj3")
        #cwc23
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, cwc23_C5lj3")
        #SPP382
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SPP382_C5lj3")
        #NTR2
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, NTR2_C5lj3")
        #PRP43
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP43_C5lj3")
        cmd.do("color grey50, chain b and 5lj3")
        cmd.do("color grey50, chain k and 5lj3")
        cmd.do("color grey50, chain e and 5lj3")
        cmd.do("color grey50, chain p and 5lj3")
        cmd.do("color grey50, chain f and 5lj3")
        cmd.do("color grey50, chain q and 5lj3")
        cmd.do("color grey50, chain g and 5lj3")
        cmd.do("color grey50, chain r and 5lj3")
        cmd.do("color grey50, chain d and 5lj3")
        cmd.do("color grey50, chain n and 5lj3")
        cmd.do("color grey50, chain h and 5lj3")
        cmd.do("color grey50, chain l and 5lj3")
        cmd.do("color grey50, chain j and 5lj3")
        cmd.do("color grey50, chain m and 5lj3")
        #PRP22
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP22_C5lj3")
        #PRP18
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP18_C5lj3")
        #SLU7
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SLU7_C5lj3")
        #SMF
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SMF_C5lj3")
        #SMG
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SMG_C5lj3")
        #PRP9
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP9_C5lj3")
        #PRP21
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP21_C5lj3")
        #SNU23
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SNU23_C5lj3")
        #PRP38
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRP38_C5lj3")
        #SPP381
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, SPP381_C5lj3")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, unknown_unassigned_C5lj3")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, Spp42_yPrp8_C5lj3")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5lj3")
        cmd.do("color orange, CWF15_yCWC15_C5lj3")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5lj3")
        cmd.do("color grey50, PRKRIP1_C5lj3")
    if '5mps' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5mps")
        cmd.do("color skyblue, PRP8_Cs5mps")
        #BRR2
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, BRR2_Cs5mps")
        #BUD31
        cmd.do("color dirtyviolet, chain L and 5mps")
        cmd.do("color dirtyviolet, BUD31_Cs5mps")
        #CEF1
        cmd.do("color raspberry, chain O and 5mps")
        cmd.do("color raspberry, CEF1_Cs5mps")
        #CLF1
        cmd.do("color raspberry, chain S and 5mps")
        cmd.do("color raspberry, CLF1_Cs5mps")
        #CWC15
        cmd.do("color orange, chain P and 5mps")
        cmd.do("color orange, CWC15_Cs5mps")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5mps")
        cmd.do("color lightteal, CWC16/YJU2_Cs5mps")
        #CWC2_hRBM22
        cmd.do("color ruby, chain M and 5mps")
        cmd.do("color ruby, CWC2_hRBM22_Cs5mps")
        #CWC21
        cmd.do("color violetpurple, chain R and 5mps")
        cmd.do("color violetpurple, CWC21_Cs5mps")
        #CWC22
        cmd.do("color bluewhite, chain H and 5mps")
        cmd.do("color bluewhite, CWC22_Cs5mps")
        #CWC25
        cmd.do("color deepteal, chain nan and 5mps")
        cmd.do("color deepteal, CWC25_Cs5mps")
        #Intron_2
        cmd.do("color black, chain nan and 5mps")
        cmd.do("color black, Intron_2_Cs5mps")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5mps")
        cmd.do("color dirtyviolet, ISY1_Cs5mps")
        #LEA1
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, LEA1_Cs5mps")
        #Msl1
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, Msl1_Cs5mps")
        #PRP45
        cmd.do("color lightpink, chain K and 5mps")
        cmd.do("color lightpink, PRP45_Cs5mps")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5mps")
        cmd.do("color smudge, PRP16_hDHX38_Cs5mps")
        #CDC40
        cmd.do("color dirtyviolet, chain o and 5mps")
        cmd.do("color dirtyviolet, CDC40_Cs5mps")
        #PRP19
        cmd.do("color grey70, chain nan and 5mps")
        cmd.do("color grey70, PRP19_Cs5mps")
        #PRP46
        cmd.do("color lightblue, chain J and 5mps")
        cmd.do("color lightblue, PRP46_Cs5mps")
        #SLT11/ECM2
        cmd.do("color chocolate, chain N and 5mps")
        cmd.do("color chocolate, SLT11/ECM2_Cs5mps")
        #SNT309
        cmd.do("color grey70, chain nan and 5mps")
        cmd.do("color grey70, SNT309_Cs5mps")
        #SNU114
        cmd.do("color slate, chain C and 5mps")
        cmd.do("color slate, SNU114_Cs5mps")
        #SYF2
        cmd.do("color brightorange, chain y and 5mps")
        cmd.do("color brightorange, SYF2_Cs5mps")
        #SYF1
        cmd.do("color brightorange, chain T and 5mps")
        cmd.do("color brightorange, SYF1_Cs5mps")
        #U2
        cmd.do("color forest, chain 2 and 5mps")
        cmd.do("color forest, U2_Cs5mps")
        #U5
        cmd.do("color density, chain 5 and 5mps")
        cmd.do("color density, U5_Cs5mps")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5mps")
        cmd.do("color deepblue, U5_SmRNP_Cs5mps")
        #U6
        cmd.do("color firebrick, chain 6 and 5mps")
        cmd.do("color firebrick, U6_Cs5mps")
        #5EXON
        cmd.do("color grey50, chain E and 5mps")
        cmd.do("color grey50, 5EXON_Cs5mps")
        #U4
        cmd.do("color brown, chain nan and 5mps")
        cmd.do("color brown, U4_Cs5mps")
        #Intron
        cmd.do("color black, chain I and 5mps")
        cmd.do("color black, Intron_Cs5mps")
        #Exon
        cmd.do("color yellow, chain E and 5mps")
        cmd.do("color yellow, Exon_Cs5mps")
        #exon-3
        cmd.do("color yellow, chain nan and 5mps")
        cmd.do("color yellow, exon-3_Cs5mps")
        #exon-5
        cmd.do("color yellow, chain nan and 5mps")
        cmd.do("color yellow, exon-5_Cs5mps")
        #PRP4
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP4_Cs5mps")
        #PRP31
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP31_Cs5mps")
        #PRP6
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP6_Cs5mps")
        #PRP3
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP3_Cs5mps")
        #DIB1
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, DIB1_Cs5mps")
        #SNU13
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SNU13_Cs5mps")
        #LSM8
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM8_Cs5mps")
        #LSM2
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM2_Cs5mps")
        #LSM3
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM3_Cs5mps")
        #LSM6
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM6_Cs5mps")
        #LSM5
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM5_Cs5mps")
        #LSM7
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM7_Cs5mps")
        #LSM4
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, LSM4_Cs5mps")
        #SNU66
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SNU66_Cs5mps")
        #RNA
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, RNA_Cs5mps")
        #BUD13
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, BUD13_Cs5mps")
        #CLF2
        cmd.do("color rasberry, chain nan and 5mps")
        cmd.do("color rasberry, CLF2_Cs5mps")
        #Cus1
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, Cus1_Cs5mps")
        #CWC24
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, CWC24_Cs5mps")
        #CWC27
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, CWC27_Cs5mps")
        #HSH155
        cmd.do("color smudge, chain nan and 5mps")
        cmd.do("color smudge, HSH155_Cs5mps")
        #HSH49
        cmd.do("color sand, chain nan and 5mps")
        cmd.do("color sand, HSH49_Cs5mps")
        #PML1
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, PML1_Cs5mps")
        #PRP11
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, PRP11_Cs5mps")
        #PRP2
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, PRP2_Cs5mps")
        #RDS3
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, RDS3_Cs5mps")
        #RSE1
        cmd.do("color smudge, chain nan and 5mps")
        cmd.do("color smudge, RSE1_Cs5mps")
        #SNU17
        cmd.do("color grey60, chain nan and 5mps")
        cmd.do("color grey60, SNU17_Cs5mps")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5mps")
        cmd.do("color palegreen, Ysf3_Cs5mps")
        #cwc23
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, cwc23_Cs5mps")
        #SPP382
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SPP382_Cs5mps")
        #NTR2
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, NTR2_Cs5mps")
        #PRP43
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP43_Cs5mps")
        #SMB1
        cmd.do("color grey50, chain b and 5mps")
        cmd.do("color grey50, SMB1_Cs5mps")
        #SME1
        cmd.do("color grey50, chain e and 5mps")
        cmd.do("color grey50, SME1_Cs5mps")
        #SMX3
        cmd.do("color grey50, chain f and 5mps")
        cmd.do("color grey50, SMX3_Cs5mps")
        #SMX2
        cmd.do("color grey50, chain g and 5mps")
        cmd.do("color grey50, SMX2_Cs5mps")
        #SMD3
        cmd.do("color grey50, chain d and 5mps")
        cmd.do("color grey50, SMD3_Cs5mps")
        #SMD1
        cmd.do("color grey50, chain h and 5mps")
        cmd.do("color grey50, SMD1_Cs5mps")
        #SMD2
        cmd.do("color grey50, chain j and 5mps")
        cmd.do("color grey50, SMD2_Cs5mps")
        #PRP22
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP22_Cs5mps")
        #PRP18
        cmd.do("color grey50, chain a and 5mps")
        cmd.do("color grey50, PRP18_Cs5mps")
        #SLU7
        cmd.do("color grey50, chain c and 5mps")
        cmd.do("color grey50, SLU7_Cs5mps")
        #SMF
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SMF_Cs5mps")
        #SMG
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SMG_Cs5mps")
        #PRP9
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP9_Cs5mps")
        #PRP21
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP21_Cs5mps")
        #SNU23
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SNU23_Cs5mps")
        #PRP38
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRP38_Cs5mps")
        #SPP381
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, SPP381_Cs5mps")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, unknown_unassigned_Cs5mps")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, Spp42_yPrp8_Cs5mps")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5mps")
        cmd.do("color orange, CWF15_yCWC15_Cs5mps")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5mps")
        cmd.do("color grey50, PRKRIP1_Cs5mps")
    if '6exn' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 6exn")
        cmd.do("color skyblue, PRP8_P6exn")
        #BRR2
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, BRR2_P6exn")
        #BUD31
        cmd.do("color dirtyviolet, chain L and 6exn")
        cmd.do("color dirtyviolet, BUD31_P6exn")
        #CEF1
        cmd.do("color raspberry, chain O and 6exn")
        cmd.do("color raspberry, CEF1_P6exn")
        #CLF1
        cmd.do("color raspberry, chain S and 6exn")
        cmd.do("color raspberry, CLF1_P6exn")
        #CWC15
        cmd.do("color orange, chain P and 6exn")
        cmd.do("color orange, CWC15_P6exn")
        #CWC16/YJU2
        cmd.do("color lightteal, chain D and 6exn")
        cmd.do("color lightteal, CWC16/YJU2_P6exn")
        #CWC2_hRBM22
        cmd.do("color ruby, chain M and 6exn")
        cmd.do("color ruby, CWC2_hRBM22_P6exn")
        #CWC21
        cmd.do("color violetpurple, chain R and 6exn")
        cmd.do("color violetpurple, CWC21_P6exn")
        #CWC22
        cmd.do("color bluewhite, chain H and 6exn")
        cmd.do("color bluewhite, CWC22_P6exn")
        #CWC25
        cmd.do("color deepteal, chain nan and 6exn")
        cmd.do("color deepteal, CWC25_P6exn")
        #Intron_2
        cmd.do("color black, chain nan and 6exn")
        cmd.do("color black, Intron_2_P6exn")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 6exn")
        cmd.do("color dirtyviolet, ISY1_P6exn")
        #LEA1
        cmd.do("color palegreen, chain W and 6exn")
        cmd.do("color palegreen, LEA1_P6exn")
        #Msl1
        cmd.do("color palegreen, chain Y and 6exn")
        cmd.do("color palegreen, Msl1_P6exn")
        #PRP45
        cmd.do("color lightpink, chain K and 6exn")
        cmd.do("color lightpink, PRP45_P6exn")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 6exn")
        cmd.do("color smudge, PRP16_hDHX38_P6exn")
        #CDC40
        cmd.do("color dirtyviolet, chain o and 6exn")
        cmd.do("color dirtyviolet, CDC40_P6exn")
        cmd.do("color grey70, chain t and 6exn")
        cmd.do("color grey70, chain u and 6exn")
        cmd.do("color grey70, chain v and 6exn")
        cmd.do("color grey70, chain w and 6exn")
        #PRP46
        cmd.do("color lightblue, chain J and 6exn")
        cmd.do("color lightblue, PRP46_P6exn")
        #SLT11/ECM2
        cmd.do("color chocolate, chain N and 6exn")
        cmd.do("color chocolate, SLT11/ECM2_P6exn")
        #SNT309
        cmd.do("color grey70, chain nan and 6exn")
        cmd.do("color grey70, SNT309_P6exn")
        #SNU114
        cmd.do("color slate, chain C and 6exn")
        cmd.do("color slate, SNU114_P6exn")
        #SYF2
        cmd.do("color brightorange, chain nan and 6exn")
        cmd.do("color brightorange, SYF2_P6exn")
        #SYF1
        cmd.do("color brightorange, chain T and 6exn")
        cmd.do("color brightorange, SYF1_P6exn")
        #U2
        cmd.do("color forest, chain 2 and 6exn")
        cmd.do("color forest, U2_P6exn")
        #U5
        cmd.do("color density, chain 5 and 6exn")
        cmd.do("color density, U5_P6exn")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 6exn")
        cmd.do("color deepblue, U5_SmRNP_P6exn")
        #U6
        cmd.do("color firebrick, chain 6 and 6exn")
        cmd.do("color firebrick, U6_P6exn")
        #5EXON
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, 5EXON_P6exn")
        #U4
        cmd.do("color brown, chain nan and 6exn")
        cmd.do("color brown, U4_P6exn")
        #Intron
        cmd.do("color black, chain I and 6exn")
        cmd.do("color black, Intron_P6exn")
        #Exon
        cmd.do("color yellow, chain E and 6exn")
        cmd.do("color yellow, Exon_P6exn")
        #exon-3
        cmd.do("color yellow, chain nan and 6exn")
        cmd.do("color yellow, exon-3_P6exn")
        #exon-5
        cmd.do("color yellow, chain nan and 6exn")
        cmd.do("color yellow, exon-5_P6exn")
        #PRP4
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP4_P6exn")
        #PRP31
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP31_P6exn")
        #PRP6
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP6_P6exn")
        #PRP3
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP3_P6exn")
        #DIB1
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, DIB1_P6exn")
        #SNU13
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SNU13_P6exn")
        #LSM8
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM8_P6exn")
        #LSM2
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM2_P6exn")
        #LSM3
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM3_P6exn")
        #LSM6
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM6_P6exn")
        #LSM5
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM5_P6exn")
        #LSM7
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM7_P6exn")
        #LSM4
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, LSM4_P6exn")
        #SNU66
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SNU66_P6exn")
        #RNA
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, RNA_P6exn")
        #BUD13
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, BUD13_P6exn")
        #CLF2
        cmd.do("color rasberry, chain nan and 6exn")
        cmd.do("color rasberry, CLF2_P6exn")
        #Cus1
        cmd.do("color palegreen, chain nan and 6exn")
        cmd.do("color palegreen, Cus1_P6exn")
        #CWC24
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, CWC24_P6exn")
        #CWC27
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, CWC27_P6exn")
        #HSH155
        cmd.do("color smudge, chain nan and 6exn")
        cmd.do("color smudge, HSH155_P6exn")
        #HSH49
        cmd.do("color sand, chain nan and 6exn")
        cmd.do("color sand, HSH49_P6exn")
        #PML1
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, PML1_P6exn")
        #PRP11
        cmd.do("color palegreen, chain nan and 6exn")
        cmd.do("color palegreen, PRP11_P6exn")
        #PRP2
        cmd.do("color palegreen, chain nan and 6exn")
        cmd.do("color palegreen, PRP2_P6exn")
        #RDS3
        cmd.do("color palegreen, chain nan and 6exn")
        cmd.do("color palegreen, RDS3_P6exn")
        #RSE1
        cmd.do("color smudge, chain nan and 6exn")
        cmd.do("color smudge, RSE1_P6exn")
        #SNU17
        cmd.do("color grey60, chain nan and 6exn")
        cmd.do("color grey60, SNU17_P6exn")
        #Ysf3
        cmd.do("color palegreen, chain nan and 6exn")
        cmd.do("color palegreen, Ysf3_P6exn")
        #cwc23
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, cwc23_P6exn")
        #SPP382
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SPP382_P6exn")
        #NTR2
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, NTR2_P6exn")
        #PRP43
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP43_P6exn")
        cmd.do("color grey50, chain b and 6exn")
        cmd.do("color grey50, chain k and 6exn")
        cmd.do("color grey50, chain e and 6exn")
        cmd.do("color grey50, chain p and 6exn")
        cmd.do("color grey50, chain f and 6exn")
        cmd.do("color grey50, chain q and 6exn")
        cmd.do("color grey50, chain g and 6exn")
        cmd.do("color grey50, chain r and 6exn")
        cmd.do("color grey50, chain d and 6exn")
        cmd.do("color grey50, chain n and 6exn")
        cmd.do("color grey50, chain h and 6exn")
        cmd.do("color grey50, chain l and 6exn")
        cmd.do("color grey50, chain j and 6exn")
        cmd.do("color grey50, chain m and 6exn")
        #PRP22
        cmd.do("color grey50, chain V and 6exn")
        cmd.do("color grey50, PRP22_P6exn")
        #PRP18
        cmd.do("color grey50, chain a and 6exn")
        cmd.do("color grey50, PRP18_P6exn")
        #SLU7
        cmd.do("color grey50, chain c and 6exn")
        cmd.do("color grey50, SLU7_P6exn")
        #SMF
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SMF_P6exn")
        #SMG
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SMG_P6exn")
        #PRP9
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP9_P6exn")
        #PRP21
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP21_P6exn")
        #SNU23
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SNU23_P6exn")
        #PRP38
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRP38_P6exn")
        #SPP381
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, SPP381_P6exn")
        #unknown_unassigned
        cmd.do("color grey50, chain X and 6exn")
        cmd.do("color grey50, unknown_unassigned_P6exn")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, Spp42_yPrp8_P6exn")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 6exn")
        cmd.do("color orange, CWF15_yCWC15_P6exn")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 6exn")
        cmd.do("color grey50, PRKRIP1_P6exn")
    if '5ylz' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5ylz")
        cmd.do("color skyblue, PRP8_P5ylz")
        #BRR2
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, BRR2_P5ylz")
        #BUD31
        cmd.do("color dirtyviolet, chain L and 5ylz")
        cmd.do("color dirtyviolet, BUD31_P5ylz")
        #CEF1
        cmd.do("color raspberry, chain J and 5ylz")
        cmd.do("color raspberry, CEF1_P5ylz")
        #CLF1
        cmd.do("color raspberry, chain I and 5ylz")
        cmd.do("color raspberry, CLF1_P5ylz")
        #CWC15
        cmd.do("color orange, chain P and 5ylz")
        cmd.do("color orange, CWC15_P5ylz")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5ylz")
        cmd.do("color lightteal, CWC16/YJU2_P5ylz")
        #CWC2_hRBM22
        cmd.do("color ruby, chain N and 5ylz")
        cmd.do("color ruby, CWC2_hRBM22_P5ylz")
        #CWC21
        cmd.do("color violetpurple, chain R and 5ylz")
        cmd.do("color violetpurple, CWC21_P5ylz")
        #CWC22
        cmd.do("color bluewhite, chain S and 5ylz")
        cmd.do("color bluewhite, CWC22_P5ylz")
        #CWC25
        cmd.do("color deepteal, chain nan and 5ylz")
        cmd.do("color deepteal, CWC25_P5ylz")
        #Intron_2
        cmd.do("color black, chain nan and 5ylz")
        cmd.do("color black, Intron_2_P5ylz")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5ylz")
        cmd.do("color dirtyviolet, ISY1_P5ylz")
        #LEA1
        cmd.do("color palegreen, chain o and 5ylz")
        cmd.do("color palegreen, LEA1_P5ylz")
        #Msl1
        cmd.do("color palegreen, chain p and 5ylz")
        cmd.do("color palegreen, Msl1_P5ylz")
        #PRP45
        cmd.do("color lightpink, chain Q and 5ylz")
        cmd.do("color lightpink, PRP45_P5ylz")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5ylz")
        cmd.do("color smudge, PRP16_hDHX38_P5ylz")
        #CDC40
        cmd.do("color dirtyviolet, chain T and 5ylz")
        cmd.do("color dirtyviolet, CDC40_P5ylz")
        cmd.do("color grey70, chain q and 5ylz")
        cmd.do("color grey70, chain r and 5ylz")
        cmd.do("color grey70, chain s and 5ylz")
        cmd.do("color grey70, chain t and 5ylz")
        #PRP46
        cmd.do("color lightblue, chain O and 5ylz")
        cmd.do("color lightblue, PRP46_P5ylz")
        #SLT11/ECM2
        cmd.do("color chocolate, chain M and 5ylz")
        cmd.do("color chocolate, SLT11/ECM2_P5ylz")
        #SNT309
        cmd.do("color grey70, chain G and 5ylz")
        cmd.do("color grey70, SNT309_P5ylz")
        #SNU114
        cmd.do("color slate, chain C and 5ylz")
        cmd.do("color slate, SNU114_P5ylz")
        #SYF2
        cmd.do("color brightorange, chain K and 5ylz")
        cmd.do("color brightorange, SYF2_P5ylz")
        #SYF1
        cmd.do("color brightorange, chain H and 5ylz")
        cmd.do("color brightorange, SYF1_P5ylz")
        #U2
        cmd.do("color forest, chain F and 5ylz")
        cmd.do("color forest, U2_P5ylz")
        #U5
        cmd.do("color density, chain B and 5ylz")
        cmd.do("color density, U5_P5ylz")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5ylz")
        cmd.do("color deepblue, U5_SmRNP_P5ylz")
        #U6
        cmd.do("color firebrick, chain D and 5ylz")
        cmd.do("color firebrick, U6_P5ylz")
        #5EXON
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, 5EXON_P5ylz")
        #U4
        cmd.do("color brown, chain nan and 5ylz")
        cmd.do("color brown, U4_P5ylz")
        #Intron
        cmd.do("color black, chain E and 5ylz")
        cmd.do("color black, Intron_P5ylz")
        #Exon
        cmd.do("color yellow, chain nan and 5ylz")
        cmd.do("color yellow, Exon_P5ylz")
        #exon-3
        cmd.do("color yellow, chain nan and 5ylz")
        cmd.do("color yellow, exon-3_P5ylz")
        #exon-5
        cmd.do("color yellow, chain nan and 5ylz")
        cmd.do("color yellow, exon-5_P5ylz")
        #PRP4
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP4_P5ylz")
        #PRP31
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP31_P5ylz")
        #PRP6
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP6_P5ylz")
        #PRP3
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP3_P5ylz")
        #DIB1
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, DIB1_P5ylz")
        #SNU13
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SNU13_P5ylz")
        #LSM8
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM8_P5ylz")
        #LSM2
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM2_P5ylz")
        #LSM3
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM3_P5ylz")
        #LSM6
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM6_P5ylz")
        #LSM5
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM5_P5ylz")
        #LSM7
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM7_P5ylz")
        #LSM4
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, LSM4_P5ylz")
        #SNU66
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SNU66_P5ylz")
        #RNA
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, RNA_P5ylz")
        #BUD13
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, BUD13_P5ylz")
        #CLF2
        cmd.do("color rasberry, chain nan and 5ylz")
        cmd.do("color rasberry, CLF2_P5ylz")
        #Cus1
        cmd.do("color palegreen, chain nan and 5ylz")
        cmd.do("color palegreen, Cus1_P5ylz")
        #CWC24
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, CWC24_P5ylz")
        #CWC27
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, CWC27_P5ylz")
        #HSH155
        cmd.do("color smudge, chain nan and 5ylz")
        cmd.do("color smudge, HSH155_P5ylz")
        #HSH49
        cmd.do("color sand, chain nan and 5ylz")
        cmd.do("color sand, HSH49_P5ylz")
        #PML1
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, PML1_P5ylz")
        #PRP11
        cmd.do("color palegreen, chain nan and 5ylz")
        cmd.do("color palegreen, PRP11_P5ylz")
        #PRP2
        cmd.do("color palegreen, chain nan and 5ylz")
        cmd.do("color palegreen, PRP2_P5ylz")
        #RDS3
        cmd.do("color palegreen, chain nan and 5ylz")
        cmd.do("color palegreen, RDS3_P5ylz")
        #RSE1
        cmd.do("color smudge, chain nan and 5ylz")
        cmd.do("color smudge, RSE1_P5ylz")
        #SNU17
        cmd.do("color grey60, chain nan and 5ylz")
        cmd.do("color grey60, SNU17_P5ylz")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5ylz")
        cmd.do("color palegreen, Ysf3_P5ylz")
        #cwc23
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, cwc23_P5ylz")
        #SPP382
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SPP382_P5ylz")
        #NTR2
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, NTR2_P5ylz")
        #PRP43
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP43_P5ylz")
        cmd.do("color grey50, chain a and 5ylz")
        cmd.do("color grey50, chain h and 5ylz")
        cmd.do("color grey50, chain b and 5ylz")
        cmd.do("color grey50, chain i and 5ylz")
        cmd.do("color grey50, chain c and 5ylz")
        cmd.do("color grey50, chain j and 5ylz")
        cmd.do("color grey50, chain d and 5ylz")
        cmd.do("color grey50, chain k and 5ylz")
        cmd.do("color grey50, chain e and 5ylz")
        cmd.do("color grey50, chain l and 5ylz")
        cmd.do("color grey50, chain f and 5ylz")
        cmd.do("color grey50, chain m and 5ylz")
        cmd.do("color grey50, chain g and 5ylz")
        cmd.do("color grey50, chain n and 5ylz")
        #PRP22
        cmd.do("color grey50, chain W and 5ylz")
        cmd.do("color grey50, PRP22_P5ylz")
        #PRP18
        cmd.do("color grey50, chain U and 5ylz")
        cmd.do("color grey50, PRP18_P5ylz")
        #SLU7
        cmd.do("color grey50, chain V and 5ylz")
        cmd.do("color grey50, SLU7_P5ylz")
        #SMF
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SMF_P5ylz")
        #SMG
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SMG_P5ylz")
        #PRP9
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP9_P5ylz")
        #PRP21
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP21_P5ylz")
        #SNU23
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SNU23_P5ylz")
        #PRP38
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRP38_P5ylz")
        #SPP381
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, SPP381_P5ylz")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, unknown_unassigned_P5ylz")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, Spp42_yPrp8_P5ylz")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5ylz")
        cmd.do("color orange, CWF15_yCWC15_P5ylz")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5ylz")
        cmd.do("color grey50, PRKRIP1_P5ylz")
    if '5y88' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain A and 5y88")
        cmd.do("color skyblue, PRP8_I5y88")
        #BRR2
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, BRR2_I5y88")
        #BUD31
        cmd.do("color dirtyviolet, chain L and 5y88")
        cmd.do("color dirtyviolet, BUD31_I5y88")
        #CEF1
        cmd.do("color raspberry, chain nan and 5y88")
        cmd.do("color raspberry, CEF1_I5y88")
        #CLF1
        cmd.do("color raspberry, chain I and 5y88")
        cmd.do("color raspberry, CLF1_I5y88")
        #CWC15
        cmd.do("color orange, chain P and 5y88")
        cmd.do("color orange, CWC15_I5y88")
        #CWC16/YJU2
        cmd.do("color lightteal, chain R and 5y88")
        cmd.do("color lightteal, CWC16/YJU2_I5y88")
        #CWC2_hRBM22
        cmd.do("color ruby, chain N and 5y88")
        cmd.do("color ruby, CWC2_hRBM22_I5y88")
        #CWC21
        cmd.do("color violetpurple, chain nan and 5y88")
        cmd.do("color violetpurple, CWC21_I5y88")
        #CWC22
        cmd.do("color bluewhite, chain nan and 5y88")
        cmd.do("color bluewhite, CWC22_I5y88")
        #CWC25
        cmd.do("color deepteal, chain G and 5y88")
        cmd.do("color deepteal, CWC25_I5y88")
        #Intron_2
        cmd.do("color black, chain E and 5y88")
        cmd.do("color black, Intron_2_I5y88")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5y88")
        cmd.do("color dirtyviolet, ISY1_I5y88")
        #LEA1
        cmd.do("color palegreen, chain o and 5y88")
        cmd.do("color palegreen, LEA1_I5y88")
        #Msl1
        cmd.do("color palegreen, chain p and 5y88")
        cmd.do("color palegreen, Msl1_I5y88")
        #PRP45
        cmd.do("color lightpink, chain Q and 5y88")
        cmd.do("color lightpink, PRP45_I5y88")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 5y88")
        cmd.do("color smudge, PRP16_hDHX38_I5y88")
        #CDC40
        cmd.do("color dirtyviolet, chain S and 5y88")
        cmd.do("color dirtyviolet, CDC40_I5y88")
        cmd.do("color grey70, chain q and 5y88")
        cmd.do("color grey70, chain r and 5y88")
        cmd.do("color grey70, chain s and 5y88")
        cmd.do("color grey70, chain t and 5y88")
        #PRP46
        cmd.do("color lightblue, chain O and 5y88")
        cmd.do("color lightblue, PRP46_I5y88")
        #SLT11/ECM2
        cmd.do("color chocolate, chain M and 5y88")
        cmd.do("color chocolate, SLT11/ECM2_I5y88")
        #SNT309
        cmd.do("color grey70, chain G and 5y88")
        cmd.do("color grey70, SNT309_I5y88")
        #SNU114
        cmd.do("color slate, chain C and 5y88")
        cmd.do("color slate, SNU114_I5y88")
        #SYF2
        cmd.do("color brightorange, chain K and 5y88")
        cmd.do("color brightorange, SYF2_I5y88")
        #SYF1
        cmd.do("color brightorange, chain H and 5y88")
        cmd.do("color brightorange, SYF1_I5y88")
        #U2
        cmd.do("color forest, chain F and 5y88")
        cmd.do("color forest, U2_I5y88")
        #U5
        cmd.do("color density, chain B and 5y88")
        cmd.do("color density, U5_I5y88")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5y88")
        cmd.do("color deepblue, U5_SmRNP_I5y88")
        #U6
        cmd.do("color firebrick, chain D and 5y88")
        cmd.do("color firebrick, U6_I5y88")
        #5EXON
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, 5EXON_I5y88")
        #U4
        cmd.do("color brown, chain nan and 5y88")
        cmd.do("color brown, U4_I5y88")
        #Intron
        cmd.do("color black, chain x and 5y88")
        cmd.do("color black, Intron_I5y88")
        #Exon
        cmd.do("color yellow, chain nan and 5y88")
        cmd.do("color yellow, Exon_I5y88")
        #exon-3
        cmd.do("color yellow, chain nan and 5y88")
        cmd.do("color yellow, exon-3_I5y88")
        #exon-5
        cmd.do("color yellow, chain nan and 5y88")
        cmd.do("color yellow, exon-5_I5y88")
        #PRP4
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP4_I5y88")
        #PRP31
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP31_I5y88")
        #PRP6
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP6_I5y88")
        #PRP3
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP3_I5y88")
        #DIB1
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, DIB1_I5y88")
        #SNU13
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SNU13_I5y88")
        #LSM8
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM8_I5y88")
        #LSM2
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM2_I5y88")
        #LSM3
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM3_I5y88")
        #LSM6
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM6_I5y88")
        #LSM5
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM5_I5y88")
        #LSM7
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM7_I5y88")
        #LSM4
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, LSM4_I5y88")
        #SNU66
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SNU66_I5y88")
        #RNA
        cmd.do("color grey50, chain x and 5y88")
        cmd.do("color grey50, RNA_I5y88")
        #BUD13
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, BUD13_I5y88")
        #CLF2
        cmd.do("color rasberry, chain nan and 5y88")
        cmd.do("color rasberry, CLF2_I5y88")
        #Cus1
        cmd.do("color palegreen, chain nan and 5y88")
        cmd.do("color palegreen, Cus1_I5y88")
        #CWC24
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, CWC24_I5y88")
        #CWC27
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, CWC27_I5y88")
        #HSH155
        cmd.do("color smudge, chain nan and 5y88")
        cmd.do("color smudge, HSH155_I5y88")
        #HSH49
        cmd.do("color sand, chain nan and 5y88")
        cmd.do("color sand, HSH49_I5y88")
        #PML1
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, PML1_I5y88")
        #PRP11
        cmd.do("color palegreen, chain nan and 5y88")
        cmd.do("color palegreen, PRP11_I5y88")
        #PRP2
        cmd.do("color palegreen, chain nan and 5y88")
        cmd.do("color palegreen, PRP2_I5y88")
        #RDS3
        cmd.do("color palegreen, chain nan and 5y88")
        cmd.do("color palegreen, RDS3_I5y88")
        #RSE1
        cmd.do("color smudge, chain nan and 5y88")
        cmd.do("color smudge, RSE1_I5y88")
        #SNU17
        cmd.do("color grey60, chain nan and 5y88")
        cmd.do("color grey60, SNU17_I5y88")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5y88")
        cmd.do("color palegreen, Ysf3_I5y88")
        #cwc23
        cmd.do("color grey50, chain T and 5y88")
        cmd.do("color grey50, cwc23_I5y88")
        #SPP382
        cmd.do("color grey50, chain U and 5y88")
        cmd.do("color grey50, SPP382_I5y88")
        #NTR2
        cmd.do("color grey50, chain V and 5y88")
        cmd.do("color grey50, NTR2_I5y88")
        #PRP43
        cmd.do("color grey50, chain W and 5y88")
        cmd.do("color grey50, PRP43_I5y88")
        cmd.do("color grey50, chain a and 5y88")
        cmd.do("color grey50, chain h and 5y88")
        cmd.do("color grey50, chain b and 5y88")
        cmd.do("color grey50, chain i and 5y88")
        cmd.do("color grey50, chain c and 5y88")
        cmd.do("color grey50, chain j and 5y88")
        cmd.do("color grey50, chain d and 5y88")
        cmd.do("color grey50, chain k and 5y88")
        cmd.do("color grey50, chain e and 5y88")
        cmd.do("color grey50, chain l and 5y88")
        cmd.do("color grey50, chain f and 5y88")
        cmd.do("color grey50, chain m and 5y88")
        cmd.do("color grey50, chain g and 5y88")
        cmd.do("color grey50, chain n and 5y88")
        #PRP22
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP22_I5y88")
        #PRP18
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP18_I5y88")
        #SLU7
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SLU7_I5y88")
        #SMF
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SMF_I5y88")
        #SMG
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SMG_I5y88")
        #PRP9
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP9_I5y88")
        #PRP21
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP21_I5y88")
        #SNU23
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SNU23_I5y88")
        #PRP38
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRP38_I5y88")
        #SPP381
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, SPP381_I5y88")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, unknown_unassigned_I5y88")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, Spp42_yPrp8_I5y88")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5y88")
        cmd.do("color orange, CWF15_yCWC15_I5y88")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5y88")
        cmd.do("color grey50, PRKRIP1_I5y88")
    if '3jb9' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain nan and 3jb9")
        cmd.do("color skyblue, PRP8_3jb9")
        #BRR2
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, BRR2_3jb9")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 3jb9")
        cmd.do("color dirtyviolet, BUD31_3jb9")
        #CEF1
        cmd.do("color raspberry, chain nan and 3jb9")
        cmd.do("color raspberry, CEF1_3jb9")
        #CLF1
        cmd.do("color raspberry, chain nan and 3jb9")
        cmd.do("color raspberry, CLF1_3jb9")
        #CWC15
        cmd.do("color orange, chain nan and 3jb9")
        cmd.do("color orange, CWC15_3jb9")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 3jb9")
        cmd.do("color lightteal, CWC16/YJU2_3jb9")
        #CWC2_hRBM22
        cmd.do("color ruby, chain nan and 3jb9")
        cmd.do("color ruby, CWC2_hRBM22_3jb9")
        #CWC21
        cmd.do("color violetpurple, chain nan and 3jb9")
        cmd.do("color violetpurple, CWC21_3jb9")
        #CWC22
        cmd.do("color bluewhite, chain nan and 3jb9")
        cmd.do("color bluewhite, CWC22_3jb9")
        #CWC25
        cmd.do("color deepteal, chain nan and 3jb9")
        cmd.do("color deepteal, CWC25_3jb9")
        #Intron_2
        cmd.do("color black, chain nan and 3jb9")
        cmd.do("color black, Intron_2_3jb9")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 3jb9")
        cmd.do("color dirtyviolet, ISY1_3jb9")
        #LEA1
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, LEA1_3jb9")
        #Msl1
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, Msl1_3jb9")
        #PRP45
        cmd.do("color lightpink, chain nan and 3jb9")
        cmd.do("color lightpink, PRP45_3jb9")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 3jb9")
        cmd.do("color smudge, PRP16_hDHX38_3jb9")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 3jb9")
        cmd.do("color dirtyviolet, CDC40_3jb9")
        #PRP19
        cmd.do("color grey70, chain nan and 3jb9")
        cmd.do("color grey70, PRP19_3jb9")
        #PRP46
        cmd.do("color lightblue, chain nan and 3jb9")
        cmd.do("color lightblue, PRP46_3jb9")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 3jb9")
        cmd.do("color chocolate, SLT11/ECM2_3jb9")
        #SNT309
        cmd.do("color grey70, chain nan and 3jb9")
        cmd.do("color grey70, SNT309_3jb9")
        #SNU114
        cmd.do("color slate, chain nan and 3jb9")
        cmd.do("color slate, SNU114_3jb9")
        #SYF2
        cmd.do("color brightorange, chain nan and 3jb9")
        cmd.do("color brightorange, SYF2_3jb9")
        #SYF1
        cmd.do("color brightorange, chain nan and 3jb9")
        cmd.do("color brightorange, SYF1_3jb9")
        #U2
        cmd.do("color forest, chain P and 3jb9")
        cmd.do("color forest, U2_3jb9")
        #U5
        cmd.do("color density, chain C and 3jb9")
        cmd.do("color density, U5_3jb9")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 3jb9")
        cmd.do("color deepblue, U5_SmRNP_3jb9")
        #U6
        cmd.do("color firebrick, chain N and 3jb9")
        cmd.do("color firebrick, U6_3jb9")
        #5EXON
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, 5EXON_3jb9")
        #U4
        cmd.do("color brown, chain nan and 3jb9")
        cmd.do("color brown, U4_3jb9")
        cmd.do("color black, chain O and 3jb9")
        cmd.do("color black, chain Q and 3jb9")
        #Exon
        cmd.do("color yellow, chain nan and 3jb9")
        cmd.do("color yellow, Exon_3jb9")
        #exon-3
        cmd.do("color yellow, chain nan and 3jb9")
        cmd.do("color yellow, exon-3_3jb9")
        #exon-5
        cmd.do("color yellow, chain nan and 3jb9")
        cmd.do("color yellow, exon-5_3jb9")
        #PRP4
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP4_3jb9")
        #PRP31
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP31_3jb9")
        #PRP6
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP6_3jb9")
        #PRP3
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP3_3jb9")
        #DIB1
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, DIB1_3jb9")
        #SNU13
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SNU13_3jb9")
        #LSM8
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM8_3jb9")
        #LSM2
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM2_3jb9")
        #LSM3
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM3_3jb9")
        #LSM6
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM6_3jb9")
        #LSM5
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM5_3jb9")
        #LSM7
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM7_3jb9")
        #LSM4
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, LSM4_3jb9")
        #SNU66
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SNU66_3jb9")
        #RNA
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, RNA_3jb9")
        #BUD13
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, BUD13_3jb9")
        #CLF2
        cmd.do("color rasberry, chain nan and 3jb9")
        cmd.do("color rasberry, CLF2_3jb9")
        #Cus1
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, Cus1_3jb9")
        #CWC24
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, CWC24_3jb9")
        #CWC27
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, CWC27_3jb9")
        #HSH155
        cmd.do("color smudge, chain nan and 3jb9")
        cmd.do("color smudge, HSH155_3jb9")
        #HSH49
        cmd.do("color sand, chain nan and 3jb9")
        cmd.do("color sand, HSH49_3jb9")
        #PML1
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, PML1_3jb9")
        #PRP11
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, PRP11_3jb9")
        #PRP2
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, PRP2_3jb9")
        #RDS3
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, RDS3_3jb9")
        #RSE1
        cmd.do("color smudge, chain nan and 3jb9")
        cmd.do("color smudge, RSE1_3jb9")
        #SNU17
        cmd.do("color grey60, chain nan and 3jb9")
        cmd.do("color grey60, SNU17_3jb9")
        #Ysf3
        cmd.do("color palegreen, chain nan and 3jb9")
        cmd.do("color palegreen, Ysf3_3jb9")
        #cwc23
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, cwc23_3jb9")
        #SPP382
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SPP382_3jb9")
        #NTR2
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, NTR2_3jb9")
        #PRP43
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP43_3jb9")
        #SMB1
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMB1_3jb9")
        #SME1
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SME1_3jb9")
        #SMX3
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMX3_3jb9")
        #SMX2
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMX2_3jb9")
        #SMD3
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMD3_3jb9")
        #SMD1
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMD1_3jb9")
        #SMD2
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMD2_3jb9")
        #PRP22
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP22_3jb9")
        #PRP18
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP18_3jb9")
        #SLU7
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SLU7_3jb9")
        #SMF
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMF_3jb9")
        #SMG
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SMG_3jb9")
        #PRP9
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP9_3jb9")
        #PRP21
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP21_3jb9")
        #SNU23
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SNU23_3jb9")
        #PRP38
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRP38_3jb9")
        #SPP381
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, SPP381_3jb9")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, unknown_unassigned_3jb9")
        #Spp42_yPrp8
        cmd.do("color grey50, chain A and 3jb9")
        cmd.do("color grey50, Spp42_yPrp8_3jb9")
        #CWF15_yCWC15
        cmd.do("color orange, chain h and 3jb9")
        cmd.do("color orange, CWF15_yCWC15_3jb9")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 3jb9")
        cmd.do("color grey50, PRKRIP1_3jb9")
    if '6icz' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain nan and 6icz")
        cmd.do("color skyblue, PRP8_hP_6icz")
        #BRR2
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, BRR2_hP_6icz")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 6icz")
        cmd.do("color dirtyviolet, BUD31_hP_6icz")
        #CEF1
        cmd.do("color raspberry, chain nan and 6icz")
        cmd.do("color raspberry, CEF1_hP_6icz")
        #CLF1
        cmd.do("color raspberry, chain nan and 6icz")
        cmd.do("color raspberry, CLF1_hP_6icz")
        #CWC15
        cmd.do("color orange, chain P and 6icz")
        cmd.do("color orange, CWC15_hP_6icz")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 6icz")
        cmd.do("color lightteal, CWC16/YJU2_hP_6icz")
        #CWC2_hRBM22
        cmd.do("color ruby, chain nan and 6icz")
        cmd.do("color ruby, CWC2_hRBM22_hP_6icz")
        #CWC21
        cmd.do("color violetpurple, chain nan and 6icz")
        cmd.do("color violetpurple, CWC21_hP_6icz")
        #CWC22
        cmd.do("color bluewhite, chain nan and 6icz")
        cmd.do("color bluewhite, CWC22_hP_6icz")
        #CWC25
        cmd.do("color deepteal, chain nan and 6icz")
        cmd.do("color deepteal, CWC25_hP_6icz")
        #Intron_2
        cmd.do("color black, chain nan and 6icz")
        cmd.do("color black, Intron_2_hP_6icz")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 6icz")
        cmd.do("color dirtyviolet, ISY1_hP_6icz")
        #LEA1
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, LEA1_hP_6icz")
        #Msl1
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, Msl1_hP_6icz")
        #PRP45
        cmd.do("color lightpink, chain nan and 6icz")
        cmd.do("color lightpink, PRP45_hP_6icz")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 6icz")
        cmd.do("color smudge, PRP16_hDHX38_hP_6icz")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 6icz")
        cmd.do("color dirtyviolet, CDC40_hP_6icz")
        #PRP19
        cmd.do("color grey70, chain nan and 6icz")
        cmd.do("color grey70, PRP19_hP_6icz")
        #PRP46
        cmd.do("color lightblue, chain nan and 6icz")
        cmd.do("color lightblue, PRP46_hP_6icz")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 6icz")
        cmd.do("color chocolate, SLT11/ECM2_hP_6icz")
        #SNT309
        cmd.do("color grey70, chain nan and 6icz")
        cmd.do("color grey70, SNT309_hP_6icz")
        #SNU114
        cmd.do("color slate, chain nan and 6icz")
        cmd.do("color slate, SNU114_hP_6icz")
        #SYF2
        cmd.do("color brightorange, chain nan and 6icz")
        cmd.do("color brightorange, SYF2_hP_6icz")
        #SYF1
        cmd.do("color brightorange, chain nan and 6icz")
        cmd.do("color brightorange, SYF1_hP_6icz")
        #U2
        cmd.do("color forest, chain H and 6icz")
        cmd.do("color forest, U2_hP_6icz")
        #U5
        cmd.do("color density, chain B and 6icz")
        cmd.do("color density, U5_hP_6icz")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 6icz")
        cmd.do("color deepblue, U5_SmRNP_hP_6icz")
        #U6
        cmd.do("color firebrick, chain F and 6icz")
        cmd.do("color firebrick, U6_hP_6icz")
        #5EXON
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, 5EXON_hP_6icz")
        #U4
        cmd.do("color brown, chain nan and 6icz")
        cmd.do("color brown, U4_hP_6icz")
        #Intron
        cmd.do("color black, chain G and 6icz")
        cmd.do("color black, Intron_hP_6icz")
        #Exon
        cmd.do("color yellow, chain nan and 6icz")
        cmd.do("color yellow, Exon_hP_6icz")
        #exon-3
        cmd.do("color yellow, chain nan and 6icz")
        cmd.do("color yellow, exon-3_hP_6icz")
        #exon-5
        cmd.do("color yellow, chain nan and 6icz")
        cmd.do("color yellow, exon-5_hP_6icz")
        #PRP4
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP4_hP_6icz")
        #PRP31
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP31_hP_6icz")
        #PRP6
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP6_hP_6icz")
        #PRP3
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP3_hP_6icz")
        #DIB1
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, DIB1_hP_6icz")
        #SNU13
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SNU13_hP_6icz")
        #LSM8
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM8_hP_6icz")
        #LSM2
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM2_hP_6icz")
        #LSM3
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM3_hP_6icz")
        #LSM6
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM6_hP_6icz")
        #LSM5
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM5_hP_6icz")
        #LSM7
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM7_hP_6icz")
        #LSM4
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, LSM4_hP_6icz")
        #SNU66
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SNU66_hP_6icz")
        #RNA
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, RNA_hP_6icz")
        #BUD13
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, BUD13_hP_6icz")
        #CLF2
        cmd.do("color rasberry, chain nan and 6icz")
        cmd.do("color rasberry, CLF2_hP_6icz")
        #Cus1
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, Cus1_hP_6icz")
        #CWC24
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, CWC24_hP_6icz")
        #CWC27
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, CWC27_hP_6icz")
        #HSH155
        cmd.do("color smudge, chain nan and 6icz")
        cmd.do("color smudge, HSH155_hP_6icz")
        #HSH49
        cmd.do("color sand, chain nan and 6icz")
        cmd.do("color sand, HSH49_hP_6icz")
        #PML1
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, PML1_hP_6icz")
        #PRP11
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, PRP11_hP_6icz")
        #PRP2
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, PRP2_hP_6icz")
        #RDS3
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, RDS3_hP_6icz")
        #RSE1
        cmd.do("color smudge, chain nan and 6icz")
        cmd.do("color smudge, RSE1_hP_6icz")
        #SNU17
        cmd.do("color grey60, chain nan and 6icz")
        cmd.do("color grey60, SNU17_hP_6icz")
        #Ysf3
        cmd.do("color palegreen, chain nan and 6icz")
        cmd.do("color palegreen, Ysf3_hP_6icz")
        #cwc23
        cmd.do("color grey50, chain 6ICZ and 6icz")
        cmd.do("color grey50, cwc23_hP_6icz")
        #SPP382
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SPP382_hP_6icz")
        #NTR2
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, NTR2_hP_6icz")
        #PRP43
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP43_hP_6icz")
        #SMB1
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMB1_hP_6icz")
        #SME1
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SME1_hP_6icz")
        #SMX3
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMX3_hP_6icz")
        #SMX2
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMX2_hP_6icz")
        #SMD3
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMD3_hP_6icz")
        #SMD1
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMD1_hP_6icz")
        #SMD2
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMD2_hP_6icz")
        #PRP22
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP22_hP_6icz")
        #PRP18
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP18_hP_6icz")
        #SLU7
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SLU7_hP_6icz")
        #SMF
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMF_hP_6icz")
        #SMG
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SMG_hP_6icz")
        #PRP9
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP9_hP_6icz")
        #PRP21
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP21_hP_6icz")
        #SNU23
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SNU23_hP_6icz")
        #PRP38
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRP38_hP_6icz")
        #SPP381
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, SPP381_hP_6icz")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, unknown_unassigned_hP_6icz")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, Spp42_yPrp8_hP_6icz")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 6icz")
        cmd.do("color orange, CWF15_yCWC15_hP_6icz")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 6icz")
        cmd.do("color grey50, PRKRIP1_hP_6icz")
    if '6ff7' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain nan and 6ff7")
        cmd.do("color skyblue, PRP8_hBa_6ff7")
        #BRR2
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, BRR2_hBa_6ff7")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 6ff7")
        cmd.do("color dirtyviolet, BUD31_hBa_6ff7")
        #CEF1
        cmd.do("color raspberry, chain nan and 6ff7")
        cmd.do("color raspberry, CEF1_hBa_6ff7")
        #CLF1
        cmd.do("color raspberry, chain nan and 6ff7")
        cmd.do("color raspberry, CLF1_hBa_6ff7")
        #CWC15
        cmd.do("color orange, chain R and 6ff7")
        cmd.do("color orange, CWC15_hBa_6ff7")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 6ff7")
        cmd.do("color lightteal, CWC16/YJU2_hBa_6ff7")
        #CWC2_hRBM22
        cmd.do("color ruby, chain P and 6ff7")
        cmd.do("color ruby, CWC2_hRBM22_hBa_6ff7")
        #CWC21
        cmd.do("color violetpurple, chain nan and 6ff7")
        cmd.do("color violetpurple, CWC21_hBa_6ff7")
        #CWC22
        cmd.do("color bluewhite, chain nan and 6ff7")
        cmd.do("color bluewhite, CWC22_hBa_6ff7")
        #CWC25
        cmd.do("color deepteal, chain nan and 6ff7")
        cmd.do("color deepteal, CWC25_hBa_6ff7")
        #Intron_2
        cmd.do("color black, chain nan and 6ff7")
        cmd.do("color black, Intron_2_hBa_6ff7")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 6ff7")
        cmd.do("color dirtyviolet, ISY1_hBa_6ff7")
        #LEA1
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, LEA1_hBa_6ff7")
        #Msl1
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, Msl1_hBa_6ff7")
        #PRP45
        cmd.do("color lightpink, chain nan and 6ff7")
        cmd.do("color lightpink, PRP45_hBa_6ff7")
        #PRP16_hDHX38
        cmd.do("color smudge, chain nan and 6ff7")
        cmd.do("color smudge, PRP16_hDHX38_hBa_6ff7")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 6ff7")
        cmd.do("color dirtyviolet, CDC40_hBa_6ff7")
        #PRP19
        cmd.do("color grey70, chain nan and 6ff7")
        cmd.do("color grey70, PRP19_hBa_6ff7")
        #PRP46
        cmd.do("color lightblue, chain nan and 6ff7")
        cmd.do("color lightblue, PRP46_hBa_6ff7")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 6ff7")
        cmd.do("color chocolate, SLT11/ECM2_hBa_6ff7")
        #SNT309
        cmd.do("color grey70, chain nan and 6ff7")
        cmd.do("color grey70, SNT309_hBa_6ff7")
        #SNU114
        cmd.do("color slate, chain nan and 6ff7")
        cmd.do("color slate, SNU114_hBa_6ff7")
        #SYF2
        cmd.do("color brightorange, chain nan and 6ff7")
        cmd.do("color brightorange, SYF2_hBa_6ff7")
        #SYF1
        cmd.do("color brightorange, chain nan and 6ff7")
        cmd.do("color brightorange, SYF1_hBa_6ff7")
        #U2
        cmd.do("color forest, chain 2 and 6ff7")
        cmd.do("color forest, U2_hBa_6ff7")
        #U5
        cmd.do("color density, chain 5 and 6ff7")
        cmd.do("color density, U5_hBa_6ff7")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 6ff7")
        cmd.do("color deepblue, U5_SmRNP_hBa_6ff7")
        #U6
        cmd.do("color firebrick, chain 6 and 6ff7")
        cmd.do("color firebrick, U6_hBa_6ff7")
        #5EXON
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, 5EXON_hBa_6ff7")
        #U4
        cmd.do("color brown, chain nan and 6ff7")
        cmd.do("color brown, U4_hBa_6ff7")
        #Intron
        cmd.do("color black, chain Z and 6ff7")
        cmd.do("color black, Intron_hBa_6ff7")
        #Exon
        cmd.do("color yellow, chain nan and 6ff7")
        cmd.do("color yellow, Exon_hBa_6ff7")
        #exon-3
        cmd.do("color yellow, chain nan and 6ff7")
        cmd.do("color yellow, exon-3_hBa_6ff7")
        #exon-5
        cmd.do("color yellow, chain nan and 6ff7")
        cmd.do("color yellow, exon-5_hBa_6ff7")
        #PRP4
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP4_hBa_6ff7")
        #PRP31
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP31_hBa_6ff7")
        #PRP6
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP6_hBa_6ff7")
        #PRP3
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP3_hBa_6ff7")
        #DIB1
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, DIB1_hBa_6ff7")
        #SNU13
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SNU13_hBa_6ff7")
        #LSM8
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM8_hBa_6ff7")
        #LSM2
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM2_hBa_6ff7")
        #LSM3
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM3_hBa_6ff7")
        #LSM6
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM6_hBa_6ff7")
        #LSM5
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM5_hBa_6ff7")
        #LSM7
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM7_hBa_6ff7")
        #LSM4
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, LSM4_hBa_6ff7")
        #SNU66
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SNU66_hBa_6ff7")
        #RNA
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, RNA_hBa_6ff7")
        #BUD13
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, BUD13_hBa_6ff7")
        #CLF2
        cmd.do("color rasberry, chain nan and 6ff7")
        cmd.do("color rasberry, CLF2_hBa_6ff7")
        #Cus1
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, Cus1_hBa_6ff7")
        #CWC24
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, CWC24_hBa_6ff7")
        #CWC27
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, CWC27_hBa_6ff7")
        #HSH155
        cmd.do("color smudge, chain nan and 6ff7")
        cmd.do("color smudge, HSH155_hBa_6ff7")
        #HSH49
        cmd.do("color sand, chain nan and 6ff7")
        cmd.do("color sand, HSH49_hBa_6ff7")
        #PML1
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, PML1_hBa_6ff7")
        #PRP11
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, PRP11_hBa_6ff7")
        #PRP2
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, PRP2_hBa_6ff7")
        #RDS3
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, RDS3_hBa_6ff7")
        #RSE1
        cmd.do("color smudge, chain nan and 6ff7")
        cmd.do("color smudge, RSE1_hBa_6ff7")
        #SNU17
        cmd.do("color grey60, chain nan and 6ff7")
        cmd.do("color grey60, SNU17_hBa_6ff7")
        #Ysf3
        cmd.do("color palegreen, chain nan and 6ff7")
        cmd.do("color palegreen, Ysf3_hBa_6ff7")
        #cwc23
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, cwc23_hBa_6ff7")
        #SPP382
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SPP382_hBa_6ff7")
        #NTR2
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, NTR2_hBa_6ff7")
        #PRP43
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP43_hBa_6ff7")
        #SMB1
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMB1_hBa_6ff7")
        #SME1
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SME1_hBa_6ff7")
        #SMX3
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMX3_hBa_6ff7")
        #SMX2
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMX2_hBa_6ff7")
        #SMD3
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMD3_hBa_6ff7")
        #SMD1
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMD1_hBa_6ff7")
        #SMD2
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMD2_hBa_6ff7")
        #PRP22
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP22_hBa_6ff7")
        #PRP18
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP18_hBa_6ff7")
        #SLU7
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SLU7_hBa_6ff7")
        #SMF
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMF_hBa_6ff7")
        #SMG
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SMG_hBa_6ff7")
        #PRP9
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP9_hBa_6ff7")
        #PRP21
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP21_hBa_6ff7")
        #SNU23
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SNU23_hBa_6ff7")
        #PRP38
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRP38_hBa_6ff7")
        #SPP381
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, SPP381_hBa_6ff7")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, unknown_unassigned_hBa_6ff7")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, Spp42_yPrp8_hBa_6ff7")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 6ff7")
        cmd.do("color orange, CWF15_yCWC15_hBa_6ff7")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 6ff7")
        cmd.do("color grey50, PRKRIP1_hBa_6ff7")
    if '5yzg' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain nan and 5yzg")
        cmd.do("color skyblue, PRP8_hC_5yzg")
        #BRR2
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, BRR2_hC_5yzg")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 5yzg")
        cmd.do("color dirtyviolet, BUD31_hC_5yzg")
        #CEF1
        cmd.do("color raspberry, chain nan and 5yzg")
        cmd.do("color raspberry, CEF1_hC_5yzg")
        #CLF1
        cmd.do("color raspberry, chain nan and 5yzg")
        cmd.do("color raspberry, CLF1_hC_5yzg")
        #CWC15
        cmd.do("color orange, chain P and 5yzg")
        cmd.do("color orange, CWC15_hC_5yzg")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5yzg")
        cmd.do("color lightteal, CWC16/YJU2_hC_5yzg")
        #CWC2_hRBM22
        cmd.do("color ruby, chain O and 5yzg")
        cmd.do("color ruby, CWC2_hRBM22_hC_5yzg")
        #CWC21
        cmd.do("color violetpurple, chain nan and 5yzg")
        cmd.do("color violetpurple, CWC21_hC_5yzg")
        #CWC22
        cmd.do("color bluewhite, chain nan and 5yzg")
        cmd.do("color bluewhite, CWC22_hC_5yzg")
        #CWC25
        cmd.do("color deepteal, chain X and 5yzg")
        cmd.do("color deepteal, CWC25_hC_5yzg")
        #Intron_2
        cmd.do("color black, chain nan and 5yzg")
        cmd.do("color black, Intron_2_hC_5yzg")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5yzg")
        cmd.do("color dirtyviolet, ISY1_hC_5yzg")
        #LEA1
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, LEA1_hC_5yzg")
        #Msl1
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, Msl1_hC_5yzg")
        #PRP45
        cmd.do("color lightpink, chain nan and 5yzg")
        cmd.do("color lightpink, PRP45_hC_5yzg")
        #PRP16_hDHX38
        cmd.do("color smudge, chain Z and 5yzg")
        cmd.do("color smudge, PRP16_hDHX38_hC_5yzg")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 5yzg")
        cmd.do("color dirtyviolet, CDC40_hC_5yzg")
        #PRP19
        cmd.do("color grey70, chain nan and 5yzg")
        cmd.do("color grey70, PRP19_hC_5yzg")
        #PRP46
        cmd.do("color lightblue, chain nan and 5yzg")
        cmd.do("color lightblue, PRP46_hC_5yzg")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 5yzg")
        cmd.do("color chocolate, SLT11/ECM2_hC_5yzg")
        #SNT309
        cmd.do("color grey70, chain nan and 5yzg")
        cmd.do("color grey70, SNT309_hC_5yzg")
        #SNU114
        cmd.do("color slate, chain nan and 5yzg")
        cmd.do("color slate, SNU114_hC_5yzg")
        #SYF2
        cmd.do("color brightorange, chain nan and 5yzg")
        cmd.do("color brightorange, SYF2_hC_5yzg")
        #SYF1
        cmd.do("color brightorange, chain nan and 5yzg")
        cmd.do("color brightorange, SYF1_hC_5yzg")
        #U2
        cmd.do("color forest, chain H and 5yzg")
        cmd.do("color forest, U2_hC_5yzg")
        #U5
        cmd.do("color density, chain B and 5yzg")
        cmd.do("color density, U5_hC_5yzg")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5yzg")
        cmd.do("color deepblue, U5_SmRNP_hC_5yzg")
        #U6
        cmd.do("color firebrick, chain F and 5yzg")
        cmd.do("color firebrick, U6_hC_5yzg")
        #5EXON
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, 5EXON_hC_5yzg")
        #U4
        cmd.do("color brown, chain nan and 5yzg")
        cmd.do("color brown, U4_hC_5yzg")
        #Intron
        cmd.do("color black, chain G and 5yzg")
        cmd.do("color black, Intron_hC_5yzg")
        #Exon
        cmd.do("color yellow, chain nan and 5yzg")
        cmd.do("color yellow, Exon_hC_5yzg")
        #exon-3
        cmd.do("color yellow, chain nan and 5yzg")
        cmd.do("color yellow, exon-3_hC_5yzg")
        #exon-5
        cmd.do("color yellow, chain nan and 5yzg")
        cmd.do("color yellow, exon-5_hC_5yzg")
        #PRP4
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP4_hC_5yzg")
        #PRP31
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP31_hC_5yzg")
        #PRP6
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP6_hC_5yzg")
        #PRP3
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP3_hC_5yzg")
        #DIB1
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, DIB1_hC_5yzg")
        #SNU13
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SNU13_hC_5yzg")
        #LSM8
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM8_hC_5yzg")
        #LSM2
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM2_hC_5yzg")
        #LSM3
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM3_hC_5yzg")
        #LSM6
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM6_hC_5yzg")
        #LSM5
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM5_hC_5yzg")
        #LSM7
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM7_hC_5yzg")
        #LSM4
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, LSM4_hC_5yzg")
        #SNU66
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SNU66_hC_5yzg")
        #RNA
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, RNA_hC_5yzg")
        #BUD13
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, BUD13_hC_5yzg")
        #CLF2
        cmd.do("color rasberry, chain nan and 5yzg")
        cmd.do("color rasberry, CLF2_hC_5yzg")
        #Cus1
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, Cus1_hC_5yzg")
        #CWC24
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, CWC24_hC_5yzg")
        #CWC27
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, CWC27_hC_5yzg")
        #HSH155
        cmd.do("color smudge, chain nan and 5yzg")
        cmd.do("color smudge, HSH155_hC_5yzg")
        #HSH49
        cmd.do("color sand, chain nan and 5yzg")
        cmd.do("color sand, HSH49_hC_5yzg")
        #PML1
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, PML1_hC_5yzg")
        #PRP11
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, PRP11_hC_5yzg")
        #PRP2
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, PRP2_hC_5yzg")
        #RDS3
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, RDS3_hC_5yzg")
        #RSE1
        cmd.do("color smudge, chain nan and 5yzg")
        cmd.do("color smudge, RSE1_hC_5yzg")
        #SNU17
        cmd.do("color grey60, chain nan and 5yzg")
        cmd.do("color grey60, SNU17_hC_5yzg")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5yzg")
        cmd.do("color palegreen, Ysf3_hC_5yzg")
        #cwc23
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, cwc23_hC_5yzg")
        #SPP382
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SPP382_hC_5yzg")
        #NTR2
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, NTR2_hC_5yzg")
        #PRP43
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP43_hC_5yzg")
        #SMB1
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMB1_hC_5yzg")
        #SME1
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SME1_hC_5yzg")
        #SMX3
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMX3_hC_5yzg")
        #SMX2
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMX2_hC_5yzg")
        #SMD3
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMD3_hC_5yzg")
        #SMD1
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMD1_hC_5yzg")
        #SMD2
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMD2_hC_5yzg")
        #PRP22
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP22_hC_5yzg")
        #PRP18
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP18_hC_5yzg")
        #SLU7
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SLU7_hC_5yzg")
        #SMF
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMF_hC_5yzg")
        #SMG
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SMG_hC_5yzg")
        #PRP9
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP9_hC_5yzg")
        #PRP21
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP21_hC_5yzg")
        #SNU23
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SNU23_hC_5yzg")
        #PRP38
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRP38_hC_5yzg")
        #SPP381
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, SPP381_hC_5yzg")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, unknown_unassigned_hC_5yzg")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, Spp42_yPrp8_hC_5yzg")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5yzg")
        cmd.do("color orange, CWF15_yCWC15_hC_5yzg")
        #PRKRIP1
        cmd.do("color grey50, chain nan and 5yzg")
        cmd.do("color grey50, PRKRIP1_hC_5yzg")
    if '5xjc' in name.lower():
        #PRP8
        cmd.do("color skyblue, chain nan and 5xjc")
        cmd.do("color skyblue, PRP8_hX_5xjc")
        #BRR2
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, BRR2_hX_5xjc")
        #BUD31
        cmd.do("color dirtyviolet, chain nan and 5xjc")
        cmd.do("color dirtyviolet, BUD31_hX_5xjc")
        #CEF1
        cmd.do("color raspberry, chain nan and 5xjc")
        cmd.do("color raspberry, CEF1_hX_5xjc")
        #CLF1
        cmd.do("color raspberry, chain nan and 5xjc")
        cmd.do("color raspberry, CLF1_hX_5xjc")
        #CWC15
        cmd.do("color orange, chain P and 5xjc")
        cmd.do("color orange, CWC15_hX_5xjc")
        #CWC16/YJU2
        cmd.do("color lightteal, chain nan and 5xjc")
        cmd.do("color lightteal, CWC16/YJU2_hX_5xjc")
        #CWC2_hRBM22
        cmd.do("color ruby, chain nan and 5xjc")
        cmd.do("color ruby, CWC2_hRBM22_hX_5xjc")
        #CWC21
        cmd.do("color violetpurple, chain nan and 5xjc")
        cmd.do("color violetpurple, CWC21_hX_5xjc")
        #CWC22
        cmd.do("color bluewhite, chain nan and 5xjc")
        cmd.do("color bluewhite, CWC22_hX_5xjc")
        #CWC25
        cmd.do("color deepteal, chain X and 5xjc")
        cmd.do("color deepteal, CWC25_hX_5xjc")
        #Intron_2
        cmd.do("color black, chain nan and 5xjc")
        cmd.do("color black, Intron_2_hX_5xjc")
        #ISY1
        cmd.do("color dirtyviolet, chain nan and 5xjc")
        cmd.do("color dirtyviolet, ISY1_hX_5xjc")
        #LEA1
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, LEA1_hX_5xjc")
        #Msl1
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, Msl1_hX_5xjc")
        #PRP45
        cmd.do("color lightpink, chain nan and 5xjc")
        cmd.do("color lightpink, PRP45_hX_5xjc")
        #PRP16_hDHX38
        cmd.do("color smudge, chain - and 5xjc")
        cmd.do("color smudge, PRP16_hDHX38_hX_5xjc")
        #CDC40
        cmd.do("color dirtyviolet, chain nan and 5xjc")
        cmd.do("color dirtyviolet, CDC40_hX_5xjc")
        #PRP19
        cmd.do("color grey70, chain nan and 5xjc")
        cmd.do("color grey70, PRP19_hX_5xjc")
        #PRP46
        cmd.do("color lightblue, chain nan and 5xjc")
        cmd.do("color lightblue, PRP46_hX_5xjc")
        #SLT11/ECM2
        cmd.do("color chocolate, chain nan and 5xjc")
        cmd.do("color chocolate, SLT11/ECM2_hX_5xjc")
        #SNT309
        cmd.do("color grey70, chain nan and 5xjc")
        cmd.do("color grey70, SNT309_hX_5xjc")
        #SNU114
        cmd.do("color slate, chain nan and 5xjc")
        cmd.do("color slate, SNU114_hX_5xjc")
        #SYF2
        cmd.do("color brightorange, chain nan and 5xjc")
        cmd.do("color brightorange, SYF2_hX_5xjc")
        #SYF1
        cmd.do("color brightorange, chain nan and 5xjc")
        cmd.do("color brightorange, SYF1_hX_5xjc")
        #U2
        cmd.do("color forest, chain H and 5xjc")
        cmd.do("color forest, U2_hX_5xjc")
        #U5
        cmd.do("color density, chain B and 5xjc")
        cmd.do("color density, U5_hX_5xjc")
        #U5_SmRNP
        cmd.do("color deepblue, chain nan and 5xjc")
        cmd.do("color deepblue, U5_SmRNP_hX_5xjc")
        #U6
        cmd.do("color firebrick, chain F and 5xjc")
        cmd.do("color firebrick, U6_hX_5xjc")
        #5EXON
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, 5EXON_hX_5xjc")
        #U4
        cmd.do("color brown, chain nan and 5xjc")
        cmd.do("color brown, U4_hX_5xjc")
        #Intron
        cmd.do("color black, chain G and 5xjc")
        cmd.do("color black, Intron_hX_5xjc")
        #Exon
        cmd.do("color yellow, chain nan and 5xjc")
        cmd.do("color yellow, Exon_hX_5xjc")
        #exon-3
        cmd.do("color yellow, chain nan and 5xjc")
        cmd.do("color yellow, exon-3_hX_5xjc")
        #exon-5
        cmd.do("color yellow, chain nan and 5xjc")
        cmd.do("color yellow, exon-5_hX_5xjc")
        #PRP4
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP4_hX_5xjc")
        #PRP31
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP31_hX_5xjc")
        #PRP6
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP6_hX_5xjc")
        #PRP3
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP3_hX_5xjc")
        #DIB1
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, DIB1_hX_5xjc")
        #SNU13
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SNU13_hX_5xjc")
        #LSM8
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM8_hX_5xjc")
        #LSM2
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM2_hX_5xjc")
        #LSM3
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM3_hX_5xjc")
        #LSM6
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM6_hX_5xjc")
        #LSM5
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM5_hX_5xjc")
        #LSM7
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM7_hX_5xjc")
        #LSM4
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, LSM4_hX_5xjc")
        #SNU66
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SNU66_hX_5xjc")
        #RNA
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, RNA_hX_5xjc")
        #BUD13
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, BUD13_hX_5xjc")
        #CLF2
        cmd.do("color rasberry, chain nan and 5xjc")
        cmd.do("color rasberry, CLF2_hX_5xjc")
        #Cus1
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, Cus1_hX_5xjc")
        #CWC24
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, CWC24_hX_5xjc")
        #CWC27
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, CWC27_hX_5xjc")
        #HSH155
        cmd.do("color smudge, chain nan and 5xjc")
        cmd.do("color smudge, HSH155_hX_5xjc")
        #HSH49
        cmd.do("color sand, chain nan and 5xjc")
        cmd.do("color sand, HSH49_hX_5xjc")
        #PML1
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, PML1_hX_5xjc")
        #PRP11
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, PRP11_hX_5xjc")
        #PRP2
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, PRP2_hX_5xjc")
        #RDS3
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, RDS3_hX_5xjc")
        #RSE1
        cmd.do("color smudge, chain nan and 5xjc")
        cmd.do("color smudge, RSE1_hX_5xjc")
        #SNU17
        cmd.do("color grey60, chain nan and 5xjc")
        cmd.do("color grey60, SNU17_hX_5xjc")
        #Ysf3
        cmd.do("color palegreen, chain nan and 5xjc")
        cmd.do("color palegreen, Ysf3_hX_5xjc")
        #cwc23
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, cwc23_hX_5xjc")
        #SPP382
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SPP382_hX_5xjc")
        #NTR2
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, NTR2_hX_5xjc")
        #PRP43
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP43_hX_5xjc")
        #SMB1
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMB1_hX_5xjc")
        #SME1
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SME1_hX_5xjc")
        #SMX3
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMX3_hX_5xjc")
        #SMX2
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMX2_hX_5xjc")
        #SMD3
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMD3_hX_5xjc")
        #SMD1
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMD1_hX_5xjc")
        #SMD2
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMD2_hX_5xjc")
        #PRP22
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP22_hX_5xjc")
        #PRP18
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP18_hX_5xjc")
        #SLU7
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SLU7_hX_5xjc")
        #SMF
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMF_hX_5xjc")
        #SMG
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SMG_hX_5xjc")
        #PRP9
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP9_hX_5xjc")
        #PRP21
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP21_hX_5xjc")
        #SNU23
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SNU23_hX_5xjc")
        #PRP38
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, PRP38_hX_5xjc")
        #SPP381
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, SPP381_hX_5xjc")
        #unknown_unassigned
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, unknown_unassigned_hX_5xjc")
        #Spp42_yPrp8
        cmd.do("color grey50, chain nan and 5xjc")
        cmd.do("color grey50, Spp42_yPrp8_hX_5xjc")
        #CWF15_yCWC15
        cmd.do("color orange, chain nan and 5xjc")
        cmd.do("color orange, CWF15_yCWC15_hX_5xjc")
        #PRKRIP1
        cmd.do("color grey50, chain X and 5xjc")
        cmd.do("color grey50, PRKRIP1_hX_5xjc")
