for i in {1..3}; do
echo " Run Number $i"
    pytest -n auto --dist load --parallel-threads auto 
done
