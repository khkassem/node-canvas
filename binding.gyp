{
      'variables': {
        'GTK_Root%': 'C:/GTK',  # Set the location of GTK all-in-one bundle
        },
    'targets': [
    {
      'target_name': 'canvas-postbuild',
      'dependencies': ['canvas'],
      'conditions': [
        ['OS=="win"', {
          'copies': [{
            'destination': '<(PRODUCT_DIR)',
            'files': [
                '<(GTK_Root)/bin/libbrotlicommon.dll',
                '<(GTK_Root)/bin/libbrotlidec.dll',
                '<(GTK_Root)/bin/libbz2-1.dll',
                '<(GTK_Root)/bin/libcairo-2.dll',
                '<(GTK_Root)/bin/libcairo-gobject-2.dll',
                '<(GTK_Root)/bin/libdatrie-1.dll',
                '<(GTK_Root)/bin/libexpat-1.dll',
                '<(GTK_Root)/bin/libffi-7.dll',
                '<(GTK_Root)/bin/libfontconfig-1.dll',
                '<(GTK_Root)/bin/libfreetype-6.dll',
                '<(GTK_Root)/bin/libfribidi-0.dll',
                '<(GTK_Root)/bin/libgcc_s_dw2-1.dll',
                '<(GTK_Root)/bin/libgdk_pixbuf-2.0-0.dll',
                '<(GTK_Root)/bin/libgif-7.dll',
                '<(GTK_Root)/bin/libgio-2.0-0.dll',
                '<(GTK_Root)/bin/libglib-2.0-0.dll',
                '<(GTK_Root)/bin/libgmodule-2.0-0.dll',
                '<(GTK_Root)/bin/libgobject-2.0-0.dll',
                '<(GTK_Root)/bin/libgraphite2.dll',
                '<(GTK_Root)/bin/libharfbuzz-0.dll',
                '<(GTK_Root)/bin/libiconv-2.dll',
                '<(GTK_Root)/bin/libintl-8.dll',
                '<(GTK_Root)/bin/libjpeg-8.dll',
                '<(GTK_Root)/bin/liblzma-5.dll',
                '<(GTK_Root)/bin/libpango-1.0-0.dll',
                '<(GTK_Root)/bin/libpangocairo-1.0-0.dll',
                '<(GTK_Root)/bin/libpangoft2-1.0-0.dll',
                '<(GTK_Root)/bin/libpangowin32-1.0-0.dll',
                '<(GTK_Root)/bin/libpcre-1.dll',
                '<(GTK_Root)/bin/libpixman-1-0.dll',
                '<(GTK_Root)/bin/libpng16-16.dll',
                '<(GTK_Root)/bin/librsvg-2-2.dll',
                '<(GTK_Root)/bin/libstdc++-6.dll',
                '<(GTK_Root)/bin/libthai-0.dll',
                '<(GTK_Root)/bin/libwinpthread-1.dll',
                '<(GTK_Root)/bin/libxml2-2.dll',
                '<(GTK_Root)/bin/zlib1.dll',

            ]
          }]
        }]
      ]
    },
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
        '<(GTK_Root)/lib/libcairo-2.lib',
        '<(GTK_Root)/lib/libpng16-16.lib',
        '<(GTK_Root)/lib/libjpeg-8.lib',
        '<(GTK_Root)/lib/libpango-1.0-0.lib',
        '<(GTK_Root)/lib/libpangocairo-1.0-0.lib',
        '<(GTK_Root)/lib/libgobject-2.0-0.lib',
        '<(GTK_Root)/lib/libglib-2.0-0.lib',
        '<(GTK_Root)/lib/libturbojpeg.lib',
        '<(GTK_Root)/lib/libgif-7.lib',
        '<(GTK_Root)/lib/libfreetype-6.lib',
        '<(GTK_Root)/lib/librsvg-2-2.lib'
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<(GTK_Root)/include',
        '<(GTK_Root)/include/harfbuzz',
        '<(GTK_Root)/include/pango-1.0',
        '<(GTK_Root)/include/cairo',
        '<(GTK_Root)/include/libpng16',
        '<(GTK_Root)/include/glib-2.0',
        '<(GTK_Root)/lib/glib-2.0/include',
        '<(GTK_Root)/include/pixman-1',
        '<(GTK_Root)/include/freetype2',
        '<(GTK_Root)/include/fontconfig',
        '<(GTK_Root)/include/librsvg-2.0',
        '<(GTK_Root)/include/gdk-pixbuf-2.0'
      ],
      'configurations': {
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarningLevel': 4,
              'ExceptionHandling': 1,
              'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714, 4512]
            }
          },
                    "msbuild_settings": {
                "Link": {
                    "ImageHasSafeExceptionHandlers": "false"
                }
            },
        },
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarningLevel': 4,
              'ExceptionHandling': 1,
              'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714, 4512]
            }
          },
          "msbuild_settings": {
                "Link": {
                    "ImageHasSafeExceptionHandlers": "false"
                }
            },
        }
      }
    }
  ]
}
