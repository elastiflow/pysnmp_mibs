# SNMP MIB module (DIGI-MODEMTEST-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MODEMTEST-TRAPS-MIB.mib
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

(digiModemTestTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiModemTestTraps")

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

_PortIndex_Type = Integer32
_PortIndex_Object = MibScalar
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 11),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortDescription_Type = DisplayString
_PortDescription_Object = MibScalar
portDescription = _PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 12),
    _PortDescription_Type()
)
portDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescription.setStatus("mandatory")
_PortPhoneNumber_Type = DisplayString
_PortPhoneNumber_Object = MibScalar
portPhoneNumber = _PortPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 13),
    _PortPhoneNumber_Type()
)
portPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPhoneNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

testModemSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 0, 1)
)
testModemSuccess.setObjects(
      *(("DIGI-MODEMTEST-TRAPS-MIB", "portIndex"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portDescription"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portPhoneNumber"))
)
if mibBuilder.loadTexts:
    testModemSuccess.setStatus(
        ""
    )

testModemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 0, 2)
)
testModemFailure.setObjects(
      *(("DIGI-MODEMTEST-TRAPS-MIB", "portIndex"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portDescription"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portPhoneNumber"))
)
if mibBuilder.loadTexts:
    testModemFailure.setStatus(
        ""
    )

testModemSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 1)
)
testModemSuccessNotification.setObjects(
      *(("DIGI-MODEMTEST-TRAPS-MIB", "portIndex"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portDescription"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portPhoneNumber"))
)
if mibBuilder.loadTexts:
    testModemSuccessNotification.setStatus(
        "current"
    )

testModemFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18, 2)
)
testModemFailureNotification.setObjects(
      *(("DIGI-MODEMTEST-TRAPS-MIB", "portIndex"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portDescription"),
        ("DIGI-MODEMTEST-TRAPS-MIB", "portPhoneNumber"))
)
if mibBuilder.loadTexts:
    testModemFailureNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MODEMTEST-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "testModemSuccess": testModemSuccess,
       "testModemFailure": testModemFailure,
       "testModemSuccessNotification": testModemSuccessNotification,
       "testModemFailureNotification": testModemFailureNotification,
       "portIndex": portIndex,
       "portDescription": portDescription,
       "portPhoneNumber": portPhoneNumber}
)
