TEXTIDOTE_LOCATION=C:/git/textidote
BASE_DIR=C:/git/bachelorarbeit

java -Dfile.encoding=UTF-8 -jar $TEXTIDOTE_LOCATION/textidote.jar \
	--check de --encoding utf-8 \
	--dict $BASE_DIR/textidote_dict.txt \
	--remove-macros autoref,lstinputlisting,enquote,nomenclature --ignore sh:stacked \
	--output html $BASE_DIR/main.tex > $BASE_DIR/textidote_report.html \
