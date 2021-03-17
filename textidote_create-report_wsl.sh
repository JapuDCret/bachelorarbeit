TEXTIDOTE_LOCATION=/mnt/c/git/textidote
BASE_DIR=/mnt/c/git/bachelorarbeit

java -Dfile.encoding=UTF-8 -jar $TEXTIDOTE_LOCATION/textidote.jar \
	--check de --encoding utf-8 \
	--dict $BASE_DIR/textidote_dict.txt
	--remove autoref,hyperref,lstinputlisting,enquote,nomenclature \
	--remove-macros autoref,hyperref,lstinputlisting,enquote,nomenclature \
	--ignore sh:stacked \
	--output html $BASE_DIR/main.tex > $BASE_DIR/textidote_report.html \
