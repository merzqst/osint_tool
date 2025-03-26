import requests
import argparse

# Функция для проверки VK
def check_vk_profile(username):
    url = f"https://vk.com/{username}"
    try:
        response = requests.get(url, timeout=10)
        return url if response.status_code != 404 and "error" not in response.url else "Страница не найдена"
    except requests.exceptions.RequestException:
        return "Страница не найдена"

# Функция для проверки Telegram
def check_telegram_profile(username):
    url = f"https://t.me/{username}"
    try:
        response = requests.get(url, timeout=10)
        return url if response.status_code == 200 and "tgme_page_extra" in response.text else "Страница не найдена"
    except requests.exceptions.RequestException:
        return "Страница не найдена"

# Функция для проверки GitHub
def check_github_profile(username):
    url = f"https://github.com/{username}"
    try:
        response = requests.get(url, timeout=10)
        return url if response.status_code == 200 else "Страница не найдена"
    except requests.exceptions.RequestException:
        return "Страница не найдена"

def search_social_networks(username):
    """Ищет профили в соцсетях VK, Telegram и GitHub."""
    return {
        "VK": check_vk_profile(username),
        "Telegram": check_telegram_profile(username),
        "GitHub": check_github_profile(username),
    }

def print_results(results):
    print("\n==========================")
    print("     Найденные ссылки")
    print("==========================\n")
    for platform, url in results.items():
        print(f"{platform}: {url}")
    print("==========================\n")

def main():
    parser = argparse.ArgumentParser(description="Поиск информации о человеке по нику в соцсетях (VK, Telegram, GitHub)")
    parser.add_argument("name", type=str, help="Никнейм для поиска")
    args = parser.parse_args()

    print(f"\nИщем информацию о {args.name} в соцсетях...\n")
    social_results = search_social_networks(args.name)

    print_results(social_results)

if __name__ == "__main__":
    main()
