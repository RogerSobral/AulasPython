import speech_recognition as sr

# Reconhecedor do que se fala e transforma em texto
rec = sr.Recognizer()

# print(sr.Microphone().list_microphone_names()) aponta a lista de mic no aparelho

with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    # tratar os ruidos
    print("pode falar que vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
    match texto:
        case "cadastrar":
            print("Estamos no menu cadastrar")
        case "salvar":
            print("Salvando o arquivo")
