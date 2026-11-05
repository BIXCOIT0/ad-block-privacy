from html.parser import HTMLParser
from pathlib import Path
import tempfile, unittest
from render_privacy import ROOT, render, inline

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[];self.links=[];self.sections={};self.tags=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs);self.tags.append(tag)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='a':self.links.append(attrs.get('href',''))
        if tag=='section':self.sections[attrs['id']]=attrs.get('lang')

class PrivacyTests(unittest.TestCase):
    def test_generated_and_structure(self):
        text=(ROOT/'index.html').read_text();self.assertEqual(text,render())
        doc=Document();doc.feed(text);self.assertNotIn('pre',doc.tags);self.assertNotIn('script',doc.tags)
        self.assertEqual(doc.sections,{'pt':'pt-BR','en':'en'});self.assertEqual(len(doc.ids),len(set(doc.ids)))
        self.assertEqual(doc.tags.count('h1'),1)
        for link in doc.links:
            if link.startswith('#'):self.assertIn(link[1:],doc.ids)
            elif not link.startswith(('https://','http://')):self.assertTrue((ROOT/link).is_file(),link)
    def test_version_scope_and_topics(self):
        pt=(ROOT/'PRIVACY.md').read_text();en=(ROOT/'PRIVACY.en.md').read_text()
        self.assertEqual(pt.count('\n## '),en.count('\n## '))
        for token in ['0.9.14','0.9.16','pageObservedCounts','pendingMatchBatch','SHA-256','Web3Forms','128','50']:
            self.assertIn(token,pt);self.assertIn(token,en)
    def test_escape_and_safe_links(self):
        self.assertEqual(inline('<script>alert(1)</script>'),'&lt;script&gt;alert(1)&lt;/script&gt;')
        self.assertNotIn('<a',inline('[bad](javascript:alert)'))
        self.assertEqual(inline('https://example.test/path.'),'<a href="https://example.test/path">https://example.test/path</a>.')
        self.assertIn('&amp;',inline('[x](https://example.test/?a=1&b=2)'))
    def test_source_change_requires_new_html(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            for name in ['PRIVACY.md','PRIVACY.en.md']:(root/name).write_text((ROOT/name).read_text())
            before=render(root);p=root/'PRIVACY.md';p.write_text(p.read_text()+'\nNew paragraph.\n')
            self.assertNotEqual(before,render(root))

if __name__=='__main__':unittest.main()
