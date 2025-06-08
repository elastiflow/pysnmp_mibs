# SNMP MIB module (A3COM-HUAWEI-LPBKDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LPBKDT-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:06 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

h3cLpbkdt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95)
)
if mibBuilder.loadTexts:
    h3cLpbkdt.setRevisions(
        ("2009-03-30 17:41",
         "2008-09-27 15:04")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLpbkdtNotifications_ObjectIdentity = ObjectIdentity
h3cLpbkdtNotifications = _H3cLpbkdtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1)
)
_H3cLpbkdtTrapPrefix_ObjectIdentity = ObjectIdentity
h3cLpbkdtTrapPrefix = _H3cLpbkdtTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0)
)
_H3cLpbkdtObjects_ObjectIdentity = ObjectIdentity
h3cLpbkdtObjects = _H3cLpbkdtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2)
)
_H3cLpbkdtVlanID_Type = VlanId
_H3cLpbkdtVlanID_Object = MibScalar
h3cLpbkdtVlanID = _H3cLpbkdtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2, 1),
    _H3cLpbkdtVlanID_Type()
)
h3cLpbkdtVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLpbkdtVlanID.setStatus("current")

# Managed Objects groups


# Notification objects

h3cLpbkdtTrapLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 1)
)
h3cLpbkdtTrapLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapLoopbacked.setStatus(
        "current"
    )

h3cLpbkdtTrapRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 2)
)
h3cLpbkdtTrapRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapRecovered.setStatus(
        "current"
    )

h3cLpbkdtTrapPerVlanLoopbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 3)
)
h3cLpbkdtTrapPerVlanLoopbacked.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapPerVlanLoopbacked.setStatus(
        "current"
    )

h3cLpbkdtTrapPerVlanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 4)
)
h3cLpbkdtTrapPerVlanRecovered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
)
if mibBuilder.loadTexts:
    h3cLpbkdtTrapPerVlanRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LPBKDT-MIB",
    **{"h3cLpbkdt": h3cLpbkdt,
       "h3cLpbkdtNotifications": h3cLpbkdtNotifications,
       "h3cLpbkdtTrapPrefix": h3cLpbkdtTrapPrefix,
       "h3cLpbkdtTrapLoopbacked": h3cLpbkdtTrapLoopbacked,
       "h3cLpbkdtTrapRecovered": h3cLpbkdtTrapRecovered,
       "h3cLpbkdtTrapPerVlanLoopbacked": h3cLpbkdtTrapPerVlanLoopbacked,
       "h3cLpbkdtTrapPerVlanRecovered": h3cLpbkdtTrapPerVlanRecovered,
       "h3cLpbkdtObjects": h3cLpbkdtObjects,
       "h3cLpbkdtVlanID": h3cLpbkdtVlanID}
)
