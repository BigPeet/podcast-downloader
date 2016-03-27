
#for i in *.py */*.py */*/*.py *.example */*.example */*/*.example ; do

for i in $(find ./ -name "*.py" -or -name "*.example" -or -name "*.list" \
    -or -name "*.conf" -or -name "*.md"); do
    sed -i "s/\t/    /g" $i
done
