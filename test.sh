level_folder=levels/$1
python3 $level_folder/pre.py
echo Starting level!
start_folder=$(pwd)

hint () {
    cat "$start_folder"/"$level_folder"/HINT.txt | less
}

readme () {
    cat "$start_folder"/"$level_folder"/README.txt | less
}

echo "If you want to see this help message again call 'readme' function"

stop (){
      echo Exiting quest!
      unset -f check
      unset -f readme
      unset -f hint
      unset -f stop
      python3 "$start_folder"/"$level_folder"/post.py
      exit
}

args=("$@")
check (){
  check_result=$(python3 "$start_folder"/"$level_folder"/check.py)
  if [[ "$check_result" == "1" ]]; then
      echo Completed!
      python3 "$start_folder"/"$level_folder"/post.py
    #   echo exit code will be ${args[1]}
      exit ${args[1]}
  else
      echo Not completed yet! Try executing hint or readme functions to get help.
  fi
}
