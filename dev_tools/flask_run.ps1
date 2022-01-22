pip3 install flask --user
pip3 install mysql --user
pip3 install flask_sqlalchemy --user
pip3 install sqlalchemy_utils --user
pip3 install --upgrade mysql-connector-python --user 
pip3 install flask_login --user


$env:FLASK_APP="mysite"
$env:FLASK_ENV="development"

Start-Process powershell "flask run"
Start-Process powershell "mysql -u root -proot"

Start-Process chrome "http://127.0.0.1:5000/"
