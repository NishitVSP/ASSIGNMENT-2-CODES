for i in {1..3}; do
echo " Run Number $i"
    pytest -n 1 --dist load --parallel-threads 1
done