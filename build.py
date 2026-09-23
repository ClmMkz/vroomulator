"""Assemble le site publiable a partir de vroomulator.html."""
import io, pathlib
racine = pathlib.Path(__file__).parent
src = io.open(racine / 'vroomulator.html', encoding='utf-8').read()
site = racine / 'site'
site.mkdir(exist_ok=True)
page = '<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n' + src + '\n</html>\n'
io.open(site / 'index.html', 'w', encoding='utf-8', newline='\n').write(page)
(site / '.nojekyll').write_text('')
print('site/index.html :', len(page), 'caracteres')
