from ilivalidator import Ilivalidator
import os
import tempfile

TEST_DATA_PATH = "ilivalidator/tests/data/"

def test_validate_file_ok():
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml"])
    assert valid == True

def test_validate_multiple_files_ok():
    valid = Ilivalidator.validate([TEST_DATA_PATH+"/OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"])
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_on_ok():
    settings = {Ilivalidator.SETTING_ALL_OBJECTS_ACCESSIBLE: True}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"], settings)
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_on_fail():
    settings = {Ilivalidator.SETTING_ALL_OBJECTS_ACCESSIBLE: True}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen_missing_REF.xml"], settings)
    assert valid == False

def test_validate_multiple_files_allobjectsaccessible_off_ok():
    settings = {Ilivalidator.SETTING_ALL_OBJECTS_ACCESSIBLE: False}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen_missing_REF.xml"], settings)
    assert valid == True

def test_validate_logfiles_on_ok():
    temp_dir = tempfile.TemporaryDirectory()
    log_file = os.path.join(temp_dir.name, "mylog.log")
    xtf_log_file = log_file + ".xtf"

    settings = {Ilivalidator.SETTING_LOGFILE: log_file, Ilivalidator.SETTING_LOGFILE_TIMESTAMP: True, Ilivalidator.SETTING_XTFLOG: xtf_log_file}
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml"], settings)
    assert valid == True

    with open(log_file, 'r') as file:
        content = file.read()
        assert -1 != content.find("Info: ...validation done")

    with open(xtf_log_file, 'r') as file:
        content = file.read()
        assert -1 != content.find("<Message>...validation done</Message>")