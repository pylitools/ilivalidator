package ch.so.agi.ilivalidator.libnative;

import org.interlis2.validator.Validator;
import org.junit.jupiter.api.Test;

import ch.ehi.basics.settings.Settings;

import static org.junit.jupiter.api.Assertions.*;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class IlivalidatorLibTest {
        
    @Test
    public void parseJsonString_Ok() throws IOException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException {
        String jsonString = "{\n"
                + "    \""+Validator.SETTING_ALL_OBJECTS_ACCESSIBLE+"\": true,\n"
                + "    \"trace\": true,\n"
                + "    \""+Validator.SETTING_MODELNAMES+"\": \"ModelA\",\n"
                + "    \""+Validator.SETTING_ILIDIRS+"\": \".;https://models.geo.admin.ch\",\n"                
                + "    \""+Validator.SETTING_LOGFILE+"\": \"mylog.log\",\n"
                + "    \""+Validator.SETTING_LOGFILE_TIMESTAMP+"\": true,\n"
                + "    \""+Validator.SETTING_XTFLOG+"\": \"mylog.log.xtf\"\n"
                + "}";
        
        Settings settings = (Settings) getJson2ConfigMethod().invoke(null, jsonString);
        
        assertEquals("true", settings.getValue(Validator.SETTING_ALL_OBJECTS_ACCESSIBLE));
        assertEquals("ModelA", settings.getValue(Validator.SETTING_MODELNAMES));
        assertEquals(".;https://models.geo.admin.ch", settings.getValue(Validator.SETTING_ILIDIRS));
        assertEquals("mylog.log", settings.getValue(Validator.SETTING_LOGFILE));
        assertEquals("true", settings.getValue(Validator.SETTING_LOGFILE_TIMESTAMP));
        assertEquals("mylog.log.xtf", settings.getValue(Validator.SETTING_XTFLOG));
    }
    
    private Method getJson2ConfigMethod() throws NoSuchMethodException {
        Method method = IlivalidatorLib.class.getDeclaredMethod("json2config", String.class);
        method.setAccessible(true);
        return method;
    }
}
