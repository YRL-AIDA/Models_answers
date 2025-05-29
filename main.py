import os
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
import concurrent.futures
import logging
import time
import threading

from langchain_together import ChatTogether
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Получаем директорию скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

class TableHeaderRecognitionTest:
    def __init__(
        self,
        tables_dir: str = os.path.join(script_dir, 'Tables_for_models'),
        answers_dir: str = os.path.join(script_dir, 'Tables_for_models_answers'),
        together_api_key: str = "your_api_key_here"
    ):
        """
        Фреймворк для тестирования распознавания заголовков таблиц.
        """
        self.tables_dir = Path(tables_dir)
        self.answers_dir = Path(answers_dir)
        if together_api_key:
            os.environ['TOGETHER_API_KEY'] = together_api_key

        self.model_names: List[str] = []
        self.prompts: List[Dict[str, Any]] = []
        self.results_df = pd.DataFrame()
        self.request_count = 0
        self.request_lock = threading.Lock()

    def register_models(self):
        """Задайте список моделей для тестирования."""
        self.model_names = [
            "mistralai/Mistral-7B-Instruct-v0.3",
            "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "google/gemma-2-27b-it",
            "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            "Qwen/Qwen2-72B-Instruct",
            "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
            "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            "mistralai/Mistral-Small-24B-Instruct-2501"
        ]

    def register_prompts(self, prompts: List[Dict[str, Any]] = None):
        """Регистрация промптов для распознавания заголовков."""
        if not prompts:
            prompts = [
                # Промпт 1: Zero-shot
                {
                    "user": "Ты эксперт по анализу таблиц. Определи заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col', указывающими индексы строк и столбцов ячеек заголовков. Текстовых значений col и row быть не должно",
                    "system": []
                },
                # Промпт 2: Пошаговая инструкция
                {
                    "user": "Ты эксперт по анализу таблиц. Определи заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col'. Текстовых значений col и row быть не должно",
                    "system": [
                        "Пошаговый алгоритм определения заголовков:",
                        "Шаг 1: Визуальный осмотр таблицы",
                        "- Изучи структуру и макет таблицы.",
                        "Шаг 2: Идентификация заголовков",
                        "- Найди ячейки с обобщающим текстом.",
                        "- Обрати внимание на форматирование.",
                        "Шаг 3: Анализ позиционирования",
                        "- Проверь заголовки сверху, слева, справа.",
                        "Шаг 4: Подготовка результата",
                        "- Сформируй JSON-ответ с 'headers'."
                    ]
                },
                # Промпт 3: Инструкция + критерии
                {
                    "user": "Ты специалист по анализу сложных таблиц. Определи все заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col'. Текстовых значений col и row быть не должно",
                    "system": [
                        "Расширенный алгоритм анализа заголовков:",
                        "Шаг 1: Семантический анализ",
                        "- Найди ключевые слова категорий.",
                        "Шаг 2: Позиционный анализ",
                        "- Определи положение заголовков.",
                        "Шаг 3: Анализ структурных паттернов",
                        "- Выяви повторяющиеся структуры.",
                        "Шаг 4: Контекстуальный анализ",
                        "- Оцени связи между ячейками.",
                        "Шаг 5: Метаданные",
                        "- Учти форматирование и координаты.",
                        "Шаг 6: Иерархия",
                        "- Выдели основные и вложенные заголовки."
                    ],
                    "key_criteria": [
                        "Семантика: ключевые слова категорий.",
                        "Расположение: позиционирование заголовков.",
                        "Шаблоны: структурные паттерны.",
                        "Контекст: связь с ячейками.",
                        "Метаданные: атрибуты форматирования.",
                        "Иерархия: многоуровневые заголовки."
                    ]
                },
                # Промпт 4: Инструкция + 1 пример
                {
                    "user": "Ты эксперт по анализу таблиц. Определи все заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col'. Текстовых значений col и row быть не должно",
                    "system": [
                        "Расширенный алгоритм анализа заголовков:",
                        "Шаг 1: Семантический анализ",
                        "- Найди ключевые слова категорий.",
                        "Шаг 2: Позиционный анализ",
                        "- Определи положение заголовков.",
                        "Шаг 3: Анализ структурных паттернов",
                        "- Выяви повторяющиеся структуры.",
                        "Шаг 4: Контекстуальный анализ",
                        "- Оцени связи между ячейками.",
                        "Шаг 5: Метаданные",
                        "- Учти форматирование и координаты.",
                        "Шаг 6: Иерархия",
                        "- Выдели основные и вложенные заголовки."
                    ],
                    "key_criteria": [
                        "Семантика: ключевые слова категорий.",
                        "Расположение: позиционирование заголовков.",
                        "Шаблоны: структурные паттерны.",
                        "Контекст: связь с ячейками.",
                        "Метаданные: атрибуты форматирования.",
                        "Иерархия: многоуровневые заголовки."
                    ],
                    "examples": [
                        {
                            "input_code": "df = pd.DataFrame({'Квартал': ['Q1 2023', 'Q1 2023', 'Q1 2023', 'Q1 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023'], 'Регион': ['Север', 'Юг', 'Восток', 'Запад', 'Север', 'Юг', 'Восток', 'Запад'], 'Продажи (млн)': [1.2, 0.8, 1.5, 0.9, 1.3, 0.9, 1.6, 1.0], 'Рост': ['+5%', '+3%', '+7%', '+2%', '+8%', '+12%', '+6%', '+11%']}, index=[0, 1, 2, 3, 4, 5, 6, 7])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}]}
                        }
                    ]
                },
                # Промпт 5: Инструкция + 2 примера
                {
                    "user": "Ты эксперт по анализу таблиц. Определи все заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col'. Текстовых значений col и row быть не должно",
                    "system": [
                        "Расширенный алгоритм анализа заголовков:",
                        "Шаг 1: Семантический анализ",
                        "- Найди ключевые слова категорий.",
                        "Шаг 2: Позиционный анализ",
                        "- Определи положение заголовков.",
                        "Шаг 3: Анализ структурных паттернов",
                        "- Выяви повторяющиеся структуры.",
                        "Шаг 4: Контекстуальный анализ",
                        "- Оцени связи между ячейками.",
                        "Шаг 5: Метаданные",
                        "- Учти форматирование и координаты.",
                        "Шаг 6: Иерархия",
                        "- Выдели основные и вложенные заголовки."
                    ],
                    "key_criteria": [
                        "Семантика: ключевые слова категорий.",
                        "Расположение: позиционирование заголовков.",
                        "Шаблоны: структурные паттерны.",
                        "Контекст: связь с ячейками.",
                        "Метаданные: атрибуты форматирования.",
                        "Иерархия: многоуровневые заголовки."

                    ],
                    "examples": [
                        {
                            "input_code": "df = pd.DataFrame({'Квартал': ['Q1 2023', 'Q1 2023', 'Q1 2023', 'Q1 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023'], 'Регион': ['Север', 'Юг', 'Восток', 'Запад', 'Север', 'Юг', 'Восток', 'Запад'], 'Продажи (млн)': [1.2, 0.8, 1.5, 0.9, 1.3, 0.9, 1.6, 1.0], 'Рост': ['+5%', '+3%', '+7%', '+2%', '+8%', '+12%', '+6%', '+11%']}, index=[0, 1, 2, 3, 4, 5, 6, 7])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}]}
                        },
                        {
                            "input_code": "df = pd.DataFrame({'Категория': ['Электроника', '', '', 'Бытовая техника', '', ''], 'Продукт': ['', 'Смартфон', 'Ноутбук', '', 'Пылесос', 'Холодильник'], 'Цена': ['', '700', '1200', '', '150', '800'], 'Скидка': ['', '10%', '15%', '', '5%', '12%']}, index=[0, 1, 2, 3, 4, 5])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}, {"row": 1, "col": 0}, {"row": 4, "col": 0}]}
                        }
                    ]
                },
                # Промпт 6: Инструкция + 3 примера
                {
                    "user": "Ты эксперт по анализу таблиц. Определи все заголовки в таблице: {table_text}. Верни результат в виде JSON-объекта с ключом 'headers', содержащим список объектов с ключами 'row' и 'col'. Текстовых значений col и row быть не должно",
                    "system": [
                        "Расширенный алгоритм анализа заголовков:",
                        "Шаг 1: Семантический анализ",
                        "- Найди ключевые слова категорий.",
                        "Шаг 2: Позиционный анализ",
                        "- Определи положение заголовков.",
                        "Шаг 3: Анализ структурных паттернов",
                        "- Выяви повторяющиеся структуры.",
                        "Шаг 4: Контекстуальный анализ",
                        "- Оцени связи между ячейками.",
                        "Шаг 5: Метаданные",
                        "- Учти форматирование и координаты.",
                        "Шаг 6: Иерархия",
                        "- Выдели основные и вложенные заголовки."
                    ],
                    "key_criteria": [
                        "Семантика: ключевые слова категорий.",
                        "Расположение: позиционирование заголовков.",
                        "Шаблоны: структурные паттерны.",
                        "Контекст: связь с ячейками.",
                        "Метаданные: атрибуты форматирования.",
                        "Иерархия: многоуровневые заголовки."

                    ],
                    "examples": [
                        {
                            "input_code": "df = pd.DataFrame({'Квартал': ['Q1 2023', 'Q1 2023', 'Q1 2023', 'Q1 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023', 'Q2 2023'], 'Регион': ['Север', 'Юг', 'Восток', 'Запад', 'Север', 'Юг', 'Восток', 'Запад'], 'Продажи (млн)': [1.2, 0.8, 1.5, 0.9, 1.3, 0.9, 1.6, 1.0], 'Рост': ['+5%', '+3%', '+7%', '+2%', '+8%', '+12%', '+6%', '+11%']}, index=[0, 1, 2, 3, 4, 5, 6, 7])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}]}
                        },
                        {
                            "input_code": "df = pd.DataFrame({'Категория': ['Электроника', '', '', 'Бытовая техника', '', ''], 'Продукт': ['', 'Смартфон', 'Ноутбук', '', 'Пылесос', 'Холодильник'], 'Цена': ['', '700', '1200', '', '150', '800'], 'Скидка': ['', '10%', '15%', '', '5%', '12%']}, index=[0, 1, 2, 3, 4, 5])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}, {"row": 1, "col": 0}, {"row": 4, "col": 0}]}
                        },
                        {
                            "input_code": "df = pd.DataFrame({'Экономический регион': ['Северная Америка', 'Европейский Союз', 'Азиатско-Тихоокеанский регион', 'Китай', 'Япония', 'Южная Корея'], 'Год': ['2022', '2022', 'Субрегионы', '2022', '2022', '2022'], 'Технологические инвестиции': ['2.7', '2.4', 'Уровень технологического развития', '3.2', '2.8', '3.0'], 'Искусственный интеллект': ['1.9', '1.6', '', '2.2', '1.7', '1.8'], 'Квантовые технологии': ['2.3', '1.8', '', '2.9', '2.5', '2.6'], 'Робототехника': ['2.1', '1.9', '', '2.5', '2.2', '2.3'], 'Биотехнологии': ['3.5', '2.7', 'Специализация', '4.1', '3.3', '3.6'], 'Стартапы': ['4.2', '3.6', '', '3.9', '3.7', '4.0'], 'Патенты': ['3.8', '3.1', '', '4.3', '3.5', '3.9'], 'Венчурные инвестиции': ['2.9', '2.5', '', '3.6', '3.1', '3.3']}, index=[0, 1, 2, 3, 4, 5])",
                            "output": {"headers": [{"row": 0, "col": 0}, {"row": 0, "col": 1}, {"row": 0, "col": 2}, {"row": 0, "col": 3}, {"row": 0, "col": 4}, {"row": 0, "col": 5}, {"row": 0, "col": 6}, {"row": 0, "col": 7}, {"row": 0, "col": 8}, {"row": 0, "col": 9}]}
                        }
                    ]
                }
            ]
        self.prompts = prompts

    def _load_tables(self) -> List[Dict[str, Any]]:
        """Загружает таблицы и их истинные заголовки из аннотаций."""
        tables = []
        table_count = 0
        for fp in self.tables_dir.glob('*.py'):
            ans_fp = self.answers_dir / fp.name
            if not ans_fp.exists():
                logging.warning(f"Ответ для {fp.name} не найден")
                continue

            # Считываем аннотацию headers: (r,c);...
            coords = []
            headers_found = False
            with open(ans_fp, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('headers:'):
                        headers_found = True
                        parts = line.split(':', 1)[1].split(';')
                        for part in parts:
                            part = part.strip().strip('()')
                            if not part:
                                continue
                            try:
                                r, c = map(int, part.split(','))
                                coords.append((r, c))
                            except ValueError:
                                logging.warning(f"Некорректный формат координат в {ans_fp.name}: {part}")
                        break
            if not headers_found:
                logging.warning(f"Строка 'headers:' не найдена в {ans_fp.name}")

            # Выполняем код таблицы и получаем df
            namespace = {}
            with open(fp, 'r', encoding='utf-8') as f:
                code = ''.join([l for l in f if not l.startswith('headers:')])
            try:
                exec(code, {'pd': pd, 'np': np}, namespace)
                # Поиск DataFrame
                for var_name, var_value in namespace.items():
                    if isinstance(var_value, pd.DataFrame):
                        df = var_value
                        logging.info(f"Найден DataFrame '{var_name}' в {fp.name}")
                        break
                else:
                    # Поиск конвертируемых структур
                    for var_name, var_value in namespace.items():
                        if isinstance(var_value, (list, dict, np.ndarray)):
                            try:
                                df = pd.DataFrame(var_value)
                                logging.info(f"Создан DataFrame из '{var_name}' для {fp.name}")
                                break
                            except ValueError as e:
                                logging.warning(f"ValueError при создании DataFrame из '{var_name}' для {fp.name}: {e}")
                                # Попытка обработать данные с разной длиной
                                if isinstance(var_value, list) and all(isinstance(row, list) for row in var_value):
                                    max_len = max(len(row) for row in var_value)
                                    padded_data = [row + [np.nan] * (max_len - len(row)) for row in var_value]
                                    df = pd.DataFrame(padded_data)
                                    logging.info(f"Создан DataFrame с padding из '{var_name}' для {fp.name}")
                                    break
                                elif isinstance(var_value, dict):
                                    try:
                                        max_len = max(len(v) for v in var_value.values() if isinstance(v, list))
                                        padded_data = {k: v + [np.nan] * (max_len - len(v)) if isinstance(v, list) else [v] * max_len for k, v in var_value.items()}
                                        df = pd.DataFrame(padded_data)
                                        logging.info(f"Создан DataFrame с padding из '{var_name}' (dict) для {fp.name}")
                                        break
                                    except:
                                        # Если словарь не содержит списков, создаём DataFrame с автоматическим индексом
                                        try:
                                            df = pd.DataFrame(var_value, index=range(max(len(v) for v in var_value.values() if isinstance(v, list))))
                                            logging.info(f"Создан DataFrame с автоматическим индексом из '{var_name}' для {fp.name}")
                                            break
                                        except:
                                            continue
                                elif isinstance(var_value, np.ndarray):
                                    # Для массивов NumPy создаём DataFrame с автоматическим индексом
                                    try:
                                        df = pd.DataFrame(var_value, index=range(var_value.shape[0]))
                                        logging.info(f"Создан DataFrame из массива NumPy '{var_name}' для {fp.name}")
                                        break
                                    except:
                                        continue
                                else:
                                    continue
                    else:
                        logging.error(f"Не найдены данные для создания DataFrame в {fp.name}")
                        continue
                # Проверка на корректность DataFrame
                if df.empty or df.shape[0] == 0 or df.shape[1] == 0:
                    logging.warning(f"DataFrame в {fp.name} пуст или имеет некорректные размеры")
                    continue
                # Попытка исправить несоответствие размеров
                try:
                    if df.index.size != df.shape[0]:
                        logging.warning(f"Исправление несоответствия размеров в {fp.name}: индекс {df.index.size}, строки {df.shape[0]}")
                        df = pd.DataFrame(df.values, index=range(df.shape[0]), columns=df.columns if not df.columns.empty else range(df.shape[1]))
                except Exception as e:
                    logging.error(f"Ошибка при исправлении размеров {fp.name}: {type(e).__name__} - {e}")
                    continue
                tables.append({'file': fp.name, 'df': df, 'true_coords': coords})
                table_count += 1
            except Exception as e:
                logging.error(f"Ошибка при загрузке {fp.name}: {type(e).__name__} - {e}")
                continue
        logging.info(f"Всего загружено таблиц: {table_count}")
        return tables

    @staticmethod
    def _prepare_messages(table: pd.DataFrame, prompt: Dict[str, Any]) -> List[Tuple[str, str]]:
        """Формирует список сообщений для ChatTogether.invoke."""
        table_str = table.to_string()
        messages = []
        if prompt.get('system'):
            sys_txt = '\n'.join(prompt['system'])
            messages.append(('system', sys_txt))
        user_txt = prompt['user'].format(table_text=table_str)
        messages.append(('human', user_txt))
        return messages

    def query_model(self, model_name, prompt_idx, tbl):
        """Выполняет запрос к модели для одной комбинации таблица-модель-промпт."""
        with self.request_lock:
            self.request_count += 1
            request_id = self.request_count
        logging.info(f"Sending request to model '{model_name}' for prompt {prompt_idx} and table '{tbl['file']}' (request {request_id})")
        request_start_time = time.time()
        llm = ChatTogether(
            model=model_name,
            temperature=0.0,
            api_key=os.environ.get('TOGETHER_API_KEY')
        )
        prompt = self.prompts[prompt_idx]
        msgs = self._prepare_messages(tbl['df'], prompt)
        try:
            ai_msg: AIMessage = llm.invoke(msgs)
            response = ai_msg.content
            request_end_time = time.time()
            request_duration = request_end_time - request_start_time
            logging.info(f"Received response from model '{model_name}' for prompt {prompt_idx} and table '{tbl['file']}' (request {request_id}) in {request_duration:.2f} seconds")
            return {
                'model': model_name,
                'prompt_idx': prompt_idx,
                'table_file': tbl['file'],
                'response': response,
                'true_coords': tbl['true_coords']
            }
        except Exception as e:
            request_end_time = time.time()
            request_duration = request_end_time - request_start_time
            logging.error(f"Error in request to model '{model_name}' for prompt {prompt_idx} and table '{tbl['file']}' (request {request_id}): {type(e).__name__} - {e} (duration: {request_duration:.2f} seconds)")
            return None

    def run_tests(self) -> pd.DataFrame:
        """Основной цикл: загрузка таблиц, параллельный вызов моделей, сбор ответов."""
        tables = self._load_tables()
        tasks = []
        for model_name in self.model_names:
            for pid in range(len(self.prompts)):
                for tbl in tables:
                    tasks.append((model_name, pid, tbl))

        total_start_time = time.time()
        logging.info(f"Starting processing of {len(tasks)} requests")

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(lambda task: self.query_model(*task), tasks))

        results = [r for r in results if r is not None]
        total_end_time = time.time()
        total_duration = total_end_time - total_start_time
        logging.info(f"Total successful responses: {len(results)}")
        logging.info(f"Total time taken: {total_duration:.2f} seconds")
        self.results_df = pd.DataFrame(results)
        self.results_df.to_csv(os.path.join(script_dir, 'detailed_results_with_responses.csv'), index=False)
        return self.results_df

if __name__ == '__main__':
    test = TableHeaderRecognitionTest(
        tables_dir=os.path.join(script_dir, 'Tables_for_models'),
        answers_dir=os.path.join(script_dir, 'Tables_for_models_answers'),
        together_api_key="4b19c1ce836b27c369e574d911831bf01ca23dc182ac4904c7b2276ceb24f7a2"  # Замените на ваш реальный API-ключ
    )
    test.register_models()
    test.register_prompts()  # Пользователь реализует этот метод самостоятельно
    results = test.run_tests()
    print(results)