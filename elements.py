elements = {
    'H': {'size': 0.1, 'color': (1.0, 0.0, 0.0)},        # Red
    'He': {'size': 0.1, 'color': (1.0, 0.5, 0.0)},       # Orange
    'Li': {'size': 0.1, 'color': (1.0, 1.0, 0.0)},       # Yellow
    'Be': {'size': 0.1, 'color': (0.5, 1.0, 0.0)},       # Yellow-Green
    'B': {'size': 0.1, 'color': (0.0, 1.0, 0.0)},        # Green
    'C': {'size': 0.1, 'color': (0.0, 1.0, 0.5)},        # Green-Cyan
    'N': {'size': 0.1, 'color': (0.0, 1.0, 1.0)},        # Cyan
    'O': {'size': 0.1, 'color': (0.0, 0.5, 1.0)},        # Cyan-Blue
    'F': {'size': 0.1, 'color': (0.0, 0.0, 1.0)},        # Blue
    'Ne': {'size': 0.1, 'color': (0.5, 0.0, 1.0)},       # Blue-Magenta
    'Na': {'size': 0.1, 'color': (1.0, 0.0, 1.0)},       # Magenta
    'Mg': {'size': 0.1, 'color': (1.0, 0.0, 0.5)},       # Magenta-Red
    'Al': {'size': 0.1, 'color': (0.5, 0.5, 0.5)},       # Gray
    'Si': {'size': 0.1, 'color': (0.5, 0.25, 0.25)},     # Brown
    'P': {'size': 0.1, 'color': (1.0, 1.0, 0.5)},        # Light Yellow
    'S': {'size': 0.1, 'color': (1.0, 0.75, 0.25)},      # Light Orange
    'Cl': {'size': 0.1, 'color': (0.0, 0.5, 0.0)},       # Dark Green
    'Ar': {'size': 0.1, 'color': (0.5, 1.0, 1.0)},       # Light Cyan
    'K': {'size': 0.1, 'color': (0.5, 0.0, 0.5)},        # Dark Magenta
    'Ca': {'size': 0.1, 'color': (0.75, 0.75, 0.75)},    # Light Gray
    'Sc': {'size': 0.1, 'color': (0.0, 0.5, 0.5)},       # Dark Cyan
    'Ti': {'size': 0.1, 'color': (0.5, 0.5, 0.0)},       # Dark Yellow
    'V': {'size': 0.1, 'color': (0.75, 0.25, 0.0)},      # Reddish Brown
    'Cr': {'size': 0.1, 'color': (0.0, 0.75, 0.75)},     # Light Green-Cyan
    'Mn': {'size': 0.1, 'color': (0.5, 0.0, 0.25)},      # Dark Reddish Magenta
    'Fe': {'size': 0.1, 'color': (1.0, 0.5, 0.5)},       # Light Reddish Brown
    'Co': {'size': 0.1, 'color': (0.0, 0.5, 0.75)},      # Dark Blue-Cyan
    'Ni': {'size': 0.1, 'color': (0.5, 0.25, 0.75)},     # Dark Violet
    'Cu': {'size': 0.1, 'color': (1.0, 0.75, 0.5)},      # Light Orange-Yellow
    'Zn': {'size': 0.1, 'color': (0.5, 0.5, 1.0)},       # Light Blue-Violet
    'Ga': {'size': 0.1, 'color': (0.75, 0.75, 1.0)},     # Very Light Blue
    'Ge': {'size': 0.1, 'color': (0.5, 0.5, 0.25)},      # Dark Yellow-Gray
    'As': {'size': 0.1, 'color': (0.5, 0.25, 0.5)},      # Dark Gray-Magenta
    'Se': {'size': 0.1, 'color': (1.0, 0.75, 0.75)},     # Light Reddish Pink
    'Br': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},       # Dark Red
    'Kr': {'size': 0.1, 'color': (0.0, 0.0, 0.5)},       # Dark Blue
    'Rb': {'size': 0.1, 'color': (0.75, 0.0, 1.0)},      # Violet-Red
    'Sr': {'size': 0.1, 'color': (0.75, 0.0, 0.75)},     # Dark Pink
    'Y': {'size': 0.1, 'color': (0.25, 0.25, 0.25)},     # Dark Gray
    'Zr': {'size': 0.1, 'color': (0.75, 0.75, 0.25)},    # Light Yellow-Gray
    'Nb': {'size': 0.1, 'color': (0.25, 0.25, 0.5)},     # Dark Blue-Gray
    'Mo': {'size': 0.1, 'color': (0.25, 0.5, 0.25)},     # Dark Green-Gray
    'Tc': {'size': 0.1, 'color': (0.75, 0.25, 0.5)},     # Light Violet-Magenta
    'Ru': {'size': 0.1, 'color': (0.5, 0.25, 1.0)},      # Light Blue-Violet
    'Rh': {'size': 0.1, 'color': (0.75, 0.25, 0.75)},    # Light Pink-Magenta
    'Pd': {'size': 0.1, 'color': (0.25, 0.5, 0.5)},      # Light Green-Cyan
    'Ag': {'size': 0.1, 'color': (1.0, 0.75, 1.0)},      # Light Pink
    'Cd': {'size': 0.1, 'color': (0.5, 0.5, 0.5)},       # Gray
    'In': {'size': 0.1, 'color': (0.75, 0.75, 1.0)},     # Very Light Blue
    'Sn': {'size': 0.1, 'color': (0.75, 0.5, 0.5)},      # Light Red-Gray
    'Sb': {'size': 0.1, 'color': (0.75, 0.5, 0.25)},     # Light Orange-Gray
    'Te': {'size': 0.1, 'color': (0.5, 0.75, 0.5)},      # Light Green-Gray
    'I': {'size': 0.1, 'color': (0.5, 0.0, 0.75)},       # Dark Magenta
    'Xe': {'size': 0.1, 'color': (0.0, 0.75, 0.5)},      # Light Green-Cyan
    'Cs': {'size': 0.1, 'color': (0.25, 0.0, 0.5)},      # Dark Blue-Magenta
    'Ba': {'size': 0.1, 'color': (0.75, 0.5, 0.0)},      # Orange-Brown
    'La': {'size': 0.1, 'color': (0.5, 0.75, 1.0)},      # Light Blue
    'Ce': {'size': 0.1, 'color': (0.75, 0.75, 0.5)},     # Light Yellow
    'Pr': {'size': 0.1, 'color': (0.5, 0.5, 0.75)},      # Light Gray-Blue
    'Nd': {'size': 0.1, 'color': (0.75, 0.5, 0.75)},     # Light Pink
    'Pm': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},       # Dark Red
    'Sm': {'size': 0.1, 'color': (0.0, 0.5, 0.0)},       # Dark Green
    'Eu': {'size': 0.1, 'color': (0.0, 0.0, 0.5)},       # Dark Blue
    'Gd': {'size': 0.1, 'color': (0.5, 0.0, 0.5)},       # Dark Magenta
    'Tb': {'size': 0.1, 'color': (0.75, 0.75, 0.0)},     # Light Yellow
    'Dy': {'size': 0.1, 'color': (0.0, 0.75, 0.75)},     # Light Cyan
    'Ho': {'size': 0.1, 'color': (0.5, 0.25, 0.25)},     # Brown
    'Er': {'size': 0.1, 'color': (0.75, 0.5, 0.25)},     # Light Brown
    'Tm': {'size': 0.1, 'color': (0.25, 0.75, 0.5)},     # Light Green-Gray
    'Yb': {'size': 0.1, 'color': (0.75, 0.25, 0.5)},     # Light Magenta
    'Lu': {'size': 0.1, 'color': (0.5, 0.5, 0.25)},      # Dark Yellow-Gray
    'Hf': {'size': 0.1, 'color': (0.25, 0.25, 0.75)},    # Dark Blue-Gray
    'Ta': {'size': 0.1, 'color': (0.75, 0.5, 0.0)},      # Orange-Brown
    'W': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},        # Dark Red
    'Re': {'size': 0.1, 'color': (0.0, 0.5, 0.0)},       # Dark Green
    'Os': {'size': 0.1, 'color': (0.0, 0.0, 0.5)},       # Dark Blue
    'Ir': {'size': 0.1, 'color': (0.5, 0.0, 0.5)},       # Dark Magenta
    'Pt': {'size': 0.1, 'color': (0.75, 0.75, 0.75)},    # Light Gray
    'Au': {'size': 0.1, 'color': (1.0, 0.75, 0.0)},      # Gold
    'Hg': {'size': 0.1, 'color': (0.75, 0.75, 1.0)},     # Light Blue
    'Tl': {'size': 0.1, 'color': (0.75, 0.25, 0.25)},    # Light Red-Brown
    'Pb': {'size': 0.1, 'color': (0.5, 0.5, 0.5)},       # Gray
    'Bi': {'size': 0.1, 'color': (0.75, 0.75, 0.5)},     # Light Yellow
    'Po': {'size': 0.1, 'color': (0.5, 0.25, 0.75)},     # Light Magenta
    'At': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},       # Dark Red
    'Rn': {'size': 0.1, 'color': (0.0, 0.5, 0.5)},       # Dark Cyan
    'Fr': {'size': 0.1, 'color': (0.75, 0.0, 1.0)},      # Violet-Red
    'Ra': {'size': 0.1, 'color': (0.75, 0.75, 0.0)},     # Light Yellow
    'Ac': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},       # Dark Red
    'Th': {'size': 0.1, 'color': (0.0, 0.5, 0.0)},       # Dark Green
    'Pa': {'size': 0.1, 'color': (0.0, 0.0, 0.5)},       # Dark Blue
    'U': {'size': 0.1, 'color': (0.5, 0.0, 0.5)},        # Dark Magenta
    'Np': {'size': 0.1, 'color': (0.75, 0.5, 0.0)},      # Orange-Brown
    'Pu': {'size': 0.1, 'color': (0.5, 0.25, 0.25)},     # Brown
    'Am': {'size': 0.1, 'color': (0.5, 0.5, 0.5)},       # Gray
    'Cm': {'size': 0.1, 'color': (0.25, 0.75, 0.5)},     # Light Green-Gray
    'Bk': {'size': 0.1, 'color': (0.75, 0.25, 0.5)},     # Light Magenta
    'Cf': {'size': 0.1, 'color': (0.5, 0.0, 0.0)},       # Dark Red
    'Es': {'size': 0.1, 'color': (0.0, 0.5, 0.0)},       # Dark Green
    'Fm': {'size': 0.1, 'color': (0.0, 0.0, 0.5)},       # Dark Blue
    'Md': {'size': 0.1, 'color': (0.5, 0.0, 0.5)},       # Dark Magenta
    'No': {'size': 0.1, 'color': (0.75, 0.75, 0.0)},     # Light Yellow
    'Lr': {'size': 0.1, 'color': (0.75, 0.5, 0.0)},      # Orange-Brown
    'Rf': {'size': 0.1, 'color': (0.75, 0.0, 0.75)},     # Dark Pink
    'Db': {'size': 0.1, 'color': (0.25, 0.25, 0.25)},    # Dark Gray
    'Sg': {'size': 0.1, 'color': (0.75, 0.75, 0.25)},    # Light Yellow-Gray
    'Bh': {'size': 0.1, 'color': (0.25, 0.25, 0.5)},     # Dark Blue-Gray
    'Hs': {'size': 0.1, 'color': (0.25, 0.5, 0.25)},     # Dark Green-Gray
    'Mt': {'size': 0.1, 'color': (0.75, 0.25, 0.5)},     # Light Magenta
    'Ds': {'size': 0.1, 'color': (0.5, 0.25, 1.0)},      # Light Blue-Violet
    'Rg': {'size': 0.1, 'color': (0.75, 0.25, 0.75)},    # Light Pink-Magenta
    'Cn': {'size': 0.1, 'color': (0.25, 0.5, 0.5)},      # Light Green-Cyan
    'Nh': {'size': 0.1, 'color': (1.0, 0.75, 1.0)},      # Light Pink
    'Fl': {'size': 0.1, 'color': (0.5, 0.5, 0.5)},       # Gray
    'Mc': {'size': 0.1, 'color': (0.75, 0.75, 1.0)},     # Very Light Blue
    'Lv': {'size': 0.1, 'color': (0.75, 0.5, 0.5)},      # Light Red-Gray
    'Ts': {'size': 0.1, 'color': (0.75, 0.5, 0.25)},     # Light Orange-Gray
    'Og': {'size': 0.1, 'color': (0.5, 0.75, 0.5)},      # Light Green-Gray
}