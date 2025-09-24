from speechkit import model_repository
from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType

#  Authentication with an API key.
configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key=''
    )
)

def recognize(path):

    model = model_repository.recognition_model()

    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Full

    result = model.transcribe_file(path)

    return result