for i in {1..3}; do
echo " Run Number $i"
    pytest -n 1 --dist no --parallel-threads 1
done
