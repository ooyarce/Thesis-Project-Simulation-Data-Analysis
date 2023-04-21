echo "|||||||||||||||||||||||||||||||||||||"
echo "Using files from FixBase folder..."
for file in */ ; do
    #Iterates over the magnitude (file) and gets inside when 'cd'

    #cp temp.py "$file"
    #cp sql_functions.py "$file"
    #cp run.sh "$file"
    #cp check_nodes.py "$file"
    #cp main_sql.py "$file"
    #cp accelerations_writter_tcl_format.py "$file"
    #cp sort_results_into_xlsx.py "$file"
    #cp exporting_results.py "$file"
    #cp materials.tcl "$file"
    #cp analysis_steps.tcl "$file"
    #cp definitions.tcl "$file"
    #cp elements.tcl "$file"
    #cp main.tcl "$file"
    #cp nodes.tcl "$file"
    #cp sections.tcl "$file"

    cd "$file"
    for file2 in */ ;do
        #Iterates over the rupture type (file2) and gets inside when 'cd'

        #cp temp.py "$file2"
        #cp sql_functions.py "$file2"
        #cp run.sh "$file2"
        #cp check_nodes.py "$file2"
        #cp main_sql.py "$file2"
        #cp accelerations_writter_tcl_format.py "$file2"
        #cp sort_results_into_xlsx.py "$file2"
        #cp exporting_results.py "$file2"
        #cp check_nodes.py "$file2"
        #cp materials.tcl "$file2"
        #cp analysis_steps.tcl "$file2"
        #cp definitions.tcl "$file2"
        #cp elements.tcl "$file2"
        #cp main.tcl "$file2"
        #cp nodes.tcl "$file2"
        #cp sections.tcl "$file2"

        cd "$file2"
        for file3 in */ ;do
            #Iterates over the station and gets inside when 'cd'

            #cp temp.py "$file3"
            #cp sql_functions.py "$file3"
            #cp run.sh "$file3"
            #cp check_nodes.py "$file3/Results/"
            #cp main_sql.py "$file3"
            #cp accelerations_writter_tcl_format.py "$file3"
            #cp sort_results_into_xlsx.py "$file3"
            #cp check_nodes.py "$file3/Results/"
            #cp materials.tcl "$file3"
            #cp analysis_steps.tcl "$file3"
            #cp definitions.tcl "$file3"
            #cp elements.tcl "$file3"
            #cp main.tcl "$file3"
            #cp nodes.tcl "$file3"
            #cp sections.tcl "$file3"
            rm tiempos.txt
            #cd "$file3"
            #cd ..
        done

        #rm temp.py
        #rm sql_functions.py 
        #rm check_nodes.py
        #rm run.sh
        #rm main_sql.py
        #rm accelerations_writter_tcl_format.py
        #rm sort_results_into_xlsx.py 
        #rm materials.tcl 
        #rm analysis_steps.tcl 
        #rm definitions.tcl 
        #rm elements.tcl 
        #rm main.tcl 
        #rm nodes.tcl 
        #rm sections.tcl 

        cd ..

    done

    #rm temp.py
    #rm sql_functions.py
    #rm check_nodes.py
    #rm run.sh
    #rm main_sql.py
    #rm accelerations_writter_tcl_format.py
    #rm sort_results_into_xlsx.py 
    #rm exporting_results.py
    #rm check_nodes.py
    #rm materials.tcl 
    #rm analysis_steps.tcl 
    #rm definitions.tcl
    #rm elements.tcl 
    #rm main.tcl 
    #rm nodes.tcl 
    #rm sections.tcl 

    cd ..

    
done

echo "Files updated succesfully!"
echo "|||||||||||||||||||||||||||||||||||||"
