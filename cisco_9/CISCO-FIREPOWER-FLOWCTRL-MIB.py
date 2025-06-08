# SNMP MIB module (CISCO-FIREPOWER-FLOWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FLOWCTRL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprFlowctrlFlowControlRx,
 CfprFlowctrlFlowControlTx,
 CfprFlowctrlPriorityPause,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprFlowctrlFlowControlRx",
    "CfprFlowctrlFlowControlTx",
    "CfprFlowctrlPriorityPause",
    "CfprPolicyPolicyOwner")

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

cfprFlowctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFlowctrlDefinitionTable_Object = MibTable
cfprFlowctrlDefinitionTable = _CfprFlowctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1)
)
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionTable.setStatus("current")
_CfprFlowctrlDefinitionEntry_Object = MibTableRow
cfprFlowctrlDefinitionEntry = _CfprFlowctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1)
)
cfprFlowctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FLOWCTRL-MIB", "cfprFlowctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionEntry.setStatus("current")
_CfprFlowctrlDefinitionInstanceId_Type = CfprManagedObjectId
_CfprFlowctrlDefinitionInstanceId_Object = MibTableColumn
cfprFlowctrlDefinitionInstanceId = _CfprFlowctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 1),
    _CfprFlowctrlDefinitionInstanceId_Type()
)
cfprFlowctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionInstanceId.setStatus("current")
_CfprFlowctrlDefinitionDn_Type = CfprManagedObjectDn
_CfprFlowctrlDefinitionDn_Object = MibTableColumn
cfprFlowctrlDefinitionDn = _CfprFlowctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 2),
    _CfprFlowctrlDefinitionDn_Type()
)
cfprFlowctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionDn.setStatus("current")
_CfprFlowctrlDefinitionRn_Type = SnmpAdminString
_CfprFlowctrlDefinitionRn_Object = MibTableColumn
cfprFlowctrlDefinitionRn = _CfprFlowctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 3),
    _CfprFlowctrlDefinitionRn_Type()
)
cfprFlowctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionRn.setStatus("current")
_CfprFlowctrlDefinitionDescr_Type = SnmpAdminString
_CfprFlowctrlDefinitionDescr_Object = MibTableColumn
cfprFlowctrlDefinitionDescr = _CfprFlowctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 4),
    _CfprFlowctrlDefinitionDescr_Type()
)
cfprFlowctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionDescr.setStatus("current")
_CfprFlowctrlDefinitionIntId_Type = SnmpAdminString
_CfprFlowctrlDefinitionIntId_Object = MibTableColumn
cfprFlowctrlDefinitionIntId = _CfprFlowctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 5),
    _CfprFlowctrlDefinitionIntId_Type()
)
cfprFlowctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionIntId.setStatus("current")
_CfprFlowctrlDefinitionName_Type = SnmpAdminString
_CfprFlowctrlDefinitionName_Object = MibTableColumn
cfprFlowctrlDefinitionName = _CfprFlowctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 6),
    _CfprFlowctrlDefinitionName_Type()
)
cfprFlowctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionName.setStatus("current")
_CfprFlowctrlDefinitionPolicyLevel_Type = Gauge32
_CfprFlowctrlDefinitionPolicyLevel_Object = MibTableColumn
cfprFlowctrlDefinitionPolicyLevel = _CfprFlowctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 7),
    _CfprFlowctrlDefinitionPolicyLevel_Type()
)
cfprFlowctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionPolicyLevel.setStatus("current")
_CfprFlowctrlDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFlowctrlDefinitionPolicyOwner_Object = MibTableColumn
cfprFlowctrlDefinitionPolicyOwner = _CfprFlowctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 1, 1, 8),
    _CfprFlowctrlDefinitionPolicyOwner_Type()
)
cfprFlowctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlDefinitionPolicyOwner.setStatus("current")
_CfprFlowctrlItemTable_Object = MibTable
cfprFlowctrlItemTable = _CfprFlowctrlItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2)
)
if mibBuilder.loadTexts:
    cfprFlowctrlItemTable.setStatus("current")
_CfprFlowctrlItemEntry_Object = MibTableRow
cfprFlowctrlItemEntry = _CfprFlowctrlItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1)
)
cfprFlowctrlItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FLOWCTRL-MIB", "cfprFlowctrlItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFlowctrlItemEntry.setStatus("current")
_CfprFlowctrlItemInstanceId_Type = CfprManagedObjectId
_CfprFlowctrlItemInstanceId_Object = MibTableColumn
cfprFlowctrlItemInstanceId = _CfprFlowctrlItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 1),
    _CfprFlowctrlItemInstanceId_Type()
)
cfprFlowctrlItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFlowctrlItemInstanceId.setStatus("current")
_CfprFlowctrlItemDn_Type = CfprManagedObjectDn
_CfprFlowctrlItemDn_Object = MibTableColumn
cfprFlowctrlItemDn = _CfprFlowctrlItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 2),
    _CfprFlowctrlItemDn_Type()
)
cfprFlowctrlItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemDn.setStatus("current")
_CfprFlowctrlItemRn_Type = SnmpAdminString
_CfprFlowctrlItemRn_Object = MibTableColumn
cfprFlowctrlItemRn = _CfprFlowctrlItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 3),
    _CfprFlowctrlItemRn_Type()
)
cfprFlowctrlItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemRn.setStatus("current")
_CfprFlowctrlItemName_Type = SnmpAdminString
_CfprFlowctrlItemName_Object = MibTableColumn
cfprFlowctrlItemName = _CfprFlowctrlItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 4),
    _CfprFlowctrlItemName_Type()
)
cfprFlowctrlItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemName.setStatus("current")
_CfprFlowctrlItemPrio_Type = CfprFlowctrlPriorityPause
_CfprFlowctrlItemPrio_Object = MibTableColumn
cfprFlowctrlItemPrio = _CfprFlowctrlItemPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 5),
    _CfprFlowctrlItemPrio_Type()
)
cfprFlowctrlItemPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemPrio.setStatus("current")
_CfprFlowctrlItemRcv_Type = CfprFlowctrlFlowControlRx
_CfprFlowctrlItemRcv_Object = MibTableColumn
cfprFlowctrlItemRcv = _CfprFlowctrlItemRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 6),
    _CfprFlowctrlItemRcv_Type()
)
cfprFlowctrlItemRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemRcv.setStatus("current")
_CfprFlowctrlItemSnd_Type = CfprFlowctrlFlowControlTx
_CfprFlowctrlItemSnd_Object = MibTableColumn
cfprFlowctrlItemSnd = _CfprFlowctrlItemSnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 31, 2, 1, 7),
    _CfprFlowctrlItemSnd_Type()
)
cfprFlowctrlItemSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFlowctrlItemSnd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FLOWCTRL-MIB",
    **{"cfprFlowctrlObjects": cfprFlowctrlObjects,
       "cfprFlowctrlDefinitionTable": cfprFlowctrlDefinitionTable,
       "cfprFlowctrlDefinitionEntry": cfprFlowctrlDefinitionEntry,
       "cfprFlowctrlDefinitionInstanceId": cfprFlowctrlDefinitionInstanceId,
       "cfprFlowctrlDefinitionDn": cfprFlowctrlDefinitionDn,
       "cfprFlowctrlDefinitionRn": cfprFlowctrlDefinitionRn,
       "cfprFlowctrlDefinitionDescr": cfprFlowctrlDefinitionDescr,
       "cfprFlowctrlDefinitionIntId": cfprFlowctrlDefinitionIntId,
       "cfprFlowctrlDefinitionName": cfprFlowctrlDefinitionName,
       "cfprFlowctrlDefinitionPolicyLevel": cfprFlowctrlDefinitionPolicyLevel,
       "cfprFlowctrlDefinitionPolicyOwner": cfprFlowctrlDefinitionPolicyOwner,
       "cfprFlowctrlItemTable": cfprFlowctrlItemTable,
       "cfprFlowctrlItemEntry": cfprFlowctrlItemEntry,
       "cfprFlowctrlItemInstanceId": cfprFlowctrlItemInstanceId,
       "cfprFlowctrlItemDn": cfprFlowctrlItemDn,
       "cfprFlowctrlItemRn": cfprFlowctrlItemRn,
       "cfprFlowctrlItemName": cfprFlowctrlItemName,
       "cfprFlowctrlItemPrio": cfprFlowctrlItemPrio,
       "cfprFlowctrlItemRcv": cfprFlowctrlItemRcv,
       "cfprFlowctrlItemSnd": cfprFlowctrlItemSnd}
)
