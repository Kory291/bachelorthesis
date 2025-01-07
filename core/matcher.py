import parse_into_graph
import networkx as nx 

musterloesung = """mermaid
    flowchart
    subgraph SG1 [ ]
        Produzent---P1(["`<ins>ProdId</ins>`"])
        Produzent---P2([Name])
        Produzent---P3(((Zertifikate)))
    end
    subgraph SG2 [ ]
        Bauteil---B1(["`<ins>Name</ins>`"])
        Bauteil---B2([Gewicht])
        Bauteil---B3([Größe])
        B3([Größe])---B4([Länge])
        B3([Größe])---B5([Breite])
        B3([Größe])---B6([Höhe])
    end
    subgraph SG3 [ ]
        Produzent--(1,*)---herstellen{herstellen}
        herstellen{herstellen}--(1,1)---Bauteil 
        herstellen{herstellen}---H1([Jahr])
        Bauteil--(0,*)---bestehen_aus{bestehen_aus}
        bestehen_aus{bestehen_aus}--(0,*)---Bauteil
    end    
    style SG1 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
    style SG2 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
    style SG3 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
"""
studentische_loesung = """mermaid
flowchart
    subgraph SG1 [ ]
        Produzent---P1(["`<ins>ProdId</ins>`"])
        Produzent---P3(((Zertifikate)))
    end
    subgraph SG2 [ ]
        Bauteil---B1(["`<ins>Name</ins>`"])
        Bauteil---B2([Gewicht])
        Bauteil---B3([Größe])
        Bauteil---B7([Farbe])
        B3([Größe])---B4([Länge])
        B3([Größe])---B5([Breite])
        B3([Größe])---B6([Höhe])
    end
    subgraph SG3 [ ]
        Produzent--(1,*)---bauen{bauen}
        bauen{bauen}--(1,1)---Bauteil 
        bauen{bauen}---H1([Jahr])
        Bauteil--(2,3)---bestehen_aus{bestehen_aus}
        bestehen_aus{bestehen_aus}--(0,*)---Bauteil
    end    
    style SG1 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
    style SG2 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
    style SG3 fill:#ff0000,fill-opacity:0.0,stroke:#333,stroke-width:0px
    style herstellen fill:#ff0000,stroke:#333,stroke-width:0px
    style P2 fill:#ffff00, stroke:#333,stroke-width:0px
    style B7 fill:#0000ff, stroke:#333,stroke-width:0px
"""
# studentische_loesung = musterloesung
musterloesung_sortiert = parse_into_graph.alhabetisch_sortieren(musterloesung)
studentische_loesung_sortiert = parse_into_graph.alhabetisch_sortieren(studentische_loesung)

muster_graph = parse_into_graph.parse_mermaid_text(musterloesung_sortiert)
studenten_graph = parse_into_graph.parse_mermaid_text(studentische_loesung_sortiert)

def compare_graphs(muster_graph, studenten_graph):
    fehler = {
        # Fehler bei Knoten
        "fehlende_Knoten": [],
        "extra_Knoten": [],
        # "falsche_Knoten": [], # typabweichung, falscher Name. semantischer Fehler
        "falscher_Typ_Knoten": [], 
        "falscher_Name_Knoten":[], # label
        # "semantischer_Fehler": [],
        # Fehler bei Kanten
        "fehlende_Kanten": [],
        "extra_Kanten": [],
        "falsche_Kanten": [] # Kardinalität, Beziehung
    }
    fehler_visualisierung= {
        "fehlende_Knoten_Info": [],
        "extra_Knoten_gelb": [],
        "falscher_Typ_Knoten_rot": [],
        "falscher_Name_Knoten_rot": [],
        "fehlende_Kanten_Info": [],
        "extra_Kanten_gelb": [],
        "falsche_Kanten_rot": []
    }

# Hinzufügen von fehlenden Kanten und Knoten auf der Fehlerliste
    for node, data in muster_graph.nodes(data=True): 
        if studenten_graph.__contains__(node) == False:
            fehler["fehlende_Knoten"].append(node)
            fehler_visualisierung["fehlende_Kanten_Info"].append(f"Fehler_Kanten[Fehler: \n Es fehlen noch Beziehungen zwischen Enitäten, Attributen oder Relationships.]\n fill:#fde2e1,stroke:#b91c1c,stroke-width:2p ")
            for knoten, daten in studenten_graph.nodes(data=True):
                # wenn alle Kanten von node und Knoten gleich sind, dann Fehler für falscher_Name_Knoten
                # print(list(studenten_graph.neighbors(knoten)))
                if muster_graph.__contains__(knoten) == False:
                    # print(f"test test {knoten} und und {node}")
                    musterloesung_neighbors= list(muster_graph.neighbors(node))
                    musterloesung_predecessors = list(muster_graph.predecessors(node))
                    studenten_graph_neighbors= list(studenten_graph.neighbors(knoten))
                    studenten_graph_predecessors = list(studenten_graph.predecessors(knoten))
                    if data == daten and sorted(musterloesung_neighbors) == sorted(studenten_graph_neighbors) and sorted(musterloesung_predecessors)==sorted(studenten_graph_predecessors):
                        fehler["falscher_Name_Knoten"].append(f"Muster: {node} ist gemeint mit: {knoten}")
                        fehler_visualisierung["falscher_Name_Knoten_rot"].append(f"style {knoten} fill:#F4CCCC,stroke:#CC0000,stroke-width:2px ")

    for edge1, edge2, data in muster_graph.edges(data=True):
        if studenten_graph.has_edge(edge1,edge2) == False: 
            fehler["fehlende_Kanten"].append(edge1 + " zu " + edge2)
            # fehler_visualisierung["extra_Kanten_gelb"].append(f"style {}") wie passe ich nur die Kante an? woher weiß ich welche Kante das ist?

# Hinzufügen von zusätzlichen Knoten und Kanten auf der Fehlerliste
    for node, data in studenten_graph.nodes(data=True): 
        if muster_graph.__contains__(node) == False:
            # if muster_graph.get_node_data():
            fehler["extra_Knoten"].append(node)
            fehler_visualisierung["extra_Knoten_gelb"].append(f"style {node} fill:#d9eaf7,stroke:#045a8d,stroke-width:2px")
    for edge1, edge2, data in studenten_graph.edges(data=True):
        if muster_graph.has_edge(edge1, edge2) == False: 
            fehler["extra_Kanten"].append(edge1 + " zu " + edge2)
            # fehler_visualisierung für Kanten --> welche kante ist das? 

# Hinzufügen von faschen Knoten und Kanten auf der Fehlerliste 
    for node, data in muster_graph.nodes(data=True):
        blabla = node, data
        # if  value not in studenten_graph.nodes(data=True):
        #     print(value) 
        if node in studenten_graph.nodes(): 
            musterloesung_data = data 
            studentenloesung_data = studenten_graph.nodes[node]
            for key, value in musterloesung_data.items():
                if key == "type": 
                    if studentenloesung_data[key] != value: 
                        fehler["falscher_Typ_Knoten"].append("Muster: " + str(blabla) + "Studentische Lösung: " + studentenloesung_data.get(key, None))
                        fehler_visualisierung["falscher_Typ_Knoten_rot"].append(f"style {node} fill:#F4CCCC,stroke:#CC0000,stroke-width:2px") 
                if key == "label": 
                    if studentenloesung_data[key] != value: 
                        fehler["falscher_Name_Knoten"].append("Muster: " + str(blabla) + "Studentische Lösung: " + studentenloesung_data.get(key, None))
                        fehler_visualisierung["falscher_Name_Knoten_rot"].append(f"style {node} fill:#F4CCCC,stroke:#CC0000,stroke-width:2px")
                # if key not in studentenloesung_data or studentenloesung_data[key] != value:
                #     # print(key)
                #     # print(value)
                #     if key == "type":
                #         fehler["falscher_Typ_Knoten"].append("Muster: " + str(blabla) + "Studentische Lösung: " + studentenloesung_data.get(key, None))
                #     if key == "label":
                #         fehler["falscher_Name_Knoten"].append("Muster: " + str(blabla) + "Studentische Lösung: " + studentenloesung_data.get(key, None))
    for edge1, edge2, data in muster_graph.edges(data=True): 
        for u, v, dataaa in studenten_graph.edges(data=True): 
            if (u,v) == (edge1, edge2): 
                if data != dataaa:                             
                    fehler["falsche_Kanten"].append(f"Muster: {edge1} zu {edge2} mit {data}, Studentische Lösung: {dataaa}")
                # for key, value in data.items(): 
                #     if dataaa.items() != data.items(): 
                #         print(data.items())
                #         print(dataaa.items())

    print(fehler)
    print(fehler_visualisierung)
    # print(f"Knoten in muster_graph: {muster_graph.nodes(data=True)}")
    # print(f"Kanten in muster_graph: {muster_graph.edges(data=True)}")
    # print(muster_graph.nodes(data=True))
    # print(studenten_graph.nodes(data=True))
    # print(muster_graph.get_node_data())
    # print(nx.vf2pp_isomorphism(muster_graph, studenten_graph, node_label="type"))
    # print(nx.vf2pp_all_isomorphisms(muster_graph, studenten_graph, node_label=None))

compare_graphs(muster_graph, studenten_graph)
