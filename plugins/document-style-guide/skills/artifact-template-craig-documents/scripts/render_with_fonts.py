"""Render a document with this template's retained Montserrat fonts."""
# Visual source: https://www.magnific.com/free-vector/gradient-annual-report-cover-template_2446649.htm
# Graphic component guidance: ../references/visual-components.md
import argparse
import os
from pathlib import Path
import subprocess
import sys
from xml.sax.saxutils import escape

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('document')
    parser.add_argument('--renderer',required=True)
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--font-dir',default=str(Path(__file__).resolve().parents[1]/'assets/fonts'))
    args=parser.parse_args()
    output=Path(args.output_dir).resolve(); output.mkdir(parents=True,exist_ok=True)
    fonts=Path(args.font_dir).resolve()
    if not all((fonts/name).is_file() for name in ['Montserrat-Black.ttf','Montserrat-Light.ttf','Montserrat-Regular.ttf','Montserrat-SemiBold.ttf']):
        raise SystemExit('Retained Montserrat font files are missing')
    deps=Path(sys.executable).parent.parent.parent
    paths=[fonts,Path('/System/Library/Fonts'),Path('/System/Library/Fonts/Supplemental'),Path('/usr/share/fonts'),deps/'native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype']
    config=output/'render-fonts.conf'
    config.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd"><fontconfig>'+''.join('<dir>'+escape(str(p))+'</dir>' for p in paths if p.exists())+'<cachedir>'+escape(str(output/'font-cache'))+'</cachedir></fontconfig>')
    env=os.environ.copy(); env['FONTCONFIG_FILE']=str(config); env['SAL_FONTPATH']=str(fonts)
    subprocess.run([sys.executable,args.renderer,str(Path(args.document).resolve()),'--output_dir',str(output),'--emit_pdf'],env=env,check=True)

if __name__=='__main__': main()
