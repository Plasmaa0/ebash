cmd=(
  --list
    --column="Номер задания"
    --column="Пройдено"
    --column="Название"
    --column="Описание"
    --column=uuid
    --hide-column=5
    --print-column=5
)

level_folder=$(python ebash.py | xargs yad "${cmd[@]}" | python start_game.py)
echo Starting level!

quest_hint () {
    cat "$level_folder"/HINT.md
}

quest_help () {
    cat "$level_folder"/README.md
}

quest_help

echo "If you want to see this help message again call quest_help function"

check (){
  check_result=$(sh "$level_folder"/check.sh)
  if [[ "$check_result" == "1" ]]; then
      echo Completed!
      unset -f check
      unset -f quest_help
      unset -f quest_hint
  else
      echo Not completed yet! Try executing quest_hint or quest_help functions to get help.
  fi
}