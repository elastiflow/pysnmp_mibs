# SNMP MIB module (CISCO-SWITCH-CGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SWITCH-CGMP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:05 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchCgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101)
)
if mibBuilder.loadTexts:
    ciscoSwitchCgmpMIB.setRevisions(
        ("1998-05-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SCgmpVlanIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchCgmpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchCgmpMIBObjects = _CiscoSwitchCgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1)
)
_SCgmpInfo_ObjectIdentity = ObjectIdentity
sCgmpInfo = _SCgmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1)
)


class _SCgmpEnable_Type(Integer32):
    """Custom type sCgmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SCgmpEnable_Type.__name__ = "Integer32"
_SCgmpEnable_Object = MibScalar
sCgmpEnable = _SCgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 1),
    _SCgmpEnable_Type()
)
sCgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCgmpEnable.setStatus("current")


class _SCgmpFastLeaveEnable_Type(Integer32):
    """Custom type sCgmpFastLeaveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SCgmpFastLeaveEnable_Type.__name__ = "Integer32"
_SCgmpFastLeaveEnable_Object = MibScalar
sCgmpFastLeaveEnable = _SCgmpFastLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 2),
    _SCgmpFastLeaveEnable_Type()
)
sCgmpFastLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCgmpFastLeaveEnable.setStatus("current")


class _SCgmpRouterHoldTime_Type(Integer32):
    """Custom type sCgmpRouterHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 6000),
    )


_SCgmpRouterHoldTime_Type.__name__ = "Integer32"
_SCgmpRouterHoldTime_Object = MibScalar
sCgmpRouterHoldTime = _SCgmpRouterHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 3),
    _SCgmpRouterHoldTime_Type()
)
sCgmpRouterHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCgmpRouterHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    sCgmpRouterHoldTime.setUnits("seconds")
_SCgmpRouterTable_Object = MibTable
sCgmpRouterTable = _SCgmpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sCgmpRouterTable.setStatus("current")
_SCgmpRouterEntry_Object = MibTableRow
sCgmpRouterEntry = _SCgmpRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1)
)
sCgmpRouterEntry.setIndexNames(
    (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterVlanIndex"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterMacAddress"),
)
if mibBuilder.loadTexts:
    sCgmpRouterEntry.setStatus("current")
_SCgmpRouterVlanIndex_Type = SCgmpVlanIndex
_SCgmpRouterVlanIndex_Object = MibTableColumn
sCgmpRouterVlanIndex = _SCgmpRouterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 1),
    _SCgmpRouterVlanIndex_Type()
)
sCgmpRouterVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCgmpRouterVlanIndex.setStatus("current")
_SCgmpRouterMacAddress_Type = MacAddress
_SCgmpRouterMacAddress_Object = MibTableColumn
sCgmpRouterMacAddress = _SCgmpRouterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 3),
    _SCgmpRouterMacAddress_Type()
)
sCgmpRouterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sCgmpRouterMacAddress.setStatus("current")
_SCgmpRouterEntryStatus_Type = RowStatus
_SCgmpRouterEntryStatus_Object = MibTableColumn
sCgmpRouterEntryStatus = _SCgmpRouterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 4),
    _SCgmpRouterEntryStatus_Type()
)
sCgmpRouterEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCgmpRouterEntryStatus.setStatus("current")
_CiscoSwitchCgmpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSwitchCgmpMIBConformance = _CiscoSwitchCgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 3)
)
_CiscoSwitchCgmpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSwitchCgmpMIBCompliances = _CiscoSwitchCgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1)
)
_CiscoSwitchCgmpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSwitchCgmpMIBGroups = _CiscoSwitchCgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2)
)

# Managed Objects groups

sCgmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2, 1)
)
sCgmpGroup.setObjects(
      *(("CISCO-SWITCH-CGMP-MIB", "sCgmpEnable"),
        ("CISCO-SWITCH-CGMP-MIB", "sCgmpFastLeaveEnable"),
        ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterHoldTime"),
        ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterEntryStatus"))
)
if mibBuilder.loadTexts:
    sCgmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSwitchCgmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1, 1)
)
ciscoSwitchCgmpMIBCompliance.setObjects(
    ("CISCO-SWITCH-CGMP-MIB", "sCgmpGroup")
)
if mibBuilder.loadTexts:
    ciscoSwitchCgmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-CGMP-MIB",
    **{"SCgmpVlanIndex": SCgmpVlanIndex,
       "ciscoSwitchCgmpMIB": ciscoSwitchCgmpMIB,
       "ciscoSwitchCgmpMIBObjects": ciscoSwitchCgmpMIBObjects,
       "sCgmpInfo": sCgmpInfo,
       "sCgmpEnable": sCgmpEnable,
       "sCgmpFastLeaveEnable": sCgmpFastLeaveEnable,
       "sCgmpRouterHoldTime": sCgmpRouterHoldTime,
       "sCgmpRouterTable": sCgmpRouterTable,
       "sCgmpRouterEntry": sCgmpRouterEntry,
       "sCgmpRouterVlanIndex": sCgmpRouterVlanIndex,
       "sCgmpRouterMacAddress": sCgmpRouterMacAddress,
       "sCgmpRouterEntryStatus": sCgmpRouterEntryStatus,
       "ciscoSwitchCgmpMIBConformance": ciscoSwitchCgmpMIBConformance,
       "ciscoSwitchCgmpMIBCompliances": ciscoSwitchCgmpMIBCompliances,
       "ciscoSwitchCgmpMIBCompliance": ciscoSwitchCgmpMIBCompliance,
       "ciscoSwitchCgmpMIBGroups": ciscoSwitchCgmpMIBGroups,
       "sCgmpGroup": sCgmpGroup}
)
