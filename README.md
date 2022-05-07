# README

## install

```bash

vim ~/.bash_profile

export TESSDATA_PREFIX=/usr/local/share/tessdata

source ~/.bash_profile

echo $TESSDATA_PREFIX

brew install automake autoconf libtool
brew install pkgconfig
brew install pkgconfig
brew install leptonica
brew install pango
brew install libarchive
brew install gcc

git clone https://github.com/tesseract-ocr/tesseract/

cd tesseract/
./autogen.sh
xcode-select --install
./configure
make -j4
sudo make install
make training
sudo make training-install
curl -o /usr/local/share/tessdata/eng.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/master/eng.traineddata
python main.py img/1.png


```


## reference

* [树洞 OCR 文字识别（一款跨平台的 OCR 小工具）(https://github.com/AnyListen/tools-ocr)

* [macOS with Homebrew](https://tesseract-ocr.github.io/tessdoc/Compiling.html#macos)

* [pytorch应用之——纸币识别（一）](https://blog.csdn.net/litt1e/article/details/90399524)

* [Tesseract running error](https://stackoverflow.com/questions/14800730/tesseract-running-error)

* [Tesseract Open Source OCR Engine (main repository)](https://github.com/tesseract-ocr/tesseract)

* [Improving the quality of the output](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)




