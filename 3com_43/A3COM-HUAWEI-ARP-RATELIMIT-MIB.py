# SNMP MIB module (A3COM-HUAWEI-ARP-RATELIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-ARP-RATELIMIT-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:05:02 2025
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

h3cARPRatelimit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110)
)
if mibBuilder.loadTexts:
    h3cARPRatelimit.setRevisions(
        ("2009-12-08 19:12",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cARPRatelimitObjects_ObjectIdentity = ObjectIdentity
h3cARPRatelimitObjects = _H3cARPRatelimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1)
)
_H3cARPRatelimitTrap_ObjectIdentity = ObjectIdentity
h3cARPRatelimitTrap = _H3cARPRatelimitTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1)
)
_H3cARPRatelimitTraps_ObjectIdentity = ObjectIdentity
h3cARPRatelimitTraps = _H3cARPRatelimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 0)
)
_H3cARPRatelimitTrapObjects_ObjectIdentity = ObjectIdentity
h3cARPRatelimitTrapObjects = _H3cARPRatelimitTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1)
)
_H3cARPRatelimitTrapVer_Type = Unsigned32
_H3cARPRatelimitTrapVer_Object = MibScalar
h3cARPRatelimitTrapVer = _H3cARPRatelimitTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 1),
    _H3cARPRatelimitTrapVer_Type()
)
h3cARPRatelimitTrapVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cARPRatelimitTrapVer.setStatus("current")
_H3cARPRatelimitTrapCount_Type = Unsigned32
_H3cARPRatelimitTrapCount_Object = MibScalar
h3cARPRatelimitTrapCount = _H3cARPRatelimitTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 2),
    _H3cARPRatelimitTrapCount_Type()
)
h3cARPRatelimitTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cARPRatelimitTrapCount.setStatus("current")


class _H3cARPRatelimitTrapMsg_Type(OctetString):
    """Custom type h3cARPRatelimitTrapMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_H3cARPRatelimitTrapMsg_Type.__name__ = "OctetString"
_H3cARPRatelimitTrapMsg_Object = MibScalar
h3cARPRatelimitTrapMsg = _H3cARPRatelimitTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 3),
    _H3cARPRatelimitTrapMsg_Type()
)
h3cARPRatelimitTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cARPRatelimitTrapMsg.setStatus("current")

# Managed Objects groups


# Notification objects

h3cARPRatelimitOverspeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 0, 1)
)
h3cARPRatelimitOverspeedTrap.setObjects(
      *(("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapVer"),
        ("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapCount"),
        ("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapMsg"))
)
if mibBuilder.loadTexts:
    h3cARPRatelimitOverspeedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-ARP-RATELIMIT-MIB",
    **{"h3cARPRatelimit": h3cARPRatelimit,
       "h3cARPRatelimitObjects": h3cARPRatelimitObjects,
       "h3cARPRatelimitTrap": h3cARPRatelimitTrap,
       "h3cARPRatelimitTraps": h3cARPRatelimitTraps,
       "h3cARPRatelimitOverspeedTrap": h3cARPRatelimitOverspeedTrap,
       "h3cARPRatelimitTrapObjects": h3cARPRatelimitTrapObjects,
       "h3cARPRatelimitTrapVer": h3cARPRatelimitTrapVer,
       "h3cARPRatelimitTrapCount": h3cARPRatelimitTrapCount,
       "h3cARPRatelimitTrapMsg": h3cARPRatelimitTrapMsg}
)
