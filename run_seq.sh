for i in {1..3}; do # I have modified this(10->3) to run for 3 time to calculate the avg T. But before that I have executed same for 10 time to find failures and flaky files. 
    echo " Run Number $i"
    pytest  
done