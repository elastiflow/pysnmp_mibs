# SNMP MIB module (RBN-SONETRDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SONETRDI-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:32 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnSonetRdiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23)
)
if mibBuilder.loadTexts:
    rbnSonetRdiMib.setRevisions(
        ("2002-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSonetRdiMibNotifications_ObjectIdentity = ObjectIdentity
rbnSonetRdiMibNotifications = _RbnSonetRdiMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 0)
)
_RbnSonetRdiMibObjects_ObjectIdentity = ObjectIdentity
rbnSonetRdiMibObjects = _RbnSonetRdiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1)
)
_RbnSonetRdi_ObjectIdentity = ObjectIdentity
rbnSonetRdi = _RbnSonetRdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1, 1)
)


class _RbnSonetRdiSlot_Type(Unsigned32):
    """Custom type rbnSonetRdiSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RbnSonetRdiSlot_Type.__name__ = "Unsigned32"
_RbnSonetRdiSlot_Object = MibScalar
rbnSonetRdiSlot = _RbnSonetRdiSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1, 1, 1),
    _RbnSonetRdiSlot_Type()
)
rbnSonetRdiSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSonetRdiSlot.setStatus("current")


class _RbnSonetRdiPort_Type(Unsigned32):
    """Custom type rbnSonetRdiPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RbnSonetRdiPort_Type.__name__ = "Unsigned32"
_RbnSonetRdiPort_Object = MibScalar
rbnSonetRdiPort = _RbnSonetRdiPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1, 1, 2),
    _RbnSonetRdiPort_Type()
)
rbnSonetRdiPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSonetRdiPort.setStatus("current")


class _RbnSonetRdiPortType_Type(DisplayString):
    """Custom type rbnSonetRdiPortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnSonetRdiPortType_Type.__name__ = "DisplayString"
_RbnSonetRdiPortType_Object = MibScalar
rbnSonetRdiPortType = _RbnSonetRdiPortType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1, 1, 3),
    _RbnSonetRdiPortType_Type()
)
rbnSonetRdiPortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSonetRdiPortType.setStatus("current")
_RbnSonetRdiFault_Type = TruthValue
_RbnSonetRdiFault_Object = MibScalar
rbnSonetRdiFault = _RbnSonetRdiFault_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 1, 1, 4),
    _RbnSonetRdiFault_Type()
)
rbnSonetRdiFault.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSonetRdiFault.setStatus("current")
_RbnSonetRdiMibConformance_ObjectIdentity = ObjectIdentity
rbnSonetRdiMibConformance = _RbnSonetRdiMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2)
)
_RbnSonetRdiMibCompliances_ObjectIdentity = ObjectIdentity
rbnSonetRdiMibCompliances = _RbnSonetRdiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2, 1)
)
_RbnSonetRdiMibGroups_ObjectIdentity = ObjectIdentity
rbnSonetRdiMibGroups = _RbnSonetRdiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2, 2)
)

# Managed Objects groups

rbnSonetRdiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2, 2, 1)
)
rbnSonetRdiGroup.setObjects(
      *(("RBN-SONETRDI-MIB", "rbnSonetRdiSlot"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiPort"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiPortType"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiFault"))
)
if mibBuilder.loadTexts:
    rbnSonetRdiGroup.setStatus("current")


# Notification objects

rbnSonetRdiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 0, 1)
)
rbnSonetRdiTrap.setObjects(
      *(("RBN-SONETRDI-MIB", "rbnSonetRdiSlot"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiPort"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiPortType"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiFault"))
)
if mibBuilder.loadTexts:
    rbnSonetRdiTrap.setStatus(
        "current"
    )


# Notifications groups

rbnSonetRdiNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2, 2, 2)
)
rbnSonetRdiNotifyGroup.setObjects(
    ("RBN-SONETRDI-MIB", "rbnSonetRdiTrap")
)
if mibBuilder.loadTexts:
    rbnSonetRdiNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSonetRdiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 23, 2, 1, 1)
)
rbnSonetRdiCompliance.setObjects(
      *(("RBN-SONETRDI-MIB", "rbnSonetRdiGroup"),
        ("RBN-SONETRDI-MIB", "rbnSonetRdiNotifyGroup"))
)
if mibBuilder.loadTexts:
    rbnSonetRdiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SONETRDI-MIB",
    **{"rbnSonetRdiMib": rbnSonetRdiMib,
       "rbnSonetRdiMibNotifications": rbnSonetRdiMibNotifications,
       "rbnSonetRdiTrap": rbnSonetRdiTrap,
       "rbnSonetRdiMibObjects": rbnSonetRdiMibObjects,
       "rbnSonetRdi": rbnSonetRdi,
       "rbnSonetRdiSlot": rbnSonetRdiSlot,
       "rbnSonetRdiPort": rbnSonetRdiPort,
       "rbnSonetRdiPortType": rbnSonetRdiPortType,
       "rbnSonetRdiFault": rbnSonetRdiFault,
       "rbnSonetRdiMibConformance": rbnSonetRdiMibConformance,
       "rbnSonetRdiMibCompliances": rbnSonetRdiMibCompliances,
       "rbnSonetRdiCompliance": rbnSonetRdiCompliance,
       "rbnSonetRdiMibGroups": rbnSonetRdiMibGroups,
       "rbnSonetRdiGroup": rbnSonetRdiGroup,
       "rbnSonetRdiNotifyGroup": rbnSonetRdiNotifyGroup}
)
