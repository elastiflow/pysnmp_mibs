# SNMP MIB module (CISCO-VLAN-BRIDGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VLAN-BRIDGING-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPortList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPortList")

(vtpVlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "vtpVlanIndex")

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


# MODULE-IDENTITY

ciscoVlanBridgingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56)
)
if mibBuilder.loadTexts:
    ciscoVlanBridgingMIB.setRevisions(
        ("2003-08-22 00:00",
         "1996-09-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVlanBridgingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVlanBridgingMIBObjects = _CiscoVlanBridgingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1)
)
_CvbStp_ObjectIdentity = ObjectIdentity
cvbStp = _CvbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1)
)
_CvbStpTable_Object = MibTable
cvbStpTable = _CvbStpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvbStpTable.setStatus("current")
_CvbStpEntry_Object = MibTableRow
cvbStpEntry = _CvbStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1)
)
cvbStpEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
)
if mibBuilder.loadTexts:
    cvbStpEntry.setStatus("current")


class _CvbStpForwardingMap_Type(OctetString):
    """Custom type cvbStpForwardingMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvbStpForwardingMap_Type.__name__ = "OctetString"
_CvbStpForwardingMap_Object = MibTableColumn
cvbStpForwardingMap = _CvbStpForwardingMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 2),
    _CvbStpForwardingMap_Type()
)
cvbStpForwardingMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvbStpForwardingMap.setStatus("deprecated")
_CvbStpForwardingMap2k_Type = CiscoPortList
_CvbStpForwardingMap2k_Object = MibTableColumn
cvbStpForwardingMap2k = _CvbStpForwardingMap2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 3),
    _CvbStpForwardingMap2k_Type()
)
cvbStpForwardingMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvbStpForwardingMap2k.setStatus("current")
_CiscoVlanBridgingMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVlanBridgingMIBConformance = _CiscoVlanBridgingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3)
)
_CiscoVlanBridgingMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVlanBridgingMIBCompliances = _CiscoVlanBridgingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1)
)
_CiscoVlanBridgingMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVlanBridgingMIBGroups = _CiscoVlanBridgingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2)
)

# Managed Objects groups

ciscoVlanBridgingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 1)
)
ciscoVlanBridgingMIBGroup.setObjects(
    ("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap")
)
if mibBuilder.loadTexts:
    ciscoVlanBridgingMIBGroup.setStatus("deprecated")

ciscoVlanBridgingMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 2)
)
ciscoVlanBridgingMIBGroup2.setObjects(
    ("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap2k")
)
if mibBuilder.loadTexts:
    ciscoVlanBridgingMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVlanBridgingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 1)
)
ciscoVlanBridgingMIBCompliance.setObjects(
    ("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoVlanBridgingMIBCompliance.setStatus(
        "deprecated"
    )

ciscoVlanBridgingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 2)
)
ciscoVlanBridgingMIBCompliance2.setObjects(
    ("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup2")
)
if mibBuilder.loadTexts:
    ciscoVlanBridgingMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-BRIDGING-MIB",
    **{"ciscoVlanBridgingMIB": ciscoVlanBridgingMIB,
       "ciscoVlanBridgingMIBObjects": ciscoVlanBridgingMIBObjects,
       "cvbStp": cvbStp,
       "cvbStpTable": cvbStpTable,
       "cvbStpEntry": cvbStpEntry,
       "cvbStpForwardingMap": cvbStpForwardingMap,
       "cvbStpForwardingMap2k": cvbStpForwardingMap2k,
       "ciscoVlanBridgingMIBConformance": ciscoVlanBridgingMIBConformance,
       "ciscoVlanBridgingMIBCompliances": ciscoVlanBridgingMIBCompliances,
       "ciscoVlanBridgingMIBCompliance": ciscoVlanBridgingMIBCompliance,
       "ciscoVlanBridgingMIBCompliance2": ciscoVlanBridgingMIBCompliance2,
       "ciscoVlanBridgingMIBGroups": ciscoVlanBridgingMIBGroups,
       "ciscoVlanBridgingMIBGroup": ciscoVlanBridgingMIBGroup,
       "ciscoVlanBridgingMIBGroup2": ciscoVlanBridgingMIBGroup2}
)
