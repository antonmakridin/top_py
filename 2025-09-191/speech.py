from argparse import ArgumentParser

from speechkit import model_repository, configure_credentials, creds

# Authentication with an API key.
configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key=''
    )
)

def synthesize(text):
    model = model_repository.synthesis_model()

    # Specify the synthesis settings.
    model.voice = 'jane'
    model.role = 'good'

    # Performing speech synthesis and creating the output audio file.
    result = model.synthesize(text, raw_format=True)
    # result.export('2025-09-191\\test.wav', 'wav')
    # return result.export('2025-09-191\\test.wav', 'wav')
    return result

if __name__ == '__main__':
#    parser = ArgumentParser()
#    parser.add_argument('--text', type=str, help='text to synthesize', required=True)
#    parser.add_argument('--export', type=str, help='export path for synthesized audio', required=False)

#    args = parser.parse_args()

#    synthesize(args.text, args.export)
    text = 'привет, как дела?'
    file = '2025-09-191\\test.wav'
    synthesize(text, file)