cd ~/.exbash; 
python3 exbash.py;
find ~ ! -name '.exbash' ! -name '.start.sh' -type f -delete && find ~ ! -name '.exbash' ! -name '.start.sh' -type d -delete
exit