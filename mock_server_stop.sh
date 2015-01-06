kill -9 $(ps -ef| grep -v grep |grep mock_server.py| awk '{print $2}')
rm mock_server.py
rm mock_server.log
