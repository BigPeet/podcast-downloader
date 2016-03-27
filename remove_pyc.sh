
for i in $(find . -name "*.pyc"); do
    echo $i
    rm $i
done
