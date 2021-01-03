set -ex

copies=$(lddtree.sh -l build/Release/canvas.node | sed -r -e '/^\/lib/d' -e '/canvas.node$/d');

apt install -y patchelf

for so in $copies; do
  cp $so build/Release
  patchelf --set-rpath '$ORIGIN' build/Release/$(basename $so)
done;
