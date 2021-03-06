{
  'targets': [
    {
      'target_name': 'canvas',
      'sources': [
        'src/backend/Backend.cc',
        'src/backend/ImageBackend.cc',
        'src/backend/PdfBackend.cc',
        'src/backend/SvgBackend.cc',
        'src/bmp/BMPParser.cc',
        'src/Backends.cc',
        'src/Canvas.cc',
        'src/CanvasGradient.cc',
        'src/CanvasPattern.cc',
        'src/CanvasRenderingContext2d.cc',
        'src/closure.cc',
        'src/color.cc',
        'src/Image.cc',
        'src/ImageData.cc',
        'src/init.cc',
        'src/register_font.cc'
      ],
      'defines': [
        'HAVE_GIF',
        'HAVE_JPEG',
        'HAVE_RSVG',
        'HAVE_BOOLEAN', # or jmorecfg.h tries to define it
        '_USE_MATH_DEFINES' # for M_PI
      ],
      'libraries': [
        'C:/msys64/mingw32/lib/libcairo-2.lib',
        'C:/msys64/mingw32/lib/libpng16-16.lib',
        'C:/msys64/mingw32/lib/libjpeg-8.lib',
        'C:/msys64/mingw32/lib/libpango-1.0-0.lib',
        'C:/msys64/mingw32/lib/libpangocairo-1.0-0.lib',
        'C:/msys64/mingw32/lib/libgobject-2.0-0.lib',
        'C:/msys64/mingw32/lib/libglib-2.0-0.lib',
        'C:/msys64/mingw32/lib/libturbojpeg.lib',
        'C:/msys64/mingw32/lib/libgif-7.lib',
        'C:/msys64/mingw32/lib/libfreetype-6.lib',
        'C:/msys64/mingw32/lib/librsvg-2-2.lib'
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        'C:/msys64/mingw32/include',
        'C:/msys64/mingw32/include/pango-1.0',
        'C:/msys64/mingw32/include/cairo',
        'C:/msys64/mingw32/include/libpng16',
        'C:/msys64/mingw32/include/glib-2.0',
        'C:/msys64/mingw32/lib/glib-2.0/include',
        'C:/msys64/mingw32/include/pixman-1',
        'C:/msys64/mingw32/include/freetype2',
        'C:/msys64/mingw32/include/fontconfig',
        'C:/msys64/mingw32/include/librsvg-2.0',
        'C:/msys64/mingw32/include/gdk-pixbuf-2.0'
      ],
      'configurations': {
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarningLevel': 4,
              'ExceptionHandling': 1,
              'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714, 4512]
            }
          }
        },
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarningLevel': 4,
              'ExceptionHandling': 1,
              'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714, 4512]
            }
          }
        }
      }
    }
  ]
}
