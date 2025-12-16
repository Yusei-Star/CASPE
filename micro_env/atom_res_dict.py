res_atom_type_dict={
'GLY':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA1', 'HA2', 'HA3', 'H2', 'H3', 'OXT'], 
'CYS':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'SG', 'HG', 'HG1', 'H2', 'H3', 'OXT'],
'ARG':['O', 'C', 'N', 'H', 'CA', 'HA', 'HN', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'NE', 'HE', 'CZ', 'NH1', 'HH11', 'HH12', 'NH2', 'HH21', 'HH22', 'H2', 'H3', 'H11', 'H12', 'OXT'],
'SER':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'OG', 'HG', 'H2', 'H3', 'OXT'],
'THR':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'OG1', 'HG1', 'CG2', 'HG21', 'HG22', 'HG23', 'H2', 'H3', 'OXT'],
'LYS':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'CE', 'HE1', 'HE2', 'HE3', 'NZ', 'HZ1', 'HZ2', 'HZ3', 'H2', 'H3', 'OXT'],
'MET':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'SD', 'CE', 'HE1', 'HE2', 'HE3', 'H2', 'H3', 'OXT'],
'ALA':['O', 'N', 'C', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'H2', 'H3', 'OXT'],
'LEU':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG', 'CD1', 'CD2', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23', 'H2', 'H3', 'OXT'],
'ILE':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'CD', 'CD1', 'HD1', 'HD2', 'HD3', 'CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23', 'HD11', 'HD12', 'HD13', 'H2', 'H3', 'OXT'],
'VAL':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23', 'H2', 'H3', 'OXT'],
'ASP':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'CG', 'OD1', 'OD2', 'H2', 'H3', 'HB3', 'OXT'],
'GLU':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'OE1', 'OE2', 'H2', 'H3', 'OXT'],
'HIS':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'ND1', 'CD2', 'CE1', 'NE2', 'HD1', 'HD2', 'HE1', 'HE2', 'H2', 'H3', 'OXT'],
'ASN':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'OD1', 'ND2', 'HD21', 'HD22', 'H2', 'H3', 'OXT'],
'PRO':['O', 'C', 'N', 'H', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'H2', 'H3', 'OXT'],
'GLN':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'OE1', 'NE2', 'HE21', 'HE22', 'H2', 'H3', 'OXT'],
'PHE':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CZ', 'HZ', 'CE1', 'HE1', 'CE2', 'HE2', 'H2', 'H3', 'OXT'],
'TRP':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'NE1', 'HE1', 'CE2', 'CE3', 'HE3', 'CZ2', 'HZ2', 'CZ3', 'HZ3', 'CH2', 'HH2', 'H2', 'H3', 'OXT'],
'TYR':['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CE1', 'HE1', 'CE2', 'HE2', 'CZ', 'OH', 'HH', 'H2', 'H3', 'OXT']
}

label_atom_type_dict={
18:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA1', 'HA2', 'HA3', 'H2', 'H3', 'OXT']), 
19:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'SG', 'HG', 'HG1', 'H2', 'H3', 'OXT']),
2:set(['O', 'C', 'N', 'H', 'CA', 'HA', 'HN', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'NE', 'HE', 'CZ', 'NH1', 'HH11', 'HH12', 'NH2', 'HH21', 'HH22', 'H2', 'H3', 'H11', 'H12', 'OXT']),
5:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'OG', 'HG', 'H2', 'H3', 'OXT']),
6:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'OG1', 'HG1', 'CG2', 'HG21', 'HG22', 'HG23', 'H2', 'H3', 'OXT']),
1:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'CE', 'HE1', 'HE2', 'HE3', 'NZ', 'HZ1', 'HZ2', 'HZ3', 'H2', 'H3', 'OXT']),
13:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'SD', 'CE', 'HE1', 'HE2', 'HE3', 'H2', 'H3', 'OXT']),
9:set(['O', 'N', 'C', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'H2', 'H3', 'OXT']),
11:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG', 'CD1', 'CD2', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23', 'H2', 'H3', 'OXT']),
12:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'CD', 'CD1', 'HD1', 'HD2', 'HD3', 'CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23', 'HD11', 'HD12', 'HD13', 'H2', 'H3', 'OXT']),
10:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB', 'CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23', 'H2', 'H3', 'OXT']),
3:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'CG', 'OD1', 'OD2', 'H2', 'H3', 'HB3', 'OXT']),
4:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'OE1', 'OE2', 'H2', 'H3', 'OXT']),
0:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'ND1', 'CD2', 'CE1', 'NE2', 'HD1', 'HD2', 'HE1', 'HE2', 'H2', 'H3', 'OXT']),
7:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'OD1', 'ND2', 'HD21', 'HD22', 'H2', 'H3', 'OXT']),
17:set(['O', 'C', 'N', 'H', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'HD1', 'HD2', 'HD3', 'H2', 'H3', 'OXT']),
8:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'HG1', 'HG2', 'HG3', 'CD', 'OE1', 'NE2', 'HE21', 'HE22', 'H2', 'H3', 'OXT']),
14:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CZ', 'HZ', 'CE1', 'HE1', 'CE2', 'HE2', 'H2', 'H3', 'OXT']),
16:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'NE1', 'HE1', 'CE2', 'CE3', 'HE3', 'CZ2', 'HZ2', 'CZ3', 'HZ3', 'CH2', 'HH2', 'H2', 'H3', 'OXT']),
15:set(['O', 'C', 'N', 'H', 'HN', 'CA', 'HA', 'CB', 'HB1', 'HB2', 'HB3', 'CG', 'CD1', 'HD1', 'CD2', 'HD2', 'CE1', 'HE1', 'CE2', 'HE2', 'CZ', 'OH', 'HH', 'H2', 'H3', 'OXT'])
}
res_group_dict={
    0:'group1',1:'group1',2:'group1',
    3:'group2',4:'group2',
    5:'group3',6:'group3',7:'group3',8:'group3',
    9:'group4',10:'group4',11:'group4',12:'group4',13:'group4',
    14:'group5',15:'group5',16:'group5',
    17:'group6',18:'group6',
    19:'group7'
    }

peptide_bond_energy=float(615+305)/2

AA_bond_dict={
'GLY':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
},

'CYS':{ 
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','SG'):259,
},

'ARG':{ 
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD'):347,
('CD','NE'):305,
('NE','CZ'):305,
('CZ','NH1'):305,
('CZ','NH2'):615,
},

'SER':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','OG'):358,
},

'THR':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','OG1'):358,
('CB','CG2'):347,
},

'LYS':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD'):347,
('CD','CE'):347,
('CE','NZ'):305,
},

'MET':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','SD'):259,
('SD','CE'):259,
},

'ALA':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
},

'LEU':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD1'):347,
('CG','CD2'):347
},

'ILE':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG1'):347,
('CB','CG2'):347,
('CG1','CD1'):347,
},

'VAL':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG1'):347,
('CB','CG2'):347,
},

'ASP':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','OD1'):745,
('CG','OD2'):358
},

'GLU':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD'):347,
('CD','OE1'):745,
('CD','OE2'):358
},

'HIS':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','ND1'):305,
('ND1','CE1'):615,
('CE1','NE2'):305,
('NE2','CD2'):305,
('CD2','CG'):614,
},

'ASN':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','OD1'):745,
('CG','ND2'):305
},

'PRO':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD'):347,
('CD','N'):305
},

'GLN':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD'):347,
('CD','OE1'):745,
('CD','NE2'):305
},

'PHE':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD1'):614,
('CD1','CE1'):347,
('CE1','CZ'):614,
('CZ','CE2'):347,
('CE2','CD2'):614,
('CD2','CG'):347,
},

'TRP':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD1'):614,
('CD1','NE1'):305,
('NE1','CE2'):305,
('CE2','CD2'):614,
('CD2','CG'):305,
('CE2','CZ2'):347,
('CZ2','CH2'):614,
('CH2','CZ3'):347,
('CZ3','CE3'):614,
('CE3','CD2'):347,
},

'TYR':{
('N','CA'):305,
('CA','C'):347,
('C','O'):745,
('CA','CB'):347,
('CB','CG'):347,
('CG','CD1'):614,
('CD1','CE1'):347,
('CE1','CZ'):614,
('CZ','OH'):358,
('CZ','CE2'):347,
('CE2','CD2'):614,
('CD2','CG'):347,
}

}


res_name_dict={'HIS','LYS','ARG','ASP','GLU','SER','THR','ASN','GLN','ALA','VAL','LEU','ILE','MET','PHE','TYR','TRP','PRO','GLY', 'CYS'}

label_res_dict={0:'HIS',1:'LYS',2:'ARG',3:'ASP',4:'GLU',5:'SER',6:'THR',7:'ASN',8:'GLN',9:'ALA',10:'VAL',11:'LEU',12:'ILE',13:'MET',14:'PHE',15:'TYR',16:'TRP',17:'PRO',18:'GLY',19:'CYS', 20:'HOH', 21:'DG', 22:'MG', 23:'DA', 24:'DC',25:'DT'}
res_label_dict={'HIS':0,'LYS':1,'ARG':2,'ASP':3,'GLU':4,'SER':5,'THR':6,'ASN':7,'GLN':8,'ALA':9,'VAL':10,'LEU':11,'ILE':12,'MET':13,'PHE':14,'TYR':15,'TRP':16,'PRO':17,'GLY':18,'CYS':19,'HOH':20, 'DG':21,'MG':22, 'DA':23, 'DC':24, 'DT':25}

amino_acid_3_to_1={'HIS':'H','LYS':'K','ARG':'R','ASP':'D','GLU':'E','SER':'S','THR':'T','ASN':'N','GLN':'Q','ALA':'A','VAL':'V','LEU':'L','ILE':'I','MET':'M','PHE':'F','TYR':'Y','TRP': 'W','PRO': 'P','GLY': 'G', 'CYS': 'C'}
amino_acid_1_to_3={'H':'HIS','K':'LYS','R':'ARG','D':'ASP','E':'GLU','S':'SER','T':'THR','N':'ASN','Q':'GLN','A':'ALA','V':'VAL','L':'LEU','I':'ILE','M':'MET','F':'PHE','Y':'TYR','W':'TRP','P':'PRO','G':'GLY','C':'CYS'}
