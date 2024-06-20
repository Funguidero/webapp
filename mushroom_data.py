# mushroom_data.py

class Mushroom:
    def __init__(self, name=None, common_name=None, toxicity=None, habitat=None, season=None, other=None):
        self.name = name
        self.common_name = common_name
        self.toxicity = self.calc_tox(toxicity)
        self.habitat = habitat
        self.season = season
        self.other = other

    def calc_tox(self, tox):
        tox_icon = ''
        if tox == 'comestible':
            tox_color = 'green'
            tox_icon = '&#127812;'
        elif tox == 'tóxica':
            tox_color = 'orange'
            tox_icon = '&#9888'
        elif tox == 'mortal':
            tox_color = 'red'
            tox_icon = '&#9760;'
        else:
            tox_color = 'black'
        return f'{tox_icon} <span style="color:{tox_color}; font-weight: bold;">{tox.upper()}</span>'

mushroom_names = [
    'agaricus_campestris', 'amanita_bisporigera', 'amanita_caesarea', 'amanita_muscaria',
    'boletus_edulis', 'boletus_satanas', 'cantharellus_cibarius', 'cortinarius_orellanus',
    'gyromitra_esculenta', 'hygrophorus_russula', 'lactarius_deliciosus', 'lycoperdon_perlatum',
    'omphalotus_olearius', 'pleurotus_eryngii', 'russula_mariae'
]

dict_hongos = {
    'agaricus_campestris':
        Mushroom(
            name='Agaricus campestris',
            common_name='champiñón silvestre',
            toxicity='comestible',
            habitat='Praderas, campo abierto, pastizales abonados por ganado, jardines y pinares.',
            season='Primavera, abril - mayo. Posible segundo brote a final de verano y otoño.',
            other='Esta especie de champiñón, no se cultiva, pero es muy común. Sale en círculos o grupos numerosos.'),
    'amanita_muscaria':
        Mushroom(
            name='Amanita muscaria',
            common_name='matamoscas',
            toxicity='tóxica',
            habitat='Bosques de coníferas (alerces, pinos, abedules), encinares, castañares. También en hayedos, jarales y bosque de frondosas.',
            season='Otoño',
            other='Especie muy abundante'),
    'amanita_bisporigera':
        Mushroom(
            name='Amanita bisporigera',
            common_name='ángel de la muerte',
            toxicity='mortal'),
    'amanita_caesarea':
        Mushroom(
            name='Amanita caesarea',
            common_name='huevo del rey',
            toxicity='comestible',
            habitat='Claros soleados y zonas orientadas al sur de bosques de frondosas: roble (sobre todo), encina, haya, castaño. También en matorral Mediterráneo.',
            season='Si hay humedad, puede aparecer ya a finales de agosto. Dura todo el otoño.',
            other='Se trata de una especie más bien escasa. Sale en pequeños grupos.'),
    'boletus_edulis':
        Mushroom(
            name='Boletus edulis',
            common_name='boleto de calabaza',
            toxicity='comestible',
            habitat='Pinares, castañares, hayedos y robledales.',
            season='Verano - otoño, siendo muy abundante en otoños húmedos.',
            other='Son excelentes en múltiples preparaciones (incluso en crudo).'),
    'boletus_satanas':
        Mushroom(
            name='Boletus satanas',
            common_name='corvall del demoni',
            toxicity='tóxica',
            habitat='Prefiere la sombra de bosques caducifolios húmedos de castaños y robles. También crece entre alcornoques y madroños. Suelos calizos.',
            season='Final del verano o inicio de otoño.',
            other='Su ingesta produce síndrome gastrointestinal.'),
    'cantharellus_cibarius':
        Mushroom(
            name='Cantharellus cibarius',
            common_name='rebozuelo',
            toxicity='comestible',
            habitat='Hayas, castaños, robles, encinas, jaras, etc. También en campas, herbales, helechos…',
            season='Primavera a otoño.',
            other='Tiene alto valor culinario. Normalmente sale en grupos numerosos.'),
    'cortinarius_orellanus':
        Mushroom(
            name='Cortinarius orellanus',
            common_name='cortinario de montaña',
            toxicity='mortal',
            habitat='Robledal, latifolios y más raramente en coníferas de montaña.',
            season='Verano - otoño.'),
    'gyromitra_esculenta':
        Mushroom(
            name='Gyromitra esculenta',
            common_name='falsa colmenilla',
            toxicity='tóxica',
            habitat='Coníferas sobre todo, aunque también puede verse en caducifolios y en matorrales. Busca suelos con humus y a una altitud de más de 800 metros.',
            season='Primavera exclusivamente.',
            other='Aunque esculenta significa comestible, es mentira, produce síndrome giromitriano. Mortal en crudo. Para volatilizar la giromitrina, debe ser desecada, esperar 6 meses hasta cocerla y retirar el agua o hervirla mucho tiempo en agua, pero quedan toxinas precancerígenas.'),
    'hygrophorus_russula':
        Mushroom(
            name='Hygrophorus russula',
            common_name='rovellón escarlata',
            toxicity='comestible',
            habitat='Bajo bosques caducifolios o mixtos. Roble melojo y brezo. Lugares húmedos y sombríos. Climas cálidos.',
            season='Verano - otoño. Sale en grupo, bajo la hojarasca. Poco frecuente.',
            other='Tiene un sabor particularmente amargo. Apreciada en la cocina catalana.'),
    'lactarius_deliciosus':
        Mushroom(
            name='Lactarius deliciosus',
            common_name='níscalo',
            toxicity='comestible',
            habitat='Se asocia con las raíces de los árboles en bosques de coníferas o mixtos, especialmente los pinares de Insignis, en el país vasco y litoral cantábrico.',
            season='Verano - otoño.',
            other='Puede confundirse con otros tipos de níscalos no comestibles, para cerciorarte realiza un corte a la seta si su látex es anaranjado puedes comerla.'),
    'lycoperdon_perlatum':
        Mushroom(
            name='Lycoperdon perlatum',
            common_name='pedo de lobo',
            toxicity='comestible con precauciones',
            habitat='Todo tipo de bosques, con predilección por coníferas. En todos los ecosistemas.',
            season='En todas las estaciones.',
            other='Solo consumible si es joven y está cocinado.'),
    'omphalotus_olearius':
        Mushroom(
            name='Omphalotus olearius',
            common_name='seta de olivo',
            toxicity='tóxica',
            habitat='Olivos pero también sobre jaras pringosas, encinas, alcornoques, acacias, etc. Especie lignícola.',
            season='Otoño.',
            other='Genera síndrome gastrointestinal grave y alucinaciones.'),
    'pleurotus_eryngii':
        Mushroom(
            name='Pleurotus eryngii',
            common_name='seta de cardo',
            toxicity='comestible',
            habitat='Campos abiertos, praderas, barbechos, bordes de caminos, zonas planas desforestadas. Especie sometida a cultivo intensivo. Abunda en Castilla.',
            season='Primavera y otoño.',
            other='Tiene valor gastronómico.'),
    'russula_mariae':
        Mushroom(
            name='Russula mariae',
            toxicity='comestible',
            habitat='Bosques mixtos de coníferas (pino piñonero) y planifolios (roble, encina).',
            season='Verano – otoño.',
            other='Aunque comestible, se considera de mediocre calidad.'),
}
