import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook
from pathlib import Path
import re
from typing import List, Dict

# Получаем директорию скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

def parse_output_coords(text: str, df: pd.DataFrame) -> list[tuple]:
    """Парсинг координат заголовков из ответа модели."""
    try:
        # Попытка извлечь JSON, начиная с ключа "headers"
        pattern = r'"headers"\s*:\s*\[(.*?)\]'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            json_str = f'{{"headers": [{match.group(1)}]}}'
            print(f"Извлечен JSON с ключом 'headers': {json_str[:200]}...")
        else:
            # Запасной вариант: найти от первой { до последней }
            start = text.find('{')
            end = text.rfind('}') + 1
            if start == -1 or end == 0:
                print(f"JSON не найден в ответе: {text[:200]}...")
                return []
            json_str = text[start:end]
            print(f"Извлечен JSON от '{' до '}': {json_str[:200]}...")

        # Парсинг JSON
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"Ошибка парсинга JSON: {e}")
            print(f"Попытка парсинга: {json_str}")
            return []

        # Извлечь заголовки под ключом 'headers'
        headers = data.get('headers', [])
        if not isinstance(headers, list):
            print(f"Предупреждение: 'headers' не является списком: {headers}")
            return []

        coords = []
        for h in headers:
            if not isinstance(h, dict):
                print(f"Предупреждение: Объект заголовка не является словарем: {h}")
                continue

            # Обработка row
            row = h.get('row')
            if row is None or row == "null":
                row = 0
                print(f"Предупреждение: 'row' is None or 'null', set to 0 в {h}")
            elif isinstance(row, str):
                # Поиск значения row по всей таблице
                row_clean = ' '.join(row.split()).lower()
                found = False
                for r in range(df.shape[0]):
                    for c in range(df.shape[1]):
                        cell_value = df.iloc[r, c]
                        if pd.isna(cell_value):
                            continue
                        cell_clean = ' '.join(str(cell_value).split()).lower()
                        if cell_clean == row_clean:
                            row = r
                            print(f"Найден 'row'={row} в позиции ({r}, {c})")
                            found = True
                            break
                    if found:
                        break
                if not found:
                    available_values = [str(df.iloc[r, c]) for r in range(df.shape[0]) for c in range(df.shape[1]) if not pd.isna(df.iloc[r, c])]
                    print(f"Предупреждение: Не найдено соответствие для 'row'='{row}' в таблице. Доступные значения: {available_values}")
                    continue
            else:
                try:
                    row = int(row)
                    if row < 0 or row >= df.shape[0]:
                        print(f"Предупреждение: 'row'={row} вне диапазона [0, {df.shape[0]-1}] в {h}")
                        continue
                except (ValueError, TypeError):
                    print(f"Предупреждение: Некорректное значение 'row'={row} в {h}")
                    continue

            # Обработка col
            col = h.get('col')
            if col is None or col == "null":
                col = 0
                print(f"Предупреждение: 'col' is None or 'null', set to 0 в {h}")
            elif isinstance(col, str):
                # Поиск значения col по всей таблице
                col_clean = ' '.join(col.split()).lower()
                found = False
                for r in range(df.shape[0]):
                    for c in range(df.shape[1]):
                        cell_value = df.iloc[r, c]
                        if pd.isna(cell_value):
                            continue
                        cell_clean = ' '.join(str(cell_value).split()).lower()
                        if cell_clean == col_clean:
                            col = c
                            print(f"Найден 'col'={col} в позиции ({r}, {c})")
                            found = True
                            break
                    if found:
                        break
                if not found:
                    available_values = [str(df.iloc[r, c]) for r in range(df.shape[0]) for c in range(df.shape[1]) if not pd.isna(df.iloc[r, c])]
                    print(f"Предупреждение: Не найдено соответствие для 'col'='{col}' в таблице. Доступные значения: {available_values}")
                    continue
            else:
                try:
                    col = int(col)
                    if col < 0 or col >= df.shape[1]:
                        print(f"Предупреждение: 'col'={col} вне диапазона [0, {df.shape[1]-1}] в {h}")
                        continue
                except (ValueError, TypeError):
                    print(f"Предупреждение: Некорректное значение 'col'={col} в {h}")
                    continue

            coords.append((row, col))

        return coords

    except Exception as e:
        print(f"Неожиданная ошибка при парсинге: {type(e).__name__} - {e}")
        return []

def evaluate(pred: List[tuple], true: List[tuple]) -> Dict[str, float]:
    """Оценка предсказаний модели WIP."""
    set_p, set_t = set(pred), set(true)
    tp = len(set_p & set_t)
    precision = tp / len(set_p) if set_p else 0.0
    recall = tp / len(set_t) if set_t else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {'precision': precision, 'recall': recall, 'f1': f1}

def load_tables(tables_dir, answers_dir):
    """Загружает таблицы и их истинные заголовки из аннотаций."""
    tables = []
    table_count = 0
    for fp in Path(tables_dir).glob('*.py'):
        ans_fp = Path(answers_dir) / fp.name
        if not ans_fp.exists():
            print(f"⚠️ Ответ для {fp.name} не найден")
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
                            print(f"Предупреждение: Некорректный формат координат в {ans_fp.name}: {part}")
                    break
        if not headers_found:
            print(f"Предупреждение: Строка 'headers:' не найдена в {ans_fp.name}")

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
                    print(f"Найден DataFrame '{var_name}' в {fp.name}")
                    break
            else:
                # Поиск конвертируемых структур
                for var_name, var_value in namespace.items():
                    if isinstance(var_value, (list, dict, np.ndarray)):
                        try:
                            df = pd.DataFrame(var_value)
                            print(f"Создан DataFrame из '{var_name}' для {fp.name}")
                            break
                        except ValueError as e:
                            print(f"ValueError при создании DataFrame из '{var_name}' для {fp.name}: {e}")
                            # Попытка обработать данные с разной длиной
                            if isinstance(var_value, list) and all(isinstance(row, list) for row in var_value):
                                max_len = max(len(row) for row in var_value)
                                padded_data = [row + [np.nan] * (max_len - len(row)) for row in var_value]
                                df = pd.DataFrame(padded_data)
                                print(f"Создан DataFrame с padding из '{var_name}' для {fp.name}")
                                break
                            elif isinstance(var_value, dict):
                                max_len = max(len(v) for v in var_value.values() if isinstance(v, list))
                                padded_data = {k: v + [np.nan] * (max_len - len(v)) if isinstance(v, list) else [v] * max_len for k, v in var_value.items()}
                                df = pd.DataFrame(padded_data)
                                print(f"Создан DataFrame с padding из '{var_name}' (dict) для {fp.name}")
                                break
                            else:
                                continue
                else:
                    print(f"Ошибка: Не найдены данные для создания DataFrame в {fp.name}")
                    continue
            # Проверка на корректность DataFrame
            if df.empty or df.shape[0] == 0 or df.shape[1] == 0:
                print(f"Предупреждение: DataFrame в {fp.name} пуст или имеет некорректные размеры")
                continue
            # Попытка исправить несоответствие размеров
            try:
                if df.index.size != df.shape[0]:
                    print(f"Предупреждение: Исправление несоответствия размеров в {fp.name}: индекс {df.index.size}, строки {df.shape[0]}")
                    df = pd.DataFrame(df.values, index=range(df.shape[0]), columns=df.columns if not df.columns.empty else range(df.shape[1]))
            except Exception as e:
                print(f"Ошибка при исправлении размеров {fp.name}: {type(e).__name__} - {e}")
                continue
            tables.append({'file': fp.name, 'df': df, 'true_coords': coords})
            table_count += 1
        except Exception as e:
            print(f"Ошибка при загрузке {fp.name}: {type(e).__name__} - {e}")
            continue
    print(f"Всего загружено таблиц: {table_count}")
    return tables

# Укажите пути к директориям
tables_dir = os.path.join(script_dir, 'Tables_for_models')
answers_dir = os.path.join(script_dir, 'Tables_for_models_answers')

# Загрузить таблицы
tables = load_tables(tables_dir, answers_dir)
table_dict = {t['file']: t for t in tables}

# Прочитать CSV
df = pd.read_csv(os.path.join(script_dir, 'detailed_results_with_responses.csv'))

# Добавить столбцы, если их нет
if 'pred_coords' not in df.columns:
    df['pred_coords'] = None
if 'precision' not in df.columns:
    df['precision'] = None
if 'recall' not in df.columns:
    df['recall'] = None
if 'f1' not in df.columns:
    df['f1'] = None

# Для каждой строки в df
for idx, row in df.iterrows():
    table_file = row['table_file']
    if table_file not in table_dict:
        print(f"Таблица {table_file} не найдена")
        continue
    table = table_dict[table_file]
    df_table = table['df']
    true_coords = eval(row['true_coords']) if isinstance(row['true_coords'], str) else row['true_coords']
    response = row['response']
    try:
        coords_pred = parse_output_coords(response, df_table)
        metrics = evaluate(coords_pred, true_coords)
        df.at[idx, 'pred_coords'] = str(coords_pred)
        df.at[idx, 'precision'] = metrics['precision']
        df.at[idx, 'recall'] = metrics['recall']
        df.at[idx, 'f1'] = metrics['f1']
    except Exception as e:
        print(f"Ошибка при обработке {table_file}: {type(e).__name__} - {e}")

# Преобразование столбца 'f1' в числовой тип
df['f1'] = pd.to_numeric(df['f1'], errors='coerce')

# Сохранить в Excel
df.to_excel(os.path.join(script_dir, 'detailed_results_coords.xlsx'), index=False)

# Анализ и построение графиков
# Проверка наличия данных
if df['f1'].isna().all():
    print("Все значения 'f1' являются NaN. Невозможно построить графики.")
else:
    # Тепловая карта F1
    pivot = df.pivot_table(values='f1', index='model', columns='prompt_idx', aggfunc='mean')
    plt.figure(figsize=(20, 16))
    sns.heatmap(pivot, annot=True, fmt='.2f', cmap='YlGnBu')
    plt.title('Среднее значение F1 по моделям и промптам')
    plt.xlabel('Индекс промпта')
    plt.ylabel('Модель')
    plt.savefig(os.path.join(script_dir, 'heatmap_f1.png'))
    plt.close()

    # Ящик с усами F1 по моделям
    plt.figure(figsize=(20, 14))
    sns.boxplot(x='model', y='f1', data=df)
    plt.xticks(rotation=45)
    plt.title('Распределение F1 по моделям')
    plt.xlabel('Модель')
    plt.ylabel('F1')
    plt.savefig(os.path.join(script_dir, 'boxplot_f1.png'))
    plt.close()

    metrics = pivot.fillna(0)
    labels = list(metrics.columns)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, polar=True)
    for idx, model in enumerate(metrics.index):
        values = metrics.loc[model].tolist()
        values += values[:1]
        ax.plot(angles, values, label=model)
        ax.fill(angles, values, alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])
    ax.set_title('Радиальная диаграмма F1 по промптам')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.savefig(os.path.join(script_dir, 'radar_f1.png'))
    plt.close()
