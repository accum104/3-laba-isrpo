from tracks import get_track  # Импорт функции для получения трека дня

def main():
    print("Добро пожаловать в Muse")
    print("Введите 'track', чтобы получить трек дня.\n")

    while True:
        command = input("👉 Ваш выбор: ").strip().lower()
        if command == "track":
            print("\n" + get_track() + "\n")
        elif command == "exit":
            print("Спасибо за использование Muse! До встречи! 👋")
            break
        else:
            print("❌ Неизвестная команда. Попробуйте снова.\n")
        

if __name__ == "__main__":
    main()