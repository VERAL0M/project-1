import g4f #Импорт библиотеки

def res(text):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
            stream=True,
        )
        for message in response:
            answer= message
        return answer
    except:
        text="Пожалуйтса введите корректный запрос"
        return text
