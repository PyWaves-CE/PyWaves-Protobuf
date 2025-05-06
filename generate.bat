cd /d %~dp0
set PROTOC_VERSION=25.7
set PROTO_WAVES_VERSION=1.5.2

set PROTOC_URL=https://github.com/protocolbuffers/protobuf/releases/download/v%PROTOC_VERSION%/
set PROTOC_ARCH=protoc-%PROTOC_VERSION%-win32.zip
set PROTO_WAVES_URL=https://github.com/wavesplatform/protobuf-schemas/archive/
set PROTO_WAVES_ARCH=v%PROTO_WAVES_VERSION%.zip

set PROTO_OUT=out
set PROTO_TEMP=protobuf-%random%%random%
set PROTO_FINAL=waves

mkdir %PROTO_TEMP%
cd %PROTO_TEMP%

curl -fsSL -o %PROTOC_ARCH% %PROTOC_URL%%PROTOC_ARCH%
7z x %PROTOC_ARCH% -aoa

curl -fsSL -o %PROTO_WAVES_ARCH% %PROTO_WAVES_URL%%PROTO_WAVES_ARCH%
7z x %PROTO_WAVES_ARCH% -aoa

mkdir %PROTO_OUT%
FOR /R "protobuf-schemas-%PROTO_WAVES_VERSION%\proto\%PROTO_FINAL%" %%f IN (*.proto) DO (
    bin\protoc --proto_path="%CD%\protobuf-schemas-%PROTO_WAVES_VERSION%\proto" --python_out=%PROTO_OUT% "%%f"
)

rmdir /s /q %PROTO_FINAL%
xcopy /s /y %PROTO_OUT%\%PROTO_FINAL% ..\%PROTO_FINAL%\
type nul > ..\%PROTO_FINAL%\__init__.py
cd ..
for /f %%n in ('dir /b /s "%PROTO_TEMP%\protobuf-schemas-%PROTO_WAVES_VERSION%\proto\%PROTO_FINAL%\*.proto" ^| find /c /v ""') do set PROTO_COUNT=%%n
for /f %%n in ('dir /b /s "%PROTO_FINAL%\*_pb2.py" ^| find /c /v ""') do set PY_COUNT=%%n
if NOT "%PROTO_COUNT%"=="%PY_COUNT%" (
    echo Error: Expected %PROTO_COUNT% compiled python files, but found %PY_COUNT%.
    pause
    exit /B 1
)
echo Success: All %PROTO_COUNT% protobuf files compiled successfully
timeout 10
rmdir /s /q %PROTO_TEMP%
pause
