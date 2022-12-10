package ch.so.agi.ilivalidator.libnative;

import org.graalvm.nativeimage.IsolateThread;
import org.graalvm.nativeimage.c.function.CEntryPoint;
import org.graalvm.nativeimage.c.type.CCharPointer;
import org.graalvm.nativeimage.c.type.CTypeConversion;
import org.interlis2.validator.Validator;

import ch.ehi.basics.settings.Settings;

public class IlivalidatorLib {
    
    @CEntryPoint(name = "ilivalidator")
    public static boolean validate(IsolateThread thread, CCharPointer dataFilename) {
        var settings = new Settings();
        boolean valid = Validator.runValidation(CTypeConversion.toJavaString(dataFilename), settings);
        return valid;
    }
}
