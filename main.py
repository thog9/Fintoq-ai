import os
import sys
import asyncio
import inspect
from colorama import init, Fore, Style
import inquirer

init(autoreset=True)

BORDER_WIDTH = 80

def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

def _banner():
    banner = r"""

    
░
████████╗██╗░░██╗░█████╗░░██████╗░████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗░░░██╗██████╗░
╚══██╔══╝██║░░██║██╔══██╗██╔════╝░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░██║██║░░░██║██╔══██╗
░░░██║░░░███████║██║░░██║██║░░██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░███████║██║░░░██║██████╦╝
░░░██║░░░██╔══██║██║░░██║██║░░╚██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔══██║██║░░░██║██╔══██╗
░░░██║░░░██║░░██║╚█████╔╝╚██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░░██║╚██████╔╝██████╦╝
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░


    """
    print(f"{Fore.GREEN}{banner:^80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
    print_border("FINTOQ AI", Fore.GREEN)
    print(f"{Fore.YELLOW}│ {'Website'}: {Fore.CYAN}https://thogtoolhub.com/{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Discord'}: {Fore.CYAN}https://discord.gg/MnmYBKfHQf{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Channel Telegram'}: {Fore.CYAN}https://t.me/thogairdrops{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')
  
async def run_checkin(language: str):
    from scripts.checkin import run_checkin
    await run_checkin(language)

async def run_checkin_web(language):
    from scripts.checkin_web import run_checkin_web
    await run_checkin_web(language)

async def run_boost(language):
    from scripts.boost import run_boost
    await run_boost(language)

async def run_chat(language):
    from scripts.chat import run_chat
    await run_chat(language)

async def run_chat_web(language):
    from scripts.chat_web import run_chat_web
    await run_chat_web(language)

async def run_quests(language):
    from scripts.quests import run_quests
    await run_quests(language)

async def cmd_exit(language: str):
    messages = {"vi": "Đang thoát...", "en": "Exiting..."}
    print_border(messages[language], Fore.GREEN)
    sys.exit(0)

SCRIPT_MAP = {
    "checkin_web": run_checkin_web,
    "checkin": run_checkin,
    "boost": run_boost,
    "chat": run_chat,
    "chat_web": run_chat_web,
    "quests": run_quests,
    "exit": cmd_exit
}

def get_available_scripts(language):
    scripts = {
        'vi': [
            {"name": "1. Web Check-in (email.txt)", "value": "checkin_web"},
            {"name": "2. Telegram Check-in (accounts.txt)", "value": "checkin"},
            {"name": "3. Telegram Boost (accounts.txt)", "value": "boost"},
            {"name": "4. Telegram Chat FXP (accounts.txt)", "value": "chat"},
            {"name": "5. Web Chat XP (email.txt)", "value": "chat_web"},
            {"name": "6. Telegram Quests (accounts.txt)", "value": "quests"},
          
            {"name": "X. Thoát", "value": "exit"},
        ],
        'en': [
            {"name": "1. Web Check-in (email.txt)", "value": "checkin_web"},
            {"name": "2. Telegram Check-in (accounts.txt)", "value": "checkin"},
            {"name": "3. Telegram Boost (accounts.txt)", "value": "boost"},
            {"name": "4. Telegram Chat FXP (accounts.txt)", "value": "chat"},
            {"name": "5. Web Chat XP (email.txt)", "value": "chat_web"},
            {"name": "6. Telegram Quests (accounts.txt)", "value": "quests"},
          
            {"name": "X. Exit", "value": "exit"},
        ]
    }
    return scripts[language]

def run_script(script_func, language):
    if inspect.iscoroutinefunction(script_func):
        asyncio.run(script_func(language))
    else:
        script_func(language)

def select_language():
    while True:
        _clear()
        _banner()
        print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("CHỌN NGÔN NGỮ / SELECT LANGUAGE", Fore.YELLOW)
        questions = [
            inquirer.List('language',
                          message=f"{Fore.CYAN}Vui lòng chọn / Please select:{Style.RESET_ALL}",
                          choices=[("1. Tiếng Việt", 'vi'), ("2. English", 'en')],
                          carousel=True)
        ]
        answer = inquirer.prompt(questions)
        if answer and answer['language'] in ['vi', 'en']:
            return answer['language']
        print(f"{Fore.RED}❌ {'Lựa chọn không hợp lệ / Invalid choice':^76}{Style.RESET_ALL}")

def main():
    _clear()
    _banner()
    language = select_language()

    messages = {
        "vi": {
            "running": "Đang thực thi: {}",
            "completed": "Đã hoàn thành: {}",
            "error": "Lỗi: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "menu_title": "MENU CHÍNH",
            "select_script": "Chọn script để chạy"
        },
        "en": {
            "running": "Running: {}",
            "completed": "Completed: {}",
            "error": "Error: {}",
            "press_enter": "Press Enter to continue...",
            "menu_title": "MAIN MENU",
            "select_script": "Select script to run"
        }
    }

    while True:
        _clear()
        _banner()
        print(f"{Fore.YELLOW}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border(messages[language]["menu_title"], Fore.YELLOW)
        print(f"{Fore.CYAN}│ {messages[language]['select_script'].center(BORDER_WIDTH - 4)} │{Style.RESET_ALL}")

        available_scripts = get_available_scripts(language)
        questions = [
            inquirer.List('script',
                          message=f"{Fore.CYAN}{messages[language]['select_script']}{Style.RESET_ALL}",
                          choices=[script["name"] for script in available_scripts],
                          carousel=True)
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            continue

        selected_script_name = answers['script']
        selected_script = next(script for script in available_scripts if script["name"] == selected_script_name)
        selected_script_value = selected_script["value"]

        script_func = SCRIPT_MAP.get(selected_script_value)
        if script_func is None:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Chưa triển khai / Not implemented'}: {selected_script_name}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
            continue

        try:
            print(f"{Fore.CYAN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["running"].format(selected_script_name), Fore.CYAN)
            run_script(script_func, language)
            print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["completed"].format(selected_script_name), Fore.GREEN)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
        except Exception as e:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["error"].format(str(e)), Fore.RED)
            print('')
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")

if __name__ == "__main__":
    main()
