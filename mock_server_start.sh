source ~/.bash_profile
tar -zxf python.tar.gz
./python27/bin/python ./create.py
nohup ./python27/bin/python ./mock_server.py > mock_server.log &
echo 'success start'
