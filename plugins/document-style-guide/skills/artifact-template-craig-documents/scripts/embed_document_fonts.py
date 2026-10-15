from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
from uuid import uuid4

def embed_fonts(docx_path, fonts_dir):
    """Embed the retained OFL Montserrat weights in the editable Word master."""
    docx_path=Path(docx_path); fonts_dir=Path(fonts_dir)
    with ZipFile(docx_path) as z: parts={n:z.read(n) for n in z.namelist()}
    w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    r='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    rel='http://schemas.openxmlformats.org/package/2006/relationships'
    ct='http://schemas.openxmlformats.org/package/2006/content-types'
    table=etree.fromstring(parts['word/fontTable.xml'])
    relpath='word/_rels/fontTable.xml.rels'
    relationships=etree.fromstring(parts[relpath]) if relpath in parts else etree.Element('{%s}Relationships'%rel,nsmap={None:rel})
    types=etree.fromstring(parts['[Content_Types].xml'])
    for i,(name,file) in enumerate([('Montserrat Black','Montserrat-Black.ttf'),('Montserrat Light','Montserrat-Light.ttf'),('Montserrat','Montserrat-Regular.ttf'),('Montserrat SemiBold','Montserrat-SemiBold.ttf')],1):
        font=next((f for f in table if f.get('{%s}name'%w)==name),None)
        if font is None: font=etree.SubElement(table,'{%s}font'%w,{'{%s}name'%w:name})
        guid=uuid4(); key=guid.bytes[::-1]
        for old in list(font):
            if old.tag=='{%s}embedRegular'%w: font.remove(old)
        rid=f'rIdCraigFont{i}'
        for old in list(relationships):
            if old.get('Id')==rid: relationships.remove(old)
        payload=bytearray((fonts_dir/file).read_bytes())
        for pos in range(32): payload[pos]^=key[pos%16]
        filename=f'montserrat-{i}.odttf'; rid=f'rIdCraigFont{i}'
        parts['word/fonts/'+filename]=bytes(payload)
        etree.SubElement(font,'{%s}embedRegular'%w,{'{%s}id'%r:rid,'{%s}fontKey'%w:'{'+str(guid).upper()+'}'})
        etree.SubElement(relationships,'{%s}Relationship'%rel,Id=rid,Type=r+'/font',Target='fonts/'+filename)
    if not any(e.get('Extension')=='odttf' for e in types):
        etree.SubElement(types,'{%s}Default'%ct,Extension='odttf',ContentType='application/vnd.openxmlformats-officedocument.obfuscatedFont')
    for path,node in [('word/fontTable.xml',table),(relpath,relationships),('[Content_Types].xml',types)]:
        parts[path]=etree.tostring(node,xml_declaration=True,encoding='UTF-8',standalone=True)
    with ZipFile(docx_path,'w',ZIP_DEFLATED) as z:
        for name,data in parts.items(): z.writestr(name,data)

if __name__=='__main__':
    import sys
    embed_fonts(sys.argv[1],sys.argv[2])
