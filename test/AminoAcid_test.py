### test binome 1 ###
#######  AA  #######
from ..AminoAcid import AminoAcid
from ..Atom import Atom

N = Atom("N",4.524,9.887,-0.667)
CA = Atom("CA", 5.918, 10.123,-0.175)
C = Atom("C",5.865, 10.943,1.122) 
O = Atom("O", 5.284,12.009,1.177)
CB = Atom("CB",6.697,10.871,-1.278)
CG= Atom ("CG", 5.715,11.124,-2.430)
CD = Atom("CD", 4.374, 10.484,-2.030)
H = Atom("H", 4.341,8.86,-0.711)
H3 = Atom("H3", 3.846, 10.334,-0.018)
HA = Atom("HA", 6.393, 9.171, 0.029)
HB2 = Atom("HB2",7.081,11.812,-0.901)
HB3 = Atom("HB3", 7.520,10.262,-1.629)
HG2 = Atom("HG2", 5.590,12.191,-2.583)
HG3 = Atom("HG3", 6.081,10.668, -3.341)
HD2 = Atom("HD2", 3.596,11.236, -2.011)
HD3 = Atom("HD3", 4.108, 9.707,-2.734)

PRO = AminoAcid("PRO",1,[N,CA,C,O],[CB,CG,CD,H,H3,HA,HB2,HB3,HG2,HG3,HD2,HD3])

# Instance creation
try:
    assert (isinstance(PRO,AminoAcid))
    print("The test of object creation of class AminoAcid has passed.")
except:
    AssertionError
    print("The test of object creation of class AminoAcid has failed.")

# test getters of atoms of the backbone
try:
    assert (PRO.get_N()).get_coords() == (4.524,9.887,-0.667) and (PRO.get_N()).get_name() == "N"
    print("The test of fuction get_N(self) has passed.")
except:
    AssertionError
    print("The test of fuction get_N(self) has failed.")
    
try:
    assert (PRO.get_C()).get_coords() == (5.865, 10.943,1.122) and (PRO.get_C()).get_name() == "C"
    print("The test of fuction get_C(self), has passed.")
except:
    AssertionError
    print("The test of fuction get_C(self) has failed.")
    
try:
    assert (PRO.get_CA()).get_coords() == (5.918, 10.123,-0.175) and (PRO.get_CA()).get_name() == "CA"
    print("The test of fuction get_CA(self) has passed.")
    
except:
    AssertionError
    print("The test of fuction get_CA(self) has failed.")

try:
    assert (PRO.get_O()).get_coords() == (5.284,12.009,1.177) and (PRO.get_O()).get_name() == "O"
    print("The test of fuction get_O(self) has passed.")
    
except:
    AssertionError
    print("The test of fuction get_O(self) has failed.")
    
# check get_res_type(self) 
try:
    assert PRO.get_res_type() == "PRO" 
    print("The test of fuctions get_res_type(self) has passed.")
except:
    AssertionError
    print("The test of fuctions get_res_type(self) has failed.")

# check get_res_type(self) and set_res_type(self, new_type)
try:
    PRO.set_res_type("ALA")
    assert PRO.get_res_type() == "ALA"
    print("The test of fuctions get_res_type(self) and set_res_type(self, new_type) has passed.")
except:
    AssertionError
    print("The test of fuctions get_res_type(self)and set_res_type(self, new_type) has failed.")    

try:
    PRO.set_res_type("PRO")
    assert PRO.get_res_type() == "PRO"
    print("The test of fuctions get_res_type(self) and set_res_type(self, new_type) has passed.")
except:
    AssertionError
    print("The test of fuctions get_res_type(self)and set_res_type(self, new_type) has failed.")    

# check get_res_number(self)
try:
    assert PRO.get_res_number() == 1
    print("The test of function get_res_number(self) has passed.")
except:
    AssertionError
    print("The test of function get_res_number(self) has failed.")

# check get_backone(self)
try:
    names= []; coords= []
    for i in PRO.get_backbone().keys():
        names.append((PRO.get_backbone()[i]).get_name())
        coords.append((PRO.get_backbone()[i]).get_coords())
    assert set(names) == {"N","C","CA","O"} and set(coords) == {(5.284,12.009,1.177),
                                                                (5.918, 10.123,-0.175),
                                                                (5.865, 10.943,1.122),
                                                                (4.524,9.887,-0.667)}
    print("The test of function get_backbone(self) has passed.")
except:
    AssertionError
    print ("The test of function get_backbone(self) has failed.")
    
# check get_side_chain(self)
try:
    names= []; coords= []
    for i in PRO.get_side_chain().keys():
        names.append((PRO.get_side_chain()[i]).get_name())
        coords.append((PRO.get_side_chain()[i]).get_coords())
    assert set(names) == {"CB","CG","CD","H","H3","HA","HB2","HB3","HG2","HG3","HD2","HD3"} \
        and set(coords) == {(6.697,10.871,-1.278),(5.715,11.124,-2.430),(4.108, 9.707,-2.734),
                            (4.374, 10.484,-2.030),(4.341,8.86,-0.711), (3.846, 10.334,-0.018),
                            (6.393, 9.171, 0.029),(7.081,11.812,-0.901),(7.520,10.262,-1.629),
                            (5.590,12.191,-2.583),(6.081,10.668, -3.341),(3.596,11.236, -2.011)}                                                            
    print("The test of function get_side_chain(self) has passed.")
except:
    AssertionError
    print ("The test of function get_side_chain(self) has failed.")

# check set_side_chain(self)
try:
    PRO.set_side_chain({"CB": CB, "CG": CG, "CD": CD})
    names= []; coords= []
    for i in PRO.get_side_chain().keys():
        names.append((PRO.get_side_chain()[i]).get_name())
        coords.append((PRO.get_side_chain()[i]).get_coords())
    assert set(names) == {"CB","CG","CD"} and \
        set(coords) == {(6.697,10.871,-1.278),(5.715,11.124,-2.430),(4.374, 10.484,-2.030)}
    print("The test of function set_side_chain(self) has passed.")
except:
    AssertionError
    print("The test of function set_side_chain(self) has failed.")

# check add_atom(self, atom)
try:
    names= []; coords= []
    PRO.add(HD3)
    for i in PRO.get_backbone().keys():
        names.append((PRO.get_backbone()[i]).get_name())
        coords.append((PRO.get_backbone()[i]).get_coords())
    assert set(names) == {"CB","CG","CD","HD3"} and \
        set(coords) == {(6.697,10.871,-1.278),(5.715,11.124,-2.430),(4.374, 10.484,-2.030),
                        (4.108, 9.707,-2.734)}
    print("The test of function add(self,atom) has passed.")
except:
    AssertionError
    print("The test of function add(self,atom) has failed.")

# check string representation of object AminoAcid
try:
    assert str((PRO)) == "Amino acid number 1 of type PRO with a list of 5 atoms"
    print("The test of string representation of object AminoAcid has passed.")
except:
    AssertionError
    print("The test of string representation of object AminoAcid has failed.")


