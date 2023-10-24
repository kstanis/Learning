
read -p "введите имя файла " fname

if [ -e "$fname" ]; then
    cat "$fname"
else
    echo "Файл не найден"
fi
