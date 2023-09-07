import argparse
from PDBStructure import StructurePDB
from Clustering import Kmeans, DBscan
from ClusteringMeasures import ClusteringMeasures
from plot import draw_plot

if __name__ == "__main__":
    #####################PARSING ARGUMENT###############################
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-k", "--kmeans", metavar="k", action="store", default=3, help="Use Kmeans for clustering")
    argparser.add_argument("-d", "--dbscan", metavar=("epsilon","min_points"), nargs=2, help="Use DBscan for clustering")
    #argparser.add_argument("-chi", metavar="AA", nargs=1, help="Calculate Chi1 and Chi2 angles for <AA> amino acid")
    argparser.add_argument("-o", "--output", action="store", metavar="file_prefix", help="Output the models Phi and Psi angles in tabulated files")
    argparser.add_argument("--noplot", action="store_true", help="Don't render a plot")
    argparser.add_argument("--nomeasure", action="store_true", help="Don't print measures")
    argparser.add_argument("file", metavar="file", action="store", help="PDB file that contains at least one model")

    #argparser.usage = "daa.py [-k k] [-d epsilon min_points] --phipsi [-o output_prefix]"
    args = argparser.parse_args()
    
    models = StructurePDB.readPDB(args.file) 
    for i in range(len(models)):
        phipsi = models[i].compute_dihedrals()

        points = list(zip(*phipsi))
        points = points[1:-1]
        if args.dbscan:
            clustering = DBscan(points, *list(map(float, args.dbscan)))
            window_title = "DBscan clustering"
        else:
            clustering = Kmeans(points, int(args.kmeans))
            window_title = "Kmeans clustering"

        cp = clustering.getClusterPoints()
        if not args.nomeasure:
            measures = ClusteringMeasures(cp)
            print(f"#### Modèle {i+1} ####")
            print("Silhouette coefficient", measures.coefficient_silhouette())
            print("Dunn score:", measures.indice_dunn())
            print("Dunn score (using centroids):", measures.indice_dunn(True))
        
        if not args.noplot:
            draw_plot(f"Modèle {i+1}",window_title , cp)

        if args.output:
            clustering.write_file(f"{args.output}{i+1}.tsv")

    ####################################################################