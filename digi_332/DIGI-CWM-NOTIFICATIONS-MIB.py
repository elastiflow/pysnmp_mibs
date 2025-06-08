# SNMP MIB module (DIGI-CWM-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-CWM-NOTIFICATIONS-MIB.mib
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

(didContact,
 didDescription,
 didDeviceID,
 didLocation) = mibBuilder.importSymbols(
    "DIGI-DEVICE-IDENT",
    "didContact",
    "didDescription",
    "didDeviceID",
    "didLocation")

(digiCwmNotifications,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiCwmNotifications")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

mgmtLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 100, 1)
)
mgmtLinkDown.setObjects(
      *(("DIGI-DEVICE-IDENT", "didDeviceID"),
        ("DIGI-DEVICE-IDENT", "didContact"),
        ("DIGI-DEVICE-IDENT", "didLocation"),
        ("DIGI-DEVICE-IDENT", "didDescription"))
)
if mibBuilder.loadTexts:
    mgmtLinkDown.setStatus(
        "current"
    )

lowRSSI = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 100, 2)
)
lowRSSI.setObjects(
      *(("DIGI-DEVICE-IDENT", "didDeviceID"),
        ("DIGI-DEVICE-IDENT", "didContact"),
        ("DIGI-DEVICE-IDENT", "didLocation"),
        ("DIGI-DEVICE-IDENT", "didDescription"))
)
if mibBuilder.loadTexts:
    lowRSSI.setStatus(
        "current"
    )

serialDataPatternMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 100, 3)
)
serialDataPatternMatch.setObjects(
      *(("DIGI-DEVICE-IDENT", "didDeviceID"),
        ("DIGI-DEVICE-IDENT", "didContact"),
        ("DIGI-DEVICE-IDENT", "didLocation"),
        ("DIGI-DEVICE-IDENT", "didDescription"))
)
if mibBuilder.loadTexts:
    serialDataPatternMatch.setStatus(
        "current"
    )

excessiveCellularData = NotificationType(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 100, 4)
)
excessiveCellularData.setObjects(
      *(("DIGI-DEVICE-IDENT", "didDeviceID"),
        ("DIGI-DEVICE-IDENT", "didContact"),
        ("DIGI-DEVICE-IDENT", "didLocation"),
        ("DIGI-DEVICE-IDENT", "didDescription"))
)
if mibBuilder.loadTexts:
    excessiveCellularData.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-CWM-NOTIFICATIONS-MIB",
    **{"mgmtLinkDown": mgmtLinkDown,
       "lowRSSI": lowRSSI,
       "serialDataPatternMatch": serialDataPatternMatch,
       "excessiveCellularData": excessiveCellularData}
)
