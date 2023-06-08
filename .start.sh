cd ~/.exbash; 
python3 exbash.py;
cd ~;
find . | grep -v ".exbash" | grep -v ".start.sh"| grep -v ".bash_logout"| grep -v ".bashrc"| grep -v ".profile"| grep -v ".cache"| grep -v ".bash_history"| grep -v ".lesshst" | grep "./" | xargs rm -rf
exit
