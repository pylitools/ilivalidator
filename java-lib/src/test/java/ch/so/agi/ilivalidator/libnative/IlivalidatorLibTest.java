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
                + "    \"allObjectsAccessible\": true\n"
                + "}";
        
        Settings settings = (Settings) getJson2ConfigMethod().invoke(null, jsonString);
        
        assertEquals("true", settings.getValue(Validator.SETTING_ALL_OBJECTS_ACCESSIBLE));
    }
    
    private Method getJson2ConfigMethod() throws NoSuchMethodException {
        Method method = IlivalidatorLib.class.getDeclaredMethod("json2config", String.class);
        method.setAccessible(true);
        return method;
    }
}
