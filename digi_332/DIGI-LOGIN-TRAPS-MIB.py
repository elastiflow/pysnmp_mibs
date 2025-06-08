# SNMP MIB module (DIGI-LOGIN-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-LOGIN-TRAPS-MIB.mib
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

(digiLoginTraps,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiLoginTraps")

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

_LoginName_Type = DisplayString
_LoginName_Object = MibScalar
loginName = _LoginName_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 11),
    _LoginName_Type()
)
loginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginName.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibScalar
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 12),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortDescription_Type = DisplayString
_PortDescription_Object = MibScalar
portDescription = _PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 13),
    _PortDescription_Type()
)
portDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

loginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 0, 1)
)
loginSuccess.setObjects(
    ("DIGI-LOGIN-TRAPS-MIB", "loginName")
)
if mibBuilder.loadTexts:
    loginSuccess.setStatus(
        ""
    )

loginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 0, 2)
)
loginFailure.setObjects(
    ("DIGI-LOGIN-TRAPS-MIB", "loginName")
)
if mibBuilder.loadTexts:
    loginFailure.setStatus(
        ""
    )

loginConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 0, 3)
)
loginConnection.setObjects(
      *(("DIGI-LOGIN-TRAPS-MIB", "loginName"),
        ("DIGI-LOGIN-TRAPS-MIB", "portIndex"),
        ("DIGI-LOGIN-TRAPS-MIB", "portDescription"))
)
if mibBuilder.loadTexts:
    loginConnection.setStatus(
        ""
    )

loginSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 1)
)
loginSuccessNotification.setObjects(
    ("DIGI-LOGIN-TRAPS-MIB", "loginName")
)
if mibBuilder.loadTexts:
    loginSuccessNotification.setStatus(
        "current"
    )

loginFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 2)
)
loginFailureNotification.setObjects(
    ("DIGI-LOGIN-TRAPS-MIB", "loginName")
)
if mibBuilder.loadTexts:
    loginFailureNotification.setStatus(
        "current"
    )

loginConnectionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14, 3)
)
loginConnectionNotification.setObjects(
      *(("DIGI-LOGIN-TRAPS-MIB", "loginName"),
        ("DIGI-LOGIN-TRAPS-MIB", "portIndex"),
        ("DIGI-LOGIN-TRAPS-MIB", "portDescription"))
)
if mibBuilder.loadTexts:
    loginConnectionNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-LOGIN-TRAPS-MIB",
    **{"DisplayString": DisplayString,
       "loginSuccess": loginSuccess,
       "loginFailure": loginFailure,
       "loginConnection": loginConnection,
       "loginSuccessNotification": loginSuccessNotification,
       "loginFailureNotification": loginFailureNotification,
       "loginConnectionNotification": loginConnectionNotification,
       "loginName": loginName,
       "portIndex": portIndex,
       "portDescription": portDescription}
)
