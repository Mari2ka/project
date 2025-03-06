

from search import get_movies
from stats import get_popular_searches

def main():
    while True:
        print("\n📌 Выберите действие:")
        print("1. 🔎 Поиск фильмов по параметрам")
        print("2. 📊 Показать популярные запросы")
        print("3. ❌ Выход")

        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            get_movies()
        elif choice == '2':
            get_popular_searches()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("❌ Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
