#set -euxo pipefail
# cmd=(
#   --list
#     --column="Номер задания"
#     --column="Пройдено"
#     --column="Название"
#     --column="Описание"
#     --column=uuid
#     --hide-column=5
#     --print-column=5
# )

# level_folder=$(python ebash.py | xargs yad "${cmd[@]}" | python start_game.py)
level_folder=levels/$1
echo Starting level!

hint () {
    cat "$level_folder"/HINT.txt
}

readme () {
    cat "$level_folder"/README.txt
}

echo "If you want to see this help message again call 'readme' function"

stop (){
      echo Exiting quest!
      unset -f check
      unset -f readme
      unset -f hint
      unset -f stop
      exit
}

args=("$@")

check (){
  check_result=$(sh "$level_folder"/check.sh)
  if [[ "$check_result" == "1" ]]; then
      echo Completed!
    #   echo exit code will be ${args[1]}
      exit ${args[1]}
  else
      echo Not completed yet! Try executing quest_hint or quest_help functions to get help.
  fi
}
