# SNMP MIB module (DIGI-MOBILE-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MOBILE-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(digiMobileTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiMobileTraps")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MobileAlarmSubject_Type = DisplayString
_MobileAlarmSubject_Object = MibScalar
mobileAlarmSubject = _MobileAlarmSubject_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 11),
    _MobileAlarmSubject_Type()
)
mobileAlarmSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileAlarmSubject.setStatus("mandatory")
_MobileInterface_Type = Integer32
_MobileInterface_Object = MibScalar
mobileInterface = _MobileInterface_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 12),
    _MobileInterface_Type()
)
mobileInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileInterface.setStatus("mandatory")
_MobileName_Type = DisplayString
_MobileName_Object = MibScalar
mobileName = _MobileName_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 13),
    _MobileName_Type()
)
mobileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileName.setStatus("mandatory")
_MobileValue_Type = DisplayString
_MobileValue_Object = MibScalar
mobileValue = _MobileValue_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 14),
    _MobileValue_Type()
)
mobileValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mobileSuboptimal = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 0, 1)
)
mobileSuboptimal.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileName"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileValue"))
)
if mibBuilder.loadTexts:
    mobileSuboptimal.setStatus(
        ""
    )

mobileOptimal = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 0, 2)
)
mobileOptimal.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileName"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileValue"))
)
if mibBuilder.loadTexts:
    mobileOptimal.setStatus(
        ""
    )

mobileConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 0, 3)
)
mobileConfigurationChange.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileConfigurationChange.setStatus(
        ""
    )

mobileSignalStrengthThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 0, 4)
)
mobileSignalStrengthThreshold.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileSignalStrengthThreshold.setStatus(
        ""
    )

mobileDataThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 0, 5)
)
mobileDataThreshold.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileDataThreshold.setStatus(
        ""
    )

mobileSuboptimalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 1)
)
mobileSuboptimalNotification.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileName"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileValue"))
)
if mibBuilder.loadTexts:
    mobileSuboptimalNotification.setStatus(
        "current"
    )

mobileOptimalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 2)
)
mobileOptimalNotification.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileName"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileValue"))
)
if mibBuilder.loadTexts:
    mobileOptimalNotification.setStatus(
        "current"
    )

mobileConfigurationChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 3)
)
mobileConfigurationChangeNotification.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileConfigurationChangeNotification.setStatus(
        "current"
    )

mobileSignalStrengthThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 4)
)
mobileSignalStrengthThresholdNotification.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileSignalStrengthThresholdNotification.setStatus(
        "current"
    )

mobileDataThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24, 5)
)
mobileDataThresholdNotification.setObjects(
      *(("DIGI-MOBILE-TRAPS-MIB", "mobileAlarmSubject"),
        ("DIGI-MOBILE-TRAPS-MIB", "mobileInterface"))
)
if mibBuilder.loadTexts:
    mobileDataThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MOBILE-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "mobileSuboptimal": mobileSuboptimal,
       "mobileOptimal": mobileOptimal,
       "mobileConfigurationChange": mobileConfigurationChange,
       "mobileSignalStrengthThreshold": mobileSignalStrengthThreshold,
       "mobileDataThreshold": mobileDataThreshold,
       "mobileSuboptimalNotification": mobileSuboptimalNotification,
       "mobileOptimalNotification": mobileOptimalNotification,
       "mobileConfigurationChangeNotification": mobileConfigurationChangeNotification,
       "mobileSignalStrengthThresholdNotification": mobileSignalStrengthThresholdNotification,
       "mobileDataThresholdNotification": mobileDataThresholdNotification,
       "mobileAlarmSubject": mobileAlarmSubject,
       "mobileInterface": mobileInterface,
       "mobileName": mobileName,
       "mobileValue": mobileValue}
)
