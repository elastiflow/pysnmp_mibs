# SNMP MIB module (RBN-FAST-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-FAST-VRRP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:47 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(VrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId")


# MODULE-IDENTITY

rbnFastVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45)
)
if mibBuilder.loadTexts:
    rbnFastVrrpMIB.setRevisions(
        ("2011-01-19 18:00",
         "2008-05-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnFastVrrpMIBObjects_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBObjects = _RbnFastVrrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1)
)
_RbnFastVrrpOperTable_Object = MibTable
rbnFastVrrpOperTable = _RbnFastVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFastVrrpOperTable.setStatus("current")
_RbnFastVrrpOperEntry_Object = MibTableRow
rbnFastVrrpOperEntry = _RbnFastVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1)
)
rbnFastVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-FAST-VRRP-MIB", "rbnFastVrrpOperVrId"),
)
if mibBuilder.loadTexts:
    rbnFastVrrpOperEntry.setStatus("current")
_RbnFastVrrpOperVrId_Type = VrId
_RbnFastVrrpOperVrId_Object = MibTableColumn
rbnFastVrrpOperVrId = _RbnFastVrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 1),
    _RbnFastVrrpOperVrId_Type()
)
rbnFastVrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFastVrrpOperVrId.setStatus("current")


class _RbnFastVrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type rbnFastVrrpOperAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_RbnFastVrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_RbnFastVrrpOperAdvertisementInterval_Object = MibTableColumn
rbnFastVrrpOperAdvertisementInterval = _RbnFastVrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 2),
    _RbnFastVrrpOperAdvertisementInterval_Type()
)
rbnFastVrrpOperAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFastVrrpOperAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    rbnFastVrrpOperAdvertisementInterval.setUnits("milliseconds")
_RbnFastVrrpConformance_ObjectIdentity = ObjectIdentity
rbnFastVrrpConformance = _RbnFastVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2)
)
_RbnFastVrrpMIBCompliances_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBCompliances = _RbnFastVrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1)
)
_RbnFastVrrpMIBGroups_ObjectIdentity = ObjectIdentity
rbnFastVrrpMIBGroups = _RbnFastVrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2)
)

# Managed Objects groups

rbnFastVrrpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2, 1)
)
rbnFastVrrpObjectGroup.setObjects(
    ("RBN-FAST-VRRP-MIB", "rbnFastVrrpOperAdvertisementInterval")
)
if mibBuilder.loadTexts:
    rbnFastVrrpObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnFastVrrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1, 1)
)
rbnFastVrrpCompliance.setObjects(
    ("RBN-FAST-VRRP-MIB", "rbnFastVrrpObjectGroup")
)
if mibBuilder.loadTexts:
    rbnFastVrrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-FAST-VRRP-MIB",
    **{"rbnFastVrrpMIB": rbnFastVrrpMIB,
       "rbnFastVrrpMIBObjects": rbnFastVrrpMIBObjects,
       "rbnFastVrrpOperTable": rbnFastVrrpOperTable,
       "rbnFastVrrpOperEntry": rbnFastVrrpOperEntry,
       "rbnFastVrrpOperVrId": rbnFastVrrpOperVrId,
       "rbnFastVrrpOperAdvertisementInterval": rbnFastVrrpOperAdvertisementInterval,
       "rbnFastVrrpConformance": rbnFastVrrpConformance,
       "rbnFastVrrpMIBCompliances": rbnFastVrrpMIBCompliances,
       "rbnFastVrrpCompliance": rbnFastVrrpCompliance,
       "rbnFastVrrpMIBGroups": rbnFastVrrpMIBGroups,
       "rbnFastVrrpObjectGroup": rbnFastVrrpObjectGroup}
)
