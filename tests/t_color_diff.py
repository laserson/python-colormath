"""
 Color Math Module (colormath) 
 Copyright (C) 2009 Gregory Taylor

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Tests for color difference (Delta E) equations.
"""
import unittest
from colormath.color_objects import *
from colormath.color_exceptions import *
from colormath.color_diff import *

class DeltaE_Tests(unittest.TestCase):
    def setUp(self):
        self.color1 = LabColor(lab_l=0.9, lab_a=16.3, lab_b=-2.22)
        self.color2 = LabColor(lab_l=0.7, lab_a=14.2, lab_b=-1.80)
        
    def test_cie2000_accuracy(self):
        result = self.color1.delta_e(self.color2, mode='cie2000')
        expected = 1.523
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CIE2000 formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
    def test_cie2000_accuracy_2(self):
        """
        Follow a different execution path based on variable values.
        """
        # These values are from ticket 8 in regards to a CIE2000 bug.
        c1 = LabColor(lab_l=32.8911,lab_a=-53.0107,lab_b=-43.3182)
        c2 = LabColor(lab_l=77.1797,lab_a=25.5928,lab_b=17.9412)
        result = c1.delta_e(c2, mode='cie2000')
        expected = 78.772
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CIE2000 formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
    def test_cie2000_accuracy_3(self):
        """
        Reference:
        "The CIEDE2000 Color-Difference Formula: Implementation Notes, 
        Supplementary Test Data, and Mathematical Observations,", G. Sharma, 
        W. Wu, E. N. Dalal, submitted to Color Research and Application,
        January 2004. http://www.ece.rochester.edu/~gsharma/ciede2000/
        """
        color1 = (
            LabColor(lab_l=50.0000, lab_a=2.6772, lab_b=-79.7751),
            LabColor(lab_l=50.0000, lab_a=3.1571, lab_b=-77.2803),
            LabColor(lab_l=50.0000, lab_a=2.8361, lab_b=-74.0200),
            LabColor(lab_l=50.0000, lab_a=-1.3802, lab_b=-84.2814),
            LabColor(lab_l=50.0000, lab_a=-1.1848, lab_b=-84.8006),
            LabColor(lab_l=50.0000, lab_a=-0.9009, lab_b=-85.5211),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=-1.0000, lab_b=2.0000),
            LabColor(lab_l=50.0000, lab_a=2.4900, lab_b=-0.0010),
            LabColor(lab_l=50.0000, lab_a=2.4900, lab_b=-0.0010),
            LabColor(lab_l=50.0000, lab_a=2.4900, lab_b=-0.0010),
            LabColor(lab_l=50.0000, lab_a=2.4900, lab_b=-0.0010),
            LabColor(lab_l=50.0000, lab_a=-0.0010, lab_b=2.4900),
            LabColor(lab_l=50.0000, lab_a=-0.0010, lab_b=2.4900),
            LabColor(lab_l=50.0000, lab_a=-0.0010, lab_b=2.4900),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=2.5000, lab_b=0.0000),
            LabColor(lab_l=60.2574, lab_a=-34.0099, lab_b=36.2677),
            LabColor(lab_l=63.0109, lab_a=-31.0961, lab_b=-5.8663),
            LabColor(lab_l=61.2901, lab_a=3.7196, lab_b=-5.3901),
            LabColor(lab_l=35.0831, lab_a=-44.1164, lab_b=3.7933),
            LabColor(lab_l=22.7233, lab_a=20.0904, lab_b=-46.6940),
            LabColor(lab_l=36.4612, lab_a=47.8580, lab_b=18.3852),
            LabColor(lab_l=90.8027, lab_a=-2.0831, lab_b=1.4410),
            LabColor(lab_l=90.9257, lab_a=-0.5406, lab_b=-0.9208),
            LabColor(lab_l=6.7747, lab_a=-0.2908, lab_b=-2.4247),
            LabColor(lab_l=2.0776, lab_a=0.0795, lab_b=-1.1350)
            )
        color2 = (
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-82.7485),
            LabColor(lab_l=50.0000, lab_a=-1.0000, lab_b=2.0000),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=-2.4900, lab_b=0.0009),
            LabColor(lab_l=50.0000, lab_a=-2.4900, lab_b=0.0010),
            LabColor(lab_l=50.0000, lab_a=-2.4900, lab_b=0.0011),
            LabColor(lab_l=50.0000, lab_a=-2.4900, lab_b=0.0012),
            LabColor(lab_l=50.0000, lab_a=0.0009, lab_b=-2.4900),
            LabColor(lab_l=50.0000, lab_a=0.0010, lab_b=-2.4900),
            LabColor(lab_l=50.0000, lab_a=0.0011, lab_b=-2.4900),
            LabColor(lab_l=50.0000, lab_a=0.0000, lab_b=-2.5000),
            LabColor(lab_l=73.0000, lab_a=25.0000, lab_b=-18.0000),
            LabColor(lab_l=61.0000, lab_a=-5.0000, lab_b=29.0000),
            LabColor(lab_l=56.0000, lab_a=-27.0000, lab_b=-3.0000),
            LabColor(lab_l=58.0000, lab_a=24.0000, lab_b=15.0000),
            LabColor(lab_l=50.0000, lab_a=3.1736, lab_b=0.5854),
            LabColor(lab_l=50.0000, lab_a=3.2972, lab_b=0.0000),
            LabColor(lab_l=50.0000, lab_a=1.8634, lab_b=0.5757),
            LabColor(lab_l=50.0000, lab_a=3.2592, lab_b=0.3350),
            LabColor(lab_l=60.4626, lab_a=-34.1751, lab_b=39.4387),
            LabColor(lab_l=62.8187, lab_a=-29.7946, lab_b=-4.0864),
            LabColor(lab_l=61.4292, lab_a=2.2480, lab_b=-4.9620),
            LabColor(lab_l=35.0232, lab_a=-40.0716, lab_b=1.5901),
            LabColor(lab_l=23.0331, lab_a=14.9730, lab_b=-42.5619),
            LabColor(lab_l=36.2715, lab_a=50.5065, lab_b=21.2231),
            LabColor(lab_l=91.1528, lab_a=-1.6435, lab_b=0.0447),
            LabColor(lab_l=88.6381, lab_a=-0.8985, lab_b=-0.7239),
            LabColor(lab_l=5.8714, lab_a=-0.0985, lab_b=-2.2286),
            LabColor(lab_l=0.9033, lab_a=-0.0636, lab_b=-0.5514)
            )
        diff = (
            2.0425, 2.8615, 3.4412, 1.0000, 1.0000, 
            1.0000, 2.3669, 2.3669, 7.1792, 7.1792, 
            7.2195, 7.2195, 4.8045, 4.8045, 4.7461, 
            4.3065, 27.1492, 22.8977, 31.9030, 19.4535, 
            1.0000, 1.0000, 1.0000, 1.0000, 1.2644, 
            1.2630, 1.8731, 1.8645, 2.0373, 1.4146, 
            1.4441, 1.5381, 0.6377, 0.9082
            )
        for set in zip(color1, color2, diff):
            result = set[0].delta_e(set[1], mode='cie2000')
            expected = set[2]
            self.assertAlmostEqual(result, expected, 4,
                "DeltaE CIE2000 formula error. Got %.4f, expected %.4f (diff: %.4f)." % (
                    result, expected, result - expected)
                    )
        
    def test_cie1994_negative_square_root(self):
        """
        Tests against a case where a negative square root in the delta_H
        calculation could happen.
        """
        standard = LabColor(lab_l=0.9, lab_a=1, lab_b=1)
        sample = LabColor(lab_l=0.7, lab_a=0, lab_b=0)
        standard.delta_e(sample, mode='cie1994')
        
        
    def test_cmc_negative_square_root(self):
        """
        Tests against a case where a negative square root in the delta_H
        calculation could happen.
        """
        standard = LabColor(lab_l=0.9, lab_a=1, lab_b=1)
        sample = LabColor(lab_l=0.7, lab_a=0, lab_b=0)
        standard.delta_e(sample, mode='cmc')
        
    def test_cmc_accuracy(self):
        # Test 2:1
        result = self.color1.delta_e(self.color2, mode='cmc', pl=2, pc=1)
        expected = 1.443
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CMC (2:1) formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
        # Test against 1:1 as well
        result = self.color1.delta_e(self.color2, mode='cmc', pl=1, pc=1)
        expected = 1.482
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CMC (1:1) formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
        # Testing atan H behavior.
        atan_color1 = LabColor(lab_l=69.417, lab_a=-12.612, lab_b=-11.271)
        atan_color2 = LabColor(lab_l=83.386, lab_a=39.426, lab_b=-17.525)
        result = atan_color1.delta_e(atan_color2, mode='cmc')
        expected = 44.346
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CMC Atan test formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
    def test_cie1976_accuracy(self):
        result = self.color1.delta_e(self.color2, mode='cie1976')
        expected = 2.151
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CIE1976 formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
    def test_cie1994_accuracy_graphic_arts(self):
        result = self.color1.delta_e(self.color2, mode='cie1994')
        expected = 1.249
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CIE1994 (graphic arts) formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
        
    def test_cie1994_accuracy_textiles(self):
        result = self.color1.delta_e(self.color2, mode='cie1994',
                                     K_1=0.048, K_2=0.014, K_L=2)
        expected = 1.204
        self.assertAlmostEqual(result, expected, 3, 
                "DeltaE CIE1994 (textiles) formula error. Got %.3f, expected %.3f (diff: %.3f)." % (
                                                        result, expected,
                                                        result - expected))
    def test_cie1994_domain_error(self):
        # These values are from ticket 98 in regards to a CIE1995
        # domain error exception being raised.
        c1 = LabColor(lab_l=50, lab_a=0, lab_b=0)
        c2 = LabColor(lab_l=50, lab_a=-1, lab_b=2)
        try:
            result = c1.delta_e(c2, mode='cie1994')
        except ValueError:
            self.fail("DeltaE CIE1994 domain error. See issue 9 in tracker.")
        
        
    def test_invalid_delta_e_arg(self):
        invalid_color = "THIS IS NOT A COLOR!"
        self.assertRaises(InvalidArgument, self.color1.delta_e, 
                          invalid_color)
        
    def test_invalid_delta_e_mode(self):
        self.assertRaises(InvalidDeltaEMode, self.color1.delta_e, 
                          self.color2, mode='blahlbah')
        
if __name__ == '__main__':
    unittest.main()