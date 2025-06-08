# SNMP MIB module (WWP-EGRESS-PORT-RESTRICTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-EGRESS-PORT-RESTRICTION-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:51:13 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpEgressPortRestrictionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34)
)
if mibBuilder.loadTexts:
    wwpEgressPortRestrictionMIB.setRevisions(
        ("2001-04-03 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpEgressPortRestrictionMIBObjects_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionMIBObjects = _WwpEgressPortRestrictionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1)
)
_WwpEgressPortRestriction_ObjectIdentity = ObjectIdentity
wwpEgressPortRestriction = _WwpEgressPortRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1)
)
_WwpEgressPortRestrictionTable_Object = MibTable
wwpEgressPortRestrictionTable = _WwpEgressPortRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpEgressPortRestrictionTable.setStatus("current")
_WwpEgressPortRestrictionEntry_Object = MibTableRow
wwpEgressPortRestrictionEntry = _WwpEgressPortRestrictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1)
)
wwpEgressPortRestrictionEntry.setIndexNames(
    (0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestVlanId"),
    (0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestPortId"),
)
if mibBuilder.loadTexts:
    wwpEgressPortRestrictionEntry.setStatus("current")
_WwpERestVlanId_Type = VlanId
_WwpERestVlanId_Object = MibTableColumn
wwpERestVlanId = _WwpERestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 1),
    _WwpERestVlanId_Type()
)
wwpERestVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpERestVlanId.setStatus("current")


class _WwpERestPortId_Type(Integer32):
    """Custom type wwpERestPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpERestPortId_Type.__name__ = "Integer32"
_WwpERestPortId_Object = MibTableColumn
wwpERestPortId = _WwpERestPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 2),
    _WwpERestPortId_Type()
)
wwpERestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpERestPortId.setStatus("current")


class _WwpERestEgreesPorts_Type(PortList):
    """Custom type wwpERestEgreesPorts based on PortList"""
    defaultHexValue = "0000"


_WwpERestEgreesPorts_Type.__name__ = "PortList"
_WwpERestEgreesPorts_Object = MibTableColumn
wwpERestEgreesPorts = _WwpERestEgreesPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 3),
    _WwpERestEgreesPorts_Type()
)
wwpERestEgreesPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpERestEgreesPorts.setStatus("current")
_WwpERestStatus_Type = RowStatus
_WwpERestStatus_Object = MibTableColumn
wwpERestStatus = _WwpERestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 4),
    _WwpERestStatus_Type()
)
wwpERestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpERestStatus.setStatus("current")
_WwpEgressPortRestrictionNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionNotificationPrefix = _WwpEgressPortRestrictionNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 2)
)
_WwpEgressPortRestrictionNotifications_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionNotifications = _WwpEgressPortRestrictionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 2, 0)
)
_WwpEgressPortRestrictionMIBConformance_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionMIBConformance = _WwpEgressPortRestrictionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 3)
)
_WwpEgressPortRestrictionMIBCompliances_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionMIBCompliances = _WwpEgressPortRestrictionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 1)
)
_WwpEgressPortRestrictionMIBGroups_ObjectIdentity = ObjectIdentity
wwpEgressPortRestrictionMIBGroups = _WwpEgressPortRestrictionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-EGRESS-PORT-RESTRICTION-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "wwpEgressPortRestrictionMIB": wwpEgressPortRestrictionMIB,
       "wwpEgressPortRestrictionMIBObjects": wwpEgressPortRestrictionMIBObjects,
       "wwpEgressPortRestriction": wwpEgressPortRestriction,
       "wwpEgressPortRestrictionTable": wwpEgressPortRestrictionTable,
       "wwpEgressPortRestrictionEntry": wwpEgressPortRestrictionEntry,
       "wwpERestVlanId": wwpERestVlanId,
       "wwpERestPortId": wwpERestPortId,
       "wwpERestEgreesPorts": wwpERestEgreesPorts,
       "wwpERestStatus": wwpERestStatus,
       "wwpEgressPortRestrictionNotificationPrefix": wwpEgressPortRestrictionNotificationPrefix,
       "wwpEgressPortRestrictionNotifications": wwpEgressPortRestrictionNotifications,
       "wwpEgressPortRestrictionMIBConformance": wwpEgressPortRestrictionMIBConformance,
       "wwpEgressPortRestrictionMIBCompliances": wwpEgressPortRestrictionMIBCompliances,
       "wwpEgressPortRestrictionMIBGroups": wwpEgressPortRestrictionMIBGroups}
)
