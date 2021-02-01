# expects node, VS, and MSYS environments to be set up already. does everything else.

deps="cairo-2 png16-16 jpeg-8 pango-1.0-0 pangocairo-1.0-0 gobject-2.0-0 glib-2.0-0 turbojpeg gif-7 freetype-6 rsvg-2-2";

# install cairo and tools to create .lib

pacman --noconfirm -S \
  wget \
  unzip \
  mingw32/mingw-w64-i686-binutils \
  mingw32/mingw-w64-i686-tools \
  mingw32/mingw-w64-i686-libjpeg-turbo \
  mingw32/mingw-w64-i686-pango \
  mingw32/mingw-w64-i686-cairo \
  mingw32/mingw-w64-i686-giflib \
  mingw32/mingw-w64-i686-freetype \
  mingw32/mingw-w64-i686-fontconfig \
  mingw32/mingw-w64-i686-librsvg \
  mingw32/mingw-w64-i686-libxml2

# create .lib files for vc++



echo "generating lib files for the MSYS2 dlls"
for lib in $deps; do
  /mingw32/bin/gendef /mingw32/bin/lib$lib.dll > /dev/null 2>&1 || {
    echo "could not find lib$lib.dll, have to skip ";
    continue;
  }

   /mingw32/bin/dlltool -d lib$lib.def -l /mingw32/lib/lib$lib.lib > /dev/null 2>&1 || {
    echo "could not create dll for lib$lib.dll";
    continue;
  }

  echo "created lib$lib.lib from lib$lib.dll";

  rm lib$lib.def
done
