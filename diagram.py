import os

# Ajouter le chemin de Graphviz à la variable PATH
os.environ["PATH"] += os.pathsep + '/opt/homebrew/bin'

# Contenu du fichier DOT avec paramètres de mise en page
dot_content = """
graph WBS {
    rankdir=TB;  // Organise de haut en bas
    nodesep=0.4; // Réduit l'espacement entre les nœuds
    ranksep=0.5; // Réduit l'espacement entre les rangs
    node [shape=rect, style=filled, fontsize=10]; // Utilise des boîtes rectangulaires

    // Couleurs pour chaque colonne
    "0" [label="Projet Freshstart", fillcolor=lightblue];
    "1" [label="Gestion de projet", fillcolor=lightyellow];
    "2" [label="Implémentation du système SAP", fillcolor=lightgreen];
    "3" [label="Gestion du changement", fillcolor=lightcoral];
    "4" [label="Infrastructure technologique", fillcolor=lightskyblue];

    // Nœuds de chaque colonne
    "1.1" [label="Planification", fillcolor=lightyellow];
    "1.2" [label="Surveillance et contrôle", fillcolor=lightyellow];
    "1.3" [label="Clôture de projet", fillcolor=lightyellow];
    "2.1" [label="Analyse des besoins", fillcolor=lightgreen];
    "2.2" [label="Conception du système", fillcolor=lightgreen];
    "2.3" [label="Développement et configuration", fillcolor=lightgreen];
    "2.4" [label="Test du système", fillcolor=lightgreen];
    "2.5" [label="Déploiement", fillcolor=lightgreen];
    "3.1" [label="Communication", fillcolor=lightcoral];
    "3.2" [label="Formation", fillcolor=lightcoral];
    "3.3" [label="Support post-implémentation", fillcolor=lightcoral];
    "4.1" [label="Mise à niveau du matériel", fillcolor=lightskyblue];
    "4.2" [label="Sécurité des données", fillcolor=lightskyblue];
    "4.3" [label="Maintenance du système", fillcolor=lightskyblue];

    // Relations entre les nœuds sans flèches
    "0" -- "1" -- "1.1";
    "1" -- "1.2";
    "1" -- "1.3";
    "0" -- "2" -- "2.1";
    "2" -- "2.2";
    "2" -- "2.3";
    "2" -- "2.4";
    "2" -- "2.5";
    "0" -- "3" -- "3.1";
    "3" -- "3.2";
    "3" -- "3.3";
    "0" -- "4" -- "4.1";
    "4" -- "4.2";
    "4" -- "4.3";
}
"""

# Écrire le contenu DOT dans un fichier
with open("wbs_diagram.dot", "w") as file:
    file.write(dot_content)

# Utiliser l'exécutable dot pour rendre le fichier DOT en PNG
os.system('dot -Tpng wbs_diagram.dot -o wbs_diagram.png')
