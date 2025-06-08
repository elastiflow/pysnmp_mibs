# SNMP MIB module (CISCO-FIREPOWER-AP-FLOWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-FLOWCTRL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApFlowctrlFlowControl,
 CfprApFlowctrlPriorityPause,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApFlowctrlFlowControl",
    "CfprApFlowctrlPriorityPause",
    "CfprApPolicyPolicyOwner")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprApFlowctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApFlowctrlDefinitionTable_Object = MibTable
cfprApFlowctrlDefinitionTable = _CfprApFlowctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1)
)
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionTable.setStatus("current")
_CfprApFlowctrlDefinitionEntry_Object = MibTableRow
cfprApFlowctrlDefinitionEntry = _CfprApFlowctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1)
)
cfprApFlowctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FLOWCTRL-MIB", "cfprApFlowctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionEntry.setStatus("current")
_CfprApFlowctrlDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApFlowctrlDefinitionInstanceId_Object = MibTableColumn
cfprApFlowctrlDefinitionInstanceId = _CfprApFlowctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 1),
    _CfprApFlowctrlDefinitionInstanceId_Type()
)
cfprApFlowctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionInstanceId.setStatus("current")
_CfprApFlowctrlDefinitionDn_Type = CfprApManagedObjectDn
_CfprApFlowctrlDefinitionDn_Object = MibTableColumn
cfprApFlowctrlDefinitionDn = _CfprApFlowctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 2),
    _CfprApFlowctrlDefinitionDn_Type()
)
cfprApFlowctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionDn.setStatus("current")
_CfprApFlowctrlDefinitionRn_Type = SnmpAdminString
_CfprApFlowctrlDefinitionRn_Object = MibTableColumn
cfprApFlowctrlDefinitionRn = _CfprApFlowctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 3),
    _CfprApFlowctrlDefinitionRn_Type()
)
cfprApFlowctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionRn.setStatus("current")
_CfprApFlowctrlDefinitionDescr_Type = SnmpAdminString
_CfprApFlowctrlDefinitionDescr_Object = MibTableColumn
cfprApFlowctrlDefinitionDescr = _CfprApFlowctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 4),
    _CfprApFlowctrlDefinitionDescr_Type()
)
cfprApFlowctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionDescr.setStatus("current")
_CfprApFlowctrlDefinitionIntId_Type = SnmpAdminString
_CfprApFlowctrlDefinitionIntId_Object = MibTableColumn
cfprApFlowctrlDefinitionIntId = _CfprApFlowctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 5),
    _CfprApFlowctrlDefinitionIntId_Type()
)
cfprApFlowctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionIntId.setStatus("current")
_CfprApFlowctrlDefinitionName_Type = SnmpAdminString
_CfprApFlowctrlDefinitionName_Object = MibTableColumn
cfprApFlowctrlDefinitionName = _CfprApFlowctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 6),
    _CfprApFlowctrlDefinitionName_Type()
)
cfprApFlowctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionName.setStatus("current")
_CfprApFlowctrlDefinitionPolicyLevel_Type = Gauge32
_CfprApFlowctrlDefinitionPolicyLevel_Object = MibTableColumn
cfprApFlowctrlDefinitionPolicyLevel = _CfprApFlowctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 7),
    _CfprApFlowctrlDefinitionPolicyLevel_Type()
)
cfprApFlowctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionPolicyLevel.setStatus("current")
_CfprApFlowctrlDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFlowctrlDefinitionPolicyOwner_Object = MibTableColumn
cfprApFlowctrlDefinitionPolicyOwner = _CfprApFlowctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 1, 1, 8),
    _CfprApFlowctrlDefinitionPolicyOwner_Type()
)
cfprApFlowctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlDefinitionPolicyOwner.setStatus("current")
_CfprApFlowctrlItemTable_Object = MibTable
cfprApFlowctrlItemTable = _CfprApFlowctrlItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2)
)
if mibBuilder.loadTexts:
    cfprApFlowctrlItemTable.setStatus("current")
_CfprApFlowctrlItemEntry_Object = MibTableRow
cfprApFlowctrlItemEntry = _CfprApFlowctrlItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1)
)
cfprApFlowctrlItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FLOWCTRL-MIB", "cfprApFlowctrlItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFlowctrlItemEntry.setStatus("current")
_CfprApFlowctrlItemInstanceId_Type = CfprApManagedObjectId
_CfprApFlowctrlItemInstanceId_Object = MibTableColumn
cfprApFlowctrlItemInstanceId = _CfprApFlowctrlItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 1),
    _CfprApFlowctrlItemInstanceId_Type()
)
cfprApFlowctrlItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemInstanceId.setStatus("current")
_CfprApFlowctrlItemDn_Type = CfprApManagedObjectDn
_CfprApFlowctrlItemDn_Object = MibTableColumn
cfprApFlowctrlItemDn = _CfprApFlowctrlItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 2),
    _CfprApFlowctrlItemDn_Type()
)
cfprApFlowctrlItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemDn.setStatus("current")
_CfprApFlowctrlItemRn_Type = SnmpAdminString
_CfprApFlowctrlItemRn_Object = MibTableColumn
cfprApFlowctrlItemRn = _CfprApFlowctrlItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 3),
    _CfprApFlowctrlItemRn_Type()
)
cfprApFlowctrlItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemRn.setStatus("current")
_CfprApFlowctrlItemName_Type = SnmpAdminString
_CfprApFlowctrlItemName_Object = MibTableColumn
cfprApFlowctrlItemName = _CfprApFlowctrlItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 4),
    _CfprApFlowctrlItemName_Type()
)
cfprApFlowctrlItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemName.setStatus("current")
_CfprApFlowctrlItemPrio_Type = CfprApFlowctrlPriorityPause
_CfprApFlowctrlItemPrio_Object = MibTableColumn
cfprApFlowctrlItemPrio = _CfprApFlowctrlItemPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 5),
    _CfprApFlowctrlItemPrio_Type()
)
cfprApFlowctrlItemPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemPrio.setStatus("current")
_CfprApFlowctrlItemRcv_Type = CfprApFlowctrlFlowControl
_CfprApFlowctrlItemRcv_Object = MibTableColumn
cfprApFlowctrlItemRcv = _CfprApFlowctrlItemRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 6),
    _CfprApFlowctrlItemRcv_Type()
)
cfprApFlowctrlItemRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemRcv.setStatus("current")
_CfprApFlowctrlItemSnd_Type = CfprApFlowctrlFlowControl
_CfprApFlowctrlItemSnd_Object = MibTableColumn
cfprApFlowctrlItemSnd = _CfprApFlowctrlItemSnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 31, 2, 1, 7),
    _CfprApFlowctrlItemSnd_Type()
)
cfprApFlowctrlItemSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFlowctrlItemSnd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-FLOWCTRL-MIB",
    **{"cfprApFlowctrlObjects": cfprApFlowctrlObjects,
       "cfprApFlowctrlDefinitionTable": cfprApFlowctrlDefinitionTable,
       "cfprApFlowctrlDefinitionEntry": cfprApFlowctrlDefinitionEntry,
       "cfprApFlowctrlDefinitionInstanceId": cfprApFlowctrlDefinitionInstanceId,
       "cfprApFlowctrlDefinitionDn": cfprApFlowctrlDefinitionDn,
       "cfprApFlowctrlDefinitionRn": cfprApFlowctrlDefinitionRn,
       "cfprApFlowctrlDefinitionDescr": cfprApFlowctrlDefinitionDescr,
       "cfprApFlowctrlDefinitionIntId": cfprApFlowctrlDefinitionIntId,
       "cfprApFlowctrlDefinitionName": cfprApFlowctrlDefinitionName,
       "cfprApFlowctrlDefinitionPolicyLevel": cfprApFlowctrlDefinitionPolicyLevel,
       "cfprApFlowctrlDefinitionPolicyOwner": cfprApFlowctrlDefinitionPolicyOwner,
       "cfprApFlowctrlItemTable": cfprApFlowctrlItemTable,
       "cfprApFlowctrlItemEntry": cfprApFlowctrlItemEntry,
       "cfprApFlowctrlItemInstanceId": cfprApFlowctrlItemInstanceId,
       "cfprApFlowctrlItemDn": cfprApFlowctrlItemDn,
       "cfprApFlowctrlItemRn": cfprApFlowctrlItemRn,
       "cfprApFlowctrlItemName": cfprApFlowctrlItemName,
       "cfprApFlowctrlItemPrio": cfprApFlowctrlItemPrio,
       "cfprApFlowctrlItemRcv": cfprApFlowctrlItemRcv,
       "cfprApFlowctrlItemSnd": cfprApFlowctrlItemSnd}
)
