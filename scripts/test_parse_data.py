import itertools
import os


if __name__ == "__main__":

    dir = os.path.abspath(os.curdir)
    array_result = []
    global_count_repeat = size_string = 0
    last_char = second_char = tmp_prev_string = ""
    delete_char = "()',"

    def input_params ():
        while True:
            try:
                global size_string
                size_string = int(input(" - Введите размер строки перебора (int): "))
                if size_string > 0 and size_string < 20:
                    return str(size_string)

                elif size_string > 0:
                    confirm = input(" - " + str(size_string) + " - очень большое количество! Вы уверены? yes / no / exit:  ")
                    if confirm == "yes":
                        return size_string

                    elif confirm == "no":
                        continue

                    elif confirm == "exit":
                        print("Exit script")
                        exit()

            except (TypeError, ValueError):
                print(' - Введите пожалуйста положительное целое число', flush=True),

    chars_in_variants = input(' - Введите варианты символов для перебора значений'
                              + '\n' + ' - click Enter если по умолчанию  a0123456789  :' )

    if chars_in_variants == "":
        chars_in_variants = "a0123456789"
        print('Поиск вариантов по символам ' + chars_in_variants)

    else:
       chars_in_variants =  "".join(sorted(set(chars_in_variants)))
       print("\n Результат уникальных символов  ", chars_in_variants)

# ////////////////////////////////////////////////
    input_params() # -> start script
# ////////////////////////////////////////////////
    for value in itertools.product(str(chars_in_variants), repeat=int(size_string)):

        for del_char in delete_char:
            value = ''.join(value)
            value.replace(del_char, '')

        for char in value:
            if char == last_char and char == second_char and tmp_prev_string != value:
                tmp_prev_string = value
                global_count_repeat += 1
                array_result.append(value)
            second_char = last_char
            last_char = char
        last_char = second_char = ""

    file_name = 'result_for_' + str(size_string) + '.txt'

    try:
        result_file = open(dir + "/" + file_name, 'w')
        for item in array_result:
            print(item)
            result_file.write(item + '\n')
        result_file.write(
            "\n Совпанений - " + str(global_count_repeat)
            + '\n Из уникальных символов - ' + str(chars_in_variants)
            + '\n Ограничение строки генерации - ' + str(size_string)
        )
        print("\nСовпанений - ", global_count_repeat)
        print("\nРезультат сохранён в текущую директорию " + "\nПуть - " + dir + "\nФайл - " + file_name)
        result_file.close()

    except (PermissionError):
        print('\n - Невозможно работать с файлом результата,'
              '\n - проверьте права доступа или использование файла '
              '\n - "' + file_name + '" другой программой', flush=True)
