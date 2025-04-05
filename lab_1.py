import numpy as np
import pandas as pd

comment = ["Эта идея хорошо подходит для нашего проекта, молодцы!",
           "Хорошо, что вы подняли эту тему, она очень важна!",
           "Мне нравится, как вы изложили свои мысли, очень хорошо!",
           "К сожалению, ситуация здесь выглядит плохо, есть над чем поработать.",
           "Плохо, что такие мнения появляются, это не конструктивно.",
           "Увы, реализация идеи вышла плохо, нужно больше усилий!"]
np.random.seed(3)
like = np.random.randint(100, 600, (6, ))
repost = np.random.randint(10, 60, (6, ))
view = np.random.randint(500, 2500, (6, ))



# 1. Проанализировать список comment. Посчитать количество символов и слов в каждом комментарии.
for i, com in enumerate (comment):
    num_words = len(com.split())
    num_symb = len(com)
    print(f"\nКоличество cлов в комментарии №{i+1}: {num_words}; Символов: {num_symb};")

# 2. Проанализировать список comment. Вывести на экран индекс комментария
# и напротив его тональность. (Если есть слово "хорошо", то тональность 
# положительная, если есть слово "плохо", то тональность отрицательная)
for i, com in enumerate (comment):
    if "хорошо" in com.lower():   # lower игнорирует регистр
        print (f"\nКомментарий {i+1}: Тональность положительная! :)")
    elif "плохо" in com.lower():
        print (f"\nКомментарий {i+1}: Тональность отрицательная! :(")
    else:
        print (f"\nКомментарий {i+1}: Тональность не определена!")
    
# 3. Создать DataFrame из списков comment, like, repost, view с идентичными названиями колонок
data = {"comment": comment,
        "like": like,
        "repost": repost,
        "view": view}
comments_df = pd.DataFrame(data)
print (comments_df)


# 4. Вывести на экран комментарий, у которого больше всего лайков.
print("\nМаксимальное количество комментариев:")
print(comments_df[comments_df['like'] == comments_df['like'].max()]) 


# 5. Посчитать для каждого комментария оценку вовлеченности ((like + repost)/view)

for i, com in comments_df.iterrows(): # позволяет обратиться к строке целиком
    mark = (com['like'] + com['repost']) / com['view']
    print(f"\nКомментарий {i + 1}: Оценка вовлеченности = {mark:.2f}")