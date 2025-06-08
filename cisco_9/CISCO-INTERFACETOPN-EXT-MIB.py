# SNMP MIB module (CISCO-INTERFACETOPN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-INTERFACETOPN-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:28 2025
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

(interfaceTopNControlEntry,) = mibBuilder.importSymbols(
    "INTERFACETOPN-MIB",
    "interfaceTopNControlEntry")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ciscoInterfaceTopNExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482)
)
if mibBuilder.loadTexts:
    ciscoInterfaceTopNExtMIB.setRevisions(
        ("2010-10-19 00:00",
         "2008-01-15 00:00",
         "2006-03-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBNotifs = _CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 0)
)
_CiscoInterfaceTopNExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBObjects = _CiscoInterfaceTopNExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1)
)


class _CitneInterfaceTopNCaps_Type(Bits):
    """Custom type citneInterfaceTopNCaps based on Bits"""
    namedValues = NamedValues(
        *(("utilization", 0),
          ("bytes", 1),
          ("packets", 2),
          ("broadcast", 3),
          ("multicast", 4),
          ("overflow", 5))
    )

_CitneInterfaceTopNCaps_Type.__name__ = "Bits"
_CitneInterfaceTopNCaps_Object = MibScalar
citneInterfaceTopNCaps = _CitneInterfaceTopNCaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 1),
    _CitneInterfaceTopNCaps_Type()
)
citneInterfaceTopNCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citneInterfaceTopNCaps.setStatus("current")
_CitneInterfaceTopNControlTable_Object = MibTable
citneInterfaceTopNControlTable = _CitneInterfaceTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2)
)
if mibBuilder.loadTexts:
    citneInterfaceTopNControlTable.setStatus("current")
_CitneInterfaceTopNControlEntry_Object = MibTableRow
citneInterfaceTopNControlEntry = _CitneInterfaceTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1)
)
if mibBuilder.loadTexts:
    citneInterfaceTopNControlEntry.setStatus("current")


class _CitneInterfaceTopNCounterType_Type(Integer32):
    """Custom type citneInterfaceTopNCounterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("utilization", 2),
          ("bytes", 3),
          ("packets", 4),
          ("broadcast", 5),
          ("multicast", 6),
          ("overflow", 7))
    )


_CitneInterfaceTopNCounterType_Type.__name__ = "Integer32"
_CitneInterfaceTopNCounterType_Object = MibTableColumn
citneInterfaceTopNCounterType = _CitneInterfaceTopNCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 1),
    _CitneInterfaceTopNCounterType_Type()
)
citneInterfaceTopNCounterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNCounterType.setStatus("current")


class _CitneInterfaceTopNInterfaceType_Type(Integer32):
    """Custom type citneInterfaceTopNInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ethernet", 2),
          ("fastEthernet", 3),
          ("gigaEthernet", 4),
          ("tenGigaEthernet", 5),
          ("portChannel", 6),
          ("layer2", 7),
          ("layer3", 8),
          ("fortyGigaEthernet", 9))
    )


_CitneInterfaceTopNInterfaceType_Type.__name__ = "Integer32"
_CitneInterfaceTopNInterfaceType_Object = MibTableColumn
citneInterfaceTopNInterfaceType = _CitneInterfaceTopNInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 2),
    _CitneInterfaceTopNInterfaceType_Type()
)
citneInterfaceTopNInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNInterfaceType.setStatus("current")


class _CitneInterfaceTopNVlanNumber_Type(VlanIndex):
    """Custom type citneInterfaceTopNVlanNumber based on VlanIndex"""
    defaultValue = 0


_CitneInterfaceTopNVlanNumber_Type.__name__ = "VlanIndex"
_CitneInterfaceTopNVlanNumber_Object = MibTableColumn
citneInterfaceTopNVlanNumber = _CitneInterfaceTopNVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 1, 2, 1, 3),
    _CitneInterfaceTopNVlanNumber_Type()
)
citneInterfaceTopNVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citneInterfaceTopNVlanNumber.setStatus("current")
_CiscoInterfaceTopNExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoInterfaceTopNExtMIBConform = _CiscoInterfaceTopNExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2)
)
_CiscoIfTopNExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIfTopNExtMIBCompliances = _CiscoIfTopNExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1)
)
_CiscoIfTopNExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIfTopNExtMIBGroups = _CiscoIfTopNExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2)
)
interfaceTopNControlEntry.registerAugmentions(
    ("CISCO-INTERFACETOPN-EXT-MIB",
     "citneInterfaceTopNControlEntry")
)
citneInterfaceTopNControlEntry.setIndexNames(*interfaceTopNControlEntry.getIndexNames())

# Managed Objects groups

ciscoIfTopNExtCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 1)
)
ciscoIfTopNExtCapsGroup.setObjects(
    ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCaps")
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtCapsGroup.setStatus("current")

ciscoIfTopNExtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 2)
)
ciscoIfTopNExtControlGroup.setObjects(
      *(("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNCounterType"),
        ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNInterfaceType"))
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtControlGroup.setStatus("current")

ciscoIfTopNExtCtrlVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 2, 3)
)
ciscoIfTopNExtCtrlVlanGroup.setObjects(
    ("CISCO-INTERFACETOPN-EXT-MIB", "citneInterfaceTopNVlanNumber")
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtCtrlVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIfTopNExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 482, 2, 1, 1)
)
ciscoIfTopNExtMIBCompliance.setObjects(
      *(("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCapsGroup"),
        ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtControlGroup"),
        ("CISCO-INTERFACETOPN-EXT-MIB", "ciscoIfTopNExtCtrlVlanGroup"))
)
if mibBuilder.loadTexts:
    ciscoIfTopNExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-INTERFACETOPN-EXT-MIB",
    **{"ciscoInterfaceTopNExtMIB": ciscoInterfaceTopNExtMIB,
       "ciscoInterfaceTopNExtMIBNotifs": ciscoInterfaceTopNExtMIBNotifs,
       "ciscoInterfaceTopNExtMIBObjects": ciscoInterfaceTopNExtMIBObjects,
       "citneInterfaceTopNCaps": citneInterfaceTopNCaps,
       "citneInterfaceTopNControlTable": citneInterfaceTopNControlTable,
       "citneInterfaceTopNControlEntry": citneInterfaceTopNControlEntry,
       "citneInterfaceTopNCounterType": citneInterfaceTopNCounterType,
       "citneInterfaceTopNInterfaceType": citneInterfaceTopNInterfaceType,
       "citneInterfaceTopNVlanNumber": citneInterfaceTopNVlanNumber,
       "ciscoInterfaceTopNExtMIBConform": ciscoInterfaceTopNExtMIBConform,
       "ciscoIfTopNExtMIBCompliances": ciscoIfTopNExtMIBCompliances,
       "ciscoIfTopNExtMIBCompliance": ciscoIfTopNExtMIBCompliance,
       "ciscoIfTopNExtMIBGroups": ciscoIfTopNExtMIBGroups,
       "ciscoIfTopNExtCapsGroup": ciscoIfTopNExtCapsGroup,
       "ciscoIfTopNExtControlGroup": ciscoIfTopNExtControlGroup,
       "ciscoIfTopNExtCtrlVlanGroup": ciscoIfTopNExtCtrlVlanGroup}
)
