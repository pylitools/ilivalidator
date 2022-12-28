package ch.so.agi.ilivalidator.libnative;

import java.io.IOException;
import java.util.Map;

import org.graalvm.nativeimage.IsolateThread;
import org.graalvm.nativeimage.c.function.CEntryPoint;
import org.graalvm.nativeimage.c.type.CCharPointer;
import org.graalvm.nativeimage.c.type.CTypeConversion;
import org.interlis2.validator.Validator;

import com.fasterxml.jackson.databind.ObjectMapper;

import ch.ehi.basics.logging.EhiLogger;
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

            if (key.equalsIgnoreCase(Validator.SETTING_ALL_OBJECTS_ACCESSIBLE)) {
                String value = ((boolean) entry.getValue()) ? Validator.TRUE : Validator.FALSE;
                settings.setValue(Validator.SETTING_ALL_OBJECTS_ACCESSIBLE,value);            
            } else if (key.equalsIgnoreCase("trace")) {
                if ((boolean) entry.getValue()) {
                    EhiLogger.getInstance().setTraceFilter(false);
                }
            } else if (key.equalsIgnoreCase(Validator.SETTING_MODELNAMES)) {
                String value = ((String) entry.getValue());
                if (value != null) {
                    settings.setValue(Validator.SETTING_MODELNAMES,value);            
                } 
            } else if (key.equalsIgnoreCase(Validator.SETTING_ILIDIRS)) {
                String value = ((String) entry.getValue());
                if (value != null) {
                    settings.setValue(Validator.SETTING_ILIDIRS,value);            
                }
            } else if (key.equalsIgnoreCase(Validator.SETTING_LOGFILE)) {
                String value = ((String) entry.getValue());
                if (value != null) {
                    settings.setValue(Validator.SETTING_LOGFILE,value);            
                }
            } else if (key.equalsIgnoreCase(Validator.SETTING_LOGFILE_TIMESTAMP)) {
                String value = ((boolean) entry.getValue()) ? Validator.TRUE : Validator.FALSE;
                if (value != null) {
                    settings.setValue(Validator.SETTING_LOGFILE_TIMESTAMP,value);            
                }
            } else if (key.equalsIgnoreCase(Validator.SETTING_XTFLOG)) {
                String value = ((String) entry.getValue());
                if (value != null) {
                    settings.setValue(Validator.SETTING_XTFLOG,value);            
                }
            }
        }
        return settings;
    }
    
    //public static final String SETTING_TRACE = "trace";
}
