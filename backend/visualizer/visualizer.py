import librosa
# for error libc++abi: terminating due to uncaught exception of type NSException
import matplotlib
matplotlib.use('Agg') 
#
import matplotlib.pyplot as plt
import io
from django.core.files.images import ImageFile


def visualizer(input):
    y, sr = librosa.load(input)

    Y = librosa.stft(y)
    Ydb = librosa.amplitude_to_db(abs(Y))
    fig, ax = plt.subplots()
    img = librosa.display.specshow(Ydb, sr=sr, x_axis='time', y_axis='hz', ax=ax)
    fig.colorbar(img, ax=ax)

    result = io.BytesIO()
    plt.savefig(result, format="png")
    return ImageFile(result)

    # if we are using pillow, we may do this
    # result = io.BytesIO()
    # canvas = Image.new('RGB', (512, 512), 'white')
    # canvas.save(result, 'png')
    # return ImageFile(result)
