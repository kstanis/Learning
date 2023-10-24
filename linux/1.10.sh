
read -p "введите имя каталога " cname

if [ -e "$cname" ]; then
    ls "$cname"
else
    echo "каталог не найден"
fi
