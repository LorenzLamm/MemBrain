import utils.star_utils as star_utils
import os
import numpy as np
import shutil


def add_inner_outer_choice(in_star, out_star, case='Chlamy'):
    data_lists = star_utils.read_star_file(in_star)
    if case in ['Chlamy', 'Chlamy_bin4']:
        inner_outer = ['_innerOuter',
                       'outer',  # Tomo_8 M2a
                       'outer',  # M4a
                       'inner',  # Tomo_1 M17c
                       'outer',  # M2
                       'inner',  # M21b
                       'inner',  # M25b
                       'outer',  # M26b
                       'inner',  # M3b
                       'inner',  # M3c
                       'outer',  # M4b
                       'inner',  # M5c
                       'inner',  # Tomo21 M12
                       'outer',  # M13a
                       'inner',  # M14a
                       'inner',  # M14b
                       'outer',  # M15
                       'inner',  # M18a
                       'outer',  # M19a
                       'inner',  # M2
                       'inner',  # M39
                       'outer',  # M3a
                       'outer',  # M40
                       'inner',  # M41
                       'outer',  # M42
                       'inner',  # M4a
                       'outer',  # M5a
                       'inner',  # M8
                       'outer',  # Tomo_9 M3a
                       'inner',  # M4b
                       'inner',  # M6a
                       'outer',  # M7a
                       ]
    elif case == 'spinach':
        inner_outer = ['_innerOuter',
                       'inner',  # M10
                       'outer',  # M11
                       'inner',  # M12
                       'outer',  # M13
                       'inner',  # M14
                       'outer',  # M15
                       'inner',  # M16
                       'outer',  # M17
                       'inner',  # M18
                       'outer',  # M19
                       'inner',  # M2
                       'inner',  # M20
                       'outer',  # M21
                       'inner',  # M22
                       'outer',  # M23
                       'inner',  #M26
                       'outer',  #M27
                       'inner',  #M28
                       'outer',  #M29
                       'outer',  #M3
                       'inner',  #M30
                       'outer',  #M31
                       'inner',  #M32
                       'outer',  #M33
                       'inner',  #M34
                       'outer',  #M35
                       'inner',  #M36
                       'outer',  #M37
                       'inner',  #M38
                       'outer',  #M39
                       'inner',  #M4
                       'inner',  #M40
                       'outer',  # M5
                       'inner',  # M6
                       'outer',  # M7
                       'inner',  # M8
                       'outer'  # M9
                       ]
    elif case == 'spinach_val':
        inner_outer = ['_innerOuter',
                       'outer',  # M1
                       'inner',  # M10
                       'outer',  # M11
                       'inner',  # M12
                       'outer',  # M13
                       'inner',  # M14
                       'outer',  # M15
                       'inner',  # M16
                       'inner',  # M2
                       'outer',  # M3
                       'inner',  # M4
                       'outer',  # M41
                       'inner',  # M42
                       'outer',  # M43
                       'inner',  # M44
                       'outer',  # M45
                       'inner',  # M46
                       'outer',  # M47
                       'inner',  # M48
                       'outer',  # M49
                       'outer',  # M5
                       'inner',  # M50
                       'outer',  # M51
                       'inner',  # M52
                       'inner',  # M6
                       'outer',  # M7
                       'inner',  # M8
                       'outer'  # M9
                       ]
    elif case == 'new_spinach':
        inner_outer = ['_innerOuter',
                       'inner',  # M10, S1 Tomo_0002_2
                       'outer',  # M11, S1 Tomo_0002_2
                       'outer',  # M7, S1 Tomo_0002_2
                       'inner',  # M8, S1 Tomo_0002_2
                       'outer',  # M9, S1 Tomo_0002_2
                       'outer',  # M12, S1, Tomo_0001
                       'outer',  # M14, S1, Tomo_0001
                       'outer',  # M16, S1, Tomo_0001
                       'inner',  # M17, S1, Tomo_0001
                       'inner',  # M19, S1, Tomo_0001
                       'inner',  # M11, S2, Tomo_0002
                       'inner',  # M13, S1C2, Tomo_0002
                       'inner',  # M15, S1C2, Tomo_0002
                       'outer',  # M20, S2, Tomo_0002
                       'inner',  # M5, S2, Tomo_0002
                       'inner',  # M10, S4, Tomo_0010
                       'inner',  # M12, S2, Tomo_0010
                       'outer',  # M19, S3, Tomo_0010
                       'outer',  # M3, S4, Tomo_0010
                       'inner',  # M4, S1, Tomo_0010
                       'inner',  # M12, S1, Tomo_0003
                       'outer',  # M13, S1, Tomo_0003
                       'inner',  # M14, S1, Tomo_0003
                       'outer',  # M15, S1, Tomo_0003
                       'inner',  # M18, S2, Tomo_0003
                       'inner',  # M38, S3, Tomo_0003
                       'outer',  # M18L, S4, Tomo_0004
                       'outer',  # M20L, S4, Tomo_0004
                       'inner',  # M3, S2, Tomo_0004
                       'inner',  # M7, S3, Tomo_0004
                       'outer',  # M8, S1, Tomo_0004
                       'inner',  # M2, S1C3, Tomo_0017
                       'inner',  # M2, S3, Tomo_0017
                       'outer',  # M3, S1C3, Tomo_0017
                       'inner',  # M4, S1C3, Tomo_0017
                       'outer',  # M5, S1C3, Tomo_0017
                       'inner',  # M14, S1, Tomo_0032
                       'outer',  # M19, S1, Tomo_0032
                       'outer',  # M21, S1C3, Tomo_0032
                       'outer',  # M3, S3, Tomo_0032
                       'inner',  # M4, S1C1, Tomo_0032
                       'outer',  # M7, S2, Tomo_0032
                       'outer',  # M15, S4, Tomo_0038
                       'inner',  # M2, S1, Tomo_0038
                       'inner',  # M2, S6, Tomo_0038
                       'inner',  # M4, S2, Tomo_0038
                       'outer',  # M5, S5, Tomo_0038
                       ]
    elif case == 'new_spinach_all':
        inner_outer = ['_innerOuter',
                       'outer',  # M1, S1 Tomo_0002_2
                       'inner',  # M10, S1 Tomo_0002_2
                       'outer',  # M11, S1 Tomo_0002_2
                       'inner',  # M12, S1 Tomo_0002_2
                       'outer',  # M13, S1 Tomo_0002_2
                       'inner',  # M14, S1 Tomo_0002_2
                       'outer',  # M15, S1 Tomo_0002_2
                       'inner',  # M16, S1 Tomo_0002_2
                       'outer',  # M17, S1 Tomo_0002_2
                       'inner',  # M18, S1 Tomo_0002_2
                       'outer',  # M18, S1 Tomo_0002_2
                       'inner',  # M2, S1 Tomo_0002_2
                       'inner',  # M20, S1 Tomo_0002_2
                       'outer',  # M21, S1 Tomo_0002_2
                       'inner',  # M22, S1 Tomo_0002_2
                       'outer',  # M23, S1 Tomo_0002_2
                       'inner',  # M24, S1 Tomo_0002_2
                       'outer',  # M25, S1 Tomo_0002_2
                       'inner',  # M26, S1 Tomo_0002_2
                       'outer',  # M27, S1 Tomo_0002_2
                       'inner',  # M28, S1 Tomo_0002_2
                       'outer',  # M29, S1 Tomo_0002_2
                       'outer',  # M3, S1 Tomo_0002_2
                       'inner',  # M30, S1 Tomo_0002_2
                       'outer',  # M31, S1 Tomo_0002_2
                       'inner',  # M32, S1 Tomo_0002_2
                       'outer',  # M33, S1 Tomo_0002_2
                       'inner',  # M34, S1 Tomo_0002_2
                       'outer',  # M35, S1 Tomo_0002_2
                       'inner',  # M36, S1 Tomo_0002_2
                       'outer',  # M37, S1 Tomo_0002_2
                       'inner',  # M38, S1 Tomo_0002_2
                       'outer',  # M39, S1 Tomo_0002_2
                       'inner',  # M4, S1 Tomo_0002_2
                       'inner',  # M40, S1 Tomo_0002_2
                       'outer',  # M41, S1 Tomo_0002_2
                       'inner',  # M42, S1 Tomo_0002_2
                       'outer',  # M5, S1 Tomo_0002_2
                       'inner',  # M6, S1 Tomo_0002_2
                       'outer',  # M7, S1 Tomo_0002_2
                       'inner',  # M8, S1 Tomo_0002_2
                       'outer',  # M9, S1 Tomo_0002_2

                       'inner',  # M1, S1 Tomo_0001
                       'inner',  # M1, S2 Tomo_0001
                       'outer',  # M10, S1 Tomo_0001
                       'outer',  # M10, S2 Tomo_0001
                       'inner',  # M11, S1 Tomo_0001
                       'inner',  # M11, S2 Tomo_0001
                       'outer',  # M12, S1 Tomo_0001
                       'outer',  # M12, S2 Tomo_0001
                       'inner',  # M13, S1 Tomo_0001
                       'inner',  # M13, S2 Tomo_0001
                       'outer',  # M14, S1 Tomo_0001
                       'outer',  # M14, S2 Tomo_0001
                       'inner',  # M15, S1 Tomo_0001
                       'inner',  # M15, S2 Tomo_0001
                       'outer',  # M16, S1 Tomo_0001
                       'outer',  # M16, S2 Tomo_0001
                       'inner',  # M17, S1 Tomo_0001
                       'inner',  # M17, S2 Tomo_0001
                       'outer',  # M18, S1 Tomo_0001
                       'outer',  # M18, S2 Tomo_0001
                       'inner',  # M19, S1 Tomo_0001
                       'inner',  # M19, S2 Tomo_0001
                       'outer',  # M2, S1 Tomo_0001
                       'outer',  # M2, S2 Tomo_0001
                       'outer',  # M20, S1 Tomo_0001
                       'outer',  # M20, S2 Tomo_0001
                       'inner',  # M21, S1 Tomo_0001
                       'outer',  # M22, S1 Tomo_0001
                       'inner',  # M23, S1 Tomo_0001
                       'outer',  # M24, S1 Tomo_0001
                       'inner',  # M3, S1 Tomo_0001
                       'inner',  # M3, S2 Tomo_0001
                       'outer',  # M4, S1 Tomo_0001
                       'outer',  # M4, S2 Tomo_0001
                       'inner',  # M5, S1 Tomo_0001
                       'inner',  # M5, S2 Tomo_0001
                       'outer',  # M6, S1 Tomo_0001
                       'outer',  # M6, S2 Tomo_0001
                       'inner',  # M7, S1 Tomo_0001
                       'inner',  # M7, S2 Tomo_0001
                       'outer',  # M8, S1 Tomo_0001
                       'outer',  # M8, S2 Tomo_0001
                       'inner',  # M9, S1 Tomo_0001
                       'inner',  # M9, S2 Tomo_0001

                       'inner',  # M1, S2 Tomo_0002
                       'outer',  # M10, S2 Tomo_0002
                       'inner',  # M11, S2 Tomo_0002
                       'outer',  # M12, S1C2 Tomo_0002
                       'outer',  # M12, S2 Tomo_0002
                       'inner',  # M13, S1C2 Tomo_0002
                       'inner',  # M13, S2 Tomo_0002
                       'outer',  # M14, S1C2 Tomo_0002
                       'outer',  # M14, S2 Tomo_0002
                       'inner',  # M15, S1C2 Tomo_0002
                       'inner',  # M15, S2 Tomo_0002
                       'outer',  # M16, S1C2 Tomo_0002
                       'outer',  # M16, S2 Tomo_0002
                       'inner',  # M17, S1C2 Tomo_0002
                       'inner',  # M17, S2 Tomo_0002
                       'outer',  # M18, S2 Tomo_0002
                       'inner',  # M19, S2 Tomo_0002
                       'outer',  # M2, S2 Tomo_0002
                       'outer',  # M20, S2 Tomo_0002
                       'inner',  # M21, S2 Tomo_0002
                       'outer',  # M22, S2 Tomo_0002
                       'inner',  # M3, S2 Tomo_0002
                       'outer',  # M4, S2 Tomo_0002
                       'inner',  # M5, S2 Tomo_0002
                       'outer',  # M6, S2 Tomo_0002
                       'inner',  # M7, S2 Tomo_0002
                       'outer',  # M8, S2 Tomo_0002
                       'inner',  # M9, S2 Tomo_0002

                       'outer',  # M1, S1 Tomo_0010
                       'outer',  # M1, S4 Tomo_0010
                       'inner',  # M10, S2 Tomo_0010
                       'inner',  # M10, S4 Tomo_0010
                       'outer',  # M11, S2 Tomo_0010
                       'outer',  # M11, S4 Tomo_0010
                       'inner',  # M12, S2 Tomo_0010
                       'inner',  # M12, S4 Tomo_0010
                       'outer',  # M13, S2 Tomo_0010
                       'outer',  # M13, S4 Tomo_0010
                       'outer',  # M13L, S2 Tomo_0010
                       'inner',  # M14, S2 Tomo_0010
                       'inner',  # M14, S4 Tomo_0010
                       'inner',  # M14L, S4 Tomo_0010
                       'outer',  # M15, S2 Tomo_0010
                       'inner',  # M16, S2 Tomo_0010
                       'outer',  # M17, S2 Tomo_0010
                       'inner',  # M18, S3 Tomo_0010
                       'outer',  # M19, S3 Tomo_0010
                       'outer',  # M1L, S1 Tomo_0010
                       'inner',  # M2, S1 Tomo_0010
                       'inner',  # M2, S4 Tomo_0010
                       'inner',  # M20, S3 Tomo_0010
                       'outer',  # M21, S3 Tomo_0010
                       'inner',  # M22, S3 Tomo_0010
                       'outer',  # M23, S3 Tomo_0010
                       'inner',  # M24, S3 Tomo_0010
                       'outer',  # M25, S3 Tomo_0010
                       'outer',  # M3, S1 Tomo_0010
                       'outer',  # M3, S4 Tomo_0010
                       'inner',  # M4, S1 Tomo_0010
                       'inner',  # M4, S4 Tomo_0010
                       'outer',  # M5, S1 Tomo_0010
                       'outer',  # M5, S4 Tomo_0010
                       'inner',  # M6, S1 Tomo_0010
                       'inner',  # M6, S4 Tomo_0010
                       'outer',  # M7, S1 Tomo_0010
                       'outer',  # M7, S4 Tomo_0010
                       'inner',  # M8, S1 Tomo_0010
                       'inner',  # M8, S4 Tomo_0010
                       'outer',  # M9, S1 Tomo_0010
                       'outer',  # M9, S4 Tomo_0010

                       'outer',  # M1, S1 Tomo_0003
                       'inner',  # M10, S1 Tomo_0003
                       'outer',  # M11, S1 Tomo_0003
                       'inner',  # M12, S1 Tomo_0003
                       'outer',  # M13, S1 Tomo_0003
                       'inner',  # M14, S1 Tomo_0003
                       'outer',  # M15, S1 Tomo_0003
                       'outer',  # M15, S2 Tomo_0003
                       'inner',  # M16, S1 Tomo_0003
                       'inner',  # M16, S2 Tomo_0003
                       'outer',  # M17, S2 Tomo_0003
                       'inner',  # M18, S2 Tomo_0003
                       'outer',  # M19, S2 Tomo_0003
                       'inner',  # M2, S1 Tomo_0003
                       'inner',  # M20, S2 Tomo_0003
                       'outer',  # M21, S2 Tomo_0003
                       'inner',  # M22, S2 Tomo_0003
                       'outer',  # M23, S2 Tomo_0003
                       'inner',  # M24, S2 Tomo_0003
                       'outer',  # M25, S2 Tomo_0003
                       'inner',  # M26, S2 Tomo_0003
                       'outer',  # M27, S2 Tomo_0003
                       'inner',  # M28, S2 Tomo_0003
                       'outer',  # M29, S2 Tomo_0003
                       'outer',  # M3, S1 Tomo_0003
                       'inner',  # M30, S2 Tomo_0003
                       'inner',  # M30, S3 Tomo_0003
                       'outer',  # M31, S2 Tomo_0003
                       'outer',  # M31, S3 Tomo_0003
                       'inner',  # M32, S2 Tomo_0003
                       'inner',  # M32, S3 Tomo_0003
                       'outer',  # M33, S3 Tomo_0003
                       'inner',  # M34, S3 Tomo_0003
                       'outer',  # M35, S3 Tomo_0003
                       'inner',  # M36, S3 Tomo_0003
                       'outer',  # M37, S3 Tomo_0003
                       'inner',  # M38, S3 Tomo_0003
                       'outer',  # M39, S3 Tomo_0003
                       'outer',  # M39, S4 Tomo_0003
                       'inner',  # M4, S1 Tomo_0003
                       'inner',  # M40, S3 Tomo_0003
                       'inner',  # M40, S4 Tomo_0003
                       'outer',  # M41, S3 Tomo_0003
                       'outer',  # M41, S4 Tomo_0003
                       'inner',  # M42, S3 Tomo_0003
                       'inner',  # M42, S4 Tomo_0003
                       'outer',  # M43, S4 Tomo_0003
                       'inner',  # M44, S4 Tomo_0003
                       'outer',  # M45, S4 Tomo_0003
                       'inner',  # M46, S4 Tomo_0003
                       'outer',  # M47, S4 Tomo_0003
                       'inner',  # M48, S4 Tomo_0003
                       'outer',  # M49, S4 Tomo_0003
                       'outer',  # M5, S1 Tomo_0003
                       'inner',  # M50, S4 Tomo_0003
                       'outer',  # M51, S4 Tomo_0003
                       'inner',  # M52, S4 Tomo_0003
                       'outer',  # M53, S4 Tomo_0003
                       'inner',  # M54, S4 Tomo_0003
                       'inner',  # M6, S1 Tomo_0003
                       'outer',  # M7, S1 Tomo_0003
                       'inner',  # M8, S1 Tomo_0003
                       'outer',  # M9, S1 Tomo_0003

                       'inner',  # M1, S1 Tomo_0004
                       'inner',  # M1, S2 Tomo_0004
                       'outer',  # M10, S1 Tomo_0004
                       'outer',  # M10, S3 Tomo_0004
                       'inner',  # M11, S1 Tomo_0004
                       'inner',  # M11, S3 Tomo_0004
                       'outer',  # M12, S1 Tomo_0004
                       'inner',  # M13, S1 Tomo_0004
                       'outer',  # M14, S1 Tomo_0004
                       'inner',  # M15, S1 Tomo_0004
                       'inner',  # M15, S1 Tomo_0004
                       'outer',  # M16, S1 Tomo_0004
                       'outer',  # M16, S3 Tomo_0004
                       'inner',  # M17, S1 Tomo_0004
                       'inner',  # M17, S4 Tomo_0004
                       'outer',  # M18, S1 Tomo_0004
                       'outer',  # M18, S3 Tomo_0004
                       'inner',  # M19, S1 Tomo_0004
                       'inner',  # M19, S4 Tomo_0004
                       'inner',  # M19L, S1 Tomo_0004
                       'outer',  # M2, S1 Tomo_0004
                       'outer',  # M2, S2 Tomo_0004
                       'outer',  # M20, S1 Tomo_0004
                       'outer',  # M20, S4 Tomo_0004
                       'outer',  # M20L, S1 Tomo_0004
                       'inner',  # M21, S1 Tomo_0004
                       'inner',  # M21, S4 Tomo_0004
                       'outer',  # M22, S1 Tomo_0004
                       'outer',  # M22, S4 Tomo_0004
                       'inner',  # M3, S1 Tomo_0004
                       'inner',  # M3, S2 Tomo_0004
                       'outer',  # M4, S1 Tomo_0004
                       'outer',  # M4, S2 Tomo_0004
                       'inner',  # M5, S1 Tomo_0004
                       'inner',  # M5, S2 Tomo_0004
                       'outer',  # M6, S1 Tomo_0004
                       'outer',  # M6, S3 Tomo_0004
                       'inner',  # M7, S1 Tomo_0004
                       'inner',  # M7, S3 Tomo_0004
                       'outer',  # M8, S1 Tomo_0004
                       'outer',  # M8, S3 Tomo_0004
                       'inner',  # M9, S1 Tomo_0004
                       'inner',  # M9, S3 Tomo_0004

                       'outer',  # M1, S1C1 Tomo_0017
                       'outer',  # M1, S1C3 Tomo_0017
                       'outer',  # M1, S2C2 Tomo_0017
                       'outer',  # M1, S3 Tomo_0017
                       'inner',  # M10, S1C1 Tomo_0017
                       'inner',  # M10, S1C3 Tomo_0017
                       'inner',  # M10, S2C2 Tomo_0017
                       'inner',  # M10, S3 Tomo_0017
                       'outer',  # M11, S1C1 Tomo_0017
                       'outer',  # M11, S1C3 Tomo_0017
                       'outer',  # M11, S2C2 Tomo_0017
                       'inner',  # M12, S1C1 Tomo_0017
                       'inner',  # M12, S1C3 Tomo_0017
                       'inner',  # M12, S2C2 Tomo_0017
                       'outer',  # M13, S1C1 Tomo_0017
                       'outer',  # M13, S1C3 Tomo_0017
                       'outer',  # M13, S2C2 Tomo_0017
                       'inner',  # M14, S1C1 Tomo_0017
                       'inner',  # M14, S1C3 Tomo_0017
                       'inner',  # M14, S2C2 Tomo_0017
                       'outer',  # M15, S1C1 Tomo_0017
                       'outer',  # M15, S1C2 Tomo_0017
                       'outer',  # M15, S2C2 Tomo_0017
                       'inner',  # M16, S1C1 Tomo_0017
                       'inner',  # M16, S1C2 Tomo_0017
                       'inner',  # M16, S2C2 Tomo_0017
                       'outer',  # M17, S1C1 Tomo_0017
                       'outer',  # M17, S1C2 Tomo_0017
                       'outer',  # M17, S2C2 Tomo_0017
                       'inner',  # M18, S1C1 Tomo_0017
                       'inner',  # M18, S1C2 Tomo_0017
                       'inner',  # M18, S2C2 Tomo_0017
                       'outer',  # M19, S1C1 Tomo_0017
                       'outer',  # M19, S1C2 Tomo_0017
                       'inner',  # M2, S1C1 Tomo_0017
                       'inner',  # M2, S1C3 Tomo_0017
                       'inner',  # M2, S2C2 Tomo_0017
                       'inner',  # M2, S3 Tomo_0017
                       'inner',  # M20, S1C1 Tomo_0017
                       'inner',  # M20, S1C2 Tomo_0017
                       'outer',  # M21, S1C1 Tomo_0017
                       'outer',  # M21, S1C2 Tomo_0017
                       'inner',  # M22, S1C1 Tomo_0017
                       'inner',  # M22, S1C2 Tomo_0017
                       'outer',  # M23, S1C1 Tomo_0017
                       'outer',  # M23, S1C2 Tomo_0017
                       'inner',  # M24, S1C1 Tomo_0017
                       'inner',  # M24, S1C2 Tomo_0017
                       'outer',  # M3, S1C1 Tomo_0017
                       'outer',  # M3, S1C3 Tomo_0017
                       'outer',  # M3, S2C2 Tomo_0017
                       'outer',  # M3, S3 Tomo_0017
                       'inner',  # M4, S1C1 Tomo_0017
                       'inner',  # M4, S1C3 Tomo_0017
                       'inner',  # M4, S2C2 Tomo_0017
                       'inner',  # M4, S3 Tomo_0017
                       'outer',  # M5, S1C1 Tomo_0017
                       'outer',  # M5, S1C3 Tomo_0017
                       'outer',  # M5, S2C2 Tomo_0017
                       'outer',  # M5, S3 Tomo_0017
                       'inner',  # M6, S1C1 Tomo_0017
                       'inner',  # M6, S1C3 Tomo_0017
                       'inner',  # M6, S2C2 Tomo_0017
                       'inner',  # M6, S3 Tomo_0017
                       'outer',  # M7, S1C1 Tomo_0017
                       'outer',  # M7, S1C3 Tomo_0017
                       'outer',  # M7, S2C2 Tomo_0017
                       'outer',  # M7, S3 Tomo_0017
                       'inner',  # M8, S1C1 Tomo_0017
                       'inner',  # M8, S1C3 Tomo_0017
                       'inner',  # M8, S2C2 Tomo_0017
                       'inner',  # M8, S3 Tomo_0017
                       'outer',  # M9, S1C1 Tomo_0017
                       'outer',  # M9, S1C3 Tomo_0017
                       'outer',  # M9, S2C2 Tomo_0017
                       'outer',  # M9, S3 Tomo_0017

                       'outer',  # M1, S1C1 Tomo_0032
                       'outer',  # M1, S1C2 Tomo_0032
                       'outer',  # M1, S2 Tomo_0032
                       'outer',  # M1, S3 Tomo_0032
                       'inner',  # M10, S1C2 Tomo_0032
                       'inner',  # M10, S2 Tomo_0032
                       'inner',  # M10, S3 Tomo_0032
                       'outer',  # M11, S1C2 Tomo_0032
                       'outer',  # M11, S3 Tomo_0032
                       'inner',  # M12, S1C2 Tomo_0032
                       'inner',  # M12, S3 Tomo_0032
                       'outer',  # M13, S1C2 Tomo_0032
                       'outer',  # M13, S1C3 Tomo_0032
                       'inner',  # M14, S1C2 Tomo_0032
                       'inner',  # M14, S1C3 Tomo_0032
                       'outer',  # M15, S1C2 Tomo_0032
                       'outer',  # M15, S1C3 Tomo_0032
                       'inner',  # M16, S1C2 Tomo_0032
                       'inner',  # M16, S1C3 Tomo_0032
                       'outer',  # M17, S1C2 Tomo_0032
                       'outer',  # M17, S1C3 Tomo_0032
                       'inner',  # M18, S1C2 Tomo_0032
                       'inner',  # M18, S1C3 Tomo_0032
                       'outer',  # M19, S1C2 Tomo_0032
                       'outer',  # M19, S1C3 Tomo_0032
                       'inner',  # M2, S1C1 Tomo_0032
                       'inner',  # M2, S1C2 Tomo_0032
                       'inner',  # M2, S2 Tomo_0032
                       'inner',  # M2, S3 Tomo_0032
                       'inner',  # M20, S1C2 Tomo_0032
                       'inner',  # M20, S1C3 Tomo_0032
                       'outer',  # M21, S1C2 Tomo_0032
                       'outer',  # M21, S1C3 Tomo_0032
                       'outer',  # M3, S1C1 Tomo_0032
                       'outer',  # M3, S1C2 Tomo_0032
                       'outer',  # M3, S2 Tomo_0032
                       'outer',  # M3, S3 Tomo_0032
                       'inner',  # M4, S1C1 Tomo_0032
                       'inner',  # M4, S1C2 Tomo_0032
                       'inner',  # M4, S2 Tomo_0032
                       'inner',  # M4, S3 Tomo_0032
                       'outer',  # M5, S1C1 Tomo_0032
                       'outer',  # M5, S1C2 Tomo_0032
                       'outer',  # M5, S2 Tomo_0032
                       'outer',  # M5, S3 Tomo_0032
                       'inner',  # M6, S1C1 Tomo_0032
                       'inner',  # M6, S1C2 Tomo_0032
                       'inner',  # M6, S2 Tomo_0032
                       'inner',  # M6, S3 Tomo_0032
                       'outer',  # M7, S1C2 Tomo_0032
                       'outer',  # M7, S2 Tomo_0032
                       'outer',  # M7, S3 Tomo_0032
                       'inner',  # M8, S1C2 Tomo_0032
                       'inner',  # M8, S2 Tomo_0032
                       'inner',  # M8, S3 Tomo_0032
                       'outer',  # M9, S1C2 Tomo_0032
                       'outer',  # M9, S2 Tomo_0032
                       'outer',  # M9, S3 Tomo_0032

                       'outer',  # M1, S1 Tomo_0038
                       'outer',  # M1, S2 Tomo_0038
                       'outer',  # M1, S5 Tomo_0038
                       'outer',  # M1, S6 Tomo_0038
                       'inner',  # M10, S6 Tomo_0038
                       'outer',  # M11, S6 Tomo_0038
                       'inner',  # M12, S6 Tomo_0038
                       'outer',  # M13, S6 Tomo_0038
                       'inner',  # M14, S6 Tomo_0038
                       'outer',  # M15, S4 Tomo_0038
                       'outer',  # M15, S6 Tomo_0038
                       'inner',  # M16, S6 Tomo_0038
                       'inner',  # M16, S6 Tomo_0038
                       'outer',  # M17, S4 Tomo_0038
                       'outer',  # M17, S6 Tomo_0038
                       'inner',  # M18, S4 Tomo_0038
                       'outer',  # M19, S4 Tomo_0038
                       'inner',  # M2, S1 Tomo_0038
                       'inner',  # M2, S2 Tomo_0038
                       'inner',  # M2, S5 Tomo_0038
                       'inner',  # M2, S6 Tomo_0038
                       'inner',  # M20, S4 Tomo_0038
                       'outer',  # M21, S4 Tomo_0038
                       'inner',  # M22, S4 Tomo_0038
                       'outer',  # M23, S4 Tomo_0038
                       'inner',  # M24, S4 Tomo_0038
                       'outer',  # M25, S4 Tomo_0038
                       'inner',  # M26, S4 Tomo_0038
                       'outer',  # M27, S4 Tomo_0038
                       'inner',  # M28, S4 Tomo_0038
                       'outer',  # M29, S4 Tomo_0038
                       'outer',  # M3, S1 Tomo_0038
                       'outer',  # M3, S2 Tomo_0038
                       'outer',  # M3, S5 Tomo_0038
                       'outer',  # M3, S6 Tomo_0038
                       'inner',  # M30, S4 Tomo_0038
                       'outer',  # M31, S4 Tomo_0038
                       'inner',  # M32, S4 Tomo_0038
                       'inner',  # M4, S1 Tomo_0038
                       'inner',  # M4, S2 Tomo_0038
                       'inner',  # M4, S5 Tomo_0038
                       'inner',  # M4, S6 Tomo_0038
                       'outer',  # M5, S1 Tomo_0038
                       'outer',  # M5, S2 Tomo_0038
                       'outer',  # M5, S5 Tomo_0038
                       'outer',  # M5, S6 Tomo_0038
                       'inner',  # M6, S1 Tomo_0038
                       'inner',  # M6, S2 Tomo_0038
                       'inner',  # M6, S5 Tomo_0038
                       'inner',  # M6, S6 Tomo_0038
                       'outer',  # M7, S1 Tomo_0038
                       'outer',  # M7, S2 Tomo_0038
                       'outer',  # M7, S5 Tomo_0038
                       'outer',  # M7, S6 Tomo_0038
                       'inner',  # M8, S1 Tomo_0038
                       'inner',  # M8, S2 Tomo_0038
                       'inner',  # M8, S5 Tomo_0038
                       'inner',  # M8, S6 Tomo_0038
                       'outer'   # M9, S6 Tomo_0038


                       ]
    elif case == 'matthias':
        inner_outer = ['_innerOuter',
                       'inner',
                       'outer',
                       'inner',
                       'outer',
                       'outer'

                       ]

    data_lists.append(inner_outer)
    star_utils.write_star_file(out_star, data_lists)



def check_dimi(dir, tomo_tokens, binning):
    flags = [False] * len(tomo_tokens)
    for i, token in enumerate(tomo_tokens):
        tomo_dir = os.path.join(dir, token)
        for file in os.listdir(tomo_dir):
            if not os.path.isdir(os.path.join(dir, file)) and '_dimi_' in file and ('bin' + str(binning)) in file:
                flags[i] = True
                break
    return not any([not flag for flag in flags])

def check_denoised(dir, tomo_tokens, binning):
    flags = [False] * len(tomo_tokens)
    for i, token in enumerate(tomo_tokens):
        tomo_dir = os.path.join(dir, token)
        for file in os.listdir(tomo_dir):
            if not os.path.isdir(os.path.join(dir, file)) and '_denoised_' in file and ('bin' + str(binning)) in file:
                flags[i] = True
                break
    return not any([not flag for flag in flags])


def get_tomo_path(in_dir, tomo_token, binning, dimi, denoised=False):
    tomo_dir = os.path.join(in_dir, tomo_token)
    for file in os.listdir(tomo_dir):
        if not os.path.isdir(os.path.join(tomo_dir, file)) and ('bin' + str(binning)) in file:
            if dimi:
                if not '_dimi_' in file:
                    continue
            elif denoised:
                if not '_denoised' in file:
                    continue
            else:
                if '_dimi_' in file or '_denoised_' in file:
                    continue
            return os.path.join(tomo_dir, file)


def create_gt_dir(tomo_token, gt_out_dir, pos_dir):
    xml_out_path = os.path.join(gt_out_dir, tomo_token, 'as_xml')
    try:
        os.makedirs(xml_out_path)
    except OSError as e:
        if False:
            raise
    for file in os.listdir(pos_dir):
        if file.endswith('.xml'):
            comp_file = os.path.join(pos_dir, file)
            out_file = os.path.join(xml_out_path, file)
            shutil.copyfile(comp_file, out_file)


def create_initial_stars(in_dir, out_star, gt_out_dir, binning=2, with_dimi=True, with_denoised=True,
                         add_bin4_paths=True, pixel_spacing_bin1=3.42, unbinned_offset_Z=None, training=False):
    tomo_tokens = []
    for folder in os.listdir(in_dir):
        if os.path.isdir(os.path.join(in_dir, folder)):
            tomo_tokens.append(folder)
    if not check_dimi(in_dir, tomo_tokens, binning):
        with_dimi = False
    if not check_denoised(in_dir, tomo_tokens, binning):
        with_denoised = False

    star_dict = {
        'tomoToken': [],
        'tomoPath': [],
        'mbToken': [],
        'segPath': [],
        'tomoBin': [],
        'tomoBin4Path': [],
        'gtPath': [],
        'pixelSpacing': [],
        'stackToken': []
    }
    if unbinned_offset_Z is not None:
        star_dict['unbinnedOffsetZ'] = []
    if with_dimi:
        star_dict['tomoPathDimi'] = []
    if with_denoised:
        star_dict['tomoPathDenoised'] = []

    mb_tokens = {}
    for tomo_token in tomo_tokens:
        mb_tokens[tomo_token] = []
        seg_mbs = []
        pos_mbs = []
        tomo_dir = os.path.join(in_dir, tomo_token)
        pos_flag, seg_flag = False, False
        for file in os.listdir(tomo_dir):
            if os.path.isdir(os.path.join(tomo_dir, file)) and 'positions' in file and not 'all_no_positions' in file:
                pos_folder = os.path.join(tomo_dir, file)
                create_gt_dir(tomo_token, gt_out_dir, pos_folder)
                pos_flag = True
        # tomo_dir += '/all_no_positions/'
        for file in os.listdir(tomo_dir):
            if os.path.isdir(os.path.join(tomo_dir, file)) and 'membranes' in file:
                mb_folder = os.path.join(tomo_dir, file)
                seg_flag = True
        if not pos_flag:
            print("WARNING: Folder for tomogram " + tomo_token + " does not contain positions folder. Only use for inference!")
        assert seg_flag, 'folder for tomogram ' + tomo_token + ' does not contain membranes folder'
        for seg in os.listdir(mb_folder):
            if not seg.endswith('.mrc'):
                continue
            mb_token = 'M' + seg.split('M')[1].split('.')[0].split('_')[0]
            stack_token = 'S' + os.path.basename(seg).split('S')[1].split('M')[0]
            seg_mbs.append((mb_token, stack_token))
        if pos_flag:
            for pos in os.listdir(pos_folder):
                if not os.path.isfile(os.path.join(pos_folder, pos)) or not pos.endswith('xml'):
                    continue
                mb_token = 'M' + pos.split('M')[1].split('.')[0].split('_')[0]
                stack_token = 'S' + os.path.basename(pos).split('S')[1].split('M')[0]
                pos_mbs.append((mb_token, stack_token))
            seg_mbs = np.unique(seg_mbs,axis=0).tolist()
            pos_mbs = np.unique(pos_mbs, axis=0).tolist()
            # remove_list = []
            # for mb in seg_mbs:
            #     if mb not in pos_mbs:
            #         remove_list.append(mb)
            # for mb in remove_list:
            #     seg_mbs.remove(mb)
            remove_list = []
            for mb in pos_mbs:
                if mb not in seg_mbs:
                    remove_list.append(mb)
            for mb in remove_list:
                pos_mbs.remove(mb)
            assert len(pos_mbs) <= len(seg_mbs), 'Labels and membranes are not consistent!'

        mb_tokens[tomo_token] = seg_mbs


    for tomo_token in tomo_tokens:
        tomo_path = get_tomo_path(in_dir, tomo_token, binning, dimi=False)
        tomo_path_bin4 = get_tomo_path(in_dir, tomo_token, binning=4, dimi=False, denoised=True)
        print(tomo_path, "<-------")
        if with_dimi:
            tomo_path_dimi = get_tomo_path(in_dir, tomo_token, binning, dimi=True)
        if with_denoised:
            tomo_path_denoised = get_tomo_path(in_dir, tomo_token, binning, dimi=False, denoised=True)
        tomo_dir = os.path.join(in_dir, tomo_token)
        # tomo_dir += '/all_no_positions/'
        for file in os.listdir(tomo_dir):
            if os.path.isdir(os.path.join(tomo_dir, file)) and 'membranes' in file:
                mb_folder = os.path.join(tomo_dir, file)

        for mb_token in mb_tokens[tomo_token]:
            star_dict['tomoToken'].append(tomo_token)
            star_dict['mbToken'].append(mb_token[0])
            star_dict['tomoPath'].append(tomo_path)
            star_dict['tomoBin'].append(str(binning))
            star_dict['tomoBin4Path'].append(tomo_path_bin4)
            if with_dimi:
                star_dict['tomoPathDimi'].append(tomo_path_dimi)
            if with_denoised:
                star_dict['tomoPathDenoised'].append(tomo_path_denoised)

            star_dict['gtPath'].append(gt_out_dir)
            star_dict['pixelSpacing'].append(str(pixel_spacing_bin1))
            if unbinned_offset_Z is not None:
                star_dict['unbinnedOffsetZ'].append(str(unbinned_offset_Z))
            for file in os.listdir(mb_folder):
                if (mb_token[0] + '_') in file or (mb_token[0] + '.') in file and mb_token[1] in file:
                    mb_path = os.path.join(mb_folder, file)
            star_dict['segPath'].append(mb_path)
            # stack_token = 'S' + os.path.basename(mb_path).split('S')[1].split('M')[0]
            star_dict['stackToken'].append(mb_token[1])

    star_utils.write_star_file_from_dict(out_star, star_dict)



def create_initial_star_pyseg(mic_dir, seg_dir, star_stem):
    out_star = os.path.join(seg_dir, star_stem + '.star')
    mics = []
    segs = []
    zeros = []
    for file in os.listdir(mic_dir):
        assert os.path.isfile(os.path.join(seg_dir, file))
        mics.append(os.path.join(mic_dir, file))
        segs.append(os.path.join(seg_dir, file))
        zeros.append(0)

    star_dict = {
        '_rlnMicrographName': mics,
        '_rlnImageName': mics,
        '_psSegImage': segs,
        '_psSegOffX': zeros,
        '_psSegOffY': zeros,
        '_psSegOffZ': zeros,
        '_psSegRot': zeros,
        '_psSegTilt': zeros,
        '_psSegPsi': zeros
    }

    star_utils.write_star_file_from_dict(out_star, star_dict)

def fuse_star_files(in_star_list, out_star, skip_denoised=True):
    star_dict = star_utils.read_star_file_as_dict(in_star_list[0])
    for i in range(1, len(in_star_list)):
        temp_dict = star_utils.read_star_file_as_dict(in_star_list[i])
        for key in star_dict.keys():
            if key not in temp_dict.keys():
                del star_dict[key]
                continue
            star_dict[key] += temp_dict[key]
    star_utils.write_star_file_from_dict(out_star, star_dict)

## For Pyseg:
# mics_dir = '/fs/pool/pool-engel/Lorenz/real_data/Pyseg_comparison/mics/'
# segs_dir = '/fs/pool/pool-engel/Lorenz/real_data/Pyseg_comparison/segs/'
# create_initial_star_pyseg(mics_dir, segs_dir, 'chlamy')
# exit()

## For neural networks:

case = 'matthias'

if case == 'Chlamy':
    in_dir = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy/tomograms/'
    out_star = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy/initial_stars/chlamy.star'
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy/initial_stars/chlamy_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_spinach/gt_coords/'
    pixel_spacing_bin1 = 13.68 / 4
    unbinned_offset_Z = 3173.74
    tomo_binning = 2
elif case == 'spinach':
    in_dir = '/fs/pool/pool-engel/Lorenz/pipeline_spinach/tomograms/'
    out_star = '/fs/pool/pool-engel/Lorenz/pipeline_spinach/initial_stars/chlamy.star'
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_spinach/initial_stars/chlamy_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_spinach/gt_coords/'
    pixel_spacing_bin1 = 14.08 / 4
    unbinned_offset_Z = 0
    tomo_binning = 4
elif case == 'Chlamy_bin4':
    in_dir = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy/tomograms/'
    out_star = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy_bin4/initial_stars/chlamy.star'
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy_bin4/initial_stars/chlamy_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_Chlamy_bin4/gt_coords/'
    pixel_spacing_bin1 = 13.68 / 4
    unbinned_offset_Z = 3173.74
    tomo_binning = 4
elif case == 'spinach_val':
    in_dir = '/fs/pool/pool-engel/Lorenz/pipeline_spinach_validation/tomograms/'
    out_star = '/fs/pool/pool-engel/Lorenz/pipeline_spinach_validation/initial_stars/chlamy.star'
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_spinach_validation/initial_stars/chlamy_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_spinach_validation/gt_coords/'
    pixel_spacing_bin1 = 14.08 / 4
    unbinned_offset_Z = 0
    tomo_binning = 4
elif case == 'new_spinach':
    in_dir = ['/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/180524/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200511/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200303',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200129',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/190601']
    out_star = ['/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach1.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach2.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach3.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach4.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach5.star']
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/initial_stars/new_spinach_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach/gt_coords/'
    pixel_spacing_bin1 = 14.08 / 4
    unbinned_offset_Z = 0
    tomo_binning = 4
elif case == 'new_spinach_all':
    in_dir = ['/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/180524/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200511/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200303/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/200129/',
              '/fs/pool/pool-engel/Spinach_project/folder_for_lorenz/190601/']
    out_star = ['/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach1.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach2.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach3.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach4.star',
                '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach5.star']
    out_star2 = '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/initial_stars/new_spinach_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/pipeline_new_spinach_all/gt_coords/'
    pixel_spacing_bin1 = 14.08 / 4
    unbinned_offset_Z = 0
    tomo_binning = 4
elif case == 'matthias':
    in_dir = ['/fs/pool/pool-engel/Lorenz/Matthias_project/data/Tomo02']
    out_star = ['/fs/pool/pool-engel/Lorenz/Matthias_project/pipeline/initial_stars/Tomo02_matthias.star']
    out_star2 = '/fs/pool/pool-engel/Lorenz/Matthias_project/pipeline/initial_stars/Tomo02_matthias_with_inner_outer.star'
    gt_out_dir = '/fs/pool/pool-engel/Lorenz/Matthias_project/pipeline/gt_coords'
    pixel_spacing_bin1 = 10.68
    unbinned_offset_Z = 0.
    tomo_binning = 4
else:
    raise IOError('Case not in cases!')

# if not isinstance(in_dir, list):
#     create_initial_stars(in_dir, out_star, gt_out_dir, binning=tomo_binning, pixel_spacing_bin1=pixel_spacing_bin1, unbinned_offset_Z=unbinned_offset_Z)
# else:
#     for i, entry in enumerate(in_dir):
#         create_initial_stars(entry, out_star[i], gt_out_dir, binning=tomo_binning, pixel_spacing_bin1=pixel_spacing_bin1,
#                              unbinned_offset_Z=unbinned_offset_Z)
# fuse_star_files(out_star, out_star2)
#
#
# add_inner_outer_choice(out_star2, out_star2, case=case)
