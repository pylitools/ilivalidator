from ilivalidator import Ilivalidator

TEST_DATA_PATH = "ilivalidator/tests/data/"

def test_validate_file_ok():
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml"])
    assert valid == True

def test_validate_multiple_files_ok():
    valid = False
    valid = Ilivalidator.validate([TEST_DATA_PATH+"/OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"])
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_ok():
    settings = {"allObjectsAccessible": True}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"], settings)
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_fail():
    settings = {"allObjectsAccessible": True}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen_missing_REF.xml"], settings)
    assert valid == False
