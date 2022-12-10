from ilivalidator import Ilivalidator

jack = Ilivalidator('jack', '21')
jack.getAge()

valid = jack.validate('tests/data/254900.itf')
print("The file is valid: {}".format(valid))

#valid2 = jack.load2gpkg('tests/data/254900.itf')
