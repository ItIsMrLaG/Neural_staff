import pandas as pd

#  =============== создание таблиц ================ #
data = pd.Series([1,2,3], index= ['first', 'second', 'third'])  # составление массива данных, который похож на словарь, но не словарь
info = data.loc[["first", "second"]]     # обращение к группе элементов (по факту - это просто преобразование большой таблички data в маленькую табличку)
info_inner = info.loc["first"]           # а это уже обращение к конкретному элементу из таблицы

data1 = pd.Series(list(range(10, 1001))) # то же,.что и data, но в отличае от него здесь ключи - индексы от (90 - n)

dataframe = pd.DataFrame([[1, 2, 3, 4,], [1, 2, 3,]],
                         columns=['first', 'second', 'third', 'forth'], # vertical_name of the table
                         index=['ind1', 'ind2'],                        # horizontal_name of the table
                         )
# ================================================== #

# ================ чтение из scv =================== #
scv_file = pd.read_csv('../for_pandas_exemp.csv')
beginning = scv_file.head(1)   # делает срез из основной таблицы (только начало) (параметр - сколько строк будет выведено)
ending = scv_file.tail(1)      # делает срез из основной табюлицы (только конец) (параметр - сколько строк будет выведено)
# ================================================== #

#  ====== получение статистичексой информации ====== #
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # такая конструкция выводит всю инфопрммация без сокращений
    # scv_file.info()                                # вывод информации о самой таблице (число столбцов, их имена...)
    tester = scv_file.describe()                     # создание таблицы со всеми статистическими данными из колонок с int
    tester1 = scv_file.describe(include=['object'])  # создание таблицы со всеми статистическими данными из колонок с str

    value_min = scv_file.min()                       # минимальная информация по столбцам в таблицы
    value_max = scv_file.max()                       # максимальное информация по столбцам таблицы
    all_sum = scv_file.sum()                         # сумма всех значений в столбце
    number = scv_file.count()                        # число элементов в столбце
    average_deviation = scv_file.std()               # отклонение от среднего значения по столбцу
    average_context = scv_file['Age'].mean()         # поиск среднего значения по конкретному столбцу из таблицы

    how_many = scv_file['Nationality'].value_counts()# число каждого элемента в выбранном диапозоне
    information = how_many.index                     # 'list' со всеми возможными эелментами (их индексы соответствуют индексу в 'how_many')
    maximum = how_many[0]                            # так как 'how_many' отсортирован, то индексу - "0" соответоствует максимальное значение
    length = len(how_many.index)                     # количество элементов
    value = how_many['Germany']                      # получение инфолрмации о конкретном элементе
    my_range = how_many.loc[how_many > 100]          # получение диапазона из таблицы

    uniq_values = scv_file['Nationality'].unique()   # получение списка всех возможных элементов (уникальных) [тоже, что и - 'information']
    number_uniq = scv_file['Nationality'].nunique()  # количество уникальных элементов [тоже, что и - 'length']
# ================================================== #

# ============= получение конкретной инфы =========== #
ans = tester.get('Age')['count']    # (столбец)[строка] - получается пересечение, которое потом и передается
# =================================================== #

# ============== получение среза таблицы ============ #
table = scv_file[(scv_file.Age < scv_file.Age.mean()) & (scv_file.Club == 'FC Barcelona')]  # взял только футболистов клуба барселона, которе младше среднего возраста
average_wage = scv_file[(scv_file.Age < scv_file.Age.mean()) & (scv_file.Club == 'FC Barcelona')].Wage.mean()
# =================================================== #

# ============== группировка элементов ============== #
info_object = scv_file.groupby(['Club'])      # группировка по признаку (вспомогательный элемент)
info_dict = scv_file.groupby(['Club']).groups # как посмотреть предыдущий пункт
sum_of_all = scv_file.groupby(['Club']).sum() # просуммировать все элементы
context_sum = scv_file.groupby(['Club']).sum().loc['Ajax']["Wage"] # посмотреть сумму элемента у конкретного объекта
all_sum_elem = scv_file.groupby(['Club'])["Wage"].sum() # посмотреть сумму элемента у группы объектов (неотсортированное)
all_sum_elem_sorted = scv_file.groupby(['Club'])["Wage"].sum().sort_values(ascending=False) # посмотреть сумму элемента у группы объектов (отсортированное)
# =================================================== #

# ============== сводная таблица ============== #
pivot = scv_file.loc[scv_file['Club'].isin(['FC Barcelona', 'Real Madrid'])].pivot_table(
    values=['Wage'],       # значение, соответствующее пересечению строки и колонки
    index=['Nationality'], # значение строки
    columns=['Club'],      # значение колонки
    aggfunc='sum',         # агригационные параметры  - ['sum', 'mean', 'count', 'median', 'max', 'min']
    margins=1,             # добавляет столбик с суммированными результатами по строке
    fill_value=0           # что будет на месте пропуска
    )
print(pivot)
# =================================================== #


## ПРИМЕРЫ ############################################
footbolers = pd.read_csv('../for_pandas_exemp.csv')

#@1 Определи название страны (Nationality), из которой больше всего игроков, чья зарплата (Wage) превышает среднее значение.
first = footbolers[footbolers.Wage > footbolers.Wage.mean()].Nationality.describe().top
#@2 Составить таблицу средней зарплаты игроков трех стран.
group1 = footbolers[footbolers.Nationality == 'Argentina'].Wage
group2 = footbolers[footbolers.Nationality == 'Brazil'].Wage
group3 = footbolers[footbolers.Nationality == 'Portugal'].Wage
second = pd.DataFrame([group1.mean(), group2.mean(), group3.mean()],
                      columns=['Wage'],
                      index=['Argentina', 'Brazil', 'Portugal'])
## КОНЕЦ #############################################