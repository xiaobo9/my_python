import cairosvg

# CairoSVG doesn't automatically find fallback fonts when the default font misses some characters.
# Please try to set a font-family property (with a font with Chinese characters), it should work.
cairosvg.svg2png(url='resources/favicon.svg', write_to='resources/favicon.png')
