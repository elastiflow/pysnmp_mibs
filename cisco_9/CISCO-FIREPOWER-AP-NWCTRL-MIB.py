# SNMP MIB module (CISCO-FIREPOWER-AP-NWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-NWCTRL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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

(CfprApNwctrlAdminState,
 CfprApNwctrlLinkFailAction,
 CfprApNwctrlRegistrationMode,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApNwctrlAdminState",
    "CfprApNwctrlLinkFailAction",
    "CfprApNwctrlRegistrationMode",
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

cfprApNwctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApNwctrlDefinitionTable_Object = MibTable
cfprApNwctrlDefinitionTable = _CfprApNwctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1)
)
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionTable.setStatus("current")
_CfprApNwctrlDefinitionEntry_Object = MibTableRow
cfprApNwctrlDefinitionEntry = _CfprApNwctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1)
)
cfprApNwctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NWCTRL-MIB", "cfprApNwctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionEntry.setStatus("current")
_CfprApNwctrlDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApNwctrlDefinitionInstanceId_Object = MibTableColumn
cfprApNwctrlDefinitionInstanceId = _CfprApNwctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 1),
    _CfprApNwctrlDefinitionInstanceId_Type()
)
cfprApNwctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionInstanceId.setStatus("current")
_CfprApNwctrlDefinitionDn_Type = CfprApManagedObjectDn
_CfprApNwctrlDefinitionDn_Object = MibTableColumn
cfprApNwctrlDefinitionDn = _CfprApNwctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 2),
    _CfprApNwctrlDefinitionDn_Type()
)
cfprApNwctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionDn.setStatus("current")
_CfprApNwctrlDefinitionRn_Type = SnmpAdminString
_CfprApNwctrlDefinitionRn_Object = MibTableColumn
cfprApNwctrlDefinitionRn = _CfprApNwctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 3),
    _CfprApNwctrlDefinitionRn_Type()
)
cfprApNwctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionRn.setStatus("current")
_CfprApNwctrlDefinitionCdp_Type = CfprApNwctrlAdminState
_CfprApNwctrlDefinitionCdp_Object = MibTableColumn
cfprApNwctrlDefinitionCdp = _CfprApNwctrlDefinitionCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 4),
    _CfprApNwctrlDefinitionCdp_Type()
)
cfprApNwctrlDefinitionCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionCdp.setStatus("current")
_CfprApNwctrlDefinitionDescr_Type = SnmpAdminString
_CfprApNwctrlDefinitionDescr_Object = MibTableColumn
cfprApNwctrlDefinitionDescr = _CfprApNwctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 5),
    _CfprApNwctrlDefinitionDescr_Type()
)
cfprApNwctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionDescr.setStatus("current")
_CfprApNwctrlDefinitionIntId_Type = SnmpAdminString
_CfprApNwctrlDefinitionIntId_Object = MibTableColumn
cfprApNwctrlDefinitionIntId = _CfprApNwctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 6),
    _CfprApNwctrlDefinitionIntId_Type()
)
cfprApNwctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionIntId.setStatus("current")
_CfprApNwctrlDefinitionMacRegisterMode_Type = CfprApNwctrlRegistrationMode
_CfprApNwctrlDefinitionMacRegisterMode_Object = MibTableColumn
cfprApNwctrlDefinitionMacRegisterMode = _CfprApNwctrlDefinitionMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 7),
    _CfprApNwctrlDefinitionMacRegisterMode_Type()
)
cfprApNwctrlDefinitionMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionMacRegisterMode.setStatus("current")
_CfprApNwctrlDefinitionName_Type = SnmpAdminString
_CfprApNwctrlDefinitionName_Object = MibTableColumn
cfprApNwctrlDefinitionName = _CfprApNwctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 8),
    _CfprApNwctrlDefinitionName_Type()
)
cfprApNwctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionName.setStatus("current")
_CfprApNwctrlDefinitionPolicyLevel_Type = Gauge32
_CfprApNwctrlDefinitionPolicyLevel_Object = MibTableColumn
cfprApNwctrlDefinitionPolicyLevel = _CfprApNwctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 9),
    _CfprApNwctrlDefinitionPolicyLevel_Type()
)
cfprApNwctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionPolicyLevel.setStatus("current")
_CfprApNwctrlDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApNwctrlDefinitionPolicyOwner_Object = MibTableColumn
cfprApNwctrlDefinitionPolicyOwner = _CfprApNwctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 10),
    _CfprApNwctrlDefinitionPolicyOwner_Type()
)
cfprApNwctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionPolicyOwner.setStatus("current")
_CfprApNwctrlDefinitionUplinkFailAction_Type = CfprApNwctrlLinkFailAction
_CfprApNwctrlDefinitionUplinkFailAction_Object = MibTableColumn
cfprApNwctrlDefinitionUplinkFailAction = _CfprApNwctrlDefinitionUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 56, 1, 1, 11),
    _CfprApNwctrlDefinitionUplinkFailAction_Type()
)
cfprApNwctrlDefinitionUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNwctrlDefinitionUplinkFailAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-NWCTRL-MIB",
    **{"cfprApNwctrlObjects": cfprApNwctrlObjects,
       "cfprApNwctrlDefinitionTable": cfprApNwctrlDefinitionTable,
       "cfprApNwctrlDefinitionEntry": cfprApNwctrlDefinitionEntry,
       "cfprApNwctrlDefinitionInstanceId": cfprApNwctrlDefinitionInstanceId,
       "cfprApNwctrlDefinitionDn": cfprApNwctrlDefinitionDn,
       "cfprApNwctrlDefinitionRn": cfprApNwctrlDefinitionRn,
       "cfprApNwctrlDefinitionCdp": cfprApNwctrlDefinitionCdp,
       "cfprApNwctrlDefinitionDescr": cfprApNwctrlDefinitionDescr,
       "cfprApNwctrlDefinitionIntId": cfprApNwctrlDefinitionIntId,
       "cfprApNwctrlDefinitionMacRegisterMode": cfprApNwctrlDefinitionMacRegisterMode,
       "cfprApNwctrlDefinitionName": cfprApNwctrlDefinitionName,
       "cfprApNwctrlDefinitionPolicyLevel": cfprApNwctrlDefinitionPolicyLevel,
       "cfprApNwctrlDefinitionPolicyOwner": cfprApNwctrlDefinitionPolicyOwner,
       "cfprApNwctrlDefinitionUplinkFailAction": cfprApNwctrlDefinitionUplinkFailAction}
)
