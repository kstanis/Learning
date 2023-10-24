
read -p "введите имя файла" fname
if  [ -e "$fname" ]; then
sed -i 's/error/warning/g' $fname
else 
echo "file not found"
fi
