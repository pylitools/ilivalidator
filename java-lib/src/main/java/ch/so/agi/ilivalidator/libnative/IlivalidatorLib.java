package ch.so.agi.ilivalidator.libnative;

import java.io.IOException;
import java.util.Map;

import org.graalvm.nativeimage.IsolateThread;
import org.graalvm.nativeimage.c.function.CEntryPoint;
import org.graalvm.nativeimage.c.type.CCharPointer;
import org.graalvm.nativeimage.c.type.CTypeConversion;
import org.interlis2.validator.Validator;

import com.fasterxml.jackson.databind.ObjectMapper;

import ch.ehi.basics.settings.Settings;

public class IlivalidatorLib {
    
    @CEntryPoint(name = "ilivalidator")
    public static boolean validate(IsolateThread thread, CCharPointer dataFilenames, CCharPointer options) {
        try {
            String[] xtfFile = CTypeConversion.toJavaString(dataFilenames).split(";");
            
            Settings settings = json2config(CTypeConversion.toJavaString(options));
            
            boolean valid = Validator.runValidation(xtfFile, settings);
            return valid;
        } catch (IOException e) {
            System.err.println(e.getMessage());
            return false;
        } catch (Exception e) {
            System.err.println(e.getMessage());
            return false;
        }
    }
    
    private static Settings json2config(String jsonString) throws IOException {
        var settings = new Settings();
        settings.setValue(Validator.SETTING_ILIDIRS, Validator.SETTING_DEFAULT_ILIDIRS);

        ObjectMapper mapper = new ObjectMapper();
        Map<String, Object> map = mapper.readValue(jsonString, Map.class);
        
        for (Map.Entry<String, Object> entry : map.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            if (key.equalsIgnoreCase("allObjectsAccessible")) {
                settings.setValue(Validator.SETTING_ALL_OBJECTS_ACCESSIBLE,Validator.TRUE);            
            }
        }
        return settings;
    }
        
    // Mmmmh, soll false auch möglich sein? Wie genau ist die API auf Python-Seite?
}
