## Jupyter Notebookで音声データを扱う

音声データはint16の配列だから多分NumPyでも扱える。

対話的にいじることができれば良さそうなのでJupyter Notebookが使えれば良さそう。

### テキトーに調べたら出てきたもの

* https://qiita.com/hisshi00/items/62c555095b8ff15f9dd2
* https://realpython.com/playing-and-recording-sound-python/
* https://algorithm.joho.info/programming/python/pydub-numpy/
* https://simpleaudio.readthedocs.io/en/latest/

### そういえばこれがあった

https://github.com/vinta/awesome-python#audio

### すごそう

https://github.com/tyiannak/pyAudioAnalysis

#### これを使うためには以下を呼んでおく必要あり(音声分析の基礎)

* https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y
* https://hackernoon.com/intro-to-audio-analysis-recognizing-sounds-using-machine-learning-qy2r3ufl

### ツール

* ffmpeg/libav - マルチメディアファイルを扱うオープンソースソフトウェア
* sox - オーディオの操作をコマンドラインでできるソフトウェア
* audacity - 音を編集するソフトウェア

### Pythonライブラリ

* pydub, scipy - オーディオデータの読込
* librosa - オーディオデータの分析
* plotly - プロット
* pyAudioAnalysis - オーディオデータの分析(more advenced)
