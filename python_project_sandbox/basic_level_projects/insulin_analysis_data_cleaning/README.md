## Insulin analysis using dataset
### Python for data cleaning

General
Practice using python to clean data and use data for analysis.
Retrieve the protein sequence of human insulin from human preproinsulin

**Notes**
From the National Library of Medicine: https://ncbi.nlm.nih.gov/
- used the dropdown menu to select Protein and 'human insulin' within the search bar
This dataset was the result: https://ncbi.nlm.nih.gov/protein/AAA59172.1

The source data of relevance for preproinsulin dataset:
ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//

**Cleaning the Data**
$ sed -i '' 's/ORIGIN//g' preproinsulin-seq.txt # had to use '' b/c of Mac OS; this removes ORIGIN
